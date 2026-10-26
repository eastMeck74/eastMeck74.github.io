#!/bin/bash

# convert all imgages to webp using imagemagick

for f in *.png; do
    convert "$f" "${f%.png}.webp"
done
