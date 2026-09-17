---
title: Transponer Rango
linktitle: Transponer Rango
description: Este artículo explica cómo transponer o rotar datos de filas a columnas o viceversa en archivos Excel usando Aspose.Cells for C++ con tres enfoques diferentes.
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo, transponer rango, rotar datos, función transponer, fórmula de matriz dinámica, fórmula de matriz, TRANSPONER Excel, Filas a Columnas
type: docs
weight: 80
url: /es/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ admite transponer (rotar) datos de manera que las filas se conviertan en columnas y las columnas se conviertan en filas de tres formas diferentes. El primer enfoque utiliza el método in situ `Range.Transpose()` y funciona en todas las versiones de Excel, mientras que el segundo utiliza `Cell.SetDynamicArrayFormula()` para escribir una fórmula moderna de matriz dinámica `=TRANSPOSE(...)` que se derrama automáticamente en Excel 365 o Excel 2021. El tercer enfoque utiliza `Cell.SetArrayFormula()` para escribir una fórmula de matriz clásica Ctrl+Shift+Enter (CSE) que es compatible con versiones anteriores de Excel. Este artículo explica cada enfoque con instrucciones paso a paso y ejemplos de código completos.
{{% /alert %}}

## **Introducción**
Transponer un rango significa rotarlo de manera que lo que era una fila se convierta en una columna y lo que era una columna se convierta en una fila, reflejando efectivamente los datos a través de su diagonal principal. En Microsoft Excel, la función de hoja de cálculo `TRANSPONER` realiza esta operación, y la referencia conceptual está documentada en [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Este concepto puede aplicarse programáticamente a un rango de celdas, lo cual resulta útil en muchos escenarios empresariales y de generación de informes.
- Reorientar informes de ventas trimestrales o anuales donde los trimestres normalmente se extienden a lo ancho de la página y las regiones a lo largo, o viceversa.
- Intercambiar la orientación de los ejes en paneles o gráficos para que una serie temporal se ejecute verticalmente en lugar de horizontalmente.
- Reformar datos importados desde sistemas externos para que coincidan con el diseño esperado por las plantillas de análisis o informes posteriores.
Para hacer concreto el resto del artículo, todos los ejemplos utilizan la siguiente tabla pequeña de ventas por región y por trimestre. En el libro de muestra, esta tabla ocupa el rango **A1:D5**, con **A1** vacío como esquina superior izquierda, **B1:D1** contiene los encabezados de región, y **A2:A5** contiene los encabezados de trimestre.
| Región            | Europa    | Asia      | América del Norte |
|-------------------|-----------|-----------|-------------------|
| Trim 1            | 21704714  | 8774099   | 12094215          |
| Trim 2            | 17987034  | 12214447  | 10873099          |
| Trim 3            | 19485029  | 14356879  | 15689543          |
| Trim 4            | 22567894  | 15763492  | 17456723          |
A continuación, el artículo presenta tres formas diferentes de transponer estos datos usando Aspose.Cells for C++, cada una adecuada para una versión diferente de Excel y un caso de uso distinto.

## **Enfoque 1 — Transponer Rango in Situ (Range.Transpose)**
Utilice este enfoque siempre que desee transponer datos sin involucrar la función de hoja de cálculo `TRANSPONER`. Funciona en **todas las versiones de Excel** y no tiene dependencia de matrices dinámicas, lo que lo convierte en la opción más segura y compatible entre versiones. Es ideal cuando solo necesita el resultado final transpuesto y no necesita conservar la fórmula original `TRANSPONER` en el libro.

### **API utilizada**
`Range.Transpose()` es un método de instancia en la clase `Aspose.Cells.Range`. Al llamarlo, voltea el rango in situ intercambiando sus filas y columnas, de modo que lo que era una fila se convierte en una columna y lo que era una columna se convierte en una fila. El método modifica directamente las celdas subyacentes sin escribir una fórmula.

### **Pasos**
1. Abra el libro de origen con `LoadOptions` establecido en el formato `.xlsx` creando un `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Obtenga la primera hoja de cálculo del libro usando `workbook.GetWorksheets().Get(0)`.
3. Acceda a la colección de celdas de la hoja de cálculo mediante `worksheet.GetCells()`.
4. Cree el rango de origen que cubre **A1:D5** llamando a `cells.CreateRange(u"A1:D5")`.
5. Llame a `source.Transpose()` para rotar el rango in situ, intercambiando filas y columnas.
6. Guarde el libro con `workbook.Save(outputFile)`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Enfoque 2 — Transponer con una Fórmula de Matriz Dinámica (Excel 365 / 2021)**
Utilice este enfoque cuando desee conservar la fórmula `=TRANSPOSE(A1:D5)` como una fórmula activa en el libro de salida para que el resultado se actualice automáticamente si los datos de origen cambian, y el archivo Excel de destino se abrirá en **Excel 365 / Excel 2021 o posterior**, donde se admiten las matrices dinámicas y el operador de derrame.

### **API utilizada**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` es un método en `Aspose.Cells.Cell` que establece la fórmula de la celda como una **fórmula de matriz dinámica**. Excel evalúa la fórmula una vez y derrama automáticamente el resultado en las celdas circundantes. El tercer parámetro, cuando se establece en `true`, indica an Aspose.Cells que también calcule los valores resultantes en el momento de la escritura.

### **Pasos**
1. Cargue el libro de origen construyendo `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Obtenga la primera hoja de cálculo mediante `workbook.GetWorksheets().Get(0)` y acceda a su colección `Cells` a través de `worksheet.GetCells()`.
3. Coloque la fórmula de matriz dinámica en la celda **A6**, justo debajo del rango de origen, llamando a `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`.
4. El argumento `nullptr` pasa el `FormulaParseOptions` por defecto, y el tercer argumento `true` indica an Aspose.Cells que trate la fórmula como una matriz dinámica y que la evalúe para que los valores derramados se escriban en el libro.
5. Guarde el libro con `workbook.Save(outputFile)`.
La celda **A6** contiene la fórmula `=TRANSPOSE(A1:D5)` y Excel derrama el resultado automáticamente en la región **A6:D10**, un bloque de 5 filas por 4 columnas igual a los datos transpuestos.

{{% alert color="primary" %}}
Este enfoque funciona **solo en Excel 365 / 2021 o posterior**. Las versiones anteriores de Excel no derramarán correctamente las fórmulas de matriz dinámica.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Enfoque 3 — Transponer con una Fórmula de Matriz Clásica (CSE)**
Utilice este enfoque cuando desee conservar una fórmula `TRANSPONER` en el libro, pero el archivo Excel de destino pueda abrirse en **versiones anteriores de Excel (anteriores a 2021, incluyendo 2019, 2016, 2013, etc.)** donde no se admite el derrame de matrices dinámicas. La fórmula de matriz CSE (Ctrl+Shift+Enter) clásica es la alternativa compatible con versiones anteriores que todas las versiones de Excel pueden evaluar.

### **API utilizada**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` es un método en `Aspose.Cells.Cell` que asigna una **fórmula de matriz (CSE) clásica** a la celda ancla y declara las dimensiones de la matriz resultante. Aspose.Cells escribe el marcador de fórmula de matriz multi-celda para que Excel evalúe la fórmula como una expresión de matriz única que llena el rango declarado.

### **Pasos**
2. Obtenga la primera hoja de cálculo mediante `workbook.GetWorksheets().Get(0)` y acceda a su colección `Cells` a través de `worksheet.GetCells()`.
3. Llame a `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`. El segundo argumento `4` es el número de filas de la matriz de destino y el tercer argumento `5` es el número de columnas.
4. Guarde el libro con `workbook.Save(outputFile)`.
La celda **A6** es el ancla de la fórmula de matriz y la matriz evaluada abarca 4 filas por 5 columnas comenzando en A6, coincidiendo con las dimensiones transpuestas del origen A1:D5. Excel escribe un único marcador de fórmula de matriz en todo el rango resultante para que las versiones anteriores de Excel la evalúen correctamente.

{{% alert color="primary" %}}
Las fórmulas de matriz CSE son la forma clásica en Excel de evaluar una expresión `TRANSPONER`, y este enfoque es universalmente compatible en todas las versiones de Excel.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Cargar el libro de origen con Opciones de Carga de xlsx
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // Acceder a la primera hoja de cálculo y a su colección de Celdas
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Establecer la fórmula de matriz CSE clásica en la celda A6.
    // La fórmula =TRANSPOSE(A1:D5) rota el rango fuente de 5 filas x 4 columnas
    // en una matriz de 4 filas x 5 columnas. El segundo argumento (4) es el número de filas
    // y el tercer argumento (5) es el número de columnas de la matriz resultante.
    // Aspose.Cells escribe el marcador de fórmula de matriz CSE para que Excel la evalúe como
    // una única fórmula de matriz de varias celdas, compatible con versiones anteriores de Excel
    // (2019, 2016, 2013, etc.) que no admiten el desbordamiento dinámico de matrices.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // Guardar el libro para que se conserve el marcador de la fórmula de matriz
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Comparación — Cuándo Usar Cada Enfoque**
| Enfoque | API / Método | Versión de Excel | ¿Fórmula fuente conservada? | Rango de salida |
|----------|--------------|------------------|----------------------------|-----------------|
| Enfoque 1 — Transposición in situ | `Range.Transpose()` | Todas las versiones de Excel | No (solo valores) | Rango ancla inicial, 5×4 |
| Enfoque 2 — Fórmula de matriz dinámica | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Sí (derrame dinámico) | Derramado desde el ancla |
| Enfoque 3 — Fórmula de matriz clásica (CSE) | `Cell.SetArrayFormula` | Todas las versiones de Excel | Sí (fórmula de matriz multi-celda) | Tamaño explícito, 4×5 |
Utilice el **Enfoque 1** cuando necesite una transformación rápida y compatible entre versiones, y solo necesite los valores transpuestos escritos en el archivo. Utilice el **Enfoque 2** cuando se garantice Excel moderno y desee que la fórmula permanezca activa y se actualice si el origen cambia. Utilice el **Enfoque 3** cuando necesite la máxima compatibilidad con una fórmula conservada en todas las versiones de Excel, incluidas las versiones anteriores que no admiten matrices dinámicas.

## **Artículos Relacionados**
- [Renderizado de Matriz de Celda Única en SmartMarker | Aspose.Cells for C++](/cells/es/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertar una Imagen en una Celda](/cells/es/cpp/inserting-an-image-into-a-cell/)
- [Dividir Archivos Excel en Múltiples Archivos](/cells/es/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}