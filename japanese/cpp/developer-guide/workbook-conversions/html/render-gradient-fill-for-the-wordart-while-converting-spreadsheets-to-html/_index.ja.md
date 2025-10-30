---
title: ExcelからHTMLに変換する際にWordArtのグラデーション塗りつぶしをレンダリングする（C++）
linktitle: スプレッドシートをHTMLに変換する際のWordArtのグラデーションフィルをレンダリング
type: docs
weight: 90
url: /ja/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: C++でスプレッドシートをHTMLに変換する際にWordArtのグラデーション塗りつぶしをレンダリングする方法を学びます。
---

## **可能な使用シナリオ**
Aspose.Cells 17.1以前のバージョンでは、ExcelファイルをHTML形式に変換するとき、ワードアートのグラデーション塗りつぶしがレンダリングされませんでした。Aspose.Cells 17.1のリリース以降、ワードアートのグラデーション塗りつぶしがサポートされています。次のスクリーンショットは、Aspose.Cells 17.1を使用してExcelファイルを変換した場合と古いバージョンを使用した場合のグラデーション塗りつぶしの効果を比較しています。

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **スプレッドシートをHTMLに変換する際のWordArtのグラデーションフィルをレンダリング**
次のサンプルコードは、[元のExcelファイル](22774111.xlsx)を[出力HTML形式](22774109.zip)に変換します。元のExcelファイルにはスクリーンショットに示すようなグラデーション塗りつぶしを持つワードアートオブジェクトが含まれています。
## **サンプルコード**
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
