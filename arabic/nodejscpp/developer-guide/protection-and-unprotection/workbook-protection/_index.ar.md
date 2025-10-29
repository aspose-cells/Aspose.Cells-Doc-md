---  
title: حماية وإلغاء حماية هيكل المصنف باستخدام Node.js عبر C++  
linktitle: حماية وإلغاء حماية هيكل دفتر العمل  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: حماية وإلغاء حماية هيكل ملف إكسل باستخدام Node.js عبر C++.  
---  


{{% alert color="primary" %}}  
لمنع المستخدمين الآخرين من عرض أوراق عمل مخفية، أو إضافتها، أو نقلها، أو حذفها، أو إخفاءها، أو إعادة تسميتها، يمكنك حماية هيكل دفتر العمل الخاص بك بكلمة مرور.  
{{% /alert %}}  


## **حماية وإلغاء حماية هيكل دفتر العمل في MS Excel**  

**![حماية وإلغاء حماية هيكل دفتر العمل](protect-and-unprotect-workbook-structure.png)**  

1. انقر على **مراجعة > حماية الدفتر**.  
١. أدخل كلمة مرور في **مربع الكلمة السرية**.  
١. حدد **موافق**, أدخل كلمة المرور مرة أخرى لتأكيدها، ثم حدد **موافق** مجددًا.  


## **حماية هيكل المصنف باستخدام Aspose.Cells for Node.js via C++**  
متطلبات الترميز البسيطة التالية فقط لتنفيذ حماية هيكل دفتر العمل لملفات Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **إلغاء حماية هيكل المصنف باستخدام Aspose.Cells for Node.js via C++**  
إلغاء حماية هيكل الدفتر بسيط مع واجهة برمجة تطبيقات Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
ملاحظة: كلمة مرور صحيحة مطلوبة.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
