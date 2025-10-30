---
title: Power Query Formular Element mit Node.js über C++ aktualisieren
linktitle: Aktualisieren des Power Query Formelelements
type: docs
weight: 120
url: /de/nodejs-cpp/update-power-query-formula-item/
description: Erfahren Sie, wie Sie die Datenquelle des Power Query Formularelements in einer Excel Datei mit Aspose.Cells for Node.js via C++ aktualisieren.
---

## **Anwendungsszenario**

Es kann Fälle geben, in denen die Quelldateien verschoben werden und die Excel-Datei die Datei nicht finden kann. In solchen Fällen bietet die API von Aspose.Cells die Option, das Power Query-Formularelement zu aktualisieren, indem die Klasse [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) verwendet wird, um den Speicherort der Quelldatei zu aktualisieren.

## **Aktualisierung des Power Query Formel-Elements**

Die API von Aspose.Cells bietet die Möglichkeit, Power Query Formular-Items zu aktualisieren. Der folgende Codeausschnitt zeigt, wie die Speicherort-Update in der Excel-Datei durch Nutzung der Eigenschaft [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--) durchgeführt wird. Die Quelldatei und die Ausgabedatei sind zum Referenzanhang beigefügt.

- [Quelldatei 1](106364953.xlsx)
- [Quelldatei 2](106364954.xlsx)
- [Ausgabedatei](106364955.xlsx)

## **Beispielcode**

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
