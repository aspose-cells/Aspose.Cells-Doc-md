---
title: ビルトインスタイル付きのワードアートテキストをC++で追加
linktitle: 組み込みスタイルを持つ WordArt テキストを追加する
type: docs
weight: 270
url: /ja/cpp/add-word-art-text-with-built-in-styles/
description: Aspose.Cells for C++を使ったビルトインスタイル付きのワードアートテキストの追加方法を学びます。
---

## **可能な使用シナリオ**
Aspose.Cellsを使ってビルトインスタイルのワードアートテキストを追加できます。この目的には[ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/)メソッドを使用してください。

## **組み込みスタイルを持つ WordArt テキストを追加する**
以下のサンプルコードは、異なる組み込みスタイルのワードアートテキストを追加します。このコードで生成された[output excel file](5115470.xlsx)をチェックしてください。これがMicrosoft Excelで表示される[output excel file](5115470.xlsx)の外観です。

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

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

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add Word Art Text with Built-in Styles
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle1, u"Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle2, u"Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle3, u"Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle4, u"Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle5, u"Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "WordArt added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
