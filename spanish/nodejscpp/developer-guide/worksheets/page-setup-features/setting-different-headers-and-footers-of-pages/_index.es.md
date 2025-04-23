---
title: Configurar encabezados y pies de página diferentes para distintas páginas con Node.js usando C++
linktitle: Configuración de diferentes encabezados y pies de página para diferentes páginas
type: docs
weight: 35
url: /es/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Este artículo proporciona código de ejemplo que muestra cómo configurar programáticamente los encabezados y pies de página de la configuración de página de la hoja de cálculo de Excel usando Aspose.Cells for Node.js via C++. Configura encabezados y pies de página para las primeras, impares y pares páginas.
keywords: Configurar encabezado y pie de página en Excel para la primera página con Node.js usando C++, configurar encabezado y pie de página en páginas impares con Node.js usando C++, configurar encabezado y pie de página en páginas pares con Node.js usando C++
---

{{% alert color="primary" %}}

 MS Excel admite la configuración de diferentes encabezados y pies de página para la primera página, páginas impares y pares desde Excel 2007.
Aspose.Cells for Node.js via C++ admite la misma función.

{{% /alert %}}

## **Configuración de diferentes encabezados y pies de página en MS Excel**

**![Configuración de diferentes encabezados y pies de página](difpage.png)**

1. Haz clic en **diseño de página > títulos de impresión > encabezado/pie de página**.
1. Verifica **Diferentes páginas impares y pares** o **Primera página diferente**.
1. Ingrese encabezados y pies de página diferentes.

## **Configurar encabezados y pies de página diferentes con Aspose.Cells for Node.js via C++**

Aspose.Cells se comporta igual que Excel.
1. Establece las banderas [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) y [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. Ingrese encabezados y pies de página diferentes.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
