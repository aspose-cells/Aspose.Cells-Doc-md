---
title: 使用Node.js在C++中提取工作表中的图片
linktitle: 使用 ImageOrPrintOptions 从工作表中提取图像
type: docs
weight: 140
url: /zh/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: 学习如何使用Aspose.Cells for Node.js via C++从Excel工作表中提取图片并保存它们。
---

{{% alert color="primary" %}} 

Microsoft Excel用户可以在电子表格中添加图片。利用Aspose.Cells for Node.js via C++，可以读取Microsoft Excel文件中的图片并保存到本地驱动器。本文展示了具体操作方法。

{{% /alert %}} 

下面的示例代码显示了如何从 Excel 文件中提取图像并保存。



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
