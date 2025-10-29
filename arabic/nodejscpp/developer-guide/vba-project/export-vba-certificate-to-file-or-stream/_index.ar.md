---
title: تصدير شهادة VBA إلى ملف أو تدفق باستخدام Node.js عبر C++
linktitle: تصدير شهادة VBA إلى ملف أو تيار
type: docs
weight: 90
url: /ar/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: تعلم كيفية تصدير شهادة VBA الرقمية إلى ملف أو تدفق باستخدام Aspose.Cells for Node.js via C++. الوصول إلى البيانات الخام لشهادات VBA الرقمية.
---

{{% alert color="primary" %}}

Aspose.Cells تسمح لك بتصدير شهادة VBA الرقمية إلى تيار مثل ملف أو تيار الذاكرة. يمكنك الوصول إلى البيانات الخام لشهادة VBA الرقمية باستخدام الخاصية [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--).

{{% /alert %}}

## **تصدير شهادة VBA إلى ملف أو تدفق في Node.js**

يرجى الاطلاع على الرمز العيني التالي الذي يحفظ البيانات الخام لشهادة VBA في ملف. يمكنك تنزيل [ملف الإكسل العيني المستخدم في هذا الرمز](5115031.xlsm) من الرابط المقدم.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file into workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleVBAProjectSigned.xlsm"));

// Retrieve bytes data of Digital Certificate of VBA Project
const certBytes = workbook.getVbaProject().getCertRawData();

// Save Certificate Data into FileStream
require("fs").writeFileSync(path.join(dataDir, "Cert_out_"), Uint8Array.from(certBytes));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
