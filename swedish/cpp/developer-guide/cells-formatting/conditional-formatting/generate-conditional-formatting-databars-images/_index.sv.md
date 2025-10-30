---
title: Generera villkorsformateringsdatabarbildningar med C++
linktitle: Generera bilder för betingad formatering DataBars
description: Aspose.Cells är ett C++ bibliotek för hantering av kalkylbladsfiler. Det stöder generation av villkorsformaterade datastavar och bilder, vilket gör att användare kan anpassa visningen av kalkylbladet baserat på cellvärden. Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att generera villkorsformat datastavar och bilder.
keywords: Aspose.Cells, Betingad formatering, Databalkar, Bilder, Kalkylblad
type: docs
weight: 40
url: /sv/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilder på DataBars för betingad formatering. Du kan använda Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/)-metod för att generera dessa bilder. Denna artikel visar hur man genererar en DataBar-bild med hjälp av Aspose.Cells.

{{% /alert %}}

Följande exempel genererar Datastapeln för cell C1. Först accessar den formateringsvillkoret för cellen, och därefter från detta objekt accessar den [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/)-objektet och använder dess [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/)-metod för att generera bilden av cellen. Slutligen sparas bilden på disken.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
