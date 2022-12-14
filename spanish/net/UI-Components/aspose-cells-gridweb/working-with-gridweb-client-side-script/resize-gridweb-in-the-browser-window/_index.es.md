---
title: Cambiar el tamaño de GridWeb en la ventana del navegador
type: docs
weight: 40
url: /es/net/resize-gridweb-in-the-browser-window/
---
## **Posibles escenarios de uso**
 veces desea Aspose.Cells. GridWeb debe cambiar su tamaño de acuerdo con la ventana del navegador. Es posible que necesite que GridWeb siempre ajuste su tamaño (alto, ancho) y sea compatible con el tamaño de la ventana del navegador. Aspose.Cells. GridWeb proporciona del lado del cliente*redimensionar()* función para el propósito. Además, incluso puede hacer que el control de GridWeb cambie de tamaño en la ventana del navegador. Por ejemplo, puede usar el controlador inferior derecho (a través del mouse) para personalizar su ancho/alto en la ventana. También debe incluir/especificar archivos jquery Javascript para que funcione en la fuente de la página en su proyecto.
## **Usando el método de cambio de tamaño de GridWeb**
El siguiente código verificará si se realiza una acción de cambio de tamaño cada 100 milisegundos. Cuando no hay más acción de cambio de tamaño, entonces piensa que la operación de cambio de tamaño ya ha terminado. Usamos un archivo de plantilla de muestra que se importa a GridWeb. Usamos el código del lado del cliente para cambiar el tamaño de GridWeb. La captura de pantalla muestra que GridWeb cambia de tamaño en consecuencia al cambiar el tamaño de la ventana del navegador.

![todo:imagen_alternativa_texto](resize-gridweb-in-the-browser-window_1.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Hacer GridWeb redimensionable usando la función jquery ui redimensionable**
El siguiente código hará que el control GridWeb se pueda cambiar de tamaño en la ventana del navegador. Por ejemplo, puede usar el controlador inferior derecho para personalizar el tamaño de GridWeb en la ventana. Usamos el mismo archivo de plantilla que se importa primero a GridWeb. Usamos secuencias de comandos jquery para hacer que GridWeb sea redimensionable. La captura de pantalla muestra que GridWeb ha sido redimensionado usando su controlador inferior derecho en la ventana del navegador.

![todo:imagen_alternativa_texto](resize-gridweb-in-the-browser-window_2.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
