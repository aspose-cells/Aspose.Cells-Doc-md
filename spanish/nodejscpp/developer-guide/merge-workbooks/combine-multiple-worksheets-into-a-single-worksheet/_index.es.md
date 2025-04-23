---
title: Combinar varias hojas de trabajo en una sola utilizando Node.js a través de C++
linktitle: Combinar varias hojas de cálculo en una sola hoja de cálculo
type: docs
weight: 160
url: /es/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Aprende a combinar varias hojas de trabajo en una sola utilizando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

A veces necesitas combinar varias hojas de cálculo en una sola hoja de cálculo. Esto se puede lograr fácilmente utilizando la API de Aspose.Cells. Este artículo te mostrará un ejemplo de código que lee un libro de trabajo fuente y combina los datos de todas las hojas de cálculo fuente en una sola hoja de cálculo dentro de un libro de trabajo de destino.

{{% /alert %}} 

El siguiente fragmento de código te muestra cómo combinar varias hojas de cálculo en una sola hoja de cálculo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const destWorkbook = new AsposeCells.Workbook();
const destSheet = destWorkbook.getWorksheets().get(0);

let TotalRowCount = 0;

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
const sourceSheet = workbook.getWorksheets().get(i);

const sourceRange = sourceSheet.getCells().getMaxDisplayRange();
const destRange = destSheet.getCells().createRange(
sourceRange.getFirstRow() + TotalRowCount,
sourceRange.getFirstColumn(),
sourceRange.getRowCount(),
sourceRange.getColumnCount()
);

destRange.copy(sourceRange);
TotalRowCount += sourceRange.getRowCount();
}

const outputFilePath = path.join(dataDir, "Output.out.xlsx");
destWorkbook.save(outputFilePath);
``` 
