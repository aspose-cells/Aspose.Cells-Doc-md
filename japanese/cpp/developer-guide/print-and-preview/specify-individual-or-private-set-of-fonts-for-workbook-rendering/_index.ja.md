---
title: ワークブックのレンダリングに対して個別またはプライベートのフォントセットを指定（C++）
linktitle: ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する
type: docs
weight: 40
url: /ja/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Aspose.Cells for C++を使用して、ワークブックのレンダリングのために個別またはプライベートフォントセットを指定する方法を学びます。
---

## **可能な使用シナリオ**

通常、すべてのワークブックに対してフォントのディレクトリまたはリストを指定しますが、時には個別またはプライベートのフォントセットを指定する必要があります。Aspose.Cellsは[**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/)クラスを提供し、これを使って個別またはプライベートのフォントをワークブックに指定できます。

## **ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する**

以下のサンプルコードは、[サンプルのExcelファイル（67338268.xlsx）]を読み込み、そのフォントセットを[**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/)クラスを使って指定します。コード内で使用されるフォントの[サンプルフォント（67338271.zip）]や、その結果生成される[出力されたPDF（67338269.pdf）]も確認してください。スクリーンショットは、フォントが正常に認識された場合の出力PDFの様子です。

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
