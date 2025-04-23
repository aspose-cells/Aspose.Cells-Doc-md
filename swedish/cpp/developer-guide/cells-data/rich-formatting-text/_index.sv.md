---
title: Åtkomst och uppdatering av delar av rik text i cell med C++
linktitle: Riktad formateringstext
type: docs
weight: 40
url: /sv/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lär dig hur du får åtkomst till och uppdaterar delar av rik text i cell via API et Aspose.Cells for C++.
keywords: Kom åt och uppdatera rik text i cell, Få rik text i cell, Redigera rik text i cell, Kom åt rik text i cell, Uppdatera rik text i cell, Ändra rik text i cell
---

{{% alert color="primary" %}}

Aspose.Cells låter dig komma åt och uppdatera delar av rik text i cellen. För detta ändamål kan du använda [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) och [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) metoder. Dessa metoder returnerar och accepterar en matris av [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) objekt som du kan använda för att komma åt och uppdatera olika egenskaper hos teckensnittet, som teckensnittsnamn, teckensnittsfärg, fetstil, osv.

{{% /alert %}}

## **Åtkomst och uppdatering av delar av riktad text från cellen**

Följande kod demonstrerar användningen av [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) och [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) metoden med hjälp av [källexcelfilen](5112369.xlsx). Källexcelfilen har rik text i cell A1 med 3 delar, var och en med ett annat typsnitt. Koden hämtar dessa delar och uppdaterar det första delens typsnitt till **"Arial"**. Den modifierade arbetsboken sparas som [utgångs excel fil](5112366.xlsx).

### C++-kod för att komma åt och uppdatera rik textdelar

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Konsoloutput som genereras av provkoden

Här är utskriften i konsolen när du använder [källexcelfilen](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
