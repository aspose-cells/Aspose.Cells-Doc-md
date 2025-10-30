---
title: Uppdatera Power Query formelobjekt med Node.js via C++
linktitle: Uppdatera Power Query formelobjekt
type: docs
weight: 120
url: /sv/nodejs-cpp/update-power-query-formula-item/
description: Lär dig hur du uppdaterar datakällan för Power Query formelobjekt i en Excel fil med Aspose.Cells for Node.js via C++.
---

## **Användningsscenarie**

Det kan finnas tillfällen då datakällfiler flyttas och Excel-filen inte kan hitta filen. I sådana fall ger Aspose.Cells API möjligheten att uppdatera Power Query Formula-objektet genom att använda `[ *PowerQueryFormulaItem* ]`-klassen för att ändra platsen för källdokumentet.

## **Uppdatera Power Query-formelobjekt**

Aspose.Cells API ger möjlighet att uppdatera Power Query Formulelementen. Följande kodexempel visar hur man uppdaterar filplatsen för datakällan i Excel-filen genom att använda `[**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--)`-egenskapen. Källdokument och utdatafiler är bifogade för referens.

- [Källfil 1](106364953.xlsx)
- [Källfil 2](106364954.xlsx)
- [Utdatafil](106364955.xlsx)

## **Exempelkod**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
