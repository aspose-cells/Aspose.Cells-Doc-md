---
title: Lägg till 2 färgskala och 3 färgskala villkorsformatering med C++
linktitle: Lägga till 2 färgade skala och 3 färgade skala villkorlig formatering
description: Hur man använder Aspose.Cells biblioteket i C++ för att lägga till villkorsformatering för två färgförhållanden och tre färgförhållanden. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och visas.
keywords: Aspose.Cells, Villkorsformatering, C++, Färgskala, Två Färgskala, Tre Färgskala
type: docs
weight: 20
url: /sv/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

**2-färgad skala** och **3-färgad skala** Villkorlig formatering läggs till på samma sätt förutom att de skiljer sig åt genom [**FormatCondition.GetIs3ColorScale()**](https://reference.aspose.com/cells/cpp/aspose.cells/colorscale/getis3colorscale/)-egenskapen. Denna egenskap är 'false' för 2-färgad skala och 'true' för 3-färgad skala villkorlig formatering.

{{% /alert %}}

Den följande exempelkoden lägger till 2-färgad skala och 3-färgad skala villkorlig formatering. Den genererar [utdata Excel-filen](5115058.xlsx).

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some data in cells
    worksheet.GetCells().Get(u"A1").PutValue(u"2-Color Scale");
    worksheet.GetCells().Get(u"D1").PutValue(u"3-Color Scale");

    for (int i = 2; i <= 15; i++)
    {
        int row = i - 1;
        worksheet.GetCells().Get(row, 0).PutValue(i); // Column A (0)
        worksheet.GetCells().Get(row, 3).PutValue(i); // Column D (3)
    }

    // Adding 2-Color Scale Conditional Formatting
    CellArea ca = CellArea::CreateCellArea(u"A2", u"A15");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    FormatCondition fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(false);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Adding 3-Color Scale Conditional Formatting
    ca = CellArea::CreateCellArea(u"D2", u"D15");

    idx = worksheet.GetConditionalFormattings().Add();
    fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(true);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMidColor(Color::Yellow());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
