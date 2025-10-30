---
title: Hitta celler med specifik stil med C++
linktitle: Hitta celler med specifik stil
type: docs
weight: 190
url: /sv/cpp/find-cells-with-specific-style/
description: Lär dig hur du hittar eller söker celler med en specifik stil som är tillämpad via API et Aspose.Cells for C++.
keywords: Hitta celler med en specifik stil, Sök celler med en specifik stil
---

{{% alert color="primary" %}}

Ibland behöver du hitta celler med en specifik stil. Du kan använda Aspose.Cells för att hitta alla celler med en gemensam stil. Aspose.Cells tillhandahåller egenskapen [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) som du kan använda för att ange stilen att söka celler för.

{{% /alert %}}

Koden i detta exempel hittar alla celler som har samma stil som cell A1. Efter att koden har utförts innehåller alla celler som har samma stil som A1 texten "Hittad".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
