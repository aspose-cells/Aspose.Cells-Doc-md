---
title: Ｃ++でHTMLをインポートする際に行間の余分なスペースを削除する
linktitle: HTMLのインポート時に改行後の余分なスペースを削除する
type: docs
weight: 20
url: /ja/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for C++を使用してHTMLをインポートする際に行間の余分なスペースを削除する方法を学びます。
---

{{% alert color="primary" %}}

[**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) プロパティを使用し、それを **true** に設定して、改行タグの後に来るすべての余分なスペースを削除してください。デフォルトではこのプロパティは **false** であり、余分なスペースは出力されるExcelファイルに保持されます。

{{% /alert %}}

HTMLLoadOptions.DeleteRedundantSpaces プロパティをfalse や trueに設定した場合の効果

このプロパティを**false**と**true**に設定した効果を以下のスクリーンショットで示します。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTMLをインポートする際に改行後の余分なスペースを削除する効果

### プログラミングサンプル

次のサンプルコードは [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) プロパティの使用例を示しています。上記のスクリーンショットに示されているように、true または false に設定してください。

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String html = u8"<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions(LoadFormat::Html);
    loadOptions.SetDeleteRedundantSpaces(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();

    Aspose::Cells::Cleanup();
    return 0;
}
```
