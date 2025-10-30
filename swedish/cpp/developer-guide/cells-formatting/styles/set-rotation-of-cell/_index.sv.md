---
title: Hur roterar man texten i en cell med C++
linktitle: Hur man roterar text i en cell
type: docs
weight: 80
url: /sv/cpp/how-to-rotate-text-of-cell/
description: C++ kod för att rotera text i cell med Aspose.Cells for C++ API
keywords: c++ rotera text i cell, c++ programmatisk rotation av text i cell i arbetsbok, programmatisk inställning av cellrotation i arbetsbok, c++ hur man roterar text i cell i excel
---

## **Rotera text i cell i Aspose.Cells**

Aspose.Cells är en kraftfull C++ komponent som möjliggör för utvecklare att arbeta med Excel-kalkylblad programmatiskt. En av funktionerna som tillhandahålls av Aspose.Cells är förmågan att rotera celler, vilket gör att du kan anpassa orienteringen av text och förbättra den visuella presentationen av dina data. I detta dokument utforskar vi hur man roterar celler med Aspose.Cells.

## **Hur man roterar text i cell i Excel**
För att rotera en cell i Excel kan du använda följande steg:
1. Öppna Excel och välj den cell eller det cellområde som du vill rotera.
1. Högerklicka på den markerade cellen/cellerna och välj "Formatera celler" i snabbmenyn. Alternativt kan du gå till fliken "Hem" i Excels menyflik, klicka på rullgardinsmenyn "Formatera" i gruppen "Celler" och välj "Formatera celler".
1. I dialogrutan "Formatera celler" navigerar du till fliken "Justering".
1. Under avsnittet "Orientering" ser du alternativen för att rotera texten. Du kan direkt ange önskad rotationsvinkel i grader i rutan "Grader". Positiva värden roterar texten moturs, och negativa värden roterar den medurs.
<br>
![todo:image_alt_text](alignment.png)
1. När du har valt önskad rotation klickar du på "OK" för att tillämpa ändringarna. Den valda cellen/cellerna kommer nu att vara roterade enligt din valda rotationsvinkel eller orientering.

## **Hur man roterar text i cell med hjälp av Aspose.Cells API**

[**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/)-egenskapen gör det bekvämt att rotera celler. För att rotera celler i Aspose.Cells måste du följa dessa steg:
1. Läs in Excel-arbetsboken
<br>
Först måste du läsa in Excel-arbetsboken med hjälp av Aspose.Cells. Du kan använda Workbook-klassen för att öppna en befintlig Excel-fil eller skapa en ny. 

1. Kom åt arbetsbladet
<br>
När arbetsboken har lästs in måste du komma åt det arbetsblad där du vill rotera cellerna. Du kan antingen komma åt arbetsbladet genom dess index eller namn. 

1. Rotera texten i cellen
<br>
Nu när du har åtkomst till arbetsbladet kan du rotera cellerna genom att ändra Style-objektet för de önskade cellerna. Style-objektet låter dig ställa in olika formateringsalternativ, inklusive rotation. 

1. Spara arbetsboken
<br>
Efter att ha roterat cellerna kan du spara den modifierade arbetsboken till en fil eller ström med hjälp av Save -metoden.

## **C++ exempel kod**

Var god se följande kod, den skapar ett arbetsboksobjekt och ställer in olika rotationsvinklar för flera celler. Skärmbilden visar resultatet efter körningen av det här provkoden.
<br>
<img src="rotation.png" width=80% />

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
