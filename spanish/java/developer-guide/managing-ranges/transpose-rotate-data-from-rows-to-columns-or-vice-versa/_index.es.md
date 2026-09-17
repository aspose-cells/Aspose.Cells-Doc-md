---
title: Transponer Rango
description: Este artículo explica cómo transponer o rotar datos de filas a columnas o viceversa en archivos Excel usando Aspose.Cells for Java, con tres enfoques diferentes.
linktitle: Transponer Rango
url: /es/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, biblioteca Java, hoja de cálculo, transponer rango, rotar datos, función transponer, fórmula de matriz dinámica, fórmula de matriz, TRANSPOSE Excel, Filas a Columnas
type: docs
weight: 80
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java admite transponer (rotar) datos de manera que las filas se conviertan en columnas y las columnas en filas de tres formas diferentes. El primer enfoque utiliza el método en el lugar `Range.transpose()` y funciona en todas las versiones de Excel, mientras que el segundo utiliza `Cell.setDynamicArrayFormula()` para escribir una fórmula moderna de matriz dinámica `=TRANSPOSE(...)` que se derrama automáticamente en Excel 365 o Excel 2021. El tercer enfoque utiliza `Cell.setArrayFormula()` para escribir una fórmula de matriz clásica Ctrl+Shift+Enter (CSE) que es compatible con versiones anteriores de Excel. Este artículo recorre cada enfoque con instrucciones paso a paso y ejemplos de código completos.
{{% /alert %}}

## **Introducción**
Transponer un rango significa rotarlo de manera que lo que era una fila se convierta en una columna y lo que era una columna se convierta en una fila, reflejando efectivamente los datos a través de su diagonal principal. En Microsoft Excel, la función de la hoja de cálculo `TRANSPOSE` realiza esta operación, y la referencia conceptual está documentada en [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Este concepto se puede aplicar mediante programación a un rango de celdas, lo cual es útil en muchos escenarios empresariales y de informes.
- Reorientar informes de ventas trimestrales o anuales donde los trimestres normalmente se muestran horizontalmente en la página y las regiones verticalmente, o viceversa.
- Cambiar la orientación de los ejes en paneles o gráficos para que una serie temporal se muestre verticalmente en lugar de horizontalmente.
- Reformar datos importados de sistemas externos para que coincidan con el diseño esperado por las plantillas de análisis o informes posteriores.
Para hacer concreto el resto del artículo, cada ejemplo utiliza la siguiente tabla pequeña de ventas por región por trimestre. En el libro de ejemplo esta tabla ocupa el rango **A1:D5**, con **A1** vacía como la esquina superior izquierda, **B1:D1** conteniendo los encabezados de región, y **A2:A5** conteniendo los encabezados de trimestre.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
El artículo presenta luego tres formas diferentes de transponer estos datos usando Aspose.Cells for Java, cada una adecuada para una versión diferente de Excel y caso de uso.

## **Enfoque 1 — Transponer Rango en el Lugar (Range.transpose)**
Use este enfoque cuando desee transponer datos sin involucrar la función de hoja de cálculo `TRANSPOSE`. Funciona en **todas las versiones de Excel** y no tiene dependencia en matrices dinámicas, lo que lo convierte en la opción más segura compatible entre versiones. Es ideal cuando solo necesita el resultado final transpuesto y no necesita mantener la fórmula original `TRANSPOSE` en el libro.

### **API utilizada**
`Range.transpose()` es un método de instancia en la clase `com.aspose.cells.Range`. Al llamarlo, voltea el rango en el lugar intercambiando sus filas y columnas, por lo que lo que era una fila se convierte en una columna y lo que era una columna se convierte en una fila. El método modifica directamente las celdas subyacentes sin escribir una fórmula.

### **Pasos**
1. Abra el libro de origen con `LoadOptions` configurado al formato `.xlsx` llamando a `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Obtenga la primera hoja de cálculo del libro usando `workbook.getWorksheets().get(0)`.
3. Acceda a la colección de celdas de la hoja de cálculo mediante `worksheet.getCells()`.
4. Cree el rango de origen que cubre **A1:D5** llamando a `cells.createRange("A1:D5")`.
5. Llame a `source.transpose()` para rotar el rango en el lugar, intercambiando filas y columnas.
6. Guarde el libro con `workbook.save(outputFile)`.
Después de la transposición, el rango ancla inicial contiene los datos rotados. La primera fila lee (vacía, **Europe**, **Asia**, **North America**) y la primera columna lee (vacía, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Cada columna original de ventas se convierte en una fila en el rango transpuesto.

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **Enfoque 2 — Transponer con una Fórmula de Matriz Dinámica (Excel 365 / 2021)**
Use este enfoque cuando desee preservar la fórmula `=TRANSPOSE(A1:D5)` como una fórmula activa en el libro de salida para que el resultado se actualice automáticamente si cambian los datos de origen, y el archivo Excel de destino se abrirá en **Excel 365 / Excel 2021 o posterior** donde se admiten matrices dinámicas y el operador de derrame.

### **API utilizada**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` es un método en `com.aspose.cells.Cell` que establece la fórmula de la celda como una **fórmula de matriz dinámica**. Excel evalúa la fórmula una vez y automáticamente derrama el resultado en las celdas circundantes. El tercer parámetro, cuando se establece en `true`, indica an Aspose.Cells que también calcule los valores resultantes en el momento de la escritura.

### **Pasos**
1. Cargue el libro de origen usando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Obtenga la primera hoja de cálculo y acceda a su colección `Cells`.
3. Coloque la fórmula de matriz dinámica en la celda **A6**, justo debajo del rango de origen, llamando a `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. El argumento `null` pasa `FormulaParseOptions` predeterminado, y el tercer argumento `true` indica an Aspose.Cells que trate la fórmula como una matriz dinámica y que la evalúe para que los valores derramados se escriban en el libro.
5. Guarde el libro con `workbook.save(outputFile)`.
La celda **A6** contiene la fórmula `=TRANSPOSE(A1:D5)` y Excel derrama automáticamente el resultado en la región **A6:D10**, un bloque de 5 filas por 4 columnas igual a los datos transpuestos.

{{% alert color="primary" %}}
Este enfoque funciona **solo en Excel 365 / 2021 o posterior**. Las versiones anteriores de Excel no derramarán correctamente las fórmulas de matriz dinámica.
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **Enfoque 3 — Transponer con una Fórmula de Matriz Clásica (CSE)**
Use este enfoque cuando desee una fórmula `TRANSPOSE` preservada en el libro pero el archivo Excel de destino podría abrirse en **versiones anteriores de Excel (anteriores a 2021, incluyendo 2019, 2016, 2013, etc.)** donde no se admite el derrame de matrices dinámicas. La fórmula de matriz clásica CSE (Ctrl+Shift+Enter) es la alternativa compatible con versiones anteriores que todas las versiones de Excel pueden evaluar.

### **API utilizada**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` es un método en `com.aspose.cells.Cell` que asigna una **fórmula de matriz clásica (CSE)** a la celda ancla y declara las dimensiones de la matriz resultante. Aspose.Cells escribe el marcador de fórmula de matriz de múltiples celdas para que Excel evalúe la fórmula como una expresión de matriz única que llena el rango declarado.

### **Pasos**
1. Cargue el libro de origen como se describe en los enfoques anteriores.
2. Obtenga la primera hoja de cálculo y acceda a su colección `Cells`.
3. Llame a `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. El segundo argumento `4` es el número de filas de la matriz de destino y el tercer argumento `5` es el número de columnas.
4. Guarde el libro con `workbook.save(outputFile)`.
La celda **A6** es el ancla de la fórmula de matriz y la matriz evaluada abarca 4 filas por 5 columnas comenzando en A6, coincidiendo con las dimensiones transpuestas del origen A1:D5. Excel escribe un único marcador de fórmula de matriz a través del rango resultante para que las versiones anteriores de Excel lo evalúen correctamente.

{{% alert color="primary" %}}
Las fórmulas de matriz CSE son la forma clásica de Excel para evaluar una expresión `TRANSPOSE` y este enfoque es universalmente compatible con todas las versiones de Excel.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Cargar el libro de origen con opciones de carga xlsx
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// Acceder a la primera hoja de cálculo y su colección Cells
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Establecer la fórmula de matriz CSE clásica en la celda A6.
// La fórmula =TRANSPOSE(A1:D5) rota el rango de origen de 5 filas x 4 columnas
// en una matriz de 4 filas x 5 columnas. El segundo argumento (4) es el número de filas
// y el tercer argumento (5) es el número de columnas de la matriz resultante.
// Aspose.Cells escribe el marcador de fórmula de matriz CSE para que Excel la evalúe como
// una fórmula de matriz de múltiples celdas única, compatible con versiones anteriores de Excel
// (2019, 2016, 2013, etc.) que no admiten el desbordamiento dinámico de matrices.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Guardar el libro para que se conserve el marcador de fórmula de matriz
workbook.save("output.xlsx");
```

## **Comparación — Cuándo Usar Cada Enfoque**
| Enfoque | API / Método | Versión de Excel | ¿Fórmula de origen preservada? | Rango de salida |
|---------|--------------|------------------|-------------------------------|-----------------|
| Enfoque 1 — Transposición en el lugar | `Range.transpose()` | Todas las versiones de Excel | No (solo valores) | Rango ancla inicial, 5×4 |
| Enfoque 2 — Fórmula de matriz dinámica | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Sí (se derrama dinámicamente) | Derrame desde el ancla |
| Enfoque 3 — Fórmula de matriz clásica (CSE) | `Cell.setArrayFormula` | Todas las versiones de Excel | Sí (fórmula de matriz de varias celdas) | Tamaño explícito, 4×5 |
Use el **Enfoque 1** cuando necesite una transformación rápida entre versiones y solo necesite los valores transpuestos escritos en el archivo. Use el **Enfoque 2** cuando se garantice Excel moderno y desee que la fórmula permanezca activa y se actualice si cambia el origen. Use el **Enfoque 3** cuando necesite la máxima compatibilidad con una fórmula preservada en todas las versiones de Excel, incluidas las versiones anteriores que no admiten matrices dinámicas.

## **Artículos Relacionados**
- [Renderizado de Matriz de Celda Única de SmartMarker | Aspose.Cells Java](/cells/es/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertar una Imagen en una Celda](/cells/es/java/inserting-an-image-into-a-cell/)
- [Dividir Archivos Excel en Múltiples Archivos](/cells/es/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}