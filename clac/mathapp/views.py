from django.shortcuts import render

def calculate_power(request):
    result = None
    power = None
    intensity = None
    resistance = None

    if request.method == "POST":
        # Get the form data
        intensity = request.POST.get('intensity')
        resistance = request.POST.get('resistance')
        power = request.POST.get('power')

        # Perform calculation based on the inputs
        try:
            if intensity and resistance:  # If intensity and resistance are provided
                intensity = float(intensity)
                resistance = float(resistance)
                power = intensity ** 2 * resistance
                result = f"Calculated Power (P) = {power:.2f} Watts"
            elif power and resistance:  # If power and resistance are provided
                power = float(power)
                resistance = float(resistance)
                intensity = (power / resistance) ** 0.5
                result = f"Calculated Intensity (I) = {intensity:.2f} Amps"
            elif power and intensity:  # If power and intensity are provided
                power = float(power)
                intensity = float(intensity)
                resistance = power / (intensity ** 2)
                result = f"Calculated Resistance (R) = {resistance:.2f} Ohms"
            else:
                result = "Please enter at least two values to calculate."
        except ValueError:
            result = "Invalid input. Please enter numeric values."

    return render(request, 'mathapp/math.html', {'result': result, 'power': power, 'intensity': intensity, 'resistance': resistance})