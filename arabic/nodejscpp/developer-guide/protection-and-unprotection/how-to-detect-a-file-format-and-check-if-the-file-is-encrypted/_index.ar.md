---  
title: كيفية اكتشاف صيغة ملف والتحقق مما إذا كان الملف مشفرًا باستخدام Node.js عبر C++  
linktitle: كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا  
type: docs  
weight: 2700  
url: /ar/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: تعلم كيفية اكتشاف صيغة ملف والتحقق مما إذا كان ملفًا مشفرًا باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
أحيانًا تحتاج إلى اكتشاف صيغة ملف قبل فتحه لأن امتداد الملف لا يضمن أن محتوى الملف مناسب. قد يكون الملف مشفرًا (ملف محمي بكلمة مرور) لذلك لا يمكن قراءته مباشرة، أو لا يتوجب علينا قراءته. يوفر Aspose.Cells for Node.js via C++ الطريقة [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) الثابتة وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة المستندات.  
{{% /alert %}}  

الرمز البريدي العيني التالي يوضح كيفية اكتشاف تنسيق الملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Detect file format
const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(require("fs").readFileSync(filePath)));

// Gets the detected load format
console.log("The spreadsheet format is: " + AsposeCells.FileFormatUtil.loadFormatToExtension(info.getLoadFormat()));

// Check if the file is encrypted.
console.log("The file is encrypted: " + info.isEncrypted());
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
