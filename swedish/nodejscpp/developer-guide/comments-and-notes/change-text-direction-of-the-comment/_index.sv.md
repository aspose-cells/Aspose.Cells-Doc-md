---
title: Ändra kommentars textinriktning med Node.js via C++
linktitle: Ändra textens riktning på kommentaren
type: docs
weight: 10
url: /sv/nodejs-cpp/change-text-direction-of-the-comment/
description: Lär dig hur du ändrar textens inriktning för kommentarer med Aspose.Cells for Node.js via C++. Anpassa kommentär anpassningsinställningar effektivt.
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att lägga till kommentarer till celler för att lägga till ytterligare information och belysa data. Utvecklare kan behöva anpassa kommentaren för att ange alignmentsinställningar och textinriktning. Aspose.Cells for Node.js via C++ tillhandahåller API:er för att genomföra uppgiften.

{{% /alert %}}

Aspose.Cells for Node.js via C++ tillhandahåller en [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) egenskap för att ställa in textinriktning för en kommentar. Följande exempel visar användningen av [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--)-egenskapen för att ställa in textinriktning för en kommentar.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
