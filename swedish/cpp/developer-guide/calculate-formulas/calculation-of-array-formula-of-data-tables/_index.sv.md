---
title: Beräkning av array formel för datatabeller med C++
linktitle: Beräkning av Data Table Arrayformel
description: Hur man använder Aspose.Cells biblioteket för att beräkna array formler för en datatabell i Microsoft Excel med C++. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att beräkna array formeln för datatabellen och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, datatabeller, array formler, beräkningar, C++
type: docs
weight: 70
url: /sv/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Du kan skapa en datatabell i Microsoft Excel genom att använda Data > Vad om-analys > Datatabell.... Aspose.Cells tillåter nu beräkning av arrayformeln för en datatabell. Använd [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) som normalt för att beräkna vilken typ av formler som helst.

{{% /alert %}}

I följande kodexempel använde vi [källa excel-fil](5115535.xlsx). Om du ändrar värdet i cell B1 till 100 blir värdena i datatabellen som är fyllda med gult färgad till 120, vilket visas i följande bilder. Detta kodexempel genererar [utdata PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Följande kod användes för att generera [utdata PDF](5115538.pdf) från [källa excel-fil](5115535.xlsx). Läs kommentarerna för mer information.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
