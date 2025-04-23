---
title: 用 Node.js 和 C++ 为 Excel 插入背景图像
linktitle: 将背景图像插入Excel
type: docs
weight: 90
url: /zh/nodejs-cpp/insert-background-image-to-excel/
description: “如何使用 Aspose.Cells for Node.js via C++ 插入背景图像到 Excel。”
---

{{% alert color="primary" %}} 

通过添加图片作为工作表背景，你可以使工作表更具吸引力。如果你有一个特殊的公司图形，它可以在不遮挡工作表数据的情况下为背景增添一丝色彩。你可以使用Aspose.Cells API设置工作表的背景图片。

{{% /alert %}} 

## **在Microsoft Excel中设置工作表背景**

在Microsoft Excel（例如Microsoft Excel 2019）中设置工作表的背景图片：

1. 从**页面布局**菜单中找到**页面设置**选项，然后点击**背景**选项。
1. 选择一张图片来设置工作表的背景图片。

   **设置工作表背景**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **使用 Aspose.Cells for Node.js via C++ 设置工作表背景**

下面的代码使用从流中读取的图像设置了一个背景图像。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## 相关文章

- [在ODS文件中处理背景](/cells/zh/nodejs-cpp/working-with-background-in-ods-files/)

