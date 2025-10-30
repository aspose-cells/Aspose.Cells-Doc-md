---
title: Webブラウザがサポートしていない境界スタイルと類似した境界スタイルをC++でエクスポートする
linktitle: Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする
type: docs
weight: 70
url: /ja/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Aspose.Cellsを使用して、Webブラウザが対応していない場合の類似境界スタイルのエクスポート方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelは、Webブラウザがサポートしない点線の境界線タイプをいくつかサポートしています。Aspose.Cellsを使用してこのようなExcelファイルをHTMLに変換すると、そのような境界線は削除されます。ただし、Aspose.Cellsは[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)プロパティを使用してその境界線を表示させることも可能です。その値を**true**に設定すると、サポートされていない境界線もHTMLファイルにエクスポートされます。

## **Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする**

以下のサンプルコードは、サポートされていない境界線を含む[sample Excelファイル](64716806.xlsx)を読み込み、次のスクリーンショットに示すようにエクスポートします。スクリーンショットはまた、[出力HTML](64716804.zip)内の[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)プロパティの効果を示しています。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
