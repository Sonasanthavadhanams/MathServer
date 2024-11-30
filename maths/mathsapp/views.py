from django.shortcuts import render 
def Power(request): 
    context={} 
    context['Power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('I','0')
        R = request.POST.get('R','0')
        print(I, R)
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        area = int(I) * int(I) * int(R) 
        context['Power'] = area 
        context['I'] = I
        context['R'] = R
        print('Power=',area) 
    return render(request,'mathsapp/maths.html',context)