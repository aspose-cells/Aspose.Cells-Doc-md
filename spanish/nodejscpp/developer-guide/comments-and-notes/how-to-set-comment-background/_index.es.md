---
title: Cómo cambiar el fondo del comentario en Excel con Node.js a través de C++
linktitle: Fondo del comentario
type: docs
weight: 190
url: /es/nodejs-cpp/how-to-set-comment-background/
description: Cómo cambiar el color en un comentario e insertar una imagen o foto en un comentario en Excel usando Aspose.Cells for Node.js via C++.
keywords: agregar una imagen de inserción, color de fondo al comentario en Excel con Node.js a través de C++
---

{{% alert color="primary" %}}
Los comentarios se añaden a las celdas para registrar observaciones, desde los detalles de cómo funciona una fórmula, el origen de un valor o preguntas de los revisores. Los comentarios juegan un papel muy importante cuando varias personas discuten o revisan el mismo documento en diferentes momentos. ¿Cómo distinguir los comentarios de diferentes personas? Sí, podemos establecer un color de fondo diferente para cada comentario. Pero cuando necesitamos procesar muchos documentos y un gran número de comentarios, hacerlo manualmente es un caos. Afortunadamente, [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) proporciona una API que te permite hacer esto en código.
{{% /alert %}}

## **Cómo cambiar el color en el comentario en Excel**

Cuando no necesitas el color de fondo predeterminado para los comentarios, tal vez quieras reemplazarlo por un color de tu interés. ¿Cómo cambio el color de fondo del cuadro de Comentarios en Excel?

El siguiente código le guiará sobre cómo usar [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) para agregar su color de fondo favorito a los comentarios de su elección.

Aquí hemos preparado un [archivo de ejemplo](exmaple.xlsx) para ti. Este archivo se usa para inicializar el objeto Workbook en el código a continuación.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Ejecute el código anterior y obtendrá un [archivo de salida](result.xlsx).

## **Cómo insertar una imagen en el comentario en Excel**

Microsoft Excel permite a los usuarios personalizar el aspecto de las hojas de cálculo en gran medida. Incluso es posible agregar imágenes de fondo a los comentarios. Agregar una imagen de fondo puede ser una opción estética o usarse para reforzar la marca.

El código de ejemplo a continuación crea un archivo XLSX desde cero usando la API de [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/), y agrega un comentario con fondo de imagen en la celda A1.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

