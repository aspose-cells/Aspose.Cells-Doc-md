---
title: 列の幅をemやパーセントのような拡張可能な単位に設定する
linktitle: emやパーセントなどのスケーラブルユニットに列の幅を設定する
type: docs
weight: 130
url: /ja/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aspose.Cells for C++を使用して、emやパーセントなどの拡張可能なユニットに列幅を設定する方法を学びます。
---

スプレッドシートからHTMLファイルを生成することは非常に一般的です。列のサイズは多くの場合「pt」で定義されています。ただし、生成されたテーブルの幅が大きい場合、600pxのコンテナパネルの幅に適合させる必要がある場合があります。この場合、生成されたテーブルの幅が大きい場合に水平スクロールバーが表示される可能性があります。[**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/)を**true**に設定すると、この固定サイズをemやパーセントなどのスケーラブルな単位に変更して、より良い表示を行うことができます。

サンプルのソースファイルと出力ファイルは以下のリンクからダウンロードできます：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```c++
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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
