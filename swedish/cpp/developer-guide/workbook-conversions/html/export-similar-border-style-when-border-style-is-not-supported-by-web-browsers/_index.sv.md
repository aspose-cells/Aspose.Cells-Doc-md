---
title: Exportera liknande kantstilar när kantstilen inte stöds av webbläsare med C++
linktitle: Exportera liknande kantsytel när kantsytele inte stöds av webbläsare
type: docs
weight: 70
url: /sv/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Lär dig hur du exporterar liknande kantstilar när de inte stöds av webbläsare med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Microsoft Excel stöder vissa typer av streckade kanter som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells tas dessa kanter bort. Men Aspose.Cells kan även visa sådana kanter med [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)-egenskapen. Sätt dess värde till **true** så exporteras även de stödda kanterna till HTML-filen.

## **Exportera liknande kantstilmall när kantstil inte stöds av webbläsare**

Följande exempel kod laddar [exempel-Excel-filen](64716806.xlsx) som innehåller vissa stödfria kanter, som visas i följande skärmbild. Skärmbilden visar ytterligare effekten av [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)-egenskapen i [utdata-HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
