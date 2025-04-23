---
title: Formel für benannte Bereiche mit C++ setzen
linktitle: Formel für benanntes Bereich setzen
type: docs
weight: 20
url: /de/cpp/setting-formula-for-named-range/
description: Erfahren Sie, wie Sie Formeln für benannte Bereiche in Excel Dateien mit Aspose.Cells in C++ festlegen.
---

## **Formel für benanntes Bereich setzen**
Genau wie die Excel-Anwendung bietet die Aspose.Cells API die Möglichkeit, beim Verwenden der [GetRefersTo()](https://reference.aspose.com/cells/cpp/aspose.cells/range/getrefersto/) Eigenschaft eine Formel für einen benannten Bereich anzugeben. Es gibt zahlreiche Anwendungsfälle für diese Funktion, einige werden im Folgenden erläutert.

### **Eine einfache Formel für benannten Bereich setzen**
Eine einfache Formel könnte eine Referenz auf eine andere Zelle im gleichen (oder anderen) Arbeitsblatt sein. Das folgende Beispiel erstellt einen benannten Bereich in einem neuen Tabellenblatt und setzt seine Referenz auf eine andere Zelle.

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

    // Create an instance of Workbook
    Workbook book;

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "NewNamedRange"
    int index = worksheets.GetNames().Add(u"NewNamedRange");

    // Access the newly created Named Range
    Name name = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
    name.SetRefersTo(u"=Sheet1!$A$3");

    // Set the formula in the cell A1 to the newly created Named Range
    worksheets.Get(0).GetCells().Get(u"A1").SetFormula(u"NewNamedRange");

    // Insert the value in cell A3 which is being referenced in the Named Range
    worksheets.Get(0).GetCells().Get(u"A3").PutValue(u"This is the value of A3");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named range created and formula calculated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Eine komplexe Formel für benannten Bereich setzen**
Eine komplexe Formel könnte alles Mögliche sein, zum Beispiel ein dynamischer Bereich oder eine Formel über mehrere Zellen in verschiedenen Arbeitsblättern. Das folgende Beispiel erstellt einen dynamischen Bereich mit der INDEX-Funktion, um den Wert aus einer Liste basierend auf seiner Position zu erhalten.

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

    // Create an instance of Workbook
    Workbook book;

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "data"
    int index = worksheets.GetNames().Add(u"data");

    // Access the newly created Named Range from the collection
    Name data = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a cell range in same worksheet
    data.SetRefersTo(u"=Sheet1!$A$1:$A$10");

    // Add another Named Range with name "range"
    index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property to a formula using the Named Range data
    range.SetRefersTo(u"=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

    // Save the workbook
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named ranges created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Hier ist ein weiteres Beispiel, das einen benannten Bereich verwendet, um Werte aus 2 Zellen in verschiedenen Arbeitsblättern zu summieren.

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

    // Create an instance of Workbook
    Workbook book;

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Insert some data in cell A1 of Sheet1
    worksheets.Get(u"Sheet1").GetCells().Get(u"A1").PutValue(10);

    // Add a new Worksheet and insert a value to cell A1
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").PutValue(10);

    // Add a new Named Range with name "range"
    int index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a SUM function
    range.SetRefersTo(u"=SUM(Sheet1!$A$1,Sheet2!$A$1)");

    // Insert the Named Range as formula to 3rd worksheet
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").SetFormula(u"range");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Output file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
