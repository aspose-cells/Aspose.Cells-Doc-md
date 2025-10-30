---
title: Erstellen, Zugriff auf, und Kopieren benannter Bereiche mit C++
linktitle: Erstellen, Zugriff auf, und Kopieren benannter Bereiche
type: docs
weight: 200
url: /de/cpp/create-access-and-copy-named-ranges/
description: Erfahren Sie, wie Sie benannte Bereiche in Excel Dateien mit Aspose.Cells und C++ erstellen, zugreifen und kopieren.
---

## **Einführung**

Normalerweise werden Spalten- und Zeilenbeschriftungen verwendet, um einzelne Zellen zu referenzieren. Es ist möglich, aussagekräftige Namen zu erstellen, um Zellen, Zellbereiche, Formeln oder Konstanten darzustellen. Das Wort **Name** kann sich auf eine Zeichenkette beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen Konstantenwert repräsentiert. Das Zuweisen eines Namens zu einem Bereich bedeutet, dass dieser Zellbereich anhand seines Namens referenziert werden kann. Verwenden Sie leicht verständliche Namen, wie z.B. Produkte, um schwer verständliche Bereiche wie Sales!C20:C30 zu kennzeichnen. Labels können in Formeln verwendet werden, die sich auf Daten im selben Arbeitsblatt beziehen; wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. *Benannte Bereiche gehören zu den leistungsstärksten Funktionen von Microsoft Excel, insbesondere wenn sie als Quellbereich für Listen, Pivot-Tabellen, Diagramme usw. genutzt werden.

## **Arbeiten mit benannten Bereich unter Verwendung von Microsoft Excel**

### **Benannte Bereiche erstellen**

Die folgenden Schritte beschreiben, wie man eine Zelle oder einen Zellbereich mit **MS Excel** benennt. Diese Methode gilt für **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** und **2002**.

1. Wählen Sie die Zelle oder den Zellbereich aus, den Sie benennen möchten.
1. Klicken Sie auf das **Namensfeld** am linken Ende der Formelzeile.
1. Geben Sie den Namen für die Zellen ein.
1. Drücken Sie die EINGABETASTE.

{{% alert color="primary" %}}

Sie können eine Zelle nicht benennen, während Sie den Inhalt der Zelle ändern.

{{% /alert %}}

## **Arbeiten mit benannten Bereich unter Verwendung von Aspose.Cells**

Hier verwenden wir die Aspose.Cells API, um die Aufgabe zu erledigen.
Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) stellt eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung bereit.

### **Benannten Bereich erstellen**

Es ist möglich, einen benannten Bereich durch Aufruf der überladenen [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)-Methode der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung zu erstellen. Eine typische Version der [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)-Methode akzeptiert folgende Parameter:

- Name der oberen linken Zelle, Name der oberen linken Zelle im Bereich.
- Name der unteren rechten Zelle, Name der unteren rechten Zelle im Bereich.

Wenn die Methode [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) aufgerufen wird, wird der neu erstellte Bereich als Instanz der Klasse [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) zurückgegeben. Verwenden Sie dieses Objekt [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/), um den benannten Bereich zu konfigurieren. Setzen Sie beispielsweise den Namen des Bereichs mit der [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/)-Eigenschaft. Das folgende Beispiel zeigt, wie man einen benannten Bereich von Zellen erstellt, der sich über B4:G14 erstreckt.

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Daten in die Zellen des benannten Bereichs eingeben**

Sie können Daten in die einzelnen Zellen eines Bereichs einfügen, indem Sie dem Muster folgen:

- **C++**: Range Zeile, Spalte

Angenommen, Sie haben einen benannten Bereich von Zellen, der A1:C4 umfasst. Die Matrix ergibt 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequentiell angeordnet: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:

- FirstRow gibt den Index der ersten Zeile im benannten Bereich zurück.
- FirstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.
- RowCount gibt die Gesamtanzahl der Zeilen im benannten Bereich zurück.
- ColumnCount gibt die Gesamtanzahl der Spalten im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Zellen im benannten Bereich identifizieren**

Sie können Daten in die einzelnen Zellen eines Bereichs einfügen, indem Sie dem Muster folgen:

- **C++**: Range Zeile, Spalte

Wenn Sie einen benannten Bereich haben, der A1:C4 umfasst. Die Matrix macht 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequentiell angeordnet: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:

- FirstRow gibt den Index der ersten Zeile im benannten Bereich zurück.
- FirstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.
- RowCount gibt die Gesamtanzahl der Zeilen im benannten Bereich zurück.
- ColumnCount gibt die Gesamtanzahl der Spalten im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Zugriff auf benannte Bereiche**

#### **Auf einen bestimmten benannten Bereich zugreifen**

Rufen Sie die Methode [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) der [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung auf, um einen Bereich nach dem angegebenen Namen zu erhalten. Eine typische [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/)-Methode nimmt den Namen des benannten Bereichs entgegen und gibt den angegebenen benannten Bereich als Instanz der [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Klasse zurück. Das folgende Beispiel zeigt, wie auf einen bestimmten Bereich nach seinem Namen zugegriffen wird.

```c++
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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **Zugriff auf alle benannten Bereiche in einer Arbeitsmappe**

Rufen Sie die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung auf, um die [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/)-Methode aufzurufen und alle benannten Bereiche in einer Tabelle zu erhalten. Die [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/)-Methode gibt ein Array aller benannten Bereiche in der [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung zurück.

Das folgende Beispiel zeigt, wie auf alle benannten Bereiche in einer Arbeitsmappe zugegriffen wird.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Benannte Bereiche kopieren**

Aspose.Cells stellt die [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/)-Methode bereit, um einen Zellbereich mit Formatierungen in einen anderen Bereich zu kopieren.

Das folgende Beispiel zeigt, wie ein Quellbereich von Zellen in einen anderen benannten Bereich kopiert wird.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
