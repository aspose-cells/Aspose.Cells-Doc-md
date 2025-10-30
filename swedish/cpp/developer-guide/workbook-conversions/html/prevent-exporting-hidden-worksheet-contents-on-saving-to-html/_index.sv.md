---
title: Förhindra export av dold arbetsbladinnehåll vid sparande till HTML med C++
linktitle: Förhindra export av dolt arbetsbladinnehåll
type: docs
weight: 210
url: /sv/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Lär dig hur du förhindrar export av dolt arbetsbladinnehåll när du sparar Excel arbetsböcker till HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Om arbetsboken dock innehåller dolda kalkylblad exporterar Aspose.Cells som standard innehållet på de dolda kalkylbladen till HTML-utdata (_files)-mappen som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, osv. Ibland är det inte lämpligt att exportera innehållet på de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte ska exporteras till _files-mappen.

{{% /alert %}}

Aspose.Cells tillhandahåller [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/)-egenskapen. Som standard är den inställd på **true** och dolda arbetsblad exporteras till HTML. Om du anger den till **false**, kommer inte Aspose.Cells att exportera innehållet på dolda arbetsblad.

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
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
