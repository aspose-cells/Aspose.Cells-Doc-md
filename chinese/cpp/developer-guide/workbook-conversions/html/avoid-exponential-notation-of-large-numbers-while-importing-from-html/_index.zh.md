---
title: 导入HTML时避免大数字的指数表示法
linktitle: 在从HTML导入时避免大数字的指数表示
type: docs
weight: 10
url: /zh/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: 学习如何在用编号Aspose.Cells for C++导入HTML时避免大数字的指数表示法。
---

{{% alert color="primary" %}}

有时候你的HTML包含像1234567890123456这样长于15位的数字，当你将HTML导入Excel时，这些数字会变成指数表示法如1.23457E+15。如果你希望数字按原样导入而不转换为指数形式，请在加载HTML时使用[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)属性并将其设置为**true**。

{{% /alert %}}

以下示例代码说明了[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)属性的用法。API将按原样导入数字，而不将其转换为指数表示法。

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
