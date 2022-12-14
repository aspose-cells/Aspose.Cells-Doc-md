---
title: Cambiar el tamaño de GridWeb y su barra de encabezado
type: docs
weight: 30
url: /es/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[Agregar GridWeb al formulario web](/cells/es/net/add-gridweb-to-web-form/), analizó el cambio de tamaño del control Aspose.Cells.GridWeb mediante WYSIWYG. Este artículo explica cómo hacer lo mismo pero en tiempo de ejecución usando Aspose.Cells.GridWeb API. También explica cómo cambiar el tamaño de las barras de encabezado del control Aspose.Cells.GridWeb para que sus datos sean más fáciles de leer.

{{% /alert %}} 
## **Cambio de ancho y alto de Aspose.Cells.GridWeb**
Cambiar el ancho y la altura del control Aspose.Cells.GridWeb es una característica simple pero importante. El control Aspose.Cells.GridWeb está representado por la clase GridWeb en API. Para cambiar el tamaño del ancho y el alto del control GridWeb, simplemente use sus propiedades de ancho y alto.

{{% alert color="primary" %}} 

El ancho y la altura del control se pueden definir en píxeles o puntos.

{{% /alert %}} 

El resultado del fragmento de código que sigue se muestra a continuación.

**Se modificó el ancho y la altura del control GridWeb.** 

![todo:imagen_alternativa_texto](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Cambiar el ancho y la altura de la barra de encabezado**
Aspose.Cells. El control GridWeb contiene dos barras de encabezado de la siguiente manera:

- Barra de encabezado superior, esta barra de encabezado representa columnas como A, B, C, D, etc.
- Barra de encabezado izquierda, esta barra de encabezado representa filas como 1, 2, 3, 4, etc.

Ambas barras de encabezado se muestran a continuación.

**Barras de encabezado** 

![todo:imagen_alternativa_texto](resize-gridweb-and-its-header-bar_2.png)

Cambie la altura de la barra de encabezado superior y el ancho de la barra de encabezado izquierda mediante las propiedades HeaderBarHeight y HeaderBarWidth del control GridWeb, respectivamente. La siguiente figura muestra el resultado del ejemplo de código que sigue.

**Se modificó el ancho y la altura de la barra de encabezado.** 

![todo:imagen_alternativa_texto](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
