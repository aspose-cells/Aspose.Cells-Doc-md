---
title: Configuración de alineación con C++
linktitle: Configuraciones de Alineación
description: En la biblioteca Aspose.Cells, puedes usar configuraciones de alineación celular para ajustar la disposición y visualización del texto. Al ajustar configuraciones como la alineación horizontal, alineación vertical y ajuste del texto, tienes más control sobre cómo fluye el texto en las celdas. Este documento te proporcionará pasos detallados y código de muestra para ayudarte a comprender rápidamente cómo usar Aspose.Cells para las configuraciones de alineación celular.
keywords: Aspose.Cells, alineación celular, alineación horizontal, alineación vertical, ajuste del texto
type: docs
weight: 20
url: /es/cpp/cells-alignment-settings/
---

## **Configurando Ajustes de Alineación**

### **Configuraciones de Alineación en Microsoft Excel**

Cualquiera que haya usado Microsoft Excel para formatear celdas estará familiarizado con las configuraciones de alineación en Microsoft Excel.

Como puedes ver en la figura anterior, hay diferentes tipos de opciones de alineación:

- Alineación de texto (horizontal y vertical)
- Sangría
- Orientación.
- Control de texto.
- Dirección del texto.

Todos estos ajustes de alineación son completamente compatibles con Aspose.Cells y se discuten con más detalle a continuación.

### **Ajustes de alineación en Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Cada elemento en la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells proporciona métodos [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) y [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) para la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) que se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) proporciona propiedades útiles para configurar los ajustes de alineación.

Seleccione cualquier tipo de alineación de texto utilizando la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/). Los tipos de alineación de texto predefinidos en la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) son:

|**Tipos de Alineación de Texto**|**Descripción**|
| :- | :- |
|Bottom|Representa la alineación del texto inferior|
|Center|Representa la alineación del texto centrado|
|CenterAcross|Representa la alineación del texto centrado a través|
|Distributed|Representa la alineación del texto distribuido|
|Fill|Representa la alineación del texto de relleno|
|General|Representa la alineación del texto general|
|Justify|Representa la alineación del texto justificado|
|Left|Representa la alineación del texto a la izquierda|
|Right|Representa la alineación del texto a la derecha|
|Top|Representa la alineación del texto superior|
|JustifiedLow|Alinea el texto con una longitud de kashida ajustada para el texto árabe.|
|ThaiDistributed|Distribuye texto en tailandés especialmente, porque cada carácter se trata como una palabra.|

{{% alert color="primary" %}}

También puedes aplicar la justificación distribuida usando la configuración [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/) property.

{{% /alert %}}

#### **Alineación horizontal**

Usa la propiedad [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) para alinear el texto horizontalmente.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Alineación vertical**

Similar a la alineación horizontal, usa la propiedad [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) para alinear el texto verticalmente.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Sangría**

Es posible establecer el nivel de sangría del texto en una celda con la propiedad [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Orientación**

Establece la orientación (rotación) del texto en una celda con la propiedad [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Control de texto**

La siguiente sección explica cómo controlar el texto mediante el ajuste del ajuste de texto, el ajuste al tamaño y otras opciones de formato.

##### **Envolver texto**

Envolver el texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para que quepa todo el texto, en lugar de cortarlo o derramarse en celdas adyacentes. Establece el ajuste de texto en on o off con la propiedad [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Reducir para ajustar**

Una opción para envolver texto en un campo es reducir el tamaño del texto para ajustarse a las dimensiones de una celda. Esto se hace configurando la propiedad [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) como **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Combinar celdas**

Al igual que Microsoft Excel, Aspose.Cells admite combinar varias celdas en una. Aspose.Cells proporciona dos enfoques para esta tarea. Una forma es llamar al método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) de la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). El método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) toma los siguientes parámetros para combinar las celdas:

- Primera fila: la primera fila desde donde comenzar a combinar.
- Primera columna: la primera columna desde donde comenzar a combinar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

La otra forma es llamar primero al método [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) de la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) para crear un rango de celdas a fusionar. El método [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) toma el mismo conjunto de parámetros que el método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) discutido anteriormente y devuelve un objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). El objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) también proporciona un método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) que fusiona el rango especificado en el objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

El orden de lectura se establece con la propiedad [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Aspose.Cells proporciona tipos de dirección de texto predefinidos en la enumeración [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|Context|El orden de lectura es coherente con el idioma del primer carácter introducido|
|LeftToRight|Orden de lectura de izquierda a derecha|
|RightToLeft|Orden de lectura de derecha a izquierda|

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Temas avanzados**
- [Cambiar la alineación de las celdas y mantener el formato existente](/cells/es/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/cpp/line-breaks-and-text-wrapping/)
