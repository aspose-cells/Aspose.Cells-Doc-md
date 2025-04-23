---
title: Konvertera datum till japanska datum med C++
linktitle: Konvertera datum till japanska datum
type: docs
weight: 350
url: /sv/cpp/convert-dates-to-japanese-dates/
description: Lär dig hur man konverterar gregorianska datum till japanska datum med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

I det japanska kalendern börjar en ny era med en ny kejsares regeringstid. Den 1 maj 2019 trädde en ny kejsare till makten, vilket avslutade Heisei-eran och började Reiwa-eran.

{{% /alert %}}

Aspose.Cells ger en metod för att konvertera gregorianska datum till japanska datum. Under denna konvertering beaktas även eraändringarna. Följande kodstycke konverterar en [källa Excel](90112015.xlsx) fil med gregorianska datum till en [utdata PDF](90112016.pdf) med japanska datum enligt bilden nedan.

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
