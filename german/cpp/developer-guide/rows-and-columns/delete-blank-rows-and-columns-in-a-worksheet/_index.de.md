---
title: Leere Zeilen und Spalten in einem Arbeitsblatt mit C++ löschen
linktitle: Löschen von leeren Zeilen und Spalten in einem Arbeitsblatt
type: docs
weight: 300
url: /de/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Leere Zeilen und Spalten in einem Arbeitsblatt mit Aspose.Cells und C++ löschen.
---

{{% alert color="primary" %}}

Es ist möglich, alle leeren Zeilen und Spalten aus einem Arbeitsblatt zu löschen. Dies ist nützlich, wenn beispielsweise eine PDF-Datei aus einer Microsoft Excel-Datei generiert wird und nur Zeilen und Spalten mit Daten oder verwandten Objekten konvertiert werden sollen.

Verwenden Sie die folgenden Aspose.Cells-Methoden, um leere Zeilen und Spalten zu löschen:

1. Um leere Zeilen zu löschen, verwenden Sie die [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/)-Methode. Bitte beachten Sie, dass für die zu löschenden leeren Zeilen nicht nur erforderlich ist, dass [**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/) wahr sein sollte, sondern es dürfen auch keine sichtbaren Kommentare für Zellen in diesen Zeilen definiert sein und kein Pivot-Table, dessen Bereich mit ihnen kollidiert.
2. Um leere Spalten zu löschen, verwenden Sie die [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/) Methode.

{{% /alert %}}

## C++ Code zum Löschen leerer Zeilen

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## C++ Code zum Löschen leerer Spalten

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
