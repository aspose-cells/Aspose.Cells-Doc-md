---
title: Aggiorna l elemento di formula Power Query con Node.js tramite C++
linktitle: Aggiornare l Elemento della Formula di Power Query
type: docs
weight: 120
url: /it/nodejs-cpp/update-power-query-formula-item/
description: Impara come aggiornare la fonte dati dell elemento Formula Power Query in un file Excel usando Aspose.Cells for Node.js via C++.
---

## **Scenario di Utilizzo**

Potrebbero esserci casi in cui i file di origine dati vengono spostati e il file Excel non riesce a individuare il file. In tali casi, l'API Aspose.Cells offre l'opzione di aggiornare l'elemento Formula Power Query utilizzando la classe [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) per aggiornare la posizione del file sorgente.

## **Aggiornare elemento della Formula Power Query**

L'API Aspose.Cells fornisce la possibilità di aggiornare gli elementi di formula Power Query. Il seguente frammento di codice dimostra come aggiornare la posizione del file di origine dei dati nel file Excel usando la proprietà [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--). I file di origine e di output sono allegati per referenza.

- [File di origine 1](106364953.xlsx)
- [File di origine 2](106364954.xlsx)
- [File di output](106364955.xlsx)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();

const powerQueryFormulas = mashupData.getPowerQueryFormulas();
const count = powerQueryFormulas.getCount();
for (let i = 0; i < count; i++) 
{
const formula = powerQueryFormulas.get(i);
const items = formula.getPowerQueryFormulaItems();
const itemsCount = items.getCount();
for (let j = 0; j < itemsCount; j++) 
{
const item = items.get(j);
if (item.getName() === "Source") 
{
item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
}
}
}

// Save the output workbook.
workbook.save(outputDir + "SamplePowerQueryFormula_out.xlsx");
```
