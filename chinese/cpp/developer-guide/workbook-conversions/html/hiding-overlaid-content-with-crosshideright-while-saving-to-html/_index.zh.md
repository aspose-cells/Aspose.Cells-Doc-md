---
title: 在使用C++保存为HTML时，通过CrossHideRight隐藏覆盖内容
linktitle: 使用 CrossHideRight 在保存为 HTML 时隐藏重叠内容
type: docs
weight: 100
url: /zh/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: 使用Aspose.Cells在C++中通过CrossHideRight隐藏覆盖内容以保存为HTML。
---

## **可能的使用场景**

将Excel文件保存为HTML时，可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells根据微软Excel生成HTML，但当你将交叉类型更改为[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)时，它会隐藏所有在单元格右侧被覆盖或重叠的字符串。

## **在保存为Html时使用CrossHideRight隐藏重叠内容**

以下示例代码加载[样本Excel文件](64716894.xlsx)，并在将[**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/)设置为[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)后将其保存为[输出HTML](64716893.zip)。截图说明了[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)如何影响默认输出的HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
