#!/bin/bash

# convert all JPG to webp using imagemagick

for f in *.png; do
    convert "$f" "${f%.png}.webp"
done
