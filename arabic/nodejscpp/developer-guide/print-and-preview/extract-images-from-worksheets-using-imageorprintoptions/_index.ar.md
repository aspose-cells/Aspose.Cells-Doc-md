---
title: استخراج الصور من أوراق العمل باستخدام ImageOrPrintOptions مع Node.js عبر C++
linktitle: استخراج الصور من الأوراق العمل باستخدام خيارات الصورة أو الطباعة
type: docs
weight: 140
url: /ar/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: تعلم كيفية استخراج الصور من أوراق عمل Excel وحفظها باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

يمكن لمستخدمي Excel إضافة الصور إلى جداول البيانات. مع Aspose.Cells for Node.js via C++، من الممكن قراءة الصور من ملفات Excel وحفظها على محرك أقراص محلي. يوضح هذا المقال كيف.

{{% /alert %}} 

يوضح الكود العيني أدناه كيفية استخراج الصور من ملف Excel وحفظها.



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
