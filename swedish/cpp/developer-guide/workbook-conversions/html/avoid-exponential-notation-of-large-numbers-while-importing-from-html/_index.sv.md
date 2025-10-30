---
title: Undvik exponentiell notation av stora nummer vid import från HTML med C++
linktitle: Undvik exponentiell notation för stora tal vid import från HTML
type: docs
weight: 10
url: /sv/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Lär dig hur man undviker exponentiell notation av stora nummer vid import från HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland innehåller din HTML nummer som 1234567890123456 som är längre än 15 siffror, och när du importerar din HTML till en Excel-fil konverteras dessa nummer till exponentiell notation som 1.23457E+15. Om du vill att ditt nummer ska importeras som det är och inte omvandlas till exponentiell notation, använd då [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)-egenskapen och ställ in den till **true** när du laddar din HTML.

{{% /alert %}}

Följande kodexempel förklarar användningen av [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)-egenskapen. API:et kommer att importera numret som det är utan att omvandla det till exponentiell notation.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String html = u"<html><body><p>1234567890123456</p></body></html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions = HtmlLoadOptions(LoadFormat::Html);
    loadOptions.SetKeepPrecision(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    Worksheet sheet = workbook.GetWorksheets().Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputAvoidExponentialNotationWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
