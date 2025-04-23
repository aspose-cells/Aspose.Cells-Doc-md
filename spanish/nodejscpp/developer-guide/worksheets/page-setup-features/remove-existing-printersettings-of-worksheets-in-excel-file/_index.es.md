---
title: Eliminar la configuración de impresora existente de las hojas de trabajo en un archivo de Excel con Node.js usando C++
linktitle: Eliminar Configuraciones de Impresora Existente de Hojas de Cálculo en Archivo Excel
type: docs
weight: 60
url: /es/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: En este artículo, aprenderás cómo eliminar la configuración de impresora existente de una hoja de cálculo dentro de un archivo de Excel de forma programática usando Aspose.Cells for Node.js via C++.
keywords: Eliminar la configuración de impresora de la hoja de trabajo con Node.js usando C++, eliminar la configuración de impresora de la hoja de cálculo con Node.js usando C++
---

## **Escenarios de uso posibles**
A veces, los desarrolladores desean evitar que Excel incluya archivos * .bin * de la configuración de impresora en los archivos XLSX guardados. Los archivos de configuración de impresora se encuentran en * "[file \"root\"] \xl \ printerSettings". *  Este documento explica cómo eliminar la configuración de impresora existente utilizando las API de Aspose.Cells.

## **Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel**
Aspose.Cells te permite eliminar la configuración de impresora existente especificada para diferentes hojas en el archivo de Excel. El siguiente código de ejemplo ilustra cómo eliminar la configuración de impresora existente para todas las hojas de trabajo en el libro. Consulta su [archivo de Excel de muestra](45056020.xlsx), [archivo de Excel de salida](45056021.xlsx), salida de la consola y captura de pantalla como referencia.

## **Captura de pantalla**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Código de muestra**
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

## **Salida de la consola**
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
