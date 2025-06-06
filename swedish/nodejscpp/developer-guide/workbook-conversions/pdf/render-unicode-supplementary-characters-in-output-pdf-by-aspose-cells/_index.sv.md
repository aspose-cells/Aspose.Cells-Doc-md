---
title: Rendera Unicode tilläggstecken i utdata PDF av Aspose.Cells for Node.js via C++
linktitle: Rendera Unicode Supplementary tecken i utmatning PDF med Aspose.Cells
type: docs
weight: 350
url: /sv/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Lär dig hur man renderar Unicode tilläggstecken i utdata PDF med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Normala Unicode-tecken är 2 byte långa medan Unicode Supplementary-tecken är 4 byte långa. Aspose.Cells stöder nu rendering av dessa 4-byte Unicode-tecken.

I den Unicode-tekniska standarden är Supplementary-tecken de tecken som tilldelats kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}}

## Rendera Unicode-tilläggstecken i utdata-PDF av Aspose.Cells for Node.js via C++

Följande skärmbild visar hur Aspose.Cells renderade [källfilen excel](5115563.xlsx) till [utdata-PDF](5115564.pdf). Som du kan se har alla tre Unicode-tilläggstecken renderats precis som av Microsoft Excel.

![todo:image_alt_text](output.png)

## Exempelkod

Du kan använda följande exempelkod för att konvertera [källa excel-filen](5115563.xlsx) till [utdata PDF](5115564.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
