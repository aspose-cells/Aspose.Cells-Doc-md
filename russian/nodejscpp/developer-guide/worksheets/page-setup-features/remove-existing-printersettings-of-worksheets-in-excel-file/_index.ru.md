---
title: Удалить существующие настройки принтера из листов Excel файла с помощью Node.js через C++
linktitle: Удаление существующих настроек принтера листов в файле Excel
type: docs
weight: 60
url: /ru/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: В этой статье вы узнаете, как программно удалить существующие настройки принтера листа внутри файла Excel с помощью Aspose.Cells for Node.js via C++.
keywords: удаление настроек принтера листа в Node.js через C++, удаление настроек принтера листа Excel в Node.js через C++
---

## **Возможные сценарии использования**
Иногда разработчики хотят предотвратить Excel от включения файлов настроек принтера *.bin* в сохраненные файлы XLSX. Файлы настроек принтера расположены в папке *“[file "root"]\xl\printerSettings”.* В этом документе объясняется, как удалить существующие настройки принтера с использованием Aspose.Cells APIs.

## **Удаление текущих настроек принтера на листах Excel**
Aspose.Cells позволяет удалять существующие настройки принтера, указанные для различных листов в файле Excel. В приведенном ниже образце кода показано, как удалить существующие настройки принтера для всех листов в книге. Пожалуйста, ознакомьтесь с [образцом файла Excel](45056020.xlsx), [выходным файлом Excel](45056021.xlsx), выводом консоли, а также скриншотами для справки.

## **Снимок экрана**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Образец кода**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");
const wb = new AsposeCells.Workbook(filePath);

// Get the sheet counts of the workbook
const sheetCount = wb.getWorksheets().getCount();

// Iterate all sheets
for (let i = 0; i < sheetCount; i++) {
// Access the i-th worksheet
const ws = wb.getWorksheets().get(i);

// Access worksheet page setup
const ps = ws.getPageSetup();

// Check if printer settings for this worksheet exist
if (ps.getPrinterSettings() != null) {
// Print the following message
console.log("PrinterSettings of this worksheet exist.");

// Print sheet name and its paper size
console.log("Sheet Name: " + ws.getName());
console.log("Paper Size: " + ps.getPaperSize());

// Remove the printer settings by setting them null
ps.setPrinterSettings(null);
console.log("Printer settings of this worksheet are now removed by setting it null.");
console.log("");
} // if
} // for

// Save the workbook
wb.save(path.join(outputDir, "outputRemoveExistingPrinterSettingsOfWorksheets.xlsx"));
```

## **Вывод в консоль**
{{< highlight javascript >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
