---
title: Überprüfen, ob der Zellwert die Datenvalidierungsregeln erfüllt mit C++
linktitle: Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht
type: docs
weight: 210
url: /de/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for C++ überprüfen, ob der Zellwert die Datenvalidierungsregeln erfüllt.
keywords: Zellenvalidierungswert erhalten, Zellenvalidierungswert erhalten, Überprüfen Sie, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht
---

{{% alert color="primary" %}} 

Microsoft Excel erlaubt es Benutzern, Datenvalidierungsregeln zu Zellen hinzuzufügen. Zum Beispiel gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Zahl eingibt, zeigt Excel eine Fehlermeldung an und fordert ihn auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie eine Zahl, z.B. 3, in die Zelle kopieren und einfügen, überprüft Excel die Validierung nicht und zeigt keine Fehlermeldung an.

Manchmal ist es erforderlich, programmgesteuert zu überprüfen, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht. Im obigen Fall sollte der Eintrag beispielsweise fehlschlagen.

{{% /alert %}} 

## **Einführung**
Aspose.Cells bietet die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) an, um Zellwerte programmatisch zu validieren. Wenn der Wert in einer Zelle die angewendete Datenvalidierungsregel nicht erfüllt, gibt die Methode **False** zurück, andernfalls **True**.

Das folgende Beispiel zeigt, wie die Methode [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) funktioniert. Zunächst wird der Wert 3 in C1 eingegeben. Da dieser die Datenvalidierungsregel nicht erfüllt, gibt die Methode **False** zurück. Danach wird der Wert 15 in C1 eingegeben, der die Regel erfüllt, und die Methode gibt **True** zurück. Für den Wert 30 ergibt die Methode wieder **False**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ergebnis**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
