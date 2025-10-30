---
title: Ange individuella eller privata teckensnittssamlingar för arbetsboksrendering med C++
linktitle: Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation
type: docs
weight: 40
url: /sv/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Lär dig hur du specificerar individuella eller privata teckensnittssamlingar för arbetsboksrendering med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Generellt sett anger du teckensnittsdirektivet eller en lista av teckensnitt för alla arbetsböcker, men ibland måste du specificera enskilda eller privata teckensnittssamlingar för dina arbetsböcker. Aspose.Cells erbjuder klassen [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) som kan användas för att specificera enskilda eller privata teckensnitt för din arbetsbok.

## **Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation**

Följande exempel laddar [exempel-Excel-filen](67338268.xlsx) med dess enskilda eller privata teckensnitt, som anges med klassen [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/). Titta på det [exempel-typsnitt](67338271.zip) som används i koden samt den [genererade PDF-filen](67338269.pdf). Nedan visas hur PDF-filen ser ut om typsnittet hittas framgångsrikt.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
