---
title: Administrar comentarios y notas
linktitle: Comentarios y notas
type: docs
weight: 128
url: /es/net/comments-and-notes/
description: Inserte y administre comentarios o notas con Aspose.Cells para .Net.
keywords: insert comments, insert notes
---
## **Introducción**

Los comentarios se utilizan para agregar información adicional a las celdas. Aspose.Cells proporciona dos métodos para agregar comentarios a las celdas. La primera es crear comentarios en un archivo de diseñador manualmente. Estos comentarios luego se importan usando Aspose.Cells. El segundo es agregar comentarios usando Aspose.Cells API en tiempo de ejecución. Este tema trata sobre la adición de comentarios a las celdas mediante Aspose.Cells API. También se explicará el formato de los comentarios.

## **Agregar un comentario**

 Agregue un comentario a una celda llamando al[**Comentarios**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) colección[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) método (encapsulado en el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objeto). El nuevo[**Comentario**](https://reference.aspose.com/cells/net/aspose.cells/comment) Se puede acceder al objeto desde el[**Comentarios**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) colección pasando el índice de comentarios. Después de acceder a la[**Comentario**](https://reference.aspose.com/cells/net/aspose.cells/comment) objeto, personalice la nota de comentario utilizando el[**Comentario**](https://reference.aspose.com/cells/net/aspose.cells/comment) objetos[**Nota**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Formato de comentario**

También es posible dar formato a la apariencia de los comentarios configurando su altura, ancho y configuración de fuente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Agregar una imagen para comentar**

Con Microsoft Excel 2007, también es posible tener una imagen como fondo de un comentario de celda. En Excel 2007 esto se logra siguiendo los siguientes pasos. (Suponen que ya ha agregado un comentario de celda).

1. Haga clic derecho en la celda que contiene el comentario.
1.  Seleccione**Mostrar/Ocultar comentarios**y borre cualquier texto del comentario.
1. Haga clic en el borde del comentario para seleccionarlo.
1.  Seleccione**Formato** , después**Comentario**.
1.  Sobre el**Colores y Líneas** pestaña, expanda la**Color** lista.
1.  Hacer clic**Efectos de relleno**.
1.  Sobre el**Fotografía** pestaña, haga clic**Seleccionar imagen**.
1. Localiza y selecciona la imagen.
1.  Hacer clic**DE ACUERDO** hasta que todos los cuadros de diálogo se hayan cerrado.

Aspose.Cells también ofrece esta función. A continuación se muestra un ejemplo de código que crea un archivo XLSX desde cero, agregando un comentario a la celda "A1" con una imagen configurada como fondo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Temas avanzados**
- [Cambiar la dirección del texto del comentario](/cells/es/net/change-text-direction-of-the-comment/)
- [Cómo cambiar el color de fuente del comentario](/cells/es/net/how-to-change-the-comment-font-color/)
- [Cómo configurar el fondo de los comentarios](/cells/es/net/how-to-set-comment-background/)
- [Comentarios encadenados](/cells/es/net/threaded-comments/)

