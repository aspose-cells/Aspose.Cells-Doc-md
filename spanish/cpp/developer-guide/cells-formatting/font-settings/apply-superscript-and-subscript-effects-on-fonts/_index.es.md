---
title: Aplicar efectos de superíndice y subíndice en fuentes con C++
linktitle: Aplicar efectos de superíndice y subíndice en fuentes
type: docs
weight: 80
url: /es/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: El código C++ para aplicar efectos de superíndice y subíndice al texto en Excel con la API Aspose.Cells for C++.
keywords: excel superíndice c++, excel subíndice c++, excel superíndice y subíndice c++, insertar subíndice y superíndice en excel c++, añadir subíndice y superíndice en excel c++, añadir superíndice y subíndice en excel c++, añadir superíndice en excel c++, añadir subíndice en excel c++
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la funcionalidad para aplicar efectos de superíndice (texto sobre la línea base) y subíndice (texto debajo de la línea base) al texto.

{{% /alert %}}

## **Trabajar con superíndice y subíndice**

Aplica el efecto de superíndice configurando la propiedad [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) del objeto [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) a **true**. Para aplicar el subíndice, establece la propiedad [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) del objeto [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) a **true**.

Los siguientes ejemplos de código muestran cómo aplicar superíndice y subíndice al texto.

### Código C++ para aplicar efecto de superíndice en texto

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Código C++ para aplicar efecto de subíndice en texto

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
