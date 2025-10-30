---
title: Inställning av delad formel med C++
linktitle: Ange Delad Formel
type: docs
weight: 10
url: /sv/cpp/setting-shared-formula/
description: Lär dig hur du ställer in delade formler i Excel ark med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Om du vill lägga till en funktion i ett kalkylblad som ska utföra beräkningar förklarar denna artikel hur du gör detta med Aspose.Cells.

{{% /alert %}}

## Ange delad formel med Aspose.Cells

Anta att du har ett kalkylblad fyllt med data i det format som liknar det följande exempelkalkylbladet.

|**Inmatningsfil med en kolumn data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första dataraden. Skatten är **9%**. Formeln som beräknar momsen är: **"=A2*0.09"**. Den här artikeln förklarar hur man tillämpar denna formel med Aspose.Cells.

Aspose.Cells låter dig ange en formel med hjälp av [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) egenskap. Det finns två alternativ för att lägga till formler till de andra cellerna (B3, B4, B5, etc.) i kolumnen.

 Antingen gör du vad du gjorde för den första cellen, effektivt ställer in formeln för varje cell, och uppdaterar cellreferensen därefter (A3*0,09, A4*0,09, A5*0,09 och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också att Aspose.Cells analyserar varje formel individuellt, vilket kan ta tid för stora kalkylblad och komplexa formler. Det lägger också till extra kodrader även om loopar kan minska detta något.

Ett annat tillvägagångssätt är att använda en **delad formel**. Med en delad formel uppdateras formlerna automatiskt för cellreferenser i varje rad så att momsen beräknas korrekt. [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) metoden är mer effektiv än det första tillvägagångssättet.

Följande exempel visar hur du använder den.

```c++
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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
