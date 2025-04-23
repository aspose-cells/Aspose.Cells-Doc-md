---
title: CrossHideRightを使用して重ね合わせコンテンツを非表示にし、HTML保存時に隠す（C++）
linktitle: HTMLで保存する際のCrossHideRightでオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Aspose.CellsをC++で使用して、HTML保存時に重なったコンテンツを非表示にするためにCrossHideRightを使用します。
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際に、セル文字列のクロスタイプを指定できます。デフォルトでは、Aspose.CellsはMicrosoft Excelに準拠したHTMLを生成しますが、クロスタイプを[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)に変更すると、セル文字列の右側に重なったり重なり合ったりしているすべての文字列が非表示となります。

## **CrossHideRightを使用してオーバーレイコンテンツを非表示にする**

以下のサンプルコードは、[サンプルExcelファイル](64716894.xlsx)を読み込み、[**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/)を[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)に設定し、[出力HTML](64716893.zip)に保存します。スクリーンショットは、[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)がデフォルトの出力にどのように影響を与えるかを示しています。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
