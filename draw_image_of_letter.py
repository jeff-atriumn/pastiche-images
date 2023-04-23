#!/usr/bin/env python3

import os
import sys
import requests
import cairocffi as cairo

letter = sys.argv[1]

# Download the Maven Pro Bold TTF font from Google Fonts
font_url = "https://github.com/google/fonts/raw/main/ofl/mavenpro/MavenPro-Bold.ttf"
response = requests.get(font_url)

# Save the font file locally
font_file = "MavenPro-Bold.ttf"
with open(font_file, "wb") as f:
    f.write(response.content)

# Create a new image with a transparent background
width, height = 300, 300
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Load the font
ctx.select_font_face("Maven Pro", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

# Set the font size
ctx.set_font_size(200)

# Define the position and color for the text
r, g, b, a = 1, 1, 0.7, 1  # Very light shade of yellow

# Calculate the text extents to center the text
text_extents = ctx.text_extents(letter)
x = (width - text_extents[2]) / 2
y = (height + text_extents[3]) / 2

# Set the color
ctx.set_source_rgba(r, g, b, a)

# Draw the text on the image
ctx.move_to(x, y)
ctx.show_text(letter)

# Save the image to a file
surface.write_to_png(f"letter_{letter}_.png")

# Remove the downloaded font file
os.remove(font_file)
