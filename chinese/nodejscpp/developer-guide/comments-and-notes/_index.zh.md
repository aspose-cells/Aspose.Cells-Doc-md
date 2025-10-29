---
title: 通过C++使用Node.js管理评论和笔记
linktitle: 注释和备注
type: docs
weight: 128
url: /zh/nodejs-cpp/comments-and-notes/
description: 用Aspose.Cells for Node.js via C++插入和管理评论或笔记。
keywords: 插入评论，插入笔记Node.js通过C++
---

## **介绍**

评论用于在单元格中添加附加信息。Aspose.Cells for Node.js via C++提供两种添加评论的方法：一种是手动在设计文件中创建评论，然后使用Aspose.Cells导入；另一种是在运行时使用Aspose.Cells API添加评论。本主题讨论如何使用Aspose.Cells API添加评论以及评论的格式化。

## **添加注释**

通过调用[**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)集合的[**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-)方法（封装在[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)对象中）在单元格中添加评论。可以通过传递评论索引从[**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)集合中访问新[**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)对象。在访问[**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)对象后，可以使用[**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--)属性自定义评论内容。

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

## **注释格式设置**

还可以通过配置其高度、宽度和字体设置来格式化注释的外观。

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

## **向注释添加图像**

在Microsoft Excel 2007中，还可以将图像添加为单元格注释的背景。在Excel 2007中，可以通过以下步骤完成这一操作。（假设您已经添加了单元格注释。）

1.右键单元格，然后选择**显示/隐藏注释**，清除注释中的任何文本。
1.点击注释的边框进行选择。
1.选择**格式**，然后选择**注释**。
1.在**颜色和线条**选项卡上，展开**颜色**列表。
1.单击**填充效果**。
1.单击**图片**选项卡。
1.在**图片**选项卡上，单击**选择图片**。
1.定位并选择图片。
1. 点击 **确定** 直到所有对话框都关闭。

Aspose.Cells 也提供了这个功能。下面是一个代码示例，从头开始创建一个 XLSX 文件，并在单元格"A1"中添加一个以图片作为背景的评论。

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

## **高级主题**
- [更改批注的文本方向](/cells/zh/nodejs-cpp/change-text-direction-of-the-comment/)
- [如何更改批注字体颜色](/cells/zh/nodejs-cpp/how-to-change-the-comment-font-color/)
- [如何设置评论背景](/cells/zh/nodejs-cpp/how-to-set-comment-background/)
- [线程化的批注](/cells/zh/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
