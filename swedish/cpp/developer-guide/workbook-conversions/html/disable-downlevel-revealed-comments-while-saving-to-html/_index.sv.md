---
title: Inaktivera Downlevel Revealed Comments vid sparning till HTML med C++
linktitle: Inaktivera Downlevel Revealed Comments
type: docs
weight: 20
url: /sv/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Eliminera Downlevel Revealed Comments vid sparande av Excel filer till HTML med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, visar Aspose.Cells Downlevel Conditional Comments. Dessa villkorskommentarer är mest relevanta för äldre versioner av Internet Explorer och är OKÄNDA för moderna webbläsare. Läs mer i detalj på följande länk.

- [Villkorlig kommentar - Låg nivå - avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells tillåter dig att eliminera dessa Downlevel Revealed Comments genom att ställa in [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-egenskapen till **true**.

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**

Följande exempel visar användningen av [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på true. Ladda ner [dokumentnamnet Excel-fil](50528257.xlsx) som används i detta exempel och den [genererade HTML-filen](50528258.zip) för referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
