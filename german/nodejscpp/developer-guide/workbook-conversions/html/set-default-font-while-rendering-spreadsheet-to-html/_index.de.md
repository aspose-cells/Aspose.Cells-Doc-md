---  
title: Standard Schriftart beim Rendern eines Tabellenblatts zu HTML mit Node.js über C++ festlegen  
linktitle: Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest  
type: docs  
weight: 370  
url: /de/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Mit Aspose.Cells können Sie beim Rendern von Tabellenkalkulationen in HTML die Standardschriftart festlegen. Verwenden Sie hierfür [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--). Diese Eigenschaft ist nützlich, wenn einige Zellen in einer Tabellenkalkulation ungültige oder nicht vorhandene Schriftarten aufweisen. Dann werden diese Zellen in einer Schriftart gerendert, die mit der Eigenschaft [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) festgelegt ist.  
{{% /alert %}}  

## Festlegen der Standardschriftart beim Rendern von Tabellenkalkulationen in HTML  

Der folgende Beispielscode erstellt eine Arbeitsmappe und fügt einen Text in Zelle B4 des ersten Arbeitsblatts hinzu und legt die Schriftart auf eine unbekannte/nicht vorhandene Schriftart fest. Dann speichert er die Arbeitsmappe in HTML, indem er verschiedene Standardschriftart-Namen wie Courier New, Arial, Times New Roman usw. festlegt.  

Das Screenshot zeigt die Auswirkung der Einstellung verschiedener Standard-Schriftartnamen über die Eigenschaft [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

Der Code generiert die [Ausgabe-HTML-Datei mit Courier New](5115516), die [Ausgabe-HTML mit Arial](5115518) und die [Ausgabe-HTML-Datei mit Times New Roman](5115517).  

## Beispielcode  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

