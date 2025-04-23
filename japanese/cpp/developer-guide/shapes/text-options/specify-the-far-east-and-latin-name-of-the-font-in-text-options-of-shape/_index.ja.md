---
title: C++を使用して図形のテキストオプションにおいて、東アジアおよびラテンフォントの名前を指定する方法について学びます。
linktitle: テキストオプションのフォントの遠隔地およびラテン名を指定する
type: docs
weight: 1600
url: /ja/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Aspose.Cells for C++を使用して、形状のテキストオプションで東アジアとラテンフォント名を指定する方法を学びます。
---

## **可能な使用シナリオ**

東アジア言語のフォント名を指定したい場合、例えば日本語、中国語、タイ語などがあります。Aspose.Cellsは[**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/)プロパティを提供しており、これを使用してフォント名を指定できます。さらに、[**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/)プロパティを使用してラテンフォント名も指定できます。

## **テキストオプションのフォントの遠隔地およびラテン名を指定する**

次のサンプルコードは、テキストボックスを作成し、その中に日本語のテキストを追加します。次に、テキストのラテンフォント名と東アジアフォント名を指定し、ワークブックを[出力Excelファイル](67338274.xlsx)として保存します。以下のスクリーンショットは、Microsoft Excelで出力されたテキストボックスのラテンと東アジアフォント名を示しています。

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet ws = wb.GetWorksheets().Get(0);

    int idx = ws.GetTextBoxes().Add(5, 5, 50, 200);
    TextBox tb = ws.GetTextBoxes().Get(idx);

    tb.SetText(u"\u3053\u3093\u306B\u3061\u306F\u4E16\u754C");

    tb.GetTextOptions().SetLatinName(u"Comic Sans MS");
    tb.GetTextOptions().SetFarEastName(u"KaiTi");

    wb.Save(u"outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", SaveFormat::Xlsx);

    std::cout << "Textbox created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
