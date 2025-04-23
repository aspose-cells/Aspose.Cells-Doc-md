---
title: إيجاد الموقع المطلق للشكل داخل ورقة العمل باستخدام Node.js عبر C++
linktitle: العثور على الموقع المطلق للشكل داخل ورقة العمل
type: docs
weight: 8000
url: /ar/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: تعلم كيفية العثور على الموقع المطلق لشكل داخل ورقة العمل باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى معرفة الموقع المطلق لشكل في ورقة العمل. توفر Aspose.Cells for Node.js via C++ الخاصيتين [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) و[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) لهذا الغرض. تعيد هذه الخصائص الموقع المطلق للشكل داخل ورقة العمل بالبكسل.

{{% /alert %}}

يعرض الكود العيني التالي الموضع المطلق لأول شكل في ورقة العمل بالبكسل. يعرض الكود العيني الإخراج التالي على وحدة التحكم:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Displays the absolute position of the shape
console.log(`Absolute Position of this Shape is (${shape.getLeftToCorner()} , ${shape.getTopToCorner()})`);
```
