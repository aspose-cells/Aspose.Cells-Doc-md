---
title: Change Text Direction of the Comment with Node.js via C++
linktitle: Change Text Direction of the Comment
type: docs
weight: 10
url: /nodejs-cpp/change-text-direction-of-the-comment/
description: Learn how to change the text direction of comments using Aspose.Cells for Node.js via C++. Customize comment alignment settings effectively.
---

{{% alert color="primary" %}}

Microsoft Excel allows users to add comments to cells to add additional information and highlight data. Developers may need to customize the comment to specify alignment settings and text direction. Aspose.Cells for Node.js via C++ provides APIs to accomplish the task.

{{% /alert %}}

Aspose.Cells for Node.js via C++ provides a [**Shape.textDirection**](https://reference.aspose.com/cells/nodejs-cpp/shape/#textDirection) property to set text direction for a comment. The following sample code demonstrates the use of [**Shape.textDirection**](https://reference.aspose.com/cells/nodejs-cpp/shape/#textDirection) property to set text direction for a comment.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

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
