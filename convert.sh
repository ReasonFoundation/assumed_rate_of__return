#!/bin/bash

#convert all pdf files to txt
files=MI2020/*.pdf

for f in $files ; do
	pdftotext "$f"

done
