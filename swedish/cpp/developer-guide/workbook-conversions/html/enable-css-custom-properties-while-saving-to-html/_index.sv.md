---
title: Aktivera CSS Användarspecifika Egenskaper vid sparande till HTML med C++
linktitle: Aktivera CSS Anpassade Egenskaper under sparande till HTML
type: docs
weight: 320
url: /sv/cpp/enable-css-custom-properties-while-saving-to-html/
description: Lär dig hur du aktiverar CSS anpassade egenskaper när du sparar Excel filer till HTML med Aspose.Cells for C++. Förbättra prestanda genom att minska redundanta bilddata.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, i scenariot att det finns flera förekomster av en base64-bild, behöver bilddata endast sparas en gång tack vare en anpassad egenskap, vilket kan förbättra prestandan hos den genererade HTML-filen. Använd [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/)-egenskapen och ställ in den till **true** när du sparar till HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Aktivera CSS Anpassade Egenskaper under sparande till HTML**

Följande exempel visar användningen av [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/)-egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på **true**. Ladda ner [dokumentnamnet Excel-fil](50528260.xlsx) som används i detta exempel och den [genererade HTML-filen](50528261.zip) för referens.

## **Exempelkod**

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
