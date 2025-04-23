---
title: Superskript und Subskript Effekte auf Schriftarten mit C++ anwenden
linktitle: Überlagerungs und Indizierungseffekte auf Schriftarten anwenden
type: docs
weight: 80
url: /de/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Der C++ Code wendet Superskript und Subskript Effekte auf Text in Excel unter Verwendung der API Aspose.Cells for C++ an.
keywords: Excel Superscript C++, Excel Subscript C++, Excel Superscript und Subscript C++, Subscript und Superscript in Excel einfügen, Subscript und Superscript in Excel hinzufügen, Superscript und Subscript in Excel hinzufügen, Superscript in Excel hinzufügen, Subscript in Excel hinzufügen
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Funktionalität, Überlagerungs- (Text über der Grundlinie) und Indizierungseffekte (Text unterhalb der Grundlinie) auf Text anzuwenden.

{{% /alert %}}

## **Arbeiten mit Überlagerungs- und Indizierungseffekten**

Wenden Sie den Überlagerungseffekt an, indem Sie die [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) des Objekts [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) Eigenschaft auf **true** setzen. Für die Anwendung der Indizierung setzen Sie die [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) des Objekts [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) Eigenschaft auf **true**.

Die folgenden Codebeispiele zeigen, wie man Über- und Indizierung auf Text anwendet.

### C++-Code zur Anwendung des Superskript-Effekts auf Text

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

### C++-Code zur Anwendung des Subskript-Effekts auf Text

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
