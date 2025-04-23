---  
title: التحقق من كلمة مرور الملفات المشفرة باستخدام Node.js عبر C++  
linktitle: التحقق من كلمة مرور الملفات المشفرة  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: التحقق من كلمة مرور ملفات Excel (xlsx، xlsb، xls، xlsm) وOpen Office (ODS) باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
إذا كانت ملفات Excel (xlsx، xlsb، xls، xlsm) وOpen Office (ODS) مقفلة بكلمة مرور، يدعم Aspose التحقق البسيط من كلمة المرور دون تحليل بيانات محددة من الملفات.  
{{% /alert %}}  

## **تحقق من كلمة المرور للملف المُشفر**  

للتحقق من كلمة مرور الملف المشفر، يوفر Aspose.Cells for Node.js via C++ أسلوب [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). يقبل هذا الأسلوب معلمتين، تدفق الملف والكلمة المرور التي يجب التحقق منها.  
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```  

