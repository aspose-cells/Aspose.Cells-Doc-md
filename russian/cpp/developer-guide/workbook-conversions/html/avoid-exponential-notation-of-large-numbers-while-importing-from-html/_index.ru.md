---
title: Избегайте экспоненциального отображения больших чисел при импорте из HTML с помощью C++
linktitle: Избегайте экспоненциальной нотации больших чисел при импорте из HTML
type: docs
weight: 10
url: /ru/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Узнайте, как избежать экспоненциального отображения больших чисел при импорте из HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда ваши HTML содержит числа вроде 1234567890123456, длиной более 15 цифр, и при импорте в файл Excel эти числа преобразуются в экспоненциальное отображение, например 1.23457E+15. Чтобы импортировать число как есть и не преобразовывать его в экспоненциальное отображение, используйте свойство [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) и установите его в **true** при загрузке HTML.

{{% /alert %}}

Следующий пример кода объясняет использование свойства [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/). API импортирует число как есть без преобразования в экспоненциальное отображение.

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
