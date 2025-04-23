---
title: Vermeiden Sie die exponentielle Notation großer Zahlen beim Import aus HTML mit C++
linktitle: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML
type: docs
weight: 10
url: /de/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Lernen Sie, wie man die exponentielle Notation großer Zahlen beim Import aus HTML mit Aspose.Cells for C++ vermeidet.
---

{{% alert color="primary" %}}

Manchmal enthält Ihr HTML Zahlen wie 1234567890123456, die länger als 15 Ziffern sind, und wenn Sie Ihr HTML in eine Excel-Datei importieren, werden diese Zahlen in die exponentielle Notation umgewandelt, z.B. 1.23457E+15. Wenn Sie möchten, dass Ihre Nummer so importiert wird, wie sie ist, ohne in die exponentielle Notation umgewandelt zu werden, verwenden Sie bitte die [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)-Eigenschaft und setzen sie auf **true**, während Sie Ihr HTML laden.

{{% /alert %}}

Der folgende Beispielcode erklärt die Verwendung der [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)-Eigenschaft. Die API importiert die Nummer so, wie sie ist, ohne sie in die exponentielle Notation umzuwandeln.

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
