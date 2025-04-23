---
title: Union Bereich mit C++ erstellen
linktitle: Union Range erstellen
type: docs
weight: 360
url: /de/cpp/create-union-range/
description: Union Bereich in Excel Dateien mit Aspose.Cells und C++ erstellen.
---

## **Union Range erstellen**
Aspose.Cells bietet die Möglichkeit, einen Union-Bereich mit der [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) Methode zu erstellen. Die [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) Methode akzeptiert zwei Parameter: die Adresse zur Erstellung des Union-Bereichs und den Index des Arbeitsblatts. Die Methode gibt ein [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/) Objekt zurück.

Das folgende Code-Snippet demonstriert die Erstellung eines Union-Bereichs mit der [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) Methode. Die durch den Code generierte Ausgabedatei ist zur Referenz beigefügt.

- [Ausgabedatei](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
