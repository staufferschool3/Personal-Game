#!/bin/bash
cat hexboot.hex |grep -vE '#*#'|tr -d '\n'|tr -d ' '|xxd -r -p >boot.bin 
qemu-system-x86_64 -drive file=boot.bin,format=raw,if=floppy
