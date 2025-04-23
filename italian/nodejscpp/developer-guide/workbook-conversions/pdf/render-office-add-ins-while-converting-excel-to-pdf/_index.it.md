---
title: Renderizza Componenti Aggiuntivi di Office durante la conversione di Excel in PDF con Node.js tramite C++
linktitle: Render Office Add Ins durante la conversione di Excel in PDF
type: docs
weight: 100
url: /it/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Possibili Scenari di Utilizzo**

In passato, Aspose.Cells non riusciva a rendere i Componenti Aggiuntivi di Office quando un file Excel veniva salvato in formato PDF. Ora Aspose.Cells li rende correttamente. Non è necessario utilizzare alcun metodo o proprietà speciale per rendere i Componenti Aggiuntivi di Office nel PDF di output. Basta salvare il file Excel in formato PDF e i componenti verranno renderizzati.

## **Render Office Add-Ins durante la conversione di Excel in PDF**

Il seguente esempio di codice salva il [file Excel di esempio](60489769.xlsx) che contiene gli componenti aggiuntivi di Office. Si prega di vedere il [PDF in output generato con la versione precedente, cioè 17.11](60489770.pdf) e il [PDF in output generato con la versione più recente, cioè 17.12 e successive](60489771.pdf). Il PDF della versione precedente è vuoto, mentre quello della versione più recente mostra l'Add-In di Office.

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
