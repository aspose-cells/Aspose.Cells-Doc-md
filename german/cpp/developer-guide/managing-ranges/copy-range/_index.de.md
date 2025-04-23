--- 
title: Kopieren von Bereichen in Excel mit C++ 
linktitle: Bereiche kopieren 
type: docs 
weight: 105 
url: /de/cpp/copy-ranges-of-excel/ 
description: Erfahren Sie, wie Sie Bereiche in Excel mit Aspose.Cells und C++ kopieren. 
--- 

## **Einführung**

In Excel können Sie einen Bereich auswählen, den Bereich kopieren und ihn mit spezifischen Optionen in dasselbe Arbeitsblatt, in andere Arbeitsblätter oder in andere Dateien einfügen.

## **Bereiche mit Aspose.Cells kopieren**

Aspose.Cells bietet einige Überladungen der Methoden [Range.Copy](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/), um Bereiche zu kopieren. Und [Range.CopyStyle](https://reference.aspose.com/cells/cpp/aspose.cells/range/copystyle/) kopiert nur den Stil des Bereichs; [Range.CopyData](https://reference.aspose.com/cells/cpp/aspose.cells/range/copydata/) kopiert nur die Werte des Bereichs.

## **Bereich kopieren**

Erstellen von zwei Bereichen: Der Quellbereich, der Zielbereich, dann Kopieren des Quellbereichs in den Zielbereich mit der Range.Copy-Methode.

Siehe den folgenden Code:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into
    // A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy source range to target range in the same worksheet 
    targetRange.Copy(sourceRange);

    // Create a new worksheet.
    worksheets.Add();
    worksheet = worksheets.Get(1);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another worksheet 
    targetRange.Copy(sourceRange);

    // Copy to another workbook
    Workbook anotherWorkbook;

    worksheet = workbook.GetWorksheets().Get(0);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another workbook 
    targetRange.Copy(sourceRange);

    std::cout << "Copy operations completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Bereich mit Optionen einfügen**

Aspose.Cells unterstützt das Einfügen des Bereichs mit einem spezifischen Typ.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Init paste options.
    PasteOptions options;
    // Set paste type.
    options.SetPasteType(PasteType::ValuesAndFormats);
    options.SetSkipBlanks(true);

    // Copy source range to target range
    targetRange.Copy(sourceRange, options);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Nur Daten des Bereichs kopieren**
Sie können auch die Daten mit der Range.CopyData-Methode wie folgt kopieren:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // A few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(123);

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy the data of source range to target range
    targetRange.CopyData(sourceRange);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Zeilenhöhen des Quellbereichs in den Zielbereich kopieren](/cells/de/cpp/copy-row-heights-of-source-range-to-destination-range/)
