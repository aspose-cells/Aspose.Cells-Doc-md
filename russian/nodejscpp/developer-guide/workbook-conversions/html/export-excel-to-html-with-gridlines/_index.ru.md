---  
title: Экспорт Excel в HTML с линиями сетки с помощью Node.js  
linktitle: Экспорт Excel в HTML с сеткой  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Узнайте, как экспортировать файл Excel в формат HTML с линиями сетки с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Если вы хотите экспортировать ваш файл Excel в HTML с линиями сетки, используйте свойство [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) и установите его в **true**.

{{% /alert %}}  
## **Экспорт Excel в HTML с сеткой**  
Следующий пример кода создает рабочую книгу, заполняет лист значениями и затем сохраняет его в формате HTML после установки свойства [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) в **true**.  

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

