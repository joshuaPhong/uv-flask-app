def get_clothing_advice(uv_index, is_cloudy=None):
	if uv_index is None:
		return "UV data unavailable."

	if is_cloudy is None:
		return "Weather data unavailable."

	# Unpack the tuple into cloud_index and location_name
	cloud_index, location_name, weather_main, weather_description, weather_icon = is_cloudy

	if cloud_index >= 50:
		if uv_index <= 2:
			return "Low UV: Minimal sun risk. Regular clothing is fine."
		elif uv_index <= 5:
			return "Moderate UV: Some UV still penetrates. Cover shoulders and consider a hat."
		elif uv_index <= 7:
			return "High UV: UV can still be strong. Use sunscreen and wear sunglasses."
		elif uv_index <= 10:
			return "Very High UV: Clouds offer partial protection. Cover up and limit exposure."
		else:
			return "Extreme UV: Dangerous even with clouds. Stay indoors or fully cover up."
	else:
		if uv_index <= 2:
			return "Low UV (sunny): No special protection needed. Light clothing is fine."
		elif uv_index <= 5:
			return "Moderate UV (sunny): Wear a hat and cover exposed skin."
		elif uv_index <= 7:
			return "High UV (sunny): Sunglasses, hat, and long sleeves recommended."
		elif uv_index <= 10:
			return "Very High UV (sunny): Avoid midday sun. Full coverage and SPF 30+ sunscreen needed."
		else:
			return "Extreme UV (sunny): Stay indoors if possible. Maximum sun protection required."
