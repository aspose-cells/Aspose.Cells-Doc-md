---
title: Filtrar Objetos al cargar Workbook o Worksheet con Node.js vía C++
linktitle: Filtrar objetos al cargar el libro o la hoja de trabajo
type: docs
weight: 330
url: /es/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aprenda a filtrar datos al cargar libros de trabajo o hojas de cálculo usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**
Por favor, utilice la propiedad [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) al filtrar datos del libro. Pero si desea filtrar datos de hojas individuales, deberá sobreescribir el método [LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/nodejs-cpp/loadfilter/#startSheet-worksheet-). Proporcione un valor apropiado del enumerador [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) al crear o trabajar con [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter).

El enumerador [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) tiene los siguientes valores posibles.

- Todo
- Configuraciones del libro
- Celda en blanco
- Celda booleana
- Datos de celda
- Error de celda
- Numérico de celda
- Cadena de celda
- Valor de celda
- Chart
- Formato condicional
- Validación de datos
- Nombres definidos
- Propiedades del documento
- Fórmula
- Hipervínculos
- Área fusionada
- Tabla Dinámica
- Configuración
- Forma
- Datos de Hoja
- Configuraciones de Hoja
- Estructura
- Estilo
- Tabla
- VBA
- MapaXml

## **Objetos de Filtro al cargar el Libro**
El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro. Por favor, revise el [archivo de Excel de ejemplo](5115258.xlsx) utilizado en este código y el [PDF de salida](5115257.pdf) generado por él. Como se puede ver en el PDF de salida, todos los gráficos han sido filtrados fuera del libro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **Objetos de Filtro al cargar la Hoja de Trabajo**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115255.xlsx) y filtra los siguientes datos de sus hojas de trabajo usando un filtro personalizado.

- Filtra los gráficos de la hoja de trabajo llamada SinGráficos.
- Filtra las formas de la hoja de trabajo llamada SinFormas.
- Filtra el formato condicional de la hoja de trabajo llamada SinFormatoCondicional.

Una vez que carga el [archivo de Excel fuente](5115255.xlsx) con un filtro personalizado, toma las imágenes de todas las hojas una por una. Aquí están las imágenes de salida para su referencia. Como se puede ver, la primera imagen no tiene gráficos, la segunda imagen no tiene formas y la tercera imagen no tiene formato condicional.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

Así es como se usa la clase CustomLoadFilter según los nombres de las hojas de cálculo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
