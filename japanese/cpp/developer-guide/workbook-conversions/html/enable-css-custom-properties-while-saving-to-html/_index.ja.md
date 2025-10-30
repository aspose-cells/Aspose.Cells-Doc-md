---
title: Ｃ++で保存時にCSSカスタムプロパティを有効にする
linktitle: HTML保存時にCSSカスタムプロパティを有効にする方法を学びます。
type: docs
weight: 320
url: /ja/cpp/enable-css-custom-properties-while-saving-to-html/
description: Aspose.Cells for C++を使用してExcelファイルをHTMLに保存する際に、CSSカスタムプロパティを有効にする方法を学びます。冗長な画像データを減らしてパフォーマンスを向上させます。
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際に、同じbase64画像が複数回出現する場合、カスタムプロパティを使用することで画像データを一度だけ保存し、生成されるHTMLのパフォーマンスを向上させることができます。[**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) プロパティを使用し、それを **true** に設定してください。

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。**

以下のサンプルコードは [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) プロパティの使用例を示しています。スクリーンショットはこのプロパティが true に設定されていない場合の効果を示しています。このコードで使用されたサンプルExcelファイル（50528260.xlsx）と、生成された出力HTML（50528261.zip）をダウンロードしてください。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample workbook
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
