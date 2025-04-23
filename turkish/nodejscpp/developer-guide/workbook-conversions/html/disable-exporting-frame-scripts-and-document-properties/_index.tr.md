---
title: Node.js ve C++ kullanarak Çerçeve Betiklerini ve Döküman Özelliklerini Devre Dışı Bırakma
linktitle: HTML e Aktarmayı Devre Dışı Bırak Çerçeve Betikleri ve Belge Özellikleri
type: docs
weight: 310
url: /tr/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma kitabını HTML ye dönüştürürken çerçeve betiklerini ve belge özelliklerini devre dışı bırakmayı öğrenin.
--- 

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabını HTML'ye dönüştürürken çerçeve scriptleri ve belge özelliklerini dışa aktarır. Aspose.Cells for Node.js via C++'ün 8.6.0 sürümü, isteğe bağlı olarak çerçeve scriptlerini ve belge özelliklerini dışa aktarmayı devre dışı bırakmanızı sağlayan bir seçenek getirir. Lütfen `HtmlSaveOptions.exportFrameScriptsAndProperties` özelliğini kullanarak dışa aktarma işlemini devre dışı bırakın.

{{% /alert %}}

## **Çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırak**

Aşağıdaki örnek kod, çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırakmanıza olanak tanır. Bir çalışma kitabını HTML'e dönüştürdüğünüzde, çıktı dosyası herhangi bir çerçeve betiği ve belge özelliği içermez.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
