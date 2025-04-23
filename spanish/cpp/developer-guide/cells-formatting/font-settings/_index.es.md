---
title: Configuración de fuente con C++
linktitle: Configuración de fuente
type: docs
weight: 30
url: /es/cpp/cells-font-settings/
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Soporta configurar las propiedades de fuente de las celdas, permitiendo a los usuarios personalizar el estilo y las propiedades de la fuente de las celdas. Este artículo introducirá cómo usar la biblioteca Aspose.Cells para configurar la fuente de las celdas.
keywords: Aspose.Cells, Celdas, Configuración de fuente, Estilos, Propiedades
---

{{% alert color="primary" %}}

El aspecto de un texto puede controlarse modificando las configuraciones de fuente. Las configuraciones de fuente pueden incluir el nombre, estilo, tamaño, color y otros efectos de las fuentes. Al igual que Microsoft Excel, Aspose.Cells también admite configurar las opciones de fuente de las celdas.

{{% /alert %}}

## **Configuración de fuente**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Cada elemento en la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells proporciona las clases [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) y los métodos [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) y [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) que se utilizan para obtener y establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) proporciona propiedades para configurar la configuración de fuente.

### **Establecer nombre de fuente**

Los desarrolladores pueden aplicar cualquier fuente al texto dentro de una celda usando la propiedad [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Establecer estilo de fuente en negrita**

Los desarrolladores pueden hacer que el texto esté en negrita configurando la propiedad [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) en **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Establecer tamaño de fuente**

Establezca el tamaño de fuente con la propiedad [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Establecer color de fuente**

Use la propiedad [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) para establecer el color de la fuente. Elija cualquier color del enumerador de colores (parte del marco de C++) y asígnelo a la propiedad [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **Establecer tipo de subrayado de fuente**

Utilice la propiedad [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) para subrayar texto. Aspose.Cells ofrece varios tipos de subrayado de fuente predefinidos en la enumeración [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/).

|**Tipos de subrayado de fuente**|**Descripción**|
| :- | :- |
|Accounting|Un solo subrayado contable|
|Double|Doble subrayado|
|DoubleAccounting|Doble subrayado|
|None|Sin subrayado|
|Single|Un solo subrayado|

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Establecer efecto tachado**

Aplicar el tachado configurando la propiedad [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) en **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Establecer efecto subíndice**

Aplicar subíndice configurando la propiedad [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) en **true**.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Establecer efecto superíndice en fuente**

Los desarrolladores pueden aplicar el efecto superíndice en la fuente configurando la propiedad [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) del objeto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) en **true**.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
