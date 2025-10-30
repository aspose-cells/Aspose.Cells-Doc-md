---
title: Zeilen in einem Excel Arbeitsblatt mit C++ einfügen oder löschen
linktitle: Zeilen einfügen oder löschen
type: docs
weight: 20
url: /de/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Dieser Artikel enthält den C++ Code zum Einfügen und Löschen von Zeilen in einem Excel Arbeitsblatt.
keywords: C++ Einfügen oder Löschen von Zeilen in Excel Arbeitsblatt, C++ Zeilen in Excel einfügen oder löschen, C++ Zeilen in Excel einfügen, C++ Zeilen in Excel löschen, Zeilen in Excel Arbeitsblatt mit C++, Zeilen in Excel mit C++, Zeilen in Excel mit C++ einfügen, Zeilen in Excel mit C++ löschen
---

{{% alert color="primary" %}}

Beim Erstellen eines neuen Arbeitsblatts oder bei der Arbeit mit einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um Daten zu berücksichtigen. In anderen Fällen könnte es erforderlich sein, Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt zu löschen.

{{% /alert %}}

Aspose.Cells bietet zwei Methoden zum Einfügen und Löschen von Zeilen: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) und [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). Diese Methoden sind auf Leistung optimiert und erledigen die Aufgabe sehr schnell.

Um eine bestimmte Anzahl von Zeilen einzufügen oder zu entfernen, empfehlen wir, stets die Methoden [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) und [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) anstelle der Verwendung der Methoden [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) oder [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) in einer Schleife zu verwenden.

Aspose.Cells arbeitet genauso wie Microsoft Excel. Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt des Arbeitsblatts nach unten und nach rechts verschoben. Wenn Zeilen oder Spalten entfernt werden, wird der Inhalt des Arbeitsblatts nach oben oder nach links verschoben. Referenzen in anderen Arbeitsblättern und Zellen werden aktualisiert, wenn Zeilen hinzugefügt oder entfernt werden.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
