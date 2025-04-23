---
title: Ändern der Textausrichtung des Kommentars mit Node.js über C++
linktitle: Ändern der Textausrichtung des Kommentars
type: docs
weight: 10
url: /de/nodejs-cpp/change-text-direction-of-the-comment/
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ die Textausrichtung von Kommentaren ändern. Passen Sie die Ausrichtungseinstellungen der Kommentare effektiv an.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, Kommentare zu Zellen hinzuzufügen, um zusätzliche Informationen bereitzustellen und Daten hervorzuheben. Entwickler müssen möglicherweise die Kommentare anpassen, um Ausrichtungseinstellungen und Textausrichtung zu spezifizieren. Aspose.Cells for Node.js via C++ stellt die APIs für diese Aufgabe bereit.

{{% /alert %}}

Aspose.Cells for Node.js via C++ bietet die [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--)-Eigenschaft, um die Textausrichtung eines Kommentars festzulegen. Der folgende Beispielcode demonstriert die Verwendung der [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--)-Eigenschaft, um die Textausrichtung eines Kommentars festzulegen.

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
