---
title: Renderizza caratteri Unicode di livello supplementare nel PDF di output usando Aspose.Cells for Node.js via C++
linktitle: Rendere i caratteri supplementari Unicode nel PDF di output con Aspose.Cells
type: docs
weight: 350
url: /it/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Impara come rendere i caratteri Unicode di livello supplementare nel PDF di output usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri supplementari Unicode sono lunghi 4 byte. Aspose.Cells ora supporta il rendering di questi caratteri Unicode a 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri assegnati a punti codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità di 16 bit).

{{% /alert %}}

## Renderizza caratteri Unicode di livello supplementare nel PDF di output con Aspose.Cells for Node.js via C++

Lo screenshot seguente mostra come Aspose.Cells ha renderizzato il [file Excel di origine](5115563.xlsx) nel [PDF di output](5115564.pdf). Come puoi vedere, tutti e tre i caratteri Unicode di livello supplementare sono stati resi esattamente come fatto da Microsoft Excel.

![todo:image_alt_text](output.png)

## Codice di esempio

Puoi utilizzare questo codice di esempio per convertire [file di Excel di origine](5115563.xlsx) in [PDF di output](5115564.pdf).

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
{{< app/cells/assistant language="nodejs-cpp" >}}
