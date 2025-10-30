---
title: Excel till HTML  Använd PresentationPreference alternativ för bättre layout med C++.
linktitle: Excel till HTML  Använd PresentationPreference alternativet för bättre layout
type: docs
weight: 220
url: /sv/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: Lär dig att rendera bättre layout när du sparar Excel filer till HTML med C++.
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller en användbar HtmlSaveOptions.PresentationPreference egenskap för utvecklare som behöver rendera bättre layout vid sparande av en Microsoft Excel-fil till HTML- eller MHT-formatet. Standardvärdet för egenskapen är false. Vi rekommenderar att du ställer in denna egenskap till true för att få en mer attraktiv presentation av Excel-rapporter.

{{% /alert %}} 

Se det följande kodexemplet nedan som visar hur man renderar en HTML-fil från Excel-rapport med presentationspreferens på.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
