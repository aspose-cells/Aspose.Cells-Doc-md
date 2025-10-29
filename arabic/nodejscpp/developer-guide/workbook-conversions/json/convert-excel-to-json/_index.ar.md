---  
title: تحويل Excel إلى JSON باستخدام Node.js عبر C++  
linktitle: تحويل إكسل إلى JSON  
type: docs  
weight: 300  
url: /ar/nodejs-cpp/convert-excel-to-json/  
description: تعلم كيف تقوم بتحويل ملف Excel إلى JSON باستخدام Aspose.Cells for Node.js via C++.  
keywords: تصدير مصنف إلى JSON باستخدام Node.js عبر C++، تحويل Excel إلى JSON باستخدام Node.js عبر C++  
---  

{{% alert color="primary" %}}  
 يدعم Aspose.Cells تحويل مصنف إلى ملف JSON (ترميز كائن جافا سكريبت).  
{{% /alert %}}  

## **تحويل دفتر العمل Excel إلى JSON**  

 لا حاجة للتساؤل عن كيفية تحويل مصنف Excel إلى JSON، لأن مكتبة Aspose.Cells for Node.js via C++ تقدم الحل الأمثل. توفر واجهة برمجة التطبيقات Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة JSON. لتصدير المصنف إلى JSON، مرر [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) كوسيط ثانٍ لطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.  

يسهل مثال الكود التالي تصدير مصنف Excel إلى JSON. يرجى مراجعة الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف JSON الناتج كمثال.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

يستخدم مثال الكود التالي فئة JsonSaveOptions لتحديد إعدادات إضافية ويظهر تصدير مصنف Excel إلى JSON. يرجى مراجعة الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف JSON الناتج كمثال.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
