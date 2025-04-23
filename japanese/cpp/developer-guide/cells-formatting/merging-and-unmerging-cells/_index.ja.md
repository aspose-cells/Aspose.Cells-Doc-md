---
title: セルの結合と解除（C++）
linktitle: セルの結合と解除
description: Aspose.Cellsは、セルの結合と解除をサポートするC++ライブラリです。この記事では、Aspose.Cellsを使用したセルの結合と解除の方法と、結合セルのスタイルのカスタマイズについて紹介します。
keywords: Aspose.Cells、C++ライブラリ、スプレッドシート、セルの結合、結合解除、スタイル設定、カスタムスタイル
type: docs
weight: 190
url: /ja/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cellsはこの機能をサポートし、ワークシート内でセルを結合することもできます。 結合されたセルは解除することもできます。 結合されたセルのセル参照は、元の選択範囲の左上のセルの参照です。

{{% /alert %}} 

## **紹介**
すべての行や列に常に同じ数のセルを必ずしも欲しいわけではありません。 たとえば、複数の列にまたがるタイトルを置きたい場合があります。 または、請求書を作成する場合、合計に対して少ない列を望むことがあります。 セルを1つに結合してみてください。 Microsoft Excelは、ユーザーがファイルを選択して自分の望むようにスプレッドシートの構造を結合できます。

{{% alert color="primary" %}} 

セルを結合すると、結合範囲の左上のセルのデータのみが保持されます。 範囲内の他のセルにデータがある場合、このデータは削除されます。
同様に、書式設定は結合されたセルに適用される範囲の左上のセルに基づいており、セルを結合すると、結合されたセルに元の書式設定が適用されます。 セルが分割されると、新しいセルは元の書式設定を維持します。

{{% /alert %}} 

## **ワークシート内でセルを結合する**
### **Microsoft Excelでセルを結合する**
以下の手順では、MS Excelを使用してワークシート内のセルを結合する方法について説明します。

1. 範囲内で左上のセルにデータをコピーします。
1. 結合したいセルを選択します。
1. 行または列内のセルを結合してセルの内容を中央に配置するには、**書式設定**ツールバーの**結合して中央配置**アイコンをクリックします。

### **Aspose.Cellsでセルの結合**
`Aspose::Cells::Cells`クラスにはこのタスクに役立つ便利なメソッドがあります。例えば、`Merge()`メソッドは指定された範囲内のセルを1つのセルに結合します。

以下の例は、ワークシート内のセル(C6:E7)を結合する方法を示しています。

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **結合されたセルの結合解除（分割）**
### **Microsoft Excel の使用**
以下の手順では、Microsoft Excelを使用して結合されたセルを分割する方法について説明します。

1. 結合されたセルを選択します。
   セルが結合されている場合、**結合して中央配置**が**書式設定**ツールバーで選択されます。
1. **書式設定**ツールバーで**結合して中央配置**をクリックします。

### **Aspose.Cellsの使用**
`Aspose::Cells::Cells`クラスには、セルを元の状態に分割する`UnMerge()`というメソッドがあります。このメソッドは結合されたセルの範囲内のセルの参照を使用してセルの結合を解除します。

以下の例は、結合されたセル(C6)を分割する方法を示しています。 この例では、前の例で作成されたファイルを使用し、結合されたセルを分割しています。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [ワークシート内の結合セルを検出する](/cells/ja/cpp/detect-merged-cells-in-a-worksheet/)
