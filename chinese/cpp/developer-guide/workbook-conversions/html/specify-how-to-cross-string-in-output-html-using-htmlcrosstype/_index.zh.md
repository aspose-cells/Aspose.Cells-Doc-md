---
title: 指定在输出HTML中如何交叉字符串，使用HtmlCrossType与C++
linktitle: 在输出HTML中指定HtmlCrossType
type: docs
weight: 140
url: /zh/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: 学习如何使用Aspose.Cells for C++结合HtmlCrossType控制HTML输出中的字符串溢出。
---

## **可能的使用场景**

当单元格包含的文本或字符串大于单元格宽度时，如果下一列的单元格为空，则字符串会溢出。导出为HTML时，可以通过指定交叉类型（[**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/)枚举）来控制此溢出，枚举值如下：

- **HtmlCrossType.Default**: 与MS Excel显示类似, 取决于下一个单元格. 如果下一个单元格为空, 字符串将跨越或被截断.

- **HtmlCrossType.MSExport**: 以MS Excel导出HTML的方式显示字符串.

- **HtmlCrossType.Cross**: 显示HTML交叉字符串, 对于创建大型HTML文件性能要比将值设置为Default或FitToCell快十倍以上.

- **HtmlCrossType.FitToCell**：仅在单元格宽度内显示字符串。

## **使用HtmlCrossType指定输出HTML中如何交叉字符串**

以下示例代码加载[示例Excel文件](51740732.xlsx)，并通过指定不同的[**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/)将其保存为HTML格式。请下载由此代码生成的[输出HTML](51740734.zip)。示例Excel文件包含一个以红色边框标记的图片，如此截图所示，展示了[**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/)值对输出HTML的影响。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
