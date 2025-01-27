from battery.battery import Battery
from utils import add_years_to_date


class SpindlerBattery(Battery):
	def __init__(self, current_date, last_service_date):
		self.current_date = current_date
		self.last_service_date = last_service_date

	def needs_service(self):
		# needs service once every 3 year
		date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
		if self.current_date >= date_which_battery_should_be_serviced_by:
			return True
		else:
			return False
