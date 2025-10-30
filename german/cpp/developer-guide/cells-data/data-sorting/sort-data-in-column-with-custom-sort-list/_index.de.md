---
title: Daten in einer Spalte mit benutzerdefinierter Sortierliste mit C++ sortieren
linktitle: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren.
type: docs
weight: 290
url: /de/cpp/sort-data-in-column-with-custom-sort-list/
description: Erfahren Sie, wie man Daten in der Spalte mithilfe einer benutzerdefinierten Liste durch die API Aspose.Cells for C++ sortiert.
keywords: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren, Daten nach benutzerdefinierter Liste sortieren.
---

## **Mögliche Verwendungsszenarien**

Sie können Daten in der Spalte mit einer benutzerdefinierten Liste sortieren. Dies kann mit [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) Methode durchgeführt werden. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommata enthalten. Falls sie Kommata wie "USA,US", "China,CN" usw. enthalten, müssen Sie die [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) Methode verwenden. Hier ist der letzte Parameter kein String, sondern ein Array von Strings.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielcode erklärt, wie die [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) Methode zum Sortieren von Daten mit einer benutzerdefinierten Sortierliste verwendet wird. Bitte sehen Sie die [Beispieldatei Excel](50528327.xlsx), die in diesem Code verwendet wird, und die [Ausgabedatei Excel](50528328.xlsx), die daraus generiert wurde. Das folgende Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
