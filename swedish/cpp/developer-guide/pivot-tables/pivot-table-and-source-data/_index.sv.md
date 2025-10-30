---
title: PivotTabell och Källdata med C++
linktitle: Pivot tabell och källdata
type: docs
weight: 30
url: /sv/cpp/pivot-table-and-source-data/
description: Lär dig hur du dynamiskt ändrar en pivottabellens källdata med Aspose.Cells i C++.
---

## **Pivot-tabellens källdata**

Det finns tillfällen då du vill skapa Microsoft Excel-rapporter med pivottabeller som hämtar data från olika datakällor (t.ex. en databas) som inte är kända vid design-tid. Denna artikel ger en metod för att dynamiskt ändra en pivot-tabells datakälla.

### **Ändra en pivot-tabells källdata**

1. Skapa en ny designer-mall.
   1. Skapa en ny designer-mallfil enligt skärmbilden nedan.
   1. Definiera sedan ett namngivet område, **Datakälla**, som hänvisar till detta cellområde.

      **Skapa en designer-mall & definiera ett namngivet område, Datakälla** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Skapa en pivot-tabell baserad på detta namngivna område.
   1. I Microsoft Excel, välj **Data**, sedan **Pivottabell** och **PivotDiagramrapport**.
   1. Skapa en pivottabell baserad på det namngivna området som skapats i det första steget.

      **Skapa en pivottabell baserad på det namngivna området, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Dra det motsvarande fältet till pivottabellraden och kolumnen, skapa sedan den resulterande pivottabellen enligt skärmdumpen nedan.

   **Skapa en pivottabell baserad på ett motsvarande fält** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Högerklicka på pivottabellen och välj **Tabelloptioner**.
   1. Markera **Uppdatera vid öppning** i inställningarna för **Dataalternativ**.

      **Inställning av pivottabellalternativ** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Nu kan du spara den här filen som din designer-mallfil.

1. Försörjning av ny data och ändring av källdata för en pivottabell.
   1. När den designer-mall är skapad, använd följande kod för att ändra källan till pivottabellen.

Genom att köra den här exempelkoden nedan ändras källan till pivottabellen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
