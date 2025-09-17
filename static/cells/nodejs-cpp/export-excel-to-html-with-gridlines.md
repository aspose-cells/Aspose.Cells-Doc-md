##Export Excel to HTML with GridLines via Node.js
Learn how to export an Excel file to HTML format with GridLines using Aspose.Cells for Node.js via C++.
If you want to export your Excel file into HTML with GridLines, then please use the [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) property and set it **true**.
## **Export Excel to HTML with GridLines**
The following sample code creates a workbook, fills its worksheet with some values, and then saves it in HTML format after setting the [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) to **true**.
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
