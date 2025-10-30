---
title: Einfügen und Löschen von Zeilen und Spalten in Excel Dateien mit C++
linktitle: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 70
url: /de/cpp/inserting-and-deleting-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen und Spalten mit der API Aspose.Cells for C++ einfügt und löscht.
keywords: Aspose.Cells C++ verwaltet Zeilen und Spalten, fügt Zeilen und Spalten ein, löscht Zeilen und Spalten
---

## **Einführung**

Beim Erstellen eines neuen Arbeitsblatts von Grund auf oder bei der Arbeit an einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um mehr Daten aufzunehmen. Umgekehrt können auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt gelöscht werden.
Um diese Anforderungen zu erfüllen, bietet Aspose.Cells eine sehr einfache Reihe von Klassen und Methoden, die nachstehend erläutert werden.

### **Zeilen und Spalten verwalten**

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Die Sammlung [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) stellt mehrere Methoden zur Verwaltung von Zeilen und Spalten in einem Arbeitsblatt bereit. Einige davon werden nachstehend erläutert.

{{% alert color="primary" %}}

Wenn Zeilen oder Spalten hinzugefügt werden, verschiebt sich der Inhalt im Arbeitsblatt nach unten oder nach rechts, und wenn Zeilen oder Spalten entfernt werden, verschiebt sich der Inhalt nach oben oder nach links.

{{% /alert %}}

## **Zeilen und Spalten einfügen**

### **Wie man eine Zeile einfügt**

Fügen Sie eine Zeile an beliebiger Stelle im Arbeitsblatt ein, indem Sie die [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)-Methode der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung aufrufen. Die [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)-Methode nimmt den Index der Zeile, an der die neue Zeile eingefügt werden soll.

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

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wie man mehrere Zeilen einfügt**

Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)-Methode der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung auf. Die [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)-Methode akzeptiert zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die insgesamt eingefügt werden müssen.

```c++
#include <iostream>
#include <fstream>
#include <memory>
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

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Wie man eine Zeile mit Formatierung einfügt**

Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)-Überladung, die [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) als Parameter akzeptiert. Setzen Sie die [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/)-Eigenschaft der [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/)-Klasse mit [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) Enumeration. Die [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/)-Enumeration hat drei Mitglieder, die unten aufgelistet sind.

- SameAsAbove: Formatiert die Zeile wie die obige Zeile.
- SameAsBelow: Formatiert die Zeile wie die Zeile unten.
- Löschen: Löscht das Format.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wie man eine Spalte einfügt**

Entwickler können auch eine Spalte in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)-Methode der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung aufrufen. Die [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)-Methode akzeptiert den Index der Spalte, an der die neue Spalte eingefügt werden soll.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Zeilen und Spalten löschen**

### **Wie man mehrere Zeilen löscht**

Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)-Methode der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung auf. Die [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)-Methode akzeptiert zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die insgesamt gelöscht werden müssen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wie man eine Spalte löscht**

Um eine Spalte aus dem Arbeitsblatt an beliebiger Stelle zu löschen, rufen Sie die [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)-Methode der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung auf. Die [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)-Methode akzeptiert den Index der zu löschenden Spalte.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
