---
title: Uppdatera referenser i andra kalkblad medan du tar bort tomma kolumner och rader i ett kalkblad med C++
linktitle: Uppdatera referenser i andra kalkblad
type: docs
weight: 5000
url: /sv/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Lära dig hur man uppdaterar referenser i andra kalkblad medan du tar bort tomma kolumner och rader i ett kalkblad med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

När du tar bort tomma kolumner och rader i ett kalkblad blir dess referenser i andra kalkblad ogiltiga. Om du vill undvika detta beteende och se till att referenser till det aktuella kalkbladet i andra kalkblad också uppdateras, använd egenskapen [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) och ställ in den till **true**.

{{% /alert %}}

## **Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad**

Se följande exempel på kod och dess konsolutdata. Cellen E3 i det andra kalkbladet har en formel `=Sheet1!C3`, som hänvisar till cell C3 i det första kalkbladet. Om du ställer in egenskapen [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) till **true**, kommer denna formel att uppdateras till `=Sheet1!A1` efter att ha tagit bort tomma kolumner och rader i det första kalkbladet. Men om du ställer in egenskapen [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) till **false**, förblir formeln i cell E3 i det andra kalkbladet `=Sheet1!C3` och blir ogiltig.

### **Programmeringsexempel**

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

### **Konsoloutput**

Detta är konsolutdata för ovanstående exempel på kod när egenskapen [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) är inställd på **true**.

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

Detta är konsolutdata för ovanstående exempel på kod när egenskapen [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) är inställd på **false**. Som du kan se, uppdateras inte formeln i cell E3 i det andra kalkbladet, och dess cellvärde är nu 0 istället för 4, vilket är ogiltigt.

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
