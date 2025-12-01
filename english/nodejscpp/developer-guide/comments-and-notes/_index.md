---
title: Manage Comments and Notes with Node.js via C++
linktitle: Comments and Notes
type: docs
weight: 128
url: /nodejs-cpp/comments-and-notes/
description: Insert and manage comments or notes with Aspose.Cells for Node.js via C++.
keywords: insert comments, insert notes Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Comments are used to add additional information to cells. Aspose.Cells for Node.js via C++ provides two methods for adding comments to cells. The first is to create comments in a designer file manually. These comments are then imported using Aspose.Cells. The second is to add comments using the Aspose.Cells API at runtime. This topic discusses adding comments to cells using the Aspose.Cells API. Formatting comments will also be explained.

## **Adding a Comment**

Add a comment to a cell by calling the [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) collection's [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-) method (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) object). The new [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) object can be accessed from the [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) collection by passing the comment index. After accessing the [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) object, customize the comment note by using the [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--) property.

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

## **Comment Formatting**

It is also possible to format comments' appearance by configuring their height, width and font settings.

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

## **Add an Image to Comment**

With Microsoft Excel 2007, it is also possible to have an image as the background to a cell comment. In Excel 2007 this is accomplished by doing the following steps. (They suppose that you have already added a cell comment.)

1. Right-click the cell that contains the comment.
1. Select **Show/Hide Comments**, and clear any text from the comment.
1. Click on the border of the comment to select it.
1. Select **Format**, then **Comment**.
1. On the **Colors and Lines** tab, expand the **Color** list.
1. Click **Fill Effects**.
1. On the **Picture** tab, click **Select Picture**.
1. Locate and select the picture.
1. Click **OK** until all dialogs have closed.

Aspose.Cells also provides this feature. Below is a code sample that creates an XLSX file from scratch, adding a comment to cell "A1" with a picture set as its background.

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

## **Advance topics**
- [Change Text Direction of the Comment](/cells/nodejs-cpp/change-text-direction-of-the-comment/)
- [How to change the Comment Font Color](/cells/nodejs-cpp/how-to-change-the-comment-font-color/)
- [How to set comment background](/cells/nodejs-cpp/how-to-set-comment-background/)
- [Threaded Comments](/cells/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
