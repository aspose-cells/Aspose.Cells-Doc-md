---
title: Determinar si el tamaño de papel de la hoja de trabajo es automático con Node.js usando C++
linktitle: Determinar si el Tamaño de Papel de la Hoja de Cálculo es Automático
type: docs
weight: 90
url: /es/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Este artículo explica cómo usar la API de Node.js con complementos C++ para determinar si el tamaño de papel de una hoja de trabajo está configurado en automático de forma programática.
keywords: Determinar si el tamaño de papel de la hoja de trabajo es automático con Node.js usando C++
---

## **Escenarios de uso posibles**

La mayoría de las veces, el tamaño del papel de la hoja de trabajo es automático. Cuando es automático, a menudo está configurado como *Carta*. Algunas veces, el usuario configura el tamaño del papel de la hoja de acuerdo con sus requisitos. En este caso, el tamaño del papel no es automático. Puedes averiguar si el tamaño del papel de la hoja de trabajo es automático o no usando la propiedad [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--).

## **Determinar si el tamaño de papel de la hoja de cálculo es automático**

El código de muestra proporcionado a continuación carga los dos siguientes archivos de Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

y averigua si el tamaño de papel de su primera hoja de cálculo es automático o no. En Microsoft Excel, puedes verificar si el tamaño de papel es automático o no a través de la ventana de Configuración de página como se muestra en esta captura de pantalla.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con los archivos de Excel de muestra proporcionados.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
