---
title: Spara arbetsboken i Strict Open XML Spreadsheet Format med C++
linktitle: Spara arbetsbok till strikt öppet XML kalkylbladsformat
type: docs
weight: 150
url: /sv/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Lär dig hur du sparar en arbetsbok i Strict Open XML Spreadsheet format med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter att du sparar arbetsboken i *Strict Open XML Spreadsheet* format. För detta ändamål tillhandahåller det egenskapen [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/). Om du ställer in dess värde till [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), kommer den ifrågavarande Excel-filen att sparas i Strict Open XML Spreadsheet-format.

## **Spara arbetsbok i strikt öppet XML-kalkylbladsformat**

Följande exempel skapar en arbetsbok och ställer in värdet av egenskapen [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/) till [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) och sparar den som [utdata Excel-fil](67338272.xlsx). Om du öppnar den genererade Excel-filen i Microsoft Excel och öppnar Spara Som... dialogrutan, kommer du att se dess format som *Strict Open XML Kalkylblad* som visas i denna skärmbild.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
