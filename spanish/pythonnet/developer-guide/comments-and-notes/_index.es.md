---
title: Gestionar comentarios y notas
linktitle: Comentarios y notas
type: docs
weight: 128
url: /es/python-net/comments-and-notes/
description: Insertar y gestionar comentarios o notas con Aspose.Cells para Python via .NET.
keywords: insertar comentarios, insertar notas
---

## **Introducción**

Los comentarios se utilizan para agregar información adicional a las celdas. Aspose.Cells proporciona dos métodos para agregar comentarios a las celdas. El primero es crear comentarios en un archivo de diseño manualmente. Estos comentarios luego se importan utilizando Aspose.Cells. El segundo es agregar comentarios usando la API de Aspose.Cells en tiempo de ejecución. Este tema trata sobre cómo agregar comentarios a las celdas mediante la API de Aspose.Cells. También se explicará el formato de comentarios.

## **Agregar un comentario**

Agregar un comentario a una celda llamando al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add) de la colección [**Comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). El nuevo objeto [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment) se puede acceder desde la colección [**Comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection) pasando el índice del comentario. Después de acceder al objeto [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment), personalice la nota del comentario utilizando la propiedad [**note**](https://reference.aspose.com/cells/python-net/aspose.cells/comment/note) del objeto [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Formato de comentario**

También es posible dar formato a la apariencia de los comentarios configurando su altura, ancho y ajustes de fuente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Agregar una imagen al comentario**

Con Microsoft Excel 2007, también es posible tener una imagen como fondo de un comentario de celda. En Excel 2007, esto se logra siguiendo los siguientes pasos. (Se supone que ya ha agregado un comentario de celda)

1. Haga clic con el botón derecho en la celda que contiene el comentario.
1. Seleccione **Mostrar/Ocultar comentarios**, y elimine cualquier texto del comentario.
1. Haga clic en el borde del comentario para seleccionarlo.
1. Seleccione **Formato**, luego **Comentario**.
1. En la pestaña **Colores y líneas**, expanda la lista de **Color**.
1. Haga clic en **Efectos de relleno**.
1. En la pestaña **Imagen**, haga clic en **Seleccionar imagen**.
1. Ubique y seleccione la imagen.
1. Haga clic en **Aceptar** hasta que se cierren todos los diálogos.

Aspose.Cells también proporciona esta función. A continuación se muestra un ejemplo de código que crea un archivo XLSX desde cero, agregando un comentario a la celda "A1" con una imagen como fondo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Temas avanzados**
- [Cambiar la dirección del texto del comentario](/cells/es/python-net/change-text-direction-of-the-comment/)
- [Cómo cambiar el color de fuente del comentario](/cells/es/python-net/how-to-change-the-comment-font-color/)
- [Cómo configurar el fondo del comentario](/cells/es/python-net/how-to-set-comment-background/)
- [Comentarios enhebrados](/cells/es/python-net/threaded-comments/)

{{< app/cells/assistant language="python-net" >}}
