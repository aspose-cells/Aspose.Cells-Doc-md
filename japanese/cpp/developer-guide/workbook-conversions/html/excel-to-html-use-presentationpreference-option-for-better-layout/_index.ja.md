---
title: ExcelからHTMLへ  より良いレイアウトのためのPresentationPreferenceオプションの使用法（Ｃ++）
linktitle: ExcelをHTMLに変換する際、PresentationPreferenceオプションを使用してレイアウトを向上させる
type: docs
weight: 220
url: /ja/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: ExcelファイルをHTMLに保存する際により良いレイアウトでレンダリングする方法を学びます。
---

{{% alert color="primary" %}} 

Aspose.Cellsは、Microsoft ExcelファイルをHTMLやMHT形式に保存する際にレイアウトを向上させたい開発者のために、HtmlSaveOptions.PresentationPreference プロパティを提供しています。このプロパティのデフォルト値は false です。Excelレポートをより魅力的に表示するためには、このプロパティを true に設定することをお勧めします。

{{% /alert %}} 

以下に、Excelレポートからレイアウト向上設定を使用してHTMLファイルをレンダリングする方法を示すサンプルコードをご覧ください。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
