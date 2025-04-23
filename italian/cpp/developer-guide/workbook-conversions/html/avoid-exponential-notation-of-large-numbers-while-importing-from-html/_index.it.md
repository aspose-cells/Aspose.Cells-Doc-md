---
title: Evita la notazione esponenziale di numeri grandi durante l’importazione da HTML con C++
linktitle: Evita la notazione esponenziale dei grandi numeri durante l importazione da HTML
type: docs
weight: 10
url: /it/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Impara come evitare la notazione esponenziale di numeri grandi durante l’importazione da HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte il tuo HTML contiene numeri come 1234567890123456 che sono più lunghi di 15 cifre, e quando importi il tuo HTML in un file Excel, questi numeri vengono convertiti in notazione esponenziale come 1.23457E+15. Se desideri che il numero venga importato così com’è e non convertito in notazione esponenziale, utilizza la proprietà [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) e impostala su **true** durante il caricamento del tuo HTML.

{{% /alert %}}

Il seguente esempio di codice spiega l’uso della proprietà [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/). L’API importerà il numero così com’è senza convertirlo in notazione esponenziale.

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
