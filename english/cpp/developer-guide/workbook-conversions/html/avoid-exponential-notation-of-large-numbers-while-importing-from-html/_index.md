---
title: Avoid exponential notation of large numbers while importing from HTML with C++
linktitle: Avoid exponential notation of large numbers while importing from HTML
type: docs
weight: 10
url: /cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Learn how to avoid exponential notation of large numbers while importing from HTML using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes your HTML contains numbers like 1234567890123456 which are longer than 15 digits, and when you import your HTML to an Excel file, these numbers convert to exponential notation like 1.23457E+15. If you want your number to be imported as it is and not converted to exponential notation, then please use the [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) property and set it to **true** while loading your HTML.

{{% /alert %}}

The following sample code explains the usage of the [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) property. The API will import the number as it is without converting it to exponential notation.

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