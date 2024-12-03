# Ex.05 Design a Website for Server Side Processing
## Date:29/11/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
maths.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculator</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f9;
            color: #333;
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 20px;
            color: #444;
        }

        form {
            background: #fff;
            padding: 20px 30px;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }

        form label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        form input {
            width: 100%;
            padding: 8px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 1rem;
        }

        form button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 1rem;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        form button:hover {
            background-color: #0056b3;
        }

        h2 {
            margin-top: 30px;
            font-size: 1.5rem;
            color: #555;
        }

        #result {
            font-size: 1.2rem;
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <h1>Power Calculator</h1>
    <h2>Sona. S24900459</h2>
    <form id="powerCalculator" method="post">
        {% csrf_token %}
        <label for="I">Intensity (Amps):</label>
        <input type="number" id="I" name="I" value="{{I}}" required step="any"><br><br>

        <label for="R">Resistance (Ohms):</label>
        <input type="number" id="R" name="R" value="{{R}}" required step="any"><br><br>


        <button type="submit" onclick="calculatePower()">Calculate Power</button>
        <h2>Result:</h2>
        <input id="Power" name="Power" value="{{Power}}">
        <p>Enter values above and click calculate.</p>
    </form>
</body>

</html>

views.py

from django.shortcuts import render 
def Power(request): 
    context={} 
    context['Power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('Intensity','0')
        R = request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        Power = (int(I) * int(I)) * int(R)
        context['Power'] = Power
        context['I'] = I
        context['R'] = R
        print('Power=',Power) 
    return render(request,'mathsapp/maths.html',context)

urls.py

from django.contrib import admin 
from django.urls import path 
from mathsapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('Power/',views.Power,name="Power"),
    path('',views.Power,name="Power")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (27).png>)

## HOMEPAGE:
![alt text](<Screenshot (28).png>)

## RESULT:
The program for performing server side processing is completed successfully.
