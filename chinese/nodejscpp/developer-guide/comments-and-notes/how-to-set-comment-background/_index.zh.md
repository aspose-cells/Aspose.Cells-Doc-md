---
title: 如何用 Node.js 通过 C++ 改变 Excel 中评论的背景
linktitle: 评论背景
type: docs
weight: 190
url: /zh/nodejs-cpp/how-to-set-comment-background/
description: 使用 Aspose.Cells for Node.js via C++ 改变评论颜色并在评论中插入图片或图像。
keywords: 使用 Node.js 通过 C++ 添加内嵌图片、颜色和评论背景到 Excel
---

{{% alert color="primary" %}}
 评论被添加到单元格以记录评论内容，从细节如公式的工作方式、数据来源到审阅者的问题。在多个人在不同时间讨论或审查同一文档时，评论扮演着极其重要的角色。如何区分不同人的评论？是的，我们可以为每个评论设置不同的背景颜色。但当需要处理大量文档和评论时，手动操作是个灾难。幸运的是，[**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) 提供了一个 API，可以让你在代码中实现此功能。
{{% /alert %}}

## **如何在Excel中更改评论的颜色**

当你不需要批注的默认背景色时，可以用自己关注的颜色替换它。如何更改 Excel 中批注框的背景色？

以下代码将指导你如何使用[**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/)为你自己选择的评论添加喜欢的背景颜色。

这里我们为你准备了一个[示例文件](exmaple.xlsx)。该文件用于初始化下面的代码中的 Workbook 对象。

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

执行上述代码，你将得到一个[输出文件](result.xlsx)。

## **如何在Excel中评论中插入图片或图像**

Microsoft Excel 允许用户极大程度地自定义电子表格的外观和感觉。甚至可以在评论中添加背景图片。添加背景图片可以是美观的选择，也可以用来强化品牌。

以下示例代码使用 [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) API 从零开始创建一个 XLSX 文件，并在单元格 A1 添加带有图片背景的评论。

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

{{< app/cells/assistant language="nodejs-cpp" >}}
