from django.urls import path
from SeguridadApp.views import acceder,calcular_interes, homePage, salir,finanzas,analisis,mate, analisisVertical, analisisHorizontal,tercera,cuarta,quinta,sexta,terceraFormula,cuartaFormula,quintaFormula,sextaFormula


urlpatterns = [
    path('', homePage, name="home"),  # Ruta para la página de inicio
    path('login/', acceder, name="login"),  
    path('logout/', salir, name="logout"), 
    path('finanzas/', finanzas, name="finanzas"),
    path('mate/', mate, name="mate"),
    path('tercera/', tercera, name="tercera"),
    path('cuarta/', cuarta, name="cuarta"),
    path('quinta/', quinta, name="quinta"),
    path('sexta/', sexta, name="sexta"),
    path('calcular/', calcular_interes, name='calcular_interes'),
    path('analisis/', analisis, name="analisis"),
    path('analisisVertical/', analisisVertical, name="analisisVertical"),
    path('analisisHorizontal/', analisisHorizontal, name="analisisHorizontal"),
    path('terceraFormula/', terceraFormula, name="terceraFormula"),
    path('cuartaFormula/', cuartaFormula, name="cuartaFormula"),
    path('quintaFormula/', quintaFormula, name="quintaFormula"),
    path('sextaFormula/', sextaFormula, name="sextaFormula"),
]
