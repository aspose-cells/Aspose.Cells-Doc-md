---
title: Redimensionar GridWeb y su barra de encabezado
type: docs
weight: 30
url: /es/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb, redimensionar
description: Este artículo presenta cómo redimensionar en GridWeb.
---

{{% alert color="primary" %}} 

[Agregar GridWeb a un formulario web](/cells/es/net/aspose-cells-gridweb/add-gridweb-to-web-form/), se discutió redimensionar el control Aspose.Cells.GridWeb usando WYSIWYG. Este artículo explica cómo hacer lo mismo pero en tiempo de ejecución utilizando la API Aspose.Cells.GridWeb. También explica cómo redimensionar las barras de encabezado del control Aspose.Cells.GridWeb para que sus datos sean más fáciles de leer.

{{% /alert %}} 
## **Cambio de ancho y alto de Aspose.Cells.GridWeb**
Cambiar el ancho y el alto del control Aspose.Cells.GridWeb es una característica simple pero importante. El control Aspose.Cells.GridWeb está representado por la clase GridWeb en la API. Para cambiar el ancho y alto del control GridWeb, simplemente use sus propiedades de ancho y alto.

{{% alert color="primary" %}} 

El ancho y alto del control se pueden definir en píxeles o puntos.

{{% /alert %}} 

La salida del fragmento de código que sigue se muestra a continuación.

**Se cambió el ancho y alto del control GridWeb** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Cambiando Ancho y Alto de la Barra de Encabezado**
El control Aspose.Cells.GridWeb contiene dos barras de encabezado de la siguiente manera:

- Barra de encabezado superior, esta barra de encabezado representa las columnas como A, B, C, D, etc.
- Barra de encabezado izquierda, esta barra de encabezado representa las filas como 1, 2, 3, 4, etc.

Ambas de estas barras de encabezado se muestran a continuación.

**Barras de encabezado** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

Cambie la altura de la barra de encabezado superior y el ancho de la barra de encabezado izquierda usando las propiedades HeaderBarHeight y HeaderBarWidth del control GridWeb. La siguiente figura muestra la salida del ejemplo de código que sigue.

**Cambiado ancho y alto de la barra de encabezado** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
