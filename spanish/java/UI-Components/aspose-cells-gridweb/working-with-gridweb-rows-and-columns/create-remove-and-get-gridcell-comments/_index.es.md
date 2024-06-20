---
title: Crear, Eliminar y Obtener Comentarios de la Celda de Grid
type: docs
weight: 10
url: /es/java/create-remove-and-get-gridcell-comments/
---

## **Escenarios de uso posibles**
El siguiente artículo explica cómo crear, eliminar y obtener comentarios de la celda de GridWeb. Es importante tener en cuenta que GridWeb muestra el comentario como tooltip al igual que MS-Excel cuando pasas el ratón sobre la celda como se muestra en esta captura de pantalla.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Crear objeto de Comentario dentro de la Celda**
Por favor, utiliza el método GridCell.CreateComment para crear un objeto de comentario dentro de la celda. El siguiente código de muestra crea un comentario de ejemplo en la celda B4 de la primera hoja de cálculo de GridWeb.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Eliminar objeto de Comentario de la Celda**
Por favor, utiliza el método GridCell.RemoveComment para eliminar un objeto de comentario de la celda. El siguiente código de muestra elimina el comentario de la celda B4 dentro de la primera hoja de cálculo de GridWeb.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Obtener objeto de Comentario de la Celda**
Por favor, utiliza el método GridCell.GetComment() para obtener el objeto de comentario de la celda. El siguiente código de muestra obtiene el objeto de comentario de la celda B4 y luego accede a sus diversas propiedades como Autor, Nota, Visibilidad, etc.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Get comment of this cell

GridComment gridComm = cell.getComment();

// Access its various properties

String strAuth = gridComm.getAuthor();

String strNote = gridComm.getNote();

boolean isVis = gridComm.isVisible();


{{< /highlight >}}




