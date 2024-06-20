---
title: Redimensionar GridWeb en la ventana del navegador
type: docs
weight: 40
url: /es/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb, redimensionar
description: Este artículo presenta cómo redimensionar en GridWeb.
---

## **Escenarios de uso posibles**
A veces quieres que Aspose.Cells.GridWeb se redimensione de acuerdo con la ventana del navegador. Es posible que necesite que GridWeb ajuste siempre su tamaño (altura, ancho) y sea compatible con el tamaño de la ventana del navegador. Aspose.Cells.GridWeb proporciona la función *resize()* del lado del cliente para este propósito. Además, incluso puede hacer que el control GridWeb sea redimensionable en la ventana del navegador. Por ejemplo, puede usar el asa de abajo a la derecha (a través del mouse) para personalizar su ancho/alto en la ventana. También es necesario incluir/especificar archivos Javascript de jquery para que funcione en la fuente de la página en tu proyecto.
## **Usar el método de redimensionamiento de GridWeb**
El siguiente código comprobará si se ha llevado a cabo una acción de redimensionamiento cada 100 milisegundos. Cuando no haya más acciones de redimensionamiento, entonces considerará que la operación de redimensionamiento ha terminado ahora. Utilizamos un archivo de plantilla de ejemplo que se importa a GridWeb. Utilizamos código del lado del cliente para redimensionar GridWeb. La captura de pantalla muestra que GridWeb se redimensiona según sea necesario al redimensionar la ventana del navegador.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Hacer que GridWeb sea redimensionable usando la función resizable jquery ui**
El siguiente código hará que el control GridWeb sea redimensionable en la ventana del navegador. Por ejemplo, puede utilizar el asa de abajo a la derecha para personalizar su tamaño en la ventana de GridWeb. Utilizamos el mismo archivo de plantilla que se importa primero en GridWeb. Utilizamos scripts de jquery para hacer que GridWeb sea redimensionable. La captura de pantalla muestra que GridWeb se ha redimensionado utilizando su asa inferior derecha en la ventana del navegador.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
