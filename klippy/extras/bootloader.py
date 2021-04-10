import mcu
import logging

class Bootloader:
    cmd_BOOTLOADER_help = "Sets the specified mcu (MCU=) into bootloader mode"
    def __init__(self, config):
        self.printer = config.get_printer()
        self.mcu_name = config.get_name().split()[-1]
        if self.mcu_name == None:
            self.mcu_name = 'mcu'
        self._mcu = mcu.get_printer_mcu(self.printer, self.mcu_name)
        self._mcu.register_config_callback(self._build_config)
        gcode = self.printer.lookup_object("gcode")
        gcode.register_mux_command("BOOTLOADER", "MCU",
                                   self.mcu_name,
                                   self.cmd_BOOTLOADER,
                                   desc='cmd_BOOTLOADER_help')

    def _build_config(self):
        self._set_cmd = self._mcu.try_lookup_command('bootloader')


    def get_mcu(self):
        return self._mcu

    def cmd_BOOTLOADER(self, gcmd):
        self._set_cmd.send()
        #self.printer.invoke_shutdown("MCU " + self.mcu_name + " goes into Bootloader")

def load_config_prefix(config):
    return Bootloader(config)

