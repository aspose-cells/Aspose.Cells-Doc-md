---
title: C++でワークシートにWordArtウォーターマークを追加
linktitle: ワードアートの管理
type: docs
weight: 180
url: /ja/cpp/add-wordart-watermark-to-worksheet/
description: Aspose.Cells for C++を使用してExcelワークシートにWordArtウォーターマークを追加する方法を学習します。
---

{{% alert color="primary" %}} 

WordArtを使用してスプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルをファイルの上に広げたり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、Excelシートにテキストを背景ウォーターマークとして適用したりできます。WordArtは、スプレッドシートに追加するための移動や配置が可能なオブジェクトになります。

{{% /alert %}} 

次の例では、ワークシートの背景ウォーターマークとしてワードアート形状を追加する方法を示します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [組み込みスタイルを持つ WordArt テキストを追加する](/cells/ja/cpp/add-word-art-text-with-built-in-styles/)
- [WordArtウォーターマークをロックする](/cells/ja/cpp/locking-wordart-watermark/)
- [テキストのシェイプに組み込みのWordArtスタイルを設定する](/cells/ja/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
