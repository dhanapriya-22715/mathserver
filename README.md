# Ex.05 Design a Website for Server Side Processing
# Date:09-11-2024
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM : 
```
math.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lamp Filament Power Calculator</title>
    <style>
        body {
            font-family: 'Arial, sans-serif';
            background-color: beige;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        h1 {
            margin-top: 50px;
            color: #007bff;
        }

        .calculator {
            background-color: white;
            width: 90%;
            max-width: 400px;
            margin: 30px auto;
            padding: 20px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }

        label {
            display: block;
            font-size: 1.2em;
            margin: 15px 0 5px;
            text-align: left;
        }

        input[type="number"] {
            width: 100%;
            padding: 10px;
            font-size: 1em;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .result {
            margin-top: 20px;
            font-size: 1.5em;
            font-weight: bold;
            color: #28a745;
        }

        .error {
            color: #d9534f;
            font-size: 0.9em;
        }

        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 1.2em;
            margin-top: 20px;
            cursor: pointer;
            border-radius: 5px;
            width: 100%;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Lamp Filament Power Calculator</h1>
    <div class="calculator">
        <label for="intensity">Intensity (I) in Amperes:</label>
        <input type="number" id="intensity" placeholder="Enter Intensity (A)" step="0.01" min="0">

        <label for="resistance">Resistance (R) in Ohms:</label>
        <input type="number" id="resistance" placeholder="Enter Resistance (Ω)" step="0.01" min="0">

        <button onclick="calculatePower()">Calculate Power</button>

        <div class="result" id="result"></div>
        <div class="error" id="error"></div>
    </div>

    <script>
        function calculatePower() {
            const intensity = parseFloat(document.getElementById('intensity').value);
            const resistance = parseFloat(document.getElementById('resistance').value);
            const resultDiv = document.getElementById('result');
            const errorDiv = document.getElementById('error');

            // Clear previous messages
            resultDiv.textContent = '';
            errorDiv.textContent = '';

            if (isNaN(intensity) || isNaN(resistance) || intensity < 0 || resistance < 0) {
                errorDiv.textContent = 'Please enter valid positive numbers for both Intensity and Resistance.';
                return;
            }

            const power = (intensity ** 2) * resistance;
            resultDiv.textContent = `Power (P) = ${power.toFixed(2)} Watts`;
        }
    </script>
</body>
</html>

views.py
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

urls.py
from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.calculate_power, name='calculate_power'),
]
```
# SERVER SIDE PROCESSING:
![Screenshot (56)](https://github.com/user-attachments/assets/bbb65d81-8a1f-430c-b158-95f95fc6bb00)

# HOMEPAGE:
![Screenshot (43)](https://github.com/user-attachments/assets/e446faeb-5e80-44db-82b3-54b37f1867ee)

# RESULT:
The program for performing server side processing is completed successfully.
