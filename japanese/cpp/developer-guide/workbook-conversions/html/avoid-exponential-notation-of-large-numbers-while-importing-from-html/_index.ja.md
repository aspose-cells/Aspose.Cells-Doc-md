---
title: C++でHTMLからインポートする際に大きな数字の指数表記を避ける
linktitle: HTMLからの大きな数値の指数表記を避ける
type: docs
weight: 10
url: /ja/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: HTMLのインポート時に大きな数字の指数表記を避ける方法を、Aspose.Cells for C++を使用して学びます。
---

{{% alert color="primary" %}}

時折、HTMLに1234567890123456のような15桁以上の数字が含まれている場合、Excelにインポートするとこれらの数字は1.23457E+15のような指数表記に変換されます。数字をそのままインポートし、指数表記に変換したくない場合は、[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)プロパティを使用し、読み込み時に**true**に設定してください。

{{% /alert %}}

次のサンプルコードは、[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/)プロパティの使い方を説明します。APIは数字を指数表記に変換せず、そのままインポートします。

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
