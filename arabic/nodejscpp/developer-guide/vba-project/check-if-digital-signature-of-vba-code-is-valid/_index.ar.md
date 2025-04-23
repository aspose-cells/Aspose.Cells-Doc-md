---
title: تحقق من صحة توقيع الرقمية لتعريف VBA باستخدام Node.js عبر C++
linktitle: تحقق ما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا
type: docs
weight: 120
url: /ar/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: تعلم كيفية التحقق من صحة توقيع الرقمية لرمز VBA باستخدام Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بالتحقق مما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا باستخدام الخاصية [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--). سيعيد **true** إذا كان التوقيع صالحًا وإلا سيعيد **false**. يصبح التوقيع الرقمي لشيفر آلي VBA غير صالح عند تغيير شيفر آلي VBA.

{{% /alert %}}

## **التحقق مما إذا كان توقيع VBA الرقمي صالحًا في Node.js**

الكود التالي يوضح استخدام هذه الخاصية باستخدام [ملف الإكسل العيني](5115030.xlsm) الذي يمكنك تنزيله من الرابط المُقدم. يحتوي نفس ملف Excel على توقيع صالح ولكن عند تعديل شيفر آلي VBA وحفظ سجل العمل ثم إعادة التحقق ، نجد أن توقيعه أصبح غير صالح.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Signature is valid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());

// Modify the VBA Code, save the workbook then reload
// VBA Code Signature will now be invalid
let code = workbook.getVbaProject().getModules().get(1).getCodes();
code = code.replace("Welcome to Aspose", "Welcome to Aspose.Cells");
workbook.getVbaProject().getModules().get(1).setCodes(code);

// Save
workbook.save(path.join(dataDir, "output_out.xlsm"));

// Reload
workbook = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsm"));

// Now the signature is invalid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());
```
