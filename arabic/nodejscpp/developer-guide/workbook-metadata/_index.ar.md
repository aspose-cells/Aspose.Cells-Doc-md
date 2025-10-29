---  
title: استخدام WorkbookMetadata مع Node.js عبر C++  
linktitle: بيانات السجل الحصري  
type: docs  
weight: 320  
url: /ar/nodejs-cpp/using-workbookmetadata/  
description: تعلم كيفية تحرير بيانات الوحدة العمل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يتيح لك Aspose.Cells تحميل نسخة خفيفة من ملف العمل إلى الذاكرة لتحرير معلومات البيانات الوصفية الخاصة به. يرجى استخدام فئة [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) لتحميل ملف العمل.  
{{% /alert %}}  

يستخدم المثال التالي للفئة [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) لتحرير خصائص المستند المخصصة لملف العمل. بمجرد فتح ملف العمل باستخدام فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، ستتمكن من قراءة خصائص المستند. إليك مثال على الكود باستخدام فئة [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open Workbook metadata
const options = new AsposeCells.MetadataOptions(AsposeCells.MetadataType.Document_Properties);
const meta = new AsposeCells.WorkbookMetadata(path.join(dataDir, "Sample1.xlsx"), options);

// Set some properties
meta.getCustomDocumentProperties().add("test", "test");

// Save the metadata info
meta.save(path.join(dataDir, "Sample2.out.xlsx"));

// Open the workbook
const w = new AsposeCells.Workbook(path.join(dataDir, "Sample2.out.xlsx"));

// Read document property
console.log(w.getCustomDocumentProperties().get("test"));

console.log("Press any key to continue...");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
