---
title: Cambiar la fuente de datos del gráfico a la hoja destino mientras se copian filas o rangos con Node.js mediante C++
linktitle: Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango
description: Aprende cómo cambiar la fuente de datos de un gráfico a una hoja de destino al copiar filas o un rango en Aspose.Cells for Node.js via C++. Esta guía demuestra cómo actualizar el rango de datos del gráfico y vincularlo a la hoja de destino.
keywords: Aspose.Cells for Node.js via C++, gráficos, fuente de datos, hoja de destino, filas, rango, copia, actualización, rango de datos, enlace.
type: docs
weight: 440
url: /es/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Escenarios de uso posibles**

Cuando copias filas o rangos que contienen gráficos a una nueva hoja, la fuente de datos del gráfico no cambia. Por ejemplo, si la fuente de datos del gráfico es `=Sheet1!$A$1:$B$4`, después de copiar filas o rango a una nueva hoja, la fuente de datos seguirá siendo la misma, es decir, `=Sheet1!$A$1:$B$4`. Aún hace referencia a la hoja antigua, es decir, Sheet1. Este también es el comportamiento en Microsoft Excel. Pero si quieres que apunte a la nueva hoja de destino, usa la propiedad [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) y establecela en **true** al llamar al método [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-). Ahora, si tu hoja de destino es DestSheet, la fuente de datos de tu gráfico cambiará de `=Sheet1!$A$1:$B$4` a `=DestSheet!$A$1:$B$4`.

## **Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango**

El siguiente código de ejemplo explica cómo usar la propiedad [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) al copiar filas o rangos que contienen gráficos a una nueva hoja. El código usa el [archivo de ejemplo en Excel](5113699.xlsx) y genera el [archivo de salida en Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
