---
title: Zeilen und Spalten mit C++ ausblenden und anzeigen
linktitle: Zeilen und Spalten ausblenden und anzeigen
type: docs
weight: 60
url: /de/cpp/hiding-and-showing-rows-and-columns/
description: Erfahren Sie, wie Sie Zeilen und Spalten in Excel Dateien programmatisch mit Aspose.Cells und C++ ausblenden und anzeigen können.
---

{{% alert color="primary" %}}

Manchmal ist es sinnvoll, bestimmte Zeilen oder Spalten in einem Arbeitsblatt auszublenden und später wieder anzuzeigen. Microsoft Excel bietet diese Funktion, ebenso Aspose.Cells.

{{% /alert %}}

## **Steuerung der Sichtbarkeit von Zeilen und Spalten**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die Sammlung [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten diskutiert.

### **Verbergen von Zeilen und Spalten**

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/)- und [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/)-Methoden der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter an, um die spezifische Zeile oder Spalte auszublenden.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}}

### **Anzeigen von Zeilen und Spalten**

Entwickler können eine versteckte Zeile oder Spalte anzeigen, indem sie die [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/)- und [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/)-Methoden der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter an:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

Wenn Sie eine ausgeblendete Spalte sichtbar machen möchten und diese wieder auf die zuvor zugewiesene Breite oder die ursprüngliche Breite zurücksetzen möchten, unblenden Sie die Spalte mit einer negativen Breite. Zum Beispiel: `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **Mehrere Zeilen und Spalten verstecken**

Entwickler können mehrere Zeilen oder Spalten auf einmal ausblenden, indem sie die [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/)- und [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/)-Methoden der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der auszublendenden Zeilen oder Spalten als Parameter an.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Es ist auch möglich, die [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)- und [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/)-Methoden der Klasse [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
