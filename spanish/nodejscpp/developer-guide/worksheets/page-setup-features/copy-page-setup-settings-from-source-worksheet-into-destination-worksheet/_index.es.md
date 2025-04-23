---
title: Copiar configuraciones de la configuración de página desde la hoja de origen a la hoja de destino con Node.js vía C++
linktitle: Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino
type: docs
weight: 80
url: /es/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Este artículo explica cómo usar la API de Node.js o el código de ejemplo de la biblioteca C++ para copiar las configuraciones de la configuración de página desde una hoja de origen a una hoja de destino programáticamente.
keywords: configurar la configuración de la página en copia de página Node.js usando C++, copiar la configuración de la página a la hoja de trabajo de destino Node.js usando C++
---

## **Escenarios de uso posibles**

Cuando agregas una nueva hoja a un libro, contiene la configuración predeterminada de *Configurar página*. Puede haber momentos en los que necesites transferir la configuración ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) de una hoja a otra. Este documento explica cómo copiar la configuración de página de una hoja a otra usando las API Aspose.Cells for Node.js via C++.

## **Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino**

El siguiente código de ejemplo ilustra cómo copiar las *Configuraciones de Configuración de Página* de una hoja a otra utilizando el método [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-). Por favor, consulta el siguiente código de ejemplo y su salida en consola para una referencia.

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **Salida de la consola**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
