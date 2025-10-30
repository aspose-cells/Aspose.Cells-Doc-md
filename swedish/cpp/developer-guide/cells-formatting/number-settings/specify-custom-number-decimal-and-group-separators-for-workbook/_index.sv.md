---
title: Specificera anpassade decimala och grupperingsseparatorer för arbetsboken med C++
linktitle: Specificera anpassade decimala och grupperingsseparatorer
type: docs
weight: 110
url: /sv/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändra nummerdecimala och grupperingsseparatorer i MS Excel och med C++ kod med hjälp av API Aspose.Cells for C++.
keywords: specificera anpassad decimalseparator i excel, specificera anpassad decimalseparator i excel c++, specificera anpassad gruppseparator i excel, specificera anpassad gruppseparator i excel c++, specificera anpassad decimal och gruppseparator i excel, specificera anpassad decimal och gruppseparator i excel c++, ändra decimal och gruppseparator i excel, ändra decimal och gruppseparator, ändra decimalseparator i excel, ändra decimalseparator i excel c++, ändra gruppseparator i excel, ändra gruppseparator i excel c++
---

{{% alert color="primary" %}}

I Microsoft Excel kan du ange anpassade decimal- och tusentalsavskiljare istället för att använda systemavskiljare från **Avancerade Excel-alternativ** enligt skärmbilden nedan.

Aspose.Cells tillhandahåller [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) och [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) egenskaper för att ange anpassade avskiljare för formatering/parsning av nummer.

{{% /alert %}}

## **Ange anpassade avskiljare i Microsoft Excel**

Följande skärmbild visar **Avancerade Excel-alternativ** och markerar avsnittet för att ange **Anpassade avskiljare**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Ange anpassade avskiljare med Aspose.Cells**

Följande exempelkod illustrerar hur man anger anpassade avskiljare med Aspose.Cells API. Det specificerar anpassade decimal- och grupptalsavskiljare som punkt och mellanslag respektive.

### C++ kod för att specificera anpassade nummerdecimala och grupperingsseparatorer

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

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
