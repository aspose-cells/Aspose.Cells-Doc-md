---
title: C++を使用したカスタム日付書式パターンgとgeのレンダリング
description: Aspose.Cellsは、 g と ge のカスタム日付書式パターンをサポートするC++のスプレッドシート処理ライブラリです。この記事では、Aspose.Cellsライブラリを使ってこれらのパターンをレンダリングし、日付の表示をコントロールする方法について説明します。
keywords: Aspose.Cells, C++ライブラリ, 電子スプレッドシート, カスタム日付書式, レンダリング, パターン g , パターン ge , 表示制御
type: docs
weight: 160
url: /ja/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Aspose.Cellsは、今やgやge.mm.ddなどのカスタム日付形式パターンをレンダリングすることができます。参考のために、添付の[source excel file](5112361.xlsx)とAspose.Cellsによる変換された[PDF](5112360.pdf)をご確認ください。

{{% /alert %}}

以下のサンプルコードは、gやge.mm.ddなどのカスタム形式パターンを含む[source excel file](5112361.xlsx)を変換し、[output PDF](5112360.pdf)に変換します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
