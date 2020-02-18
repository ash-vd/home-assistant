import appdaemon.plugins.hass.hassapi as hass

class MotionReset(hass.Hass):
    def initialize(self):
        self.listen_state(self.handleMotion, "binary_sensor.zigbee_occupancy_1_occupancy", new="on")

    def handleMotion(self, entity, attribute, old, new, kwargs):
        self.run_in(self.setStateOff, 6)

    def setStateOff(self, kwargs):
        self.set_state(entity, state="off")

