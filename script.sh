#!/bin/bash

# convert all JPG to webp using imagemagick

for f in *.JPG; do
    convert "$f" "${f%.JPG}.webp"
done
