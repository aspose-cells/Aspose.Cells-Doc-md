---
title: Gestionar comentarios y notas con Node.js a través de C++
linktitle: Comentarios y notas
type: docs
weight: 128
url: /es/nodejs-cpp/comments-and-notes/
description: Insertar y gestionar comentarios o notas con Aspose.Cells for Node.js via C++.
keywords: insertar comentarios, insertar notas Node.js a través de C++
---

## **Introducción**

 Los comentarios se utilizan para agregar información adicional a las celdas. Aspose.Cells for Node.js via C++ proporciona dos métodos para agregar comentarios a las celdas. El primero es crear comentarios en un archivo de diseño manualmente. Estos comentarios luego se importan usando Aspose.Cells. El segundo es agregar comentarios usando la API de Aspose.Cells en tiempo de ejecución. Este tema trata sobre cómo agregar comentarios a las celdas usando la API de Aspose.Cells. También se explicará cómo formatear comentarios.

## **Agregar un comentario**

 Agregue un comentario a una celda llamando al método [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-) de la colección [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). El nuevo objeto [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) se puede acceder desde la colección [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) pasando su índice de comentario. Después de acceder al objeto [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment), personalice la nota del comentario usando la propiedad [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Formato de comentario**

También es posible dar formato a la apariencia de los comentarios configurando su altura, ancho y ajustes de fuente.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

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

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Temas avanzados**
- [Cambiar la dirección del texto del comentario](/cells/es/nodejs-cpp/change-text-direction-of-the-comment/)
- [Cómo cambiar el color de fuente del comentario](/cells/es/nodejs-cpp/how-to-change-the-comment-font-color/)
- [Cómo configurar el fondo del comentario](/cells/es/nodejs-cpp/how-to-set-comment-background/)
- [Comentarios enhebrados](/cells/es/nodejs-cpp/threaded-comments/)

