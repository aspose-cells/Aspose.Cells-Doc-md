---
title: حفظ كـ ODF 1.1، 1.2 و 1.3 باستخدام Node.js عبر C++
linktitle: حفظ ملف ODS بصيغة ODF 1.1 و 1.2 و 1.3
description: تحويل إكسل إلى مواصفات ODF 1.1 و 1.2 و 1.3 باستخدام Aspose.Cells for Node.js via C++.
type: docs
weight: 230
url: /ar/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells حفظ ملف ODS (**جداول بيانات المستند المفتوح**) بصيغة ODF (**صيغة المستند المفتوح**) وفقًا لمواصفات 1.1 و 1.2 و 1.3. لدى Aspose.Cells خاصية [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) التي تحدد إصدار ODF لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/)، لذلك الملف ODS المحفوظ بدون ضبط هذه الخاصية يستخدم مواصفات 1.2.

{{% /alert %}}

يفترض الكود النموذجي أدناه إنشاء كائن عمل، يضيف قيمة إلى الخلية A1 في الورقة الأولى ثم يقوم بحفظ ملف ODS وفقًا لمواصفات ODF 1.1 و 1.2 و 1.3. بشكل افتراضي، يتم حفظ ملف ODS بمواصفات ODF 1.2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
