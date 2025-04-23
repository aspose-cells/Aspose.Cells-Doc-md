---  
title: تصدير Excel إلى HTML مع خطوط الشبكة عبر Node.js  
linktitle: تصدير Excel إلى HTML مع خطوط الشبكة  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: تعلم كيفية تصدير ملف Excel إلى تنسيق HTML مع خطوط الشبكة باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

إذا رغبت في تصدير ملف Excel الخاص بك إلى HTML مع خطوط الشبكة، يرجى استخدام الخاصية [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) وتعيينها على **true**.

{{% /alert %}}  
## **تصدير Excel إلى HTML مع خطوط الشبكة**  
يُنشئ رمز المثال التالي كتاب عمل، يملأ ورقة العمل بقيم ثم يحفظه بصيغة HTML بعد ضبط [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) إلى **true**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create your workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Fill worksheet with some integer values
for (let r = 0; r < 10; r++) {
for (let c = 0; c < 10; c++) {
ws.getCells().get(r, c).putValue(r * 1);
}
}

// Save your workbook in HTML format and export gridlines
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportGridLines(true);
wb.save(path.join(dataDir, "ExportToHTMLWithGridLines_out.html"), opts);
```  

