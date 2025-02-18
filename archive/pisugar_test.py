from sugarpie import pisugar

pisugar.switch_system_watchdog('on')
pisugar.reset_system_watchdog()
pisugar.switch_system_watchdog('off')
pisugar.get_temperature()