[bits 16]           ; Tell the assembler we are in 16-bit Real Mode
[org 0x7c00]        ; Set the starting address for the BIOS bootloader

start:
    ; --- Register Initialization (The first 11 bytes) ---
    xor ax, ax      ; 31 C0
    mov ds, ax      ; 8E D8
    mov es, ax      ; 8E C0
    mov ss, ax      ; 8E D0
    mov sp, 0x7c00  ; BC 00 7C

    ; --- Video Setup (The next 5 bytes) ---
    mov ax, 0x0013  ; b8 13 00 (Mode 13h: 320x200, 256 colors)
    int 0x10        ; CD 10    (Call BIOS video interrupt)

    mov ax, 4F02h    ; VBE Function: Set Video Mode
    mov bx, 105h     ; Mode number for 1024x768 @ 256 colors
    int 10h          ; Call BIOS video interrupt

    ; --- Point ES to Video Memory (The next 5 bytes) ---
    mov ax, 0xa000  ; b8 00 A0
    mov es, ax      ; 8E C0

    ; --- Draw the Pixel (The next 6 bytes) ---
    ; Writes color 04 (red) to ES:[0000]
    mov byte [es:0x0000], 0x04 ; 26 C6 06 00 00 04

    ; --- Infinite Loop (The next 2 bytes) ---
hang:
    jmp hang        ; EB FE

; --- Bootloader Padding & Signature ---
times 510-($-$$) db 0   ; Fill the rest of the 512 bytes with zeros
dw 0xaa55               ; The 55 AA magic boot signature
