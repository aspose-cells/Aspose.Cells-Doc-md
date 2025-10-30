---
title: Hitta om arbetsbladet är en Dialogblad med C++
linktitle: Ta reda på om kalkylbladet är Dialog sheet
type: docs
weight: 90
url: /sv/cpp/find-if-the-worksheet-is-dialog-sheet/
description: Dialogblad är ett gammalt format av blad. Denna artikel ger instruktioner och exempel på kod för att avgöra programmässigt om ett Excel arbetsblad är ett Dialogblad med C++ API.
keywords: Hitta Excel arbetsblad som dialogtyp C++, arbetsblad dialog C++
---

## **Möjliga användningsscenario**

Dialog Sheet är ett gammalt format av ark som innehåller en dialogruta. Ett sådant ark kunde sättas in av en äldre version av Microsoft Excel t.ex. 2003 som visas på denna skärmbild. Det kan också sättas in med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan hitta om bladet är ett dialogblad eller någon annan typ av blad med egenskapen [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) som tillhandahålls av Aspose.Cells. Om det returnerar värdet [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) betyder det att du hanterar ett dialogblad.

## **Ta reda på om kalkylbladet är Dialog sheet**

Följande exempel laddar [provfiler](64716820.xlsx) som innehåller ett dialogblad. Den kontrollerar egenskapen [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/), jämför den med [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) och skriver ut meddelandet. Se gärna konsolutmatningen av kodexemplet nedan för mer hjälp.

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Konsoloutput**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
