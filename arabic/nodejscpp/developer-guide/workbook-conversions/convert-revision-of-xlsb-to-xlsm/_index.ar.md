---  
title: تحويل مراجعة ملف XLSB إلى XLSM باستخدام Node.js عبر C++  
linktitle: تحويل مراجعة ملف XLSB إلى ملف XLSM  
type: docs  
weight: 290  
url: /ar/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: تعلم كيف تقوم بتحويل مراجعات ملفات XLSB بالكامل إلى تنسيق XLSM باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

يدعم Aspose.Cells الآن التحويل الكامل لمراجعات ملفات XLSB إلى ملفات XLSM. تُوجد المراجعات داخل المسار \xl\revisions. يمكنك عرضها عن طريق تغيير امتداد ملف XLSB الخاص بك إلى ZIP. يحتوي مسار \xl\revisions على ملفات تنتهي بامتداد .bin.  

عند تحويل ملف XLSB الخاص بك إلى ملف XLSM باستخدام Aspose.Cells، يتم تحويل هذه ملفات .bin بنجاح إلى ملفات .xml كما هو موضح في هاتين اللقطتين.  

{{% /alert %}}  

يعرض المثال التالي لكيفية تحويل ملف XLSB إلى تنسيق XLSM باستخدام Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

