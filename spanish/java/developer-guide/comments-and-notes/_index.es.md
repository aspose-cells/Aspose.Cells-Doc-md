---
title: Administrar comentarios y notas
linktitle: Comentarios y notas
type: docs
weight: 128
url: /es/java/comments-and-notes/
description: Inserte y administre comentarios o notas con Aspose.Cells para java.
keywords: insert comments, insert notes
---
## **Introducción**

Los comentarios se utilizan para agregar información adicional a las celdas. Aspose.Cells proporciona dos métodos para agregar comentarios a las celdas. La primera es crear comentarios en un archivo de diseñador manualmente. Estos comentarios luego se importan usando Aspose.Cells. El segundo es agregar comentarios usando Aspose.Cells API en tiempo de ejecución. Este tema trata sobre la adición de comentarios a las celdas mediante Aspose.Cells API. También se explicará el formato de los comentarios.

## **Agregar un comentario**

 Agregue un comentario a una celda llamando al[**Comentarios**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) colección**Agregar** método (encapsulado en el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objeto). El nuevo[**Comentario**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) Se puede acceder al objeto desde el[**Comentarios**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) colección pasando el índice de comentarios. Después de acceder a la[**Comentario**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objeto, personalice la nota de comentario utilizando el[**Comentario**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) objetos[**Nota**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Formato de comentario**

También es posible dar formato a la apariencia de los comentarios configurando su altura, ancho y configuración de fuente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Agregar una imagen para comentar**

Con Microsoft Excel 2007, también es posible tener una imagen como fondo de un comentario de celda. En Excel 2007 esto se logra siguiendo los siguientes pasos. (Suponen que ya ha agregado un comentario de celda).

1. Haga clic derecho en la celda que contiene el comentario.
1.  Seleccione**Mostrar/Ocultar comentarios**y borre cualquier texto del comentario.
1. Haga clic en el borde del comentario para seleccionarlo.
1.  Seleccione**Formato** , después**Comentario**.
1.  Sobre el**Colores y Líneas** pestaña, expanda la**Color** lista.
1.  Hacer clic**Efectos de relleno**.
1.  Sobre el**Imagen** pestaña, haga clic**Seleccionar imagen**.
1. Localiza y selecciona la imagen.
1.  Hacer clic**OK** hasta que todos los cuadros de diálogo se hayan cerrado.

Aspose.Cells también ofrece esta función. A continuación se muestra un ejemplo de código que crea un archivo XLSX desde cero, agregando un comentario a la celda "A1" con una imagen configurada como fondo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Temas avanzados**
- [Cambiar la dirección del texto del comentario](/cells/es/java/change-text-direction-of-the-comment/)
- [Cómo cambiar el color de fuente del comentario](/cells/es/java/how-to-change-the-comment-font-color/)
- [Cómo configurar el fondo de los comentarios](/cells/es/java/how-to-set-comment-background/)
- [Comentarios encadenados](/cells/es/java/threaded-comments/)

