---  
title: إنشاء مدى موحد باستخدام Node.js عبر C++  
linktitle: إنشاء مجموعة الاتحاد  
type: docs  
weight: 360  
url: /ar/nodejs-cpp/create-union-range/  
description: تعلم كيفية إنشاء مدى موحد باستخدام Aspose.Cells for Node.js via C++.  
keywords: إنشاء مدى موحد عبر Node.js باستخدام C++، مدى موحد في Aspose.Cells باستخدام Node.js، مجموعة ورقة العمل إنشاء مدى موحد باستخدام Node.js  
---  

## **إنشاء مجموعة الاتحاد**  
توفر Aspose.Cells القدرة على إنشاء مدى موحد باستخدام طريقة [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). تقبل طريقة [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) معلمتين، العنوان لإنشاء المدى الموحد، وفهرس ورقة العمل. وتعيد الطريقة كائن [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange).  

يوضح الكود التالي كيفية إنشاء مدى موحد باستخدام طريقة [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). الملف الناتج الذي تم إنشاؤه بواسطة الكود مرفق للمراجعة.  

- [ملف الناتج](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
