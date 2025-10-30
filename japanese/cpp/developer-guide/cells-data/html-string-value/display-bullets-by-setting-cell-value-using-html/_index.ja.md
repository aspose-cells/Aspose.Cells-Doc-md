---
title: C++でHTMLを使用してセル値を設定し、箇条書きを表示する方法
linktitle: HTML を使用してセルの値を設定して箇条書きを表示
type: docs
weight: 130
url: /ja/cpp/display-bullets-by-setting-cell-value-using/
description: HTMLと使いやすいAspose.Cells for C++ APIを使用してExcelセルに箇条書きを追加します。
keywords: Excelに箇条書きを追加、Excelに箇条書きを追加(C++)、Excelで箇条書きを表示、Excelで箇条書きを表示(C++)、HTMLを使ったExcelへの箇条書き追加、HTMLを使ったExcelへの箇条書き追加(C++)、HTMLでExcelの箇条書きを表示、HTMLでExcelの箇条書きを表示(C++)、HTMLを使用してExcelに箇条書きを表示、HTMLを使用してExcelに箇条書きを追加
---

{{% alert color="primary" %}}

Aspose.CellsはHTMLコードで箇条書きを表示することをサポートしています。この記事では、HTMLを使用してセルの値を設定することによって箇条書きを表示する方法を説明します。私たちは[**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)プロパティを使用してセルの値を設定します。

{{% /alert %}}

## HTMLを設定して箇条書きを表示するC++コード

次のコードは、HTML コードを使用してセルの値を設定します。このコードを実行すると、以下の画像に示すような出力が得られます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## サンプルコードによって生成された出力

上記のサンプルコードの出力を以下のスクリーンショットで示します。

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
