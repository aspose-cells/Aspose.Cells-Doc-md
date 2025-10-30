---
title: Använd FormelText funktionen i Aspose.Cells med C++
linktitle: Använda FormelText funktionen
description: Denna artikel introducerar hur man använder FormulaText funktionen i Aspose.Cells biblioteket för att bearbeta formler i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att få och ställa in formeltexten för cellen och få resultatet. Till slut sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, FormulaText funktioner
type: docs
weight: 60
url: /sv/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText är en funktion i Excel 2013 och senare. Den stöds inte av tidigare versioner som Excel 2010 eller 2007 etc. Som namnet antyder skriver den ut texten i formeln som finns i en given cell. Den här artikeln kommer att visa dig hur du använder den här funktionen med Aspose.Cells.

{{% /alert %}} 

Följande exempelkod visar användningen av FormulaText med Aspose.Cells. Koden skriver först en formel i cell A1 och skriver sedan ut texten för formeln med FormulaText i cell A2.

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

## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
