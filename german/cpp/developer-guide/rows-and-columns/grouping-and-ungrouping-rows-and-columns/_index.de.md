---
title: Gruppieren und Gruppierung von Zeilen und Spalten mit C++
linktitle: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 50
url: /de/cpp/grouping-and-ungrouping-rows-and-columns/
description: Erfahren Sie, wie man Zeilen und Spalten in Excel Dateien mit Aspose.Cells und C++ gruppiert und aufhebt.
---

## **Einführung**

In einer Microsoft Excel-Datei können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Ebenen von Details anzuzeigen und auszublenden.

Klicken Sie auf die **Gliederungssymbole**, 1,2,3, + und -, um nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt bereitstellen, oder verwenden Sie die Symbole, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen, wie unten in der Abbildung gezeigt:

|**Gruppieren von Zeilen und Spalten.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gruppenverwaltung von Zeilen und Spalten**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse stellt eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung dar, die alle Zellen in der Arbeitsmappe repräsentiert.

Die [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einer Arbeitsmappe, einige davon werden unten genauer erläutert.

### **Zeilen und Spalten gruppieren**

Es ist möglich, Zeilen oder Spalten zu gruppieren, indem man die [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/)- und [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/)-Methoden der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung aufruft. Beide Methoden nehmen folgende Parameter an:

- Erster Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Group first six rows (from 0 to 5) and make them hidden
    worksheet.GetCells().GroupRows(0, 5, true);

    // Group first three columns (from 0 to 2) and make them hidden
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns grouped successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Gruppeneinstellungen**

Microsoft Excel ermöglicht es Ihnen, Gruppeneinstellungen für die Anzeige zu konfigurieren:

- Zusammenfassungszeilen unterhalb von Details.
- Zusammenfassungsspalten rechts neben dem Detail.

Entwickler können diese Gruppeneinstellungen mithilfe der [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/)-Eigenschaft der [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse konfigurieren.

### **Zusammenfassungszeilen unterhalb der Details**

Es ist möglich zu steuern, ob Zusammenfassungszeilen unterhalb des Details angezeigt werden, indem man die [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/)-Eigenschaft der [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/)-Klasse auf **true** oder **false** setzt.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Setting SummaryRowBelow property to false
    worksheet.GetOutline().SetSummaryRowBelow(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Zusammenfassungsspalten rechts von den Details**

Entwickler können auch steuern, ob Zusammenfassungsspalten rechts neben dem Detail angezeigt werden, indem sie die [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/)-Eigenschaft der [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/)-Klasse auf **true** oder **false** setzen.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Set summary column to the right
    worksheet.GetOutline().SetSummaryColumnRight(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Zeilen und Spalten entgruppieren**

Um gruppierte Zeilen oder Spalten aufzuheben, rufen Sie die [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlungsmethoden [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) und [**UngroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) auf. Beide Methoden nehmen zwei Parameter an:

- Erster Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.

[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) hat eine Überladung, die einen dritten booleschen Parameter akzeptiert. Wenn dieser auf **true** gesetzt wird, werden alle gruppierten Informationen entfernt. Andernfalls wird nur die äußere Gruppeninformation entfernt.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Ungrouping first six rows (from 0 to 5)
    worksheet.GetCells().UngroupRows(0, 5);

    // Ungrouping first three columns (from 0 to 2)
    worksheet.GetCells().UngroupColumns(0, 2);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```
