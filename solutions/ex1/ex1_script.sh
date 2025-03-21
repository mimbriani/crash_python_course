#! /bin/bash

mkdir bandpass_margherita

# Defining the directory
dir="./bandpass_raw"

# Check if the directory exists

if [[ ! -d "$dir" ]]; then
    echo "Error: directory $dir does not exist."
    exit 1
fi


# Take the files and count the extensions
find "$dir" -type f | sed -n 's/.*\.\([a-zA-Z0-9]*\)$/\1/p' | sort | uniq -c | sort -nr



# For cycle to rename every file, the for goes for all the files in dir (*)
for file in "$dir"/*; do

    # Save the file name without extension
    name=$(basename "$file")

    if grep -q "photon" "$file"; then
        newname="${name%.*}.photon.dat"  # Changes the extension and adds photon
    elif grep -q "energy" "$file"; then
        newname="${name%.*}.energy.dat"  # Changes the extension and adds energy
    else
        newname="${name%.*}.unknown.dat"  # Changes the extension and adds unknown for not given files
    fi

    cp "$file" "./bandpass_margherita/$newname"

done



echo "All files have been renamed successfully in 'bandpass_margherita'!"
