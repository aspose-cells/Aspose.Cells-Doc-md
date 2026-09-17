---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Python via .NET, with three different approaches.
linktitle: Transponer rango
url: /es/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells for Python via .NET, hoja de cálculo, transponer rango, rotar datos, función TRANSPOSE, fórmula de matriz dinámica, fórmula matricial, TRANSPOSE de Excel, Filas a Columnas
type: docs
weight: 80
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET admite transponer (rotar) datos de modo que las filas se conviertan en columnas y las columnas se conviertan en filas de tres maneras diferentes. El primer enfoque utiliza el método in situ `range.transpose()` y funciona en todas las versiones de Excel, mientras que el segundo utiliza `cell.set_dynamic_array_formula()` para escribir una fórmula moderna de matriz dinámica `=TRANSPOSE(...)` que se derrama automáticamente en Excel 365 o Excel 2021. El tercer enfoque utiliza `cell.set_array_formula()` para escribir una fórmula matricial clásica Ctrl+Shift+Enter (CSE) compatible con versiones anteriores de Excel. Este artículo recorre cada enfoque con instrucciones paso a paso y ejemplos de código completos.
{{% /alert %}}

## **Introducción**
Transponer un rango significa rotarlo de manera que lo que era una fila se convierta en una columna y lo que era una columna se convierta en una fila, reflejando efectivamente los datos a través de su diagonal principal. En Microsoft Excel, la función de hoja de cálculo `TRANSPOSE` realiza esta operación, y la referencia conceptual está documentada en [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La misma idea se puede aplicar mediante programación a un rango de celdas, lo cual es útil en muchos escenarios empresariales y de informes.
Los escenarios comunes en los que la transposición resulta útil incluyen los siguientes.
- Reorientar informes de ventas trimestrales o anuales donde los trimestres normalmente se extienden a lo largo de la página y las regiones bajan por la página, o viceversa.
- Cambiar la orientación de los ejes en paneles o gráficos para que una serie temporal se ejecute hacia abajo en la página en lugar de a lo ancho.
- Reformar los datos importados de sistemas externos para que coincidan con el diseño esperado por los análisis posteriores o las plantillas de informes.
Para hacer concreto el resto del artículo, cada ejemplo utiliza la siguiente tabla pequeña de ventas por región y por trimestre. En el libro de muestra esta tabla ocupa el rango **A1:D5**, con **A1** dejada vacía como la esquina superior izquierda, **B1:D1** conteniendo los encabezados de región, y **A2:A5** conteniendo los encabezados de trimestre.
| Región       | Europa   | Asia      | Norteamérica |
|--------------|----------|-----------|--------------|
| Trimestre 1  | 21704714 | 8774099   | 12094215     |
| Trimestre 2  | 17987034 | 12214447  | 10873099     |
| Trimestre 3  | 19485029 | 14356879  | 15689543     |
| Trimestre 4  | 22567894 | 15763492  | 17456723     |
El artículo presenta entonces tres maneras diferentes de transponer estos datos usando Aspose.Cells for Python via .NET, cada una adecuada para una versión de Excel y un caso de uso diferentes.

## **Enfoque 1 — Transponer rango en su lugar (range.transpose)**
Use este enfoque siempre que desee transponer datos sin involucrar la función de hoja de cálculo `TRANSPOSE`. Funciona en **todas las versiones de Excel** y no depende de matrices dinámicas, lo que lo convierte en la opción más segura compatible entre versiones. Es ideal cuando solo necesita el resultado final transpuesto y no necesita mantener la fórmula original `TRANSPOSE` en el libro.

### **API utilizada**
`range.transpose()` es un método de instancia en la clase `Aspose.Cells.Range`. Al llamarlo, se voltea el rango en su lugar intercambiando sus filas y columnas, de modo que lo que era una fila se convierte en una columna y lo que era una columna se convierte en una fila. El método modifica las celdas subyacentes directamente sin escribir una fórmula.

### **Pasos**
1. Abra el libro de origen con `LoadOptions` establecido en el formato `.xlsx` llamando a `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Obtenga la primera hoja de cálculo del libro usando `workbook.worksheets[0]`.
3. Acceda a la colección de celdas de la hoja de cálculo a través de `worksheet.cells`.
4. Cree el rango de origen que cubre **A1:D5** llamando a `cells.create_range("A1:D5")`.
5. Llame a `source.transpose()` para rotar el rango en su lugar, intercambiando filas y columnas.
6. Guarde el libro con `workbook.save(outputFile)`.
Después de la transposición, el mismo rango ancla contiene los datos rotados. La primera fila dice (vacío, **Europa**, **Asia**, **Norteamérica**) y la primera columna dice (vacío, **Trimestre 1**, **Trimestre 2**, **Trimestre 3**, **Trimestre 4**). Cada columna original de ventas se convierte en una fila en el rango transpuesto.

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **Enfoque 2 — Transponer con una fórmula de matriz dinámica (Excel 365 / 2021)**
Use este enfoque cuando desee conservar la fórmula `=TRANSPOSE(A1:D5)` como una fórmula activa en el libro de salida para que el resultado se actualice automáticamente si los datos de origen cambian, y el archivo Excel de destino se abrirá en **Excel 365 / Excel 2021 o posterior**, donde se admiten las matrices dinámicas y el operador de derrame.

### **API utilizada**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` es un método en `Aspose.Cells.Cell` que establece la fórmula de la celda como una **fórmula de matriz dinámica**. Excel evalúa la fórmula una vez y derrama automáticamente el resultado en las celdas circundantes. El tercer parámetro, cuando se establece en `True`, indica an Aspose.Cells que también calcule los valores resultantes en el momento de la escritura.

### **Pasos**
1. Cargue el libro de origen usando `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Obtenga la primera hoja de cálculo y acceda a su colección `cells`.
3. Coloque la fórmula de matriz dinámica en la celda **A6**, justo debajo del rango de origen, llamando a `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`.
4. El argumento `None` pasa el `FormulaParseOptions` por defecto, y el tercer argumento `True` indica an Aspose.Cells que trate la fórmula como una matriz dinámica y que la evalúe para que los valores derramados se escriban en el libro.
5. Guarde el libro con `workbook.save(outputFile)`.
La celda **A6** contiene la fórmula `=TRANSPOSE(A1:D5)` y Excel derrama el resultado automáticamente en la región **A6:D10**, un bloque de 5 filas por 4 columnas igual a los datos transpuestos.

{{% alert color="primary" %}}
Este enfoque funciona **solo en Excel 365 / 2021 o posterior**. Las versiones anteriores de Excel no derramarán las fórmulas de matriz dinámica correctamente.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **Enfoque 3 — Transponer con una fórmula matricial clásica (CSE)**
Use este enfoque cuando desee conservar una fórmula `TRANSPOSE` en el libro pero el archivo Excel de destino pueda abrirse en **versiones anteriores de Excel (anteriores a 2021, incluyendo 2019, 2016, 2013, etc.)** donde no se admite el derrame de matrices dinámicas. La fórmula matricial clásica CSE (Ctrl+Shift+Enter) es la alternativa compatible con versiones anteriores que todas las versiones de Excel pueden evaluar.

### **API utilizada**
`cell.set_array_formula(array_formula, n_rows, n_columns)` es un método en `Aspose.Cells.Cell` que asigna una **fórmula matricial (CSE) clásica** a la celda ancla y declara las dimensiones de la matriz resultante. Aspose.Cells escribe el marcador de fórmula matricial multicelda para que Excel evalúe la fórmula como una única expresión matricial que llena el rango declarado.

### **Pasos**
1. Cargue el libro de origen de la misma manera que en los enfoques anteriores.
2. Obtenga la primera hoja de cálculo y acceda a su colección `cells`.
3. Llame a `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`. El segundo argumento `4` es el número de filas de la matriz de destino y el tercer argumento `5` es el número de columnas.
4. Guarde el libro con `workbook.save(outputFile)`.
La celda **A6** es el ancla de la fórmula matricial y la matriz evaluada abarca 4 filas por 5 columnas comenzando en A6, coincidiendo con las dimensiones transpuestas del origen A1:D5. Excel escribe un único marcador de fórmula matricial a lo largo del rango resultante para que las versiones anteriores de Excel lo evalúen correctamente.

{{% alert color="primary" %}}
Las fórmulas matriciales CSE son la forma clásica de Excel para evaluar una expresión `TRANSPOSE` y este enfoque es universalmente compatible en todas las versiones de Excel.
{{% /alert %}}

```python
import aspose.cells as ac
# Cargar el libro de trabajo de origen con LoadOptions de xlsx
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# Acceder a la primera hoja de trabajo y su colección Cells
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Establecer la fórmula de matriz CSE clásica en la celda A6.
# La fórmula =TRANSPOSE(A1:D5) rota el rango de origen de 5 filas x 4 columnas
# en una matriz de 4 filas x 5 columnas. El segundo argumento (4) es el número de filas
# y el tercer argumento (5) es el número de columnas de la matriz resultante.
# Aspose.Cells escribe el marcador de fórmula de matriz CSE para que Excel lo evalúe como
# una fórmula de matriz de múltiples celdas única, compatible con versiones anteriores de Excel
# (2019, 2016, 2013, etc.) que no admiten el desbordamiento de matriz dinámica.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Guardar el libro de trabajo para que el marcador de fórmula de matriz se conserve
workbook.save("output.xlsx")
```

## **Comparación — Cuándo usar cada enfoque**
| Enfoque | API / Método | Versión de Excel | ¿Fórmula de origen conservada? | Rango de salida |
|---------|--------------|------------------|-------------------------------|-----------------|
| Enfoque 1 — Transposición in situ | `range.transpose()` | Todas las versiones de Excel | No (solo valores) | Mismo rango ancla, 5×4 |
| Enfoque 2 — Fórmula de matriz dinámica | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Sí (derrame dinámico) | Derramado desde el ancla |
| Enfoque 3 — Fórmula matricial clásica (CSE) | `cell.set_array_formula` | Todas las versiones de Excel | Sí (fórmula matricial multicelda) | Tamaño explícito, 4×5 |
Use el **Enfoque 1** cuando necesite una transformación rápida y compatible entre versiones y solo necesite que los valores transpuestos se escriban en el archivo. Use el **Enfoque 2** cuando se garantice Excel moderno y desee que la fórmula permanezca activa y se actualice si la fuente cambia. Use el **Enfoque 3** cuando necesite la máxima compatibilidad con una fórmula conservada en todas las versiones de Excel, incluidas las versiones anteriores que no admiten matrices dinámicas.

## **Artículos relacionados**
- [Renderizado de matriz de celda única de SmartMarker | Aspose.Cells for Python via .NET](/cells/es/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertar una imagen en una celda](/cells/es/python-net/inserting-an-image-into-a-cell/)
- [Dividir archivos de Excel en varios archivos](/cells/es/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}