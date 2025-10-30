---
title: Gizli Sayfa İçeriğini HTML ye Kaydederken Dışa Aktarmayı Engelle Node.js ve C++ ile
linktitle: HTML ye Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelleyin
type: docs
weight: 210
url: /tr/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aspose.Cells for Node.js via C++ kullanarak HTML ye kaydederken gizli sayfa içeriğinin dışa aktarımını nasıl engelleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML olarak kaydedebilirsiniz. Ancak, çalışma kitabı gizli çalışma sayfalarını içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini (_files) dizinine dışa aktarır. Bu dizin, çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css gibi dosyalar içerir. Bazı durumlarda, gizli çalışma sayfalarının bu şekilde içeriğinin dışa aktarılması uygun olmayabilir. Örneğin, gizli çalışma sayfası dışa aktarılmaması gereken resimler içeriyorsa.

{{% /alert %}}

Aspose.Cells for Node.js via C++, [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--) özelliği sağlar. Varsayılan olarak **true** olarak ayarlanmıştır ve gizli sayfalar HTML'ye dışa aktarılır. Bunu **false** yaparsanız, Aspose.Cells gizli sayfa içeriğini dışa aktarmaz.

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
