---
title: 用C++在形状的文本选项中指定远东和拉丁字体名称
linktitle: 在形状的文本选项中指定远东和拉丁文字体的名字
type: docs
weight: 1600
url: /zh/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: 学习如何在形状的文本选项中使用编号Aspose.Cells for C++指定远东和拉丁字体名称。
---

## **可能的使用场景**

有时你希望在远东语言字体中显示文本，例如日语、汉语、泰语等。Aspose.Cells提供[**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/)属性，可以用来指定远东语言的字体名。此外，你还可以使用[**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/)属性指定拉丁字体名称。

## **在形状的文本选项中指定远东和拉丁文字体的名字**

以下示例代码创建了一个文本框并在其中添加一些日语文本，然后指定了文本的拉丁和远东字体名称，并将工作簿保存为[输出Excel文件](67338274.xlsx)。下方截图显示输出文本框在Microsoft Excel中的拉丁和远东字体名称。

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **示例代码**

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
