---
title: 使用 Node.js 通过 C++ 更改评论的文本方向
linktitle: 更改评论的文本方向
type: docs
weight: 10
url: /zh/nodejs-cpp/change-text-direction-of-the-comment/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 更改评论的文本方向。有效自定义评论对齐设置。
---

{{% alert color="primary" %}}

 Microsoft Excel 允许用户为单元格添加评论，以提供额外信息和突出显示数据。开发者可能需要自定义评论以指定对齐设置和文本方向。Aspose.Cells for Node.js via C++ 提供实现此任务的 API。

{{% /alert %}}

Aspose.Cells for Node.js via C++ 提供一个 [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) 属性，用于设置评论的文本方向。以下示例代码演示了如何使用 [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) 属性来设置评论的文本方向。

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
