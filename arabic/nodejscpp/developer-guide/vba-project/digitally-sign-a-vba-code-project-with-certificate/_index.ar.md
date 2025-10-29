---
title: توقيع مشروع رمز VBA رقميًا باستخدام شهادة عبر Node.js عبر C++
linktitle: التوقيع الرقمي لمشروع كود VBA بشهادة
type: docs
weight: 110
url: /ar/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: تعلم كيفية توقيع مشروع VBA رقميًا باستخدام شهادة عبر Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

يمكنك توقيع مشروع كود VBA رقميًا باستخدام Aspose.Cells مع طريقتها [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). يرجى اتباع هذه الخطوات للتحقق مما إذا كان ملف إكسل الخاص بك موقعًا رقمياً بشهادة.

- انقر فوق **Basic Visual** من علامة التبويب **المطور** لفتح **البيئة المتقدمة لتطبيقات Basic Visual**
- انقر فوق **أدوات** > **التوقيعات الرقمية...** من **بيئة Visual Basic للتطبيقات**

وسيظهر النموذج التوقيع **الرقمي** يظهر إذا كان المستند موقعًا رقميًا بشهادة أم لا.

{{% /alert %}} 

## ** توقيع مشروع VBA رقميًا باستخدام شهادة في Node.js**

 يوضح رمز العينة التالي كيفية استخدام [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-) الطريقتين. إليك ملفات الإدخال والإخراج للرمز التجريبي. يمكنك استخدام أي ملف Excel وأي شهادة لاختبار هذا الرمز.

- [ملف Excel المصدر](5115028.xlsm) المستخدم في الكود العيني.
- [ملف pfx العيني](5115039.pfx) لإنشاء توقيع رقمي. يرجى تثبيته على جهاز الكمبيوتر الخاص بك لتشغيل هذا الكود. كلمة المرور الخاصة به هي 1234.
- [ملف Excel الناتج](5115029.xlsm) الذي تم إنشاؤه بواسطة الكود العيني.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Set up paths
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const pfxPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.pfx");
const workbookPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.xlsm");

// Set Digital Signature
const password = "1234";
const comment = "Signing Digital Signature using Aspose.Cells";
const digitalSignature = new AsposeCells.DigitalSignature(fs.readFileSync(pfxPath), password, comment, new Date());

// Create workbook object from excel file
const workbook = new AsposeCells.Workbook(workbookPath);

// Sign VBA Code Project with Digital Signature
workbook.getVbaProject().sign(digitalSignature);

// Save the workbook
workbook.save(path.join(outputDir, "outputDigitallySignVbaProjectWithCertificate.xlsm"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
