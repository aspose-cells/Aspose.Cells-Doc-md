---
title: Ｃ++で保存時にCSSを無効にする
linktitle: HTMLに保存する際にCSSを無効にする
type: docs
weight: 320
url: /ja/cpp/disable-css-while-saving-to-html/
description: Aspose.Cells for C++を使用してExcelファイルをHTMLに保存する際にCSSを無効にする方法を学びます。
---

## **可能な使用シナリオ**

Excelファイルを単一ページのHTMLとして保存すると、通常、CSS要素はHTMLファイル内に埋め込まれ、HEADセクションに配置されます。このファイルをメールのコンテンツまたは本文として添付すると、ほとんどのメールクライアントはCSS要素を除去し、正しく表示されなくなることがあります。Aspose.Cellsのバージョン24.12では、CSSをオプションで無効にし、スタイルを直接HTML要素内に適用できるオプションを導入しています。メールのコンテンツまたは本文にHTMLを設定したい場合は、[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) プロパティを使用し、それを **true** に設定してください。

## **HTML保存時にCSSを無効にする**

以下のサンプルコードは、[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) プロパティの使用方法を示しています。

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
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
