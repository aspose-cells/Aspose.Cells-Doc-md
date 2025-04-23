---
title: Cambiar la dirección del texto del comentario con Node.js a través de C++
linktitle: Cambiar la dirección del texto del comentario
type: docs
weight: 10
url: /es/nodejs-cpp/change-text-direction-of-the-comment/
description: Aprende cómo cambiar la dirección del texto de los comentarios usando Aspose.Cells for Node.js via C++. Personaliza la alineación del comentario de manera efectiva.
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios agregar comentarios a las celdas para agregar información adicional y resaltar datos. Los desarrolladores pueden necesitar personalizar el comentario para especificar configuraciones de alineación y dirección del texto. Aspose.Cells for Node.js via C++ proporciona APIs para lograr esta tarea.

{{% /alert %}}

Aspose.Cells for Node.js via C++ proporciona una propiedad [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) para establecer la dirección del texto en un comentario. El siguiente código de ejemplo demuestra el uso de la propiedad [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) para configurar la dirección del texto en un comentario.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first worksheet
const sheet = wb.getWorksheets().get(0);

// Add a comment to A1 cell
const commentIndex = sheet.getComments().add("A1");
const comment = sheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set its horizontal alignment setting
comment.getCommentShape().setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Right);

// Set the Text Direction - Right-to-Left
comment.getCommentShape().setTextOrientationType(AsposeCells.TextDirectionType.RightToLeft);

// Set the Comment note
comment.setNote("This is my Comment Text. This is test");

const outputFilePath = path.join(dataDir, "OutCommentShape.out.xlsx");
// Save the Excel file
wb.save(outputFilePath);
```
