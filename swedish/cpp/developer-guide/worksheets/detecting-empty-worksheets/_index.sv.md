---
title: Upptäcka tomma arbetsblad med C++
linktitle: Upptäcka tomma kalkylblad
type: docs
weight: 410
url: /sv/cpp/detecting-empty-worksheets/
description: Denna artikel visar kod som förklarar hur du kan upptäcka tomma Excel arbetsblad programmässigt med C++ API och Aspose.Cells bibliotek.
keywords: Upptäcka tomt arbetsblad C++, hitta tomt Excel arbetsblad C++
---

## **Kontrollera Populerade celler**

Arbetsblad kan ha en eller flera celler fyllda med värden, där ett värde kan vara enkelt (text, tal, datum/tid) eller en formel eller ett formelbaserat värde. Det är lätt att avgöra om ett givet arbetsblad är tomt eller inte. Allt vi behöver kontrollera är egenskaperna [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) eller [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/). Om de nämnda egenskaperna returnerar noll eller positiva värden betyder det att en eller flera celler har fyllts. Men om någon av dessa egenskaper ger -1, innebär det att inga celler har fyllts i det givna arbetsbladet.

{{% alert color="primary" %}}

Samlingarna för rader och kolumner har nollbaserade index, därför betyder en cell i rad 0 och kolumn 0 den första cellen i arbetsbladet, det vill säga A1.

{{% /alert %}}

## **Kontrollera toma initialiserade celler**

Alla celler som har värden initialiseras automatiskt. Men det är möjligt att ett arbetsblad har celler med endast formatering tillämpad. I ett sådant scenario kommer egenskaperna [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) eller [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) att returnera -1, vilket indikerar att inga ifyllda värden finns. Men initialiserade celler på grund av cellformat kan inte upptäckas med denna metod. För att kontrollera om ett arbetsblad innehåller tomma initialiserade celler rekommenderas att använda `MoveNext`-metoden på enumeratorn som hämtas från [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen. Om `MoveNext`-metoden returnerar **true**, betyder det att det finns en eller flera initialiserade celler i det givna arbetsbladet.

## **Kontrollera former**

Det är möjligt att ett givet arbetsblad inte har några ifyllda celler, men kan innehålla former och objekt som kontroller, diagram, bilder och så vidare. Om vi behöver kontrollera om ett arbetsblad innehåller någon form kan vi göra det genom att inspektera egenskapen [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/). Alla positiva värden indikerar att arbetsbladet innehåller form(ar).

## **Programmeringsexempel**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
