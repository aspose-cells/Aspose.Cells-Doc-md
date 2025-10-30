---
title: Actualizar el elemento de fórmula de Power Query con Node.js a través de C++
linktitle: Actualizar elemento de fórmula de Power Query
type: docs
weight: 120
url: /es/nodejs-cpp/update-power-query-formula-item/
description: Aprende cómo actualizar la fuente de datos del elemento de fórmula de Power Query en un archivo Excel usando Aspose.Cells for Node.js via C++.
---

## **Escenario de uso**

Puede haber casos en los que los archivos de fuente de datos se mueven y el archivo Excel no puede localizar el archivo. En tales casos, la API de Aspose.Cells ofrece la opción de actualizar el elemento de fórmula de Power Query utilizando la clase [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) para actualizar la ubicación del archivo fuente.

## **Actualizar elemento de fórmula de Power Query**

La API de Aspose.Cells proporciona la capacidad de actualizar los elementos de fórmula de Power Query. El siguiente fragmento de código demuestra cómo actualizar la ubicación del archivo de fuente de datos en el archivo Excel usando la propiedad [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--). Los archivos de origen y de salida adjuntos son para su referencia.

- [Archivo de origen 1](106364953.xlsx)
- [Archivo de origen 2](106364954.xlsx)
- [Archivo de salida](106364955.xlsx)

## **Código de muestra**

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
