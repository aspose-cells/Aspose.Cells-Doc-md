---
title: Filtrar proyecto VBA al cargar un libro de trabajo con Node.js mediante C++
linktitle: Filtrar proyecto VBA al cargar un libro de trabajo
type: docs
weight: 140
url: /es/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Aprenda cómo filtrar proyectos VBA al cargar libros de Excel usando Aspose.Cells for Node.js via C++.
---

## **Filtrar proyecto VBA al cargar un libro de Excel en Node.js mediante C++**

Algunos archivos .xlsm/.xslb tienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells for Node.js via C++ cargará incondicionalmente estos datos (meta) al abrir dichos libros. Puede que necesite controlar esto mediante [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) cuando realmente solo necesita extraer nombres de hojas para una gran cantidad de libros, saltándose contenido innecesario. Este filtro se proporciona introduciendo una nueva opción, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions).

## **Código de muestra**

El siguiente código de muestra carga un libro de trabajo de manera que solo VBA está filtrado. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
