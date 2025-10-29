---  
title: اكتشاف تنسيق ملف ملفات Office Open XML المشفرة مع Node.js عبر C++  
linktitle: الكشف عن تنسيق الملف لملفات Office Open XML المُشفرة  
type: docs  
weight: 340  
url: /ar/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: تعلم كيفية اكتشاف تنسيق ملف ملفات OOXML المشفرة باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (المعروف أيضًا باسم **OOXML** أو **Microsoft Open XML** (MOX)) هو تنسيق ملف قائم على XML تم تطويره بواسطة Microsoft لتمثيل مستندات المكتب مثل جداول البيانات، المخططات، العروض التقديمية، ومستندات المعالجة النصية.  

{{% /alert %}}  

 يوفر Aspose.Cells وسيلة لاكتشاف تنسيق ملفات **Microsoft Open XML** المشفرة. لتحديد نوع الملف، استخدم طريقة [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) كما هو موضح في مثال الكود أدناه.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "encryptedBook1.out.tmp");

fs.writeFileSync(filePath, Buffer.from([0x50, 0x4B, 0x03, 0x04]));
const stream = fs.readFileSync(filePath);
AsposeCells.FileFormatUtil.verifyPassword(stream, "1234");
const fileFormatInfo = AsposeCells.FileFormatUtil.detectFileFormat(stream);

console.log("File Format: " + fileFormatInfo.getFileFormatType());
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
