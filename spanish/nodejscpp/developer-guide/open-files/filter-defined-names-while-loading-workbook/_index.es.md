---
title: Filtrar Nombres definidos al cargar Workbook con Node.js vía C++
linktitle: Filtrar nombres definidos al cargar el libro de trabajo
type: docs
weight: 50
url: /es/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells le permite filtrar o eliminar nombres definidos presentes en el libro de trabajo. Por favor, utilice [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) para cargar nombres definidos y [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) para eliminarlos al cargar el libro. Tenga en cuenta que, si elimina los nombres definidos, las fórmulas dentro del libro pueden dejar de funcionar.

## **Filtrar nombres definidos al cargar el libro de trabajo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767860.xlsx) que tiene una fórmula en la celda **C1** que contiene los nombres definidos, es decir, *=SUM(MyName1, MyName2)*. Como estamos usando [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) para eliminar los nombres definidos al cargar el libro, la fórmula en la celda C1 en el [archivo de Excel de salida](61767861.xlsx) se rompe y muestra *#NAME?* en su lugar. Por favor, vea la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
