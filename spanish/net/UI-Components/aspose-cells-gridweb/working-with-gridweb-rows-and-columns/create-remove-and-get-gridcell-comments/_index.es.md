---
title: Crear, Eliminar y Obtener Comentarios de la Celda de Grid
type: docs
weight: 100
url: /es/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: Este artículo introduce cómo trabajar con comentarios en GridWeb.
---

## **Escenarios de uso posibles**
El siguiente artículo explica cómo crear, eliminar y obtener comentarios de una celda (GridCell) dentro de la hoja de cálculo de GridWeb. Cabe señalar que GridWeb muestra el comentario como un tooltip similar a MS-Excel cuando pasas el mouse sobre la celda, como se muestra en esta captura de pantalla.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Crear objeto de Comentario dentro de la Celda**
Por favor, utiliza el método GridCell.CreateComment para crear un objeto de comentario dentro de la celda. El siguiente código de muestra crea un comentario de ejemplo en la celda B4 de la primera hoja de cálculo de GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Eliminar objeto de Comentario de la Celda**
Utilice el método GridCell.RemoveComment para eliminar un objeto de comentario de la celda. El siguiente código de ejemplo elimina el comentario de la celda B4 dentro de la primera hoja de cálculo de GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Obtener objeto de Comentario de la Celda**
Utilice el método GridCell.GetComment() para obtener el objeto de comentario de la celda. El siguiente código de ejemplo obtiene el objeto de comentario de la celda B4 y luego accede a sus diversas propiedades como Autor, Nota, Visibilidad, etc.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Get comment of this cell

GridComment gridComm = cell.GetComment();

//Access its various properties

string strAuth = gridComm.Author;

string strNote = gridComm.Note;

bool isVis = gridComm.IsVisible;

{{< /highlight >}}
