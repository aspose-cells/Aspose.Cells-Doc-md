---  
title: 	Json مع Node.js عبر C++  
linktitle: Json  
type: docs  
weight: 300  
url: /ar/nodejs-cpp/convert-workbook-to-json/  
description: تعلم كيفية تحويل دفتر عمل Excel إلى JSON باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يدعم Aspose.Cells تحويل مصنف إلى ملف Json (ترميز كائن JavaScript).  
{{% /alert %}}  

## **تحويل دفتر العمل Excel إلى JSON**  

توفر API Aspose.Cells دعمًا لتحويل جداول البيانات إلى تنسيق JSON. لتصدير دفتر العمل إلى JSON، مرر [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) كوسيط ثاني لطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.  

يوضح المثال التالي تصدير ورقة العمل النشطة إلى JSON باستخدام عضو التعداد [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json). يرجى مراجعة الكود لتحويل [ملف المصدر](book1.xlsx) إلى ملف JSON الناتج [الذي أنشأه الكود](book1.Json) للمرجعية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **مواضيع متقدمة**  
- [تحويل CSV إلى JSON](/cells/ar/nodejs-cpp/convert-csv-to-json/)  
- [تحويل-Excel-إلى-JSON](/cells/ar/nodejs-cpp/convert-excel-to-json/)  
- [تحويل JSON إلى CSV](/cells/ar/nodejs-cpp/convert-json-to-csv/)  
- [تحويل JSON إلى Excel](/cells/ar/nodejs-cpp/convert-json-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
