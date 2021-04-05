build klipper with 12k bootloader!
can-flash:
> bootloader_flash -i can0 -b klipper.bin  -a 0x08003000 -c "3d-tool" 5 --page-size 1024

scan for bootloader available:
> bootloader_read_config -i can0 -a

using can-bootloader revilo196/can-bootloader/platfrom/can-3d-tool

bootloader aware klipper
config to make a klipper mcu acces its bootloader
[bootloader <mcu-name>] if <mcu-name> is omitted the default mcu is used
this anables the BOOTLOADER MCU=<mcu-name> comand that will put this mcu in bootloader mode an the rest of the printer in shutdown
