# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Usuario

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Usuario

def acceder(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            # Lógica para el login
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
                return render(request, 'login.html')

        elif 'register' in request.POST:
            # Lógica para el registro
            username = request.POST.get('name')
            email = request.POST.get('email')
            direccion = request.POST.get('direccion')
            ruc_dni = request.POST.get('ruc_dni')
            password = request.POST.get('register_password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, "Las contraseñas no coinciden.")
                return render(request, 'login.html')

            if Usuario.objects.filter(username=username).exists():
                messages.error(request, "El nombre de usuario ya está registrado.")
                return render(request, 'login.html')

            # Crear un nuevo usuario
            usuario = Usuario(
                username=username,
                email=email,
                direccion=direccion,
                ruc_dni=ruc_dni,
                estado=True
            )
            usuario.set_password(password)  # Guarda la contraseña encriptada
            usuario.save()

            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def salir(request): 
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login")

def homePage(request):
    context = {
        'user': request.user,  # Agrega el objeto del usuario al contexto
    }
    return render(request,"bienvenido.html",context) 
def finanzas(request):
    return render(request, 'finanzas.html')

def analisis(request):
    return render(request, 'analisis.html')

def mate(request):
    return render(request, 'mate copy.html')

def tercera(request):
    return render(request, 'TerceraFormula.html')

def cuarta(request):
    return render(request, 'CuartaFormula.html')    

def quinta(request):
    return render(request, 'QuintaFormula.html')

def sexta(request):
    return render(request, 'SextaFormula.html')

def analisisVertical(request):
    return render(request, 'analisis_vertical.html')

def analisisHorizontal(request):
    return render(request, 'analisis_horizontal.html')

def calcular_interes(request):
    if request.method == 'POST':
        monto = request.POST.get('monto', None)
        tasa = request.POST.get('tasa', None)
        tiempo = request.POST.get('tiempo', None)
        monto_final = request.POST.get('monto_final', None)
        tipo_interes = request.POST.get('tipo_interes', None)
        
        interes_simple = None
        interes_compuesto = None
        monto_final_result = None

        if tipo_interes == 'simple' and monto and tasa and tiempo:
            # Calcular interés simple y monto final
            monto = float(monto)
            tasa = float(tasa) / 100
            tiempo = float(tiempo)
            interes_simple = monto * tasa * tiempo
            monto_final_result = monto + interes_simple
        elif tipo_interes == 'compuesto' and monto and tasa and tiempo:
            # Calcular interés compuesto y monto final 
            monto = float(monto)
            tasa = float(tasa) / 100
            tiempo = float(tiempo)
            monto_final_result = monto * (1 + tasa) ** tiempo
            interes_compuesto = monto_final_result - monto
        elif monto_final and tasa and tiempo and tipo_interes == 'simple':
            # Calcular monto inicial desde monto final para interés simple -->PRIMERA FORMA
            monto_final_result = float(monto_final)
            tasa = float(tasa) / 100
            tiempo = float(tiempo)
            monto = monto_final_result / (1 + (tasa * tiempo))
            interes_simple = monto_final_result - monto
        elif monto_final and tasa and tiempo and tipo_interes == 'compuesto':
            # Calcular monto inicial desde monto final para interés compuesto --> SEGUNDA FORMA
            monto_final_result = float(monto_final)
            tasa = float(tasa) / 100
            tiempo = float(tiempo)
            monto = monto_final_result / ((1 + tasa) ** tiempo)
            interes_compuesto = monto_final_result - monto

    return render(request, 'mate.html', {
        'interes_simple': interes_simple,
        'interes_compuesto': interes_compuesto,
        'monto_final': monto_final_result,
    })



def terceraFormula(request):
    flujoPago = 0.0
    tiempo=0.0

    if request.method == 'POST':
        if request.POST.get('tipo', None) =='Mensual':
            montoInicial = float(request.POST.get('montoInicial', 0))
            tasa = interesEquivalente(float(request.POST.get('tasa', 0)))
            tiempo = float(request.POST.get('tiempo', 0))*12
        else:
            montoInicial = float(request.POST.get('montoInicial', 0))
            tasa = interesEquivalente(float(request.POST.get('tasa', 0)))
            tiempo = float(request.POST.get('tiempo', 0))

        flujoPago= float(montoInicial * (((1+tasa)**tiempo*tasa)/((1+tasa)**tiempo-1)))
        print(flujoPago)
    return render(request, 'mate copy.html', {
        'stockFinal': flujoPago,
        'tiempo': tiempo,
    })


def cuartaFormula(request):
    stockInicial = 0.0
    tiempo=0.0

    if request.method == 'POST':
        flujoPago = interesEquivalente(float(request.POST.get('flujoPago', 0)))
        tasa = float(request.POST.get('tasa', 0))/100
        tiempo = float(request.POST.get('tiempo', 0))*12

        stockInicial= flujoPago * (((1+tasa)**tiempo-1)/((1+tasa)**tiempo*tasa))
        print(stockInicial)
    return render(request, 'CuartaFormula.html', {
        'stockInicial': stockInicial,
        'tiempo': tiempo,
    })   
    
def quintaFormula(request):
    stockFinal = 0.0
    tiempo=0.0

    if request.method == 'POST':
        flujoPago = float(request.POST.get('flujoPago', 0))
        tasa = float(request.POST.get('tasa', 0))/100
        tiempo = float(request.POST.get('tiempo', 0))

        stockFinal= flujoPago * (((1+tasa)**tiempo-1)/tasa)
    
    return render(request, 'QuintaFormula.html', {
        'stockFinal': stockFinal,
        'tiempo': tiempo,
    })
    
def sextaFormula(request):
    flujoPago = 0.0
    tiempo=0.0
    if request.method == 'POST':
        if request.POST.get('tipo', None) =='Mensual':
            stockInicial = float(request.POST.get('stockInicial', 0))
            tasa = interesEquivalente(float(request.POST.get('tasa', 0)))
            tiempo = float(request.POST.get('tiempo', 0))*12
        else:
            stockInicial = float(request.POST.get('stockInicial', 0))
            tasa = float(request.POST.get('tasa', 0))/100
            tiempo = float(request.POST.get('tiempo', 0))

        flujoPago= stockInicial * (tasa/(1-(1+tasa)**-tiempo))
    return render(request, 'SextaFormula.html', {
        'flujoPago': flujoPago,
        'tiempo': tiempo,
    })



def interesEquivalente(interes):
    return float(((1+(interes/100))**(30/360)-1))



