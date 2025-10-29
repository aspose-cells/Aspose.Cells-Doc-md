---
title: منع تصدير محتوى المصنف المخفي عند الحفظ إلى HTML باستخدام Node.js عبر C++
linktitle: منع تصدير محتويات ورقة عمل مخفية عند الحفظ إلى HTML
type: docs
weight: 210
url: /ar/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: تعلم كيفية منع تصدير محتوى الورقة المخفي عند حفظ ملفات إكسل إلى HTML باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

يمكنك حفظ سجلات العمل في Excel إلى HTML. ومع ذلك، إذا كانت سجلات العمل تحتوي على أوراق عمل مخفية، فإن Aspose.Cells بشكل افتراضي يصدر محتويات ورقة العمل المخفية إلى دليل الإخراج الخاص ب HTML (_files) الذي يحتوي على ملفات مثل أوراق العمل، الصور، tabstrip.htm، stylesheet.css إلخ. في بعض الأحيان، سيصدر محتوى أوراق العمل المخفية بهذه الطريقة ليس مناسبًا. على سبيل المثال، إذا كانت ورقة العمل المخفية تحتوي على صور يجب عدم تصديرها إلى دليل _files.

{{% /alert %}}

يوفر Aspose.Cells for Node.js via C++ الخاصية [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--). بشكل افتراضي، تكون مضبوطة على **true** ويتم تصدير الأوراق المخفية إلى HTML. إذا قمت بضبطها على **false**، فلن يصدِّر Aspose.Cells محتوى الأوراق المخفية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
