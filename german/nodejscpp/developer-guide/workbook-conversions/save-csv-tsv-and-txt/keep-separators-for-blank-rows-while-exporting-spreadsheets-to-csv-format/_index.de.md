---  
title: Behalte Trenner für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format mit Node.js über C++  
linktitle: Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV Format beibehalten  
type: docs  
weight: 160  
url: /de/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten**  

Aspose.Cells bietet die Möglichkeit, Zeilentrenner beim Konvertieren von Tabellenkalkulationen ins CSV-Format beizubehalten. Dafür können Sie die [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) Eigenschaft von [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/) verwenden. [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) ist eine Boolesche Eigenschaft. Um die Trenner für leere Zeilen beim Konvertieren der Excel-Datei in CSV beizubehalten, setzen Sie die [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) Eigenschaft auf **true**.  

Der folgende Beispielcode lädt die [Quellexcel-Datei](84378743.xlsx). Es setzt die [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--)-Eigenschaft auf **true** und speichert sie als [output.csv](84378744.csv). Der Screenshot zeigt den Vergleich zwischen der Quell-Excel-Datei, der standardmäßigen Ausgabe beim Konvertieren in CSV und der Ausgabe, die durch Setzen von [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) auf **true** erzeugt wurde.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

