---
title: Obtener el ancho y la altura del papel en la configuración de página de la hoja de trabajo con Node.js usando C++
linktitle: Obtener el ancho y alto del papel del Diseño de página de la hoja de cálculo
type: docs
weight: 50
url: /es/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Descubre cómo obtener el ancho y la altura del papel de la página de la hoja de cálculo de Excel usando Node.js con C++ de forma programática.
keywords: configuración de página de Excel ancho del papel en Node.js usando C++, altura del papel en Node.js usando C++
---

## **Escenarios de uso posibles**

A veces, necesitas conocer el ancho y la altura del tamaño del papel configurado en la configuración de página de la hoja de trabajo. Usa las propiedades [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) y [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) para este propósito.

## **Obtener el ancho y alto del papel del diseño de página de la hoja de cálculo**

El siguiente código de ejemplo explica el uso de las propiedades [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) y [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--). Primero cambia el tamaño del papel a *A2* y luego encuentra el ancho y la altura del papel, después lo cambia a *A3*, *A4*, *Carta* y encuentra el ancho y la altura del papel respectivamente.

### **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **Salida de la consola**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
