---
title: Evitar notación exponencial para números grandes al importar desde HTML con C++
linktitle: Evitar la notación exponencial de números grandes al importar desde HTML
type: docs
weight: 10
url: /es/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Aprenda cómo evitar la notación exponencial para números grandes al importar desde HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, su HTML contiene números como 1234567890123456 que son más largos que 15 dígitos, y cuando importa su HTML a un archivo de Excel, estos números se convierten en notación exponencial como 1.23457E+15. Si desea que su número se importe tal cual y no se convierta en notación exponencial, utilice la propiedad [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) y configúrela en **true** al cargar su HTML.

{{% /alert %}}

El siguiente código de ejemplo explica el uso de la propiedad [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/). La API importará el número tal cual sin convertirlo en notación exponencial.

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
