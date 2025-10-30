---
title: ツールチップ付きでExcelをHTMLに変換（C++使用）
linktitle: ツールチップ付きでExcelをHTMLに変換する
type: docs
weight: 200
url: /ja/cpp/convert-excel-to-html-with-tooltip/
description: Aspose.Cellsを用いて、ツールチップを追加しながらExcelをHTMLに変換します。
---

## **ツールチップ付きでExcelをHTMLに変換する**

生成されたHTMLでテキストが切り取られる場合に、ホバー時に完全なテキストをツールチップとして表示したいことがあります。Aspose.Cellsはこれをサポートしており、[**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/)プロパティを設定します。[**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/)プロパティを**true**に設定すると、完全なテキストをツールチップとして追加します。

次の画像は、生成されたHTMLファイル内のツールチップを示しています。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

次のコードサンプルは、[源となるExcelファイル](98107416.xlsx)を読み込み、ツールチップ付きの[出力HTMLファイル](98107417.zip)を生成します。

サンプルコード

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
