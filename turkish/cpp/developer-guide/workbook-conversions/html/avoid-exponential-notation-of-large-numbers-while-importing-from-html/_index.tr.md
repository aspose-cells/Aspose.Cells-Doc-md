---
title: HTML den büyük sayıları alırken üssel gösterimi önleyin
linktitle: Html den içe aktarırken büyük sayıların üstel gösterimini önleme
type: docs
weight: 10
url: /tr/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Aspose.Cells for C++ kullanarak, HTML ye aktarırken büyük sayıların üssel gösterimini önlemeyi öğrenin.
---

{{% alert color="primary" %}}

Bazen HTML'nizde 1234567890123456 gibi 15'ten uzun sayılar bulunur ve bu sayılar Excel'e ithal edildiğinde 1.23457E+15 gibi üssel gösterime dönüşür. Sayınızın olduğu gibi kalmasını ve üssel gösterimle dönüştürülmemesini istiyorsanız, lütfen [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) özelliğini kullanın ve HTML yüklerken **true** olarak ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) özelliğinin kullanımını anlatır. API, sayıyı olduğu gibi ithal eder ve üssel gösterime dönüştürmez.

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
