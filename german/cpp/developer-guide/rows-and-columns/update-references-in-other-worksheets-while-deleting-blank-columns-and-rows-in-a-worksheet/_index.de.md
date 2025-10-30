---
title: Aktualisieren Sie Referenzen in anderen Arbeitsblättern beim Löschen leerer Spalten und Zeilen in einem Arbeitsblatt mit C++
linktitle: Referenzen in anderen Arbeitsblättern aktualisieren
type: docs
weight: 5000
url: /de/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Lernen Sie, wie Sie Referenzen in anderen Arbeitsblättern aktualisieren, während Sie leere Spalten und Zeilen in einem Arbeitsblatt mit Aspose.Cells for C++ löschen.
---

{{% alert color="primary" %}}

Wenn Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen, werden seine Referenzen in anderen Arbeitsblättern ungültig. Wenn Sie dieses Verhalten vermeiden und sicherstellen möchten, dass Referenzen auf das aktuelle Arbeitsblatt in anderen Arbeitsblättern ebenfalls aktualisiert werden, verwenden Sie die [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)-Eigenschaft und setzen Sie sie auf **true**.

{{% /alert %}}

## **Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen**

Bitte sehen Sie sich den folgenden Beispielcode und seine Konsolenausgabe an. Die Zelle E3 im zweiten Arbeitsblatt enthält eine Formel `=Sheet1!C3`, die sich auf die Zelle C3 im ersten Arbeitsblatt bezieht. Wenn Sie die [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)-Eigenschaft auf **true** setzen, wird diese Formel nach dem Löschen leerer Spalten und Zeilen im ersten Arbeitsblatt zu `=Sheet1!A1` aktualisiert. Wenn Sie jedoch die [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)-Eigenschaft auf **false** setzen, bleibt die Formel in Zelle E3 des zweiten Arbeitsblatts `=Sheet1!C3` und wird ungültig.

### **Programmierbeispiel**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Add second sheet with name Sheet2
    wb.GetWorksheets().Add(u"Sheet2");

    // Access first sheet and add some integer value in cell C1
    // Also add some value in any cell to increase the number of blank rows and columns
    Worksheet sht1 = wb.GetWorksheets().Get(0);
    sht1.GetCells().Get(u"C1").PutValue(4);
    sht1.GetCells().Get(u"K30").PutValue(4);

    // Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
    Worksheet sht2 = wb.GetWorksheets().Get(1);
    sht2.GetCells().Get(u"E3").SetFormula(u"'Sheet1'!C1");

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
    std::cout << "Cell E3 before deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    // If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
    DeleteOptions opts;
    opts.SetUpdateReference(true);

    // Delete all blank rows and columns with delete options
    sht1.GetCells().DeleteBlankColumns(opts);
    sht1.GetCells().DeleteBlankRows(opts);

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "Cell E3 after deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konsolenausgabe**

Dies ist die Konsolenausgabe des oben genannten Beispielcodes, wenn die [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)-Eigenschaft auf **true** gesetzt ist.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4

{{< /highlight >}}

Dies ist die Konsolenausgabe des oben genannten Beispielcodes, wenn die [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)-Eigenschaft auf **false** gesetzt ist. Wie Sie sehen können, wird die Formel in Zelle E3 des zweiten Arbeitsblatts nicht aktualisiert, und ihr Zellwert ist jetzt 0 anstelle von 4, was ungültig ist.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
