---
title: DatenSortierung mit C++
linktitle: Daten sortieren
type: docs
weight: 130
url: /de/cpp/sort-data-of-excel/
description: Lernen Sie, wie Sie Daten mit der Aspose.Cells for C++ API sortieren.
keywords: Sortieren Sie Daten in aufsteigender oder absteigender Reihenfolge, sortieren Sie Daten basierend auf der Hintergrundfarbe
---

{{% alert color="primary" %}}

Die Datensortierung ist eine der vielen nützlichen Funktionen von Microsoft Excel. Benutzer können Daten zur einfacheren Überprüfung sortieren. Aspose.Cells ermöglicht Entwicklern, Tabellendaten alphabetisch oder numerisch zu sortieren, was genauso funktioniert wie Microsoft Excel, um Daten zu sortieren.

{{% /alert %}}

## **Daten sortieren in Microsoft Excel**

Um Daten in Microsoft Excel zu sortieren:

1. Wählen Sie **Daten** im **Sortieren**-Menü aus. Der Sortieren-Dialog wird angezeigt.
1. Wählen Sie eine Sortieroption aus.

Im Allgemeinen wird das Sortieren auf einer Liste durchgeführt - definiert als eine zusammenhängende Gruppe von Daten, bei der die Daten in Spalten angezeigt werden.

## **Daten mit Aspose.Cells sortieren**

Aspose.Cells bietet die [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/)-Klasse zur Sortierung von Daten in aufsteigender oder absteigender Reihenfolge. Die Klasse hat einige wichtige Elemente, wie z.B. Eigenschaften wie Key1 ... Key3 und Order1 ... Order3. Diese Elemente werden verwendet, um sortierte Schlüssel zu definieren und die Sortierreihenfolge des Schlüssels anzugeben.

Sie müssen Schlüssel definieren und die Sortierreihenfolge festlegen, bevor Sie das Daten sortieren implementieren. Die Klasse bietet die [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/)-Methode, die verwendet wird, um Daten nach den Zelldaten in einem Arbeitsblatt zu sortieren.

Die [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/)-Methode akzeptiert die folgenden Parameter:

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), die Zellen für das zugrunde liegende Arbeitsblatt.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), der Bereich von Zellen. Definieren Sie den Zellenbereich, bevor Sie das Daten sortieren anwenden.

In diesem Beispiel wird die Vorlagendatei "Buch1.xls" verwendet, die in Microsoft Excel erstellt wurde. Nach Ausführen des unten stehenden Codes wird die Daten entsprechend sortiert.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Wenn Sie *Von links nach rechts sortieren* möchten, verwenden Sie das [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/)-Attribut.

{{% /alert %}}

### **Daten mit Hintergrundfarbe sortieren**

Excel bietet Funktionen zur Sortierung von Daten basierend auf der Hintergrundfarbe. Die gleiche Funktion wird mit Aspose.Cells über den DataSorter bereitgestellt, in dem [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor in [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) verwendet werden kann, um Daten basierend auf der Hintergrundfarbe zu sortieren. Alle Zellen, die die angegebene Farbe in der [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/)-Funktion enthalten, werden oben oder unten platziert, je nach Einstellung von SortOrder, und die Reihenfolge der restlichen Zellen wird überhaupt nicht geändert.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Daten in Spalte mit benutzerdefinierter Sortierliste sortieren](/cells/de/cpp/sort-data-in-column-with-custom-sort-list/)
- [Spezifizieren von Sortierwarnungen beim Sortieren von Daten](/cells/de/cpp/specifying-sort-warning-while-sorting-data/)
