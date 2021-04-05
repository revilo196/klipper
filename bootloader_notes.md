build klipper with 12k bootloader!
can-flash:
 bootloader_flash -i can0 -b klipper.bin  -a 0x08003000 -c "3d-tool" 5 --page-size 102

scan for bootloader available:
bootloader_read_config -i can0 -a

using can-bootloader revilo196/can-bootloader/platfrom/can-3d-tool
