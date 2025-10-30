---
title: Render Office tillägg när du konverterar Excel till PDF med C++
linktitle: Rendera Office tillägg vid konvertering av Excel till PDF
type: docs
weight: 100
url: /sv/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Lär dig hur du renderar Office tillägg när du konverterar Excel filer till PDF med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Tidigare kunde inte Aspose.Cells rendera Office-tillägg när en Excel-fil sparades till PDF-format. Nu renderar Aspose.Cells det korrekt. Du behöver inte använda någon speciell metod eller egenskap för att rendera Office-tillägg i den utgående PDF-filen. Spara helt enkelt din Excel-fil till PDF-format, och den kommer att rendera Office-tilläggen.

## **Rendera Office-tillägg vid konvertering av Excel till PDF**

Följande exempel kod sparar [exempel Excel-fil](60489769.xlsx) som innehåller Office-tillägg. Se [utdata PDF genererad med den tidigare versionen, dvs. 17.11](60489770.pdf) och den [nyare versionen, dvs. 17.12 och senare](60489771.pdf). Den föregående versionens utdata PDF är tom, men den nyare versionen visar Office-tillägget.

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
