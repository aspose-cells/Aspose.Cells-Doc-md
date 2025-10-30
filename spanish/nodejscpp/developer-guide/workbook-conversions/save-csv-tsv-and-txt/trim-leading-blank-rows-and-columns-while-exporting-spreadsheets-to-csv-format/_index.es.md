---
title: Recortar filas y columnas en blanco iniciales al exportar hojas de cálculo en formato CSV con Node.js mediante C++
linktitle: Recortar Filas y Columnas en Blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 100
url: /es/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aprenda cómo recortar filas y columnas en blanco iniciales al exportar hojas de cálculo a formato CSV utilizando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

A veces, tu archivo de Excel o CSV tiene columnas o filas en blanco al principio. Por ejemplo, considera esta línea

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Aquí las tres primeras celdas o columnas están en blanco. Cuando abres un archivo CSV en Microsoft Excel, Microsoft Excel descarta estas filas y columnas en blanco.

Por defecto, Aspose.Cells for Node.js via C++ no elimina columnas y filas en blanco iniciales al guardar, pero si desea eliminarlas como lo hace Microsoft Excel, Aspose.Cells proporciona la propiedad [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--). Por favor, configúrela en **true** y todas las filas y columnas en blanco iniciales serán descartadas al guardar.

{{% alert color="primary" %}}

Antes del lanzamiento de Aspose.Cells for Node.js via C++ 20.4, el valor predeterminado de [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) era **false**. Desde la versión 20.4, el valor predeterminado de [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) es **true**.

{{% /alert %}}

## **Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV**

El siguiente código de ejemplo carga el [archivo Excel de origen](sampleTrimBlankColumns.xlsx) que tiene dos columnas en blanco al principio. Primero guarda el archivo Excel en formato CSV sin cambios y luego establece la propiedad [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) en **true** y lo guarda nuevamente. La captura de pantalla muestra el [archivo Excel fuente](sampleTrimBlankColumns.xlsx), el [archivo CSV sin recorte](outputWithoutTrimBlankColumns.csv) y el [archivo CSV con recorte](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
