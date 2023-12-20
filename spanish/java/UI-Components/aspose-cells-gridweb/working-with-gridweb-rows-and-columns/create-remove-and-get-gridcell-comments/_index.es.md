---
title: Crear quitar y obtener comentarios de GridCell
type: docs
weight: 10
url: /es/java/create-remove-and-get-gridcell-comments/
---
## **Posibles escenarios de uso**
El siguiente artículo explica cómo crear, eliminar y obtener comentarios de GridCell dentro de la hoja de trabajo de GridWeb. Vale la pena señalar que GridWeb muestra comentarios como información sobre herramientas como MS-Excel cuando pasa el mouse sobre la celda como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](create-remove-and-get-gridcell-comments_1.png)
## **Crear objeto de comentario dentro de Cell**
Utilice el método GridCell.CreateComment para crear un objeto de comentario dentro de la celda. El siguiente código de ejemplo crea un comentario de ejemplo en la celda B4 de la primera hoja de cálculo de GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Eliminar objeto de comentario de Cell**
Utilice el método GridCell.RemoveComment para eliminar un objeto de comentario de la celda. El siguiente código de ejemplo elimina el comentario de la celda B4 dentro de la primera hoja de trabajo de GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Obtener objeto de comentario de Cell**
Utilice el método GridCell.GetComment() para obtener el objeto de comentario de la celda. El siguiente código de ejemplo obtiene el objeto de comentario de la celda B4 y luego accede a sus diversas propiedades como Autor, Nota, Visibilidad, etc.

{{< highlight "java" >}}

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




