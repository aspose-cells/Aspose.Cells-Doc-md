---
title: Transponer Rango
description: Este artículo explica cómo transponer o rotar datos de filas a columnas o viceversa en archivos de Excel usando Aspose.Cells for .NET con tres enfoques diferentes.
linktitle: Transponer Rango
url: /es/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, transponer rango, rotar datos, función transponer, fórmula de matriz dinámica, fórmula matricial, TRANSPONER de Excel, Filas a Columnas
type: docs
weight: 80
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET admite transponer (rotar) datos de modo que las filas se conviertan en columnas y las columnas se conviertan en filas de tres maneras diferentes. El primer enfoque utiliza el método en su lugar `Range.Transpose()` y funciona en todas las versiones de Excel, mientras que el segundo utiliza `Cell.SetDynamicArrayFormula()` para escribir una fórmula moderna de matriz dinámica `=TRANSPOSE(...)` que se derrama automáticamente en Excel 365 o Excel 2021. El tercer enfoque utiliza `Cell.SetArrayFormula()` para escribir una fórmula matricial clásica Ctrl+Shift+Enter (CSE) que es compatible con versiones anteriores de Excel. Este artículo recorre cada enfoque con instrucciones paso a paso y ejemplos de código completos.
{{% /alert %}}

## **Introducción**
Transponer un rango significa rotarlo de modo que lo que era una fila se convierta en una columna y lo que era una columna se convierta en una fila, reflejando efectivamente los datos a través de su diagonal principal. En Microsoft Excel, la función de hoja de cálculo `TRANSPOSE` realiza esta operación, y la referencia conceptual se documenta en [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Este concepto se puede aplicar programáticamente a un rango de celdas, lo cual es útil en muchos escenarios empresariales y de informes.
- Reorientar informes de ventas trimestrales o anuales donde los trimestres normalmente se extienden a lo largo de la página y las regiones descienden por la página, o viceversa.
- Intercambiar la orientación de los ejes en paneles o gráficos para que una serie temporal se extienda hacia abajo en lugar de a lo ancho de la página.
- Reformar los datos importados de sistemas externos para que coincidan con el diseño esperado por las plantillas de análisis o informes posteriores.
Para que el resto del artículo sea concreto, cada ejemplo utiliza la siguiente pequeña tabla de ventas por región y por trimestre. En el libro de trabajo de muestra esta tabla ocupa el rango **A1:D5**, con **A1** vacío como la esquina superior izquierda, **B1:D1** conteniendo los encabezados de las regiones y **A2:A5** conteniendo los encabezados de los trimestres.
| Región           | Europa     | Asia       | Norteamérica |
|------------------|------------|------------|---------------|
| Trim 1           | 21704714   | 8774099    | 12094215      |
| Trim 2           | 17987034   | 12214447   | 10873099      |
| Trim 3           | 19485029   | 14356879   | 15689543      |
| Trim 4           | 22567894   | 15763492   | 17456723      |
El artículo presenta luego tres formas diferentes de transponer estos datos usando Aspose.Cells for .NET, cada una adecuada para una versión diferente de Excel y caso de uso.

## **Enfoque 1 — Transponer Rango en su lugar (Range.Transpose)**
Utilice este enfoque cuando desee transponer datos sin involucrar la función de hoja de cálculo `TRANSPOSE`. Funciona en **todas las versiones de Excel** y no tiene dependencia de matrices dinámicas, lo que lo convierte en la opción más segura y compatible entre versiones. Es ideal cuando solo necesita el resultado final transpuesto y no necesita mantener la fórmula original `TRANSPOSE` en el libro de trabajo.

### **API utilizada**
`Range.Transpose()` es un método de instancia de la clase `Aspose.Cells.Range`. Al llamarlo, voltea el rango en su lugar intercambiando sus filas y columnas, de modo que lo que era una fila se convierte en una columna y lo que era una columna se convierte en una fila. El método modifica las celdas subyacentes directamente sin escribir una fórmula.

### **Pasos**
1. Abra el libro de trabajo fuente con `LoadOptions` configurado en el formato `.xlsx` llamando a `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recupere la primera hoja de cálculo del libro de trabajo usando `workbook.Worksheets[0]`.
3. Acceda a la colección de celdas de la hoja de cálculo a través de `worksheet.Cells`.
4. Cree el rango fuente que cubre **A1:D5** llamando a `cells.CreateRange("A1:D5")`.
5. Llame a `source.Transpose()` para rotar el rango en su lugar, intercambiando filas y columnas.
6. Guarde el libro de trabajo con `workbook.Save(outputFile)`.
Después de la transposición, este rango ancla contiene los datos rotados. La primera fila se lee (vacío, **Europa**, **Asia**, **Norteamérica**) y la primera columna se lee (vacío, **Trim 1**, **Trim 2**, **Trim 3**, **Trim 4**). Cada columna original de ventas se convierte en una fila en el rango transpuesto.

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **Enfoque 2 — Transponer con una Fórmula de Matriz Dinámica (Excel 365 / 2021)**
Utilice este enfoque cuando desee conservar la fórmula `=TRANSPOSE(A1:D5)` como una fórmula activa en el libro de trabajo de salida, de modo que el resultado se actualice automáticamente si los datos fuente cambian, y el archivo Excel destino se abrirá en **Excel 365 / Excel 2021 o posterior**, donde se admiten matrices dinámicas y el operador de derrame.

### **API utilizada**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` es un método de `Aspose.Cells.Cell` que establece la fórmula de la celda como una **fórmula de matriz dinámica**. Excel evalúa la fórmula una vez y derrama automáticamente el resultado en las celdas circundantes. El tercer parámetro, cuando se establece en `true`, indica an Aspose.Cells que también calcule los valores resultantes en el momento de la escritura.

### **Pasos**
1. Cargue el libro de trabajo fuente usando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recupere la primera hoja de cálculo y acceda a su colección `Cells`.
3. Coloque la fórmula de matriz dinámica en la celda **A6**, justo debajo del rango fuente, llamando a `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. El argumento `new FormulaParseOptions()` usa la configuración predeterminada de `FormulaParseOptions`, y el tercer argumento `true` indica an Aspose.Cells que trate la fórmula como una matriz dinámica y que la evalúe para que los valores derramados se escriban en el libro de trabajo.
5. Guarde el libro de trabajo con `workbook.Save(outputFile)`.
La celda **A6** contiene la fórmula `=TRANSPOSE(A1:D5)` y Excel derrama el resultado automáticamente en la región **A6:E9**, un bloque de 4 filas por 5 columnas igual a los datos transpuestos.

{{% alert color="primary" %}}
Este enfoque funciona **solo en Excel 365 / 2021 o posterior**. Las versiones anteriores de Excel no derramarán correctamente las fórmulas de matriz dinámica.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **Enfoque 3 — Transponer con una Fórmula Matricial Clásica (CSE)**
Utilice este enfoque cuando desee una fórmula `TRANSPOSE` conservada en el libro de trabajo, pero el archivo Excel destino puede abrirse en **versiones anteriores de Excel (anteriores a 2021, incluidos 2019, 2016, 2013, etc.)**, donde no se admite el derrame de matrices dinámicas. La fórmula matricial clásica CSE (Ctrl+Shift+Enter) es la alternativa compatible con versiones anteriores que todas las versiones de Excel pueden evaluar.

### **API utilizada**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` es un método de `Aspose.Cells.Cell` que asigna una **fórmula matricial clásica (CSE)** a la celda ancla y declara las dimensiones de la matriz resultante. Aspose.Cells escribe el marcador de fórmula matricial multicelda para que Excel evalúe la fórmula como una expresión matricial única que llena el rango declarado.

### **Pasos**
1. Cargue el libro de trabajo fuente como se describe en los enfoques anteriores.
2. Recupere la primera hoja de cálculo y acceda a su colección `Cells`.
3. Llame a `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. El segundo argumento `4` es el número de filas de la matriz destino y el tercer argumento `5` es el número de columnas.
4. Guarde el libro de trabajo con `workbook.Save(outputFile)`.
La celda **A6** es el ancla de la fórmula matricial y la matriz evaluada abarca 4 filas por 5 columnas comenzando en A6, coincidiendo con las dimensiones transpuestas de la fuente A1:D5. Excel escribe un único marcador de fórmula matricial a lo largo del rango resultante para que las versiones anteriores de Excel lo evalúen correctamente.

{{% alert color="primary" %}}
Las fórmulas matriciales CSE son la forma clásica de Excel para evaluar una expresión `TRANSPOSE` y este enfoque es universalmente compatible entre versiones de Excel.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// Cargar el libro de origen con las opciones de carga xlsx
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// Acceder a la primera hoja de cálculo y a su colección de celdas
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// Establecer la fórmula de matriz CSE clásica en la celda A6.
// La fórmula =TRANSPOSE(A1:D5) rota el rango de origen de 5 filas x 4 columnas
// en una matriz de 4 filas x 5 columnas. El segundo argumento (4) es el número de filas
// y el tercer argumento (5) es el número de columnas de la matriz resultante.
// Aspose.Cells escribe el marcador de fórmula-matriz CSE para que Excel la evalúe como
// una única fórmula de matriz de varias celdas, compatible con versiones anteriores de Excel
// (2019, 2016, 2013, etc.) que no admiten el derrame dinámico de matrices.
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Guardar el libro para que se conserve el marcador de la fórmula de matriz
workbook.Save("output.xlsx");
```

## **Comparación — Cuándo Usar Cada Enfoque**
| Enfoque | API / Método | Versión de Excel | ¿Fórmula fuente conservada? | Rango de salida |
|---------|--------------|------------------|-----------------------------|-----------------|
| Enfoque 1 — Transposición en su lugar | `Range.Transpose()` | Todas las versiones de Excel | No (solo valores) | Rango ancla inicial, 5×4 |
| Enfoque 2 — Fórmula de matriz dinámica | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Sí (derrame dinámico) | Derramado desde el ancla |
| Enfoque 3 — Fórmula matricial clásica (CSE) | `Cell.SetArrayFormula` | Todas las versiones de Excel | Sí (fórmula matricial multicelda) | Tamaño explícito, 4×5 |
Use **Enfoque 1** cuando necesite una transformación rápida y compatible entre versiones y solo necesite que los valores transpuestos se escriban en el archivo. Use **Enfoque 2** cuando se garantice Excel moderno y desee que la fórmula permanezca activa y se actualice si la fuente cambia. Use **Enfoque 3** cuando necesite la mayor compatibilidad con una fórmula conservada en todas las versiones de Excel, incluidas las versiones anteriores que no admiten matrices dinámicas.

{{< app/cells/assistant language="csharp" >}}