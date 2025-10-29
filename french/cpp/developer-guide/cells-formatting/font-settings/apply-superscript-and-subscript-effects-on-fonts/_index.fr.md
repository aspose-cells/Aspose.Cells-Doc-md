---
title: Appliquer des effets de exposant et indice atomique aux polices avec C++
linktitle: Appliquer des effets de exposant et d indice sur les polices
type: docs
weight: 80
url: /fr/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Le code C++ pour appliquer l effet exposant et indice atomique au texte dans Excel avec l API Aspose.Cells for C++.
keywords: Excel exposant C++, Excel indice atomique C++, Excel exposant et indice atomique C++, insérer indice atomique et exposant dans Excel C++, ajouter indice atomique et exposant dans Excel C++, ajouter exposant et indice atomique Excel C++, ajouter exposant Excel C++, ajouter indice atomique Excel C++
---

{{% alert color="primary" %}}

Aspose.Cells offre la fonctionnalité d'appliquer les effets d'exposant (texte au-dessus de la ligne de base) et d'indice (texte en dessous de la ligne de base) au texte.

{{% /alert %}}

## **Travailler avec l'effet d'exposant et d'indice**

Appliquez l'effet d'exposant en définissant la propriété [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) de l'objet [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) sur **true**. Pour appliquer un indice, définissez la propriété [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) de l'objet [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) sur **true**.

Les exemples de code suivants montrent comment appliquer un exposant et un indice au texte.

### Code C++ pour appliquer l'effet exposant au texte

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

### Code C++ pour appliquer l'effet indice atomique au texte

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
