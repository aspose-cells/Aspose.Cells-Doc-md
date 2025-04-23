---  
title: Node.js kullanarak ızgaralı Çizgilerle Excel i HTML ye aktarma  
linktitle: Excel den HTML e Grid Çizgileri ile Dışa Aktar  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Aspose.Cells for Node.js via C++ kullanarak, ızgaralı çizgilerle Excel dosyasını HTML ye nasıl aktaracağınızı öğrenin.  
---  

{{% alert color="primary" %}}  

İşte, HTML'ye ızgaralı çizgilerle Excel dosyanızı dışa aktarmak istiyorsanız, lütfen [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) özelliğini kullanın ve **true** yapın.

{{% /alert %}}  
## **Excel'den HTML'e Grid Çizgileri ile Dışa Aktar**  
Aşağıdaki örnek kod, bir çalışma kitabı oluşturur, sayfasına bazı değerler doldurur ve ardından [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) ayarını **true** yaparak HTML formatında kaydeder.  

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

