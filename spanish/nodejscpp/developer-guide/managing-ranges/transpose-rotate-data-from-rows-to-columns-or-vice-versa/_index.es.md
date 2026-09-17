---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
linktitle: Transponer Rango
url: /es/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Node.js via C++ library, hoja de cálculo, transponer rango, rotar datos, función TRANSPOSE, fórmula de matriz dinámica, fórmula de matriz, Excel TRANSPOSE, Filas a Columnas
type: docs
weight: 80
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ admite la transposición (rotación) de datos de manera que las filas se conviertan en columnas y las columnas en filas de tres formas diferentes. El primer enfoque utiliza el método en el lugar `range.transpose()` y funciona en todas las versiones de Excel, mientras que el segundo utiliza `cell.setDynamicArrayFormula()` para escribir una fórmula moderna de matriz dinámica `=TRANSPOSE(...)` que se desborda automáticamente en Excel 365 o Excel 2021. El tercer enfoque utiliza `cell.setArrayFormula()` para escribir una fórmula de matriz clásica Ctrl+Shift+Enter (CSE) que es compatible con versiones anteriores de Excel. Este artículo recorre cada enfoque con instrucciones paso a paso y ejemplos de código completos.
{{% /alert %}}

## **Introducción**
Transponer un rango significa rotarlo de manera que lo que era una fila se convierta en una columna y lo que era una columna se convierta en una fila, reflejando efectivamente los datos a través de su diagonal principal. En Microsoft Excel, la función de hoja de cálculo `TRANSPOSE` realiza esta operación, y la referencia conceptual está documentada en [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La misma idea puede aplicarse mediante programación a un rango de celdas, lo cual es útil en muchos escenarios empresariales y de informes.
Los escenarios comunes donde la transposición resulta útil incluyen los siguientes.
- Reorientar informes trimestrales o anuales de ventas donde los trimestres normalmente se extienden a lo largo de la página y las regiones van hacia abajo, o viceversa.
- Intercambiar la orientación de los ejes en paneles o gráficos para que una serie temporal se ejecute hacia abajo en lugar de a lo largo de la página.
- Reformar los datos importados de sistemas externos para que coincidan con el diseño esperado por las plantillas de análisis o informes posteriores.
Para hacer concreto el resto del artículo, cada ejemplo utiliza la siguiente tabla pequeña de ventas por región y por trimestre. En el libro de trabajo de muestra esta tabla ocupa el rango **A1:D5**, con **A1** vacío como la esquina superior izquierda, **B1:D1** con los encabezados de las regiones y **A2:A5** con los encabezados de los trimestres.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
A continuación, el artículo presenta tres formas diferentes de transponer estos datos usando Aspose.Cells for Node.js via C++, cada una adecuada para una versión de Excel y un caso de uso diferentes.

## **Enfoque 1 — Transponer Rango en el Lugar (range.transpose)**
Use este enfoque siempre que desee transponer datos sin involucrar la función de hoja de cálculo `TRANSPOSE`. Funciona en **todas las versiones de Excel** y no depende de las matrices dinámicas, lo que lo convierte en la opción más segura y compatible entre versiones. Es ideal cuando solo necesita el resultado final transpuesto y no necesita conservar la fórmula `TRANSPOSE` original en el libro de trabajo.

### **API utilizada**
`range.transpose()` es un método de instancia de la clase `Aspose.Cells.Range`. Al llamarlo, el rango se voltea en su lugar intercambiando sus filas y columnas, de modo que lo que era una fila se convierte en una columna y lo que era una columna se convierte en una fila. El método modifica las celdas subyacentes directamente sin escribir una fórmula.

### **Pasos**
1. Abra el libro de trabajo de origen con `LoadOptions` configurado en el formato `.xlsx` llamando a `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recupere la primera hoja de cálculo del libro de trabajo usando `workbook.getWorksheets().get(0)`.
3. Acceda a la colección de celdas de la hoja de cálculo mediante `worksheet.getCells()`.
4. Cree el rango de origen que cubre **A1:D5** llamando a `cells.createRange("A1:D5")`.
5. Llame a `source.transpose()` para rotar el rango en su lugar, intercambiando filas y columnas.
6. Guarde el libro de trabajo con `workbook.save(outputFile)`.
Tras la transposición, el mismo rango de anclaje contiene los datos rotados. La primera fila se lee (vacía, **Europe**, **Asia**, **North America**) y la primera columna se lee (vacía, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Cada columna original de ventas se convierte en una fila del rango transpuesto.

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Enfoque 2 — Transponer con una Fórmula de Matriz Dinámica (Excel 365 / 2021)**
Use este enfoque cuando desee conservar la fórmula `=TRANSPOSE(A1:D5)` como una fórmula activa en el libro de trabajo de salida, de modo que el resultado se actualice automáticamente si los datos de origen cambian, y el archivo de Excel de destino se abrirá en **Excel 365 / Excel 2021 o posterior**, donde se admiten matrices dinámicas y el operador de desbordamiento.

### **API utilizada**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` es un método de `Aspose.Cells.Cell` que establece la fórmula de la celda como una **fórmula de matriz dinámica**. Excel evalúa la fórmula una vez y desborda automáticamente el resultado en las celdas circundantes. El tercer parámetro, cuando se establece en `true`, indica an Aspose.Cells que también calcule los valores resultantes en el momento de la escritura.

### **Pasos**
1. Cargue el libro de trabajo de origen usando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recupere la primera hoja de cálculo y acceda a su colección `Cells`.
3. Coloque la fórmula de matriz dinámica en la celda **A6**, justo debajo del rango de origen, llamando a `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. El argumento `null` pasa las `FormulaParseOptions` por defecto, y el tercer argumento `true` indica an Aspose.Cells que trate la fórmula como una matriz dinámica y que la evalúe para que los valores desbordados se escriban en el libro de trabajo.
5. Guarde el libro de trabajo con `workbook.save(outputFile)`.
La celda **A6** contiene la fórmula `=TRANSPOSE(A1:D5)` y Excel desborda automáticamente el resultado en la región **A6:D10**, un bloque de 5 filas por 4 columnas igual a los datos transpuestos.

{{% alert color="primary" %}}
Este enfoque funciona **solo en Excel 365 / 2021 o posterior**. Las versiones anteriores de Excel no desbordarán correctamente las fórmulas de matriz dinámica.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Enfoque 3 — Transponer con una Fórmula de Matriz Clásica (CSE)**
Use este enfoque cuando desee que se conserve una fórmula `TRANSPOSE` en el libro de trabajo, pero el archivo de Excel de destino puede abrirse en **versiones anteriores de Excel (anteriores a 2021, incluidas 2019, 2016, 2013, etc.)** donde no se admite el desbordamiento de matrices dinámicas. La fórmula de matriz clásica CSE (Ctrl+Shift+Enter) es la alternativa compatible con versiones anteriores que todas las versiones de Excel pueden evaluar.

### **API utilizada**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` es un método de `Aspose.Cells.Cell` que asigna una **fórmula de matriz clásica (CSE)** a la celda de anclaje y declara las dimensiones de la matriz resultante. Aspose.Cells escribe el marcador de fórmula de matriz multi-celda para que Excel evalúe la fórmula como una única expresión de matriz que rellena el rango declarado.

### **Pasos**
1. Cargue el libro de trabajo de origen de la misma forma que en los enfoques anteriores.
2. Recupere la primera hoja de cálculo y acceda a su colección `Cells`.
3. Llame a `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. El segundo argumento `4` es el número de filas de la matriz de destino y el tercer argumento `5` es el número de columnas.
4. Guarde el libro de trabajo con `workbook.save(outputFile)`.
La celda **A6** es el anclaje de la fórmula de matriz y la matriz evaluada abarca 4 filas por 5 columnas comenzando en A6, coincidiendo con las dimensiones transpuestas de la fuente A1:D5. Excel escribe un único marcador de fórmula de matriz a lo largo del rango resultante para que las versiones anteriores de Excel lo evalúen correctamente.

{{% alert color="primary" %}}
Las fórmulas de matriz CSE son la forma clásica de Excel para evaluar una expresión `TRANSPOSE` y este enfoque es universalmente compatible con todas las versiones de Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Cargar el libro de origen con opciones de carga xlsx
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Acceder a la primera hoja de trabajo y su colección de celdas
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Establecer la fórmula de matriz CSE clásica en la celda A6.
// La fórmula =TRANSPOSE(A1:D5) rota el rango de origen de 5 filas x 4 columnas
// en una matriz de 4 filas x 5 columnas. El segundo argumento (4) es el número de filas
// y el tercer argumento (5) es el número de columnas de la matriz resultante.
// Aspose.Cells escribe el marcador de fórmula de matriz CSE para que Excel la evalúe como
// una única fórmula de matriz de varias celdas, compatible con versiones anteriores de Excel
// (2019, 2016, 2013, etc.) que no admiten el derrame de matrices dinámicas.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Guardar el libro para que el marcador de la fórmula de matriz se persista
workbook.save("output.xlsx");
```

## **Comparación — Cuándo Usar Cada Enfoque**
| Enfoque | API / Método | Versión de Excel | ¿Fórmula fuente conservada? | Rango de salida |
|----------|--------------|-------------------|------------------------------|-----------------|
| Enfoque 1 — Transposición en el lugar | `range.transpose()` | Todas las versiones de Excel | No (solo valores) | Mismo rango de anclaje, 5×4 |
| Enfoque 2 — Fórmula de matriz dinámica | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Sí (se desborda dinámicamente) | Desbordado desde el anclaje |
| Enfoque 3 — Fórmula de matriz clásica (CSE) | `cell.setArrayFormula` | Todas las versiones de Excel | Sí (fórmula de matriz multi-celda) | Tamaño explícito, 4×5 |
Use el **Enfoque 1** cuando necesite una transformación rápida y compatible entre versiones y solo necesite los valores transpuestos escritos en el archivo. Use el **Enfoque 2** cuando se garantice Excel moderno y desee que la fórmula permanezca activa y se actualice si la fuente cambia. Use el **Enfoque 3** cuando necesite la máxima compatibilidad con una fórmula conservada en todas las versiones de Excel, incluidas las versiones anteriores que no admiten matrices dinámicas.

## **Artículos Relacionados**
- [Renderizado de Matriz de Celda Única en SmartMarker](/cells/es/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserción de una Imagen en una Celda](/cells/es/nodejs-cpp/inserting-an-image-into-a-cell/)
- [División de Archivos de Excel en Múltiples Archivos](/cells/es/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}