---
title: Maximalbereich in einem Arbeitsblatt mit C++ abrufen
linktitle: Holen Sie den maximalen Bereich in einem Arbeitsblatt ab
type: docs
weight: 360
url: /de/cpp/get-max-range-in-a-worksheet/
description: Dieser Artikel beschreibt, wie man den Maximalbereich, den Maximal Datenbereich und den Maximal Anzeige Bereich von Excel Dateien mit der Aspose.Cells for C++ Bibliothek ermittelt.
---

{{% alert color="primary" %}} 

Beim Lesen von Daten aus dem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Kopieren aller Daten aus einem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Exportieren eines bestimmten Bereichs nach HTML und PDF müssen wir den maximalen Bereich kennen.

Aspose.Cells for C++ bietet verschiedene Möglichkeiten, den Maximalbereich in einem Arbeitsblatt zu ermitteln. 

{{% /alert %}} 

## **Den Maximalbereich abrufen**
In Aspose.Cells werden, wenn die Objekte [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) und [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) initialisiert sind, diese Zeilen und Spalten zum maximalen Bereich gezählt, selbst wenn in leeren Zeilen oder Spalten keine Daten vorhanden sind.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Maximalen Datenbereich abrufen**
In den meisten Fällen müssen wir nur alle Bereiche erhalten, die alle Daten enthalten, auch wenn die leeren Zellen außerhalb des Bereichs formatiert sind.
Und die Einstellungen zu Formen, Tabellen und Pivot-Tabellen werden ignoriert.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Maximale Anzeigebereich erhalten**
Wenn wir alle Daten aus dem Arbeitsblatt in HTML, PDF oder Bildern exportieren, müssen wir einen Bereich erhalten, der alle sichtbaren Objekte enthält, einschließlich Daten, Styles, Grafiken, Tabellen und Pivot-Tabellen.
Die folgenden Codes zeigen, wie der maximale Anzeigebereich in HTML gerendert wird:

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Hier ist die [Quelldatei Excel](Book1.xlsx).
{{< app/cells/assistant language="cpp" >}}
