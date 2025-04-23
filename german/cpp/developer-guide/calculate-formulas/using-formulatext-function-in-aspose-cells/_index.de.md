---
title: Verwendung der FormulaText Funktion in Aspose.Cells mit C++
linktitle: Verwendung der FormulaText Funktion
description: In diesem Artikel wird gezeigt, wie man die Funktion FormulaText in der Aspose.Cells Bibliothek verwendet, um Formeln in Microsoft Excel zu verarbeiten. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um den Formeltext der Zelle zu erhalten und zu setzen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, FormulaText Funktionen
type: docs
weight: 60
url: /de/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText ist eine Funktion von Excel 2013 und späteren Versionen. Sie wird nicht von früheren Versionen wie Excel 2010 oder 2007 usw. unterstützt. Wie der Name schon sagt, druckt sie den Text der Formel, der in einer bestimmten Zelle vorhanden ist. Dieser Artikel zeigt Ihnen, wie Sie diese Funktion mit Aspose.Cells verwenden können.

{{% /alert %}} 

Der folgende Beispielcode zeigt die Verwendung von FormulaText mit Aspose.Cells. Der Code schreibt zuerst eine Formel in Zelle A1 und druckt dann den Text der Formel mit FormulaText in Zelle A2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
