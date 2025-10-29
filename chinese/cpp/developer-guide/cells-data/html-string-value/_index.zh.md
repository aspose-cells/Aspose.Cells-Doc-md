---
title: 在单元格中添加HTML富文本的C++示例
linktitle: HTML 字符串值
type: docs
weight: 50
url: /zh/cpp/adding-html-rich-text-inside-the-cell/
description: 学习如何通过 Aspose.Cells for C++ API在单元格中添加HTML富文本。
keywords: 在单元格内添加 HTML 富文本，设置单元格内的 HTML 富文本，在单元格中添加 HTML 富文本
---

{{% alert color="primary" %}}

Aspose.Cells支持将以Microsoft Excel为导向的HTML转换为XLS/XLSX格式。也就是说，由Microsoft Excel生成的HTML可以使用Aspose.Cells转换回XLS/XLSX格式。

类似地，如果是一些简单的HTML，Aspose.Cells可以将其转换为HTML富文本。Aspose.Cells提供 [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) 方法，能够接受简单HTML并将其转换为格式化的单元格文本。

{{% /alert %}}

下面的代码示例向您展示了如何在单元格中添加HTML富文本。请查看输出Excel文件的屏幕截图。

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 相关文章

- [使用HTML设置单元格值显示项目符号](/cells/zh/cpp/display-bullets-by-setting-cell-value-using/)
- [从单元格获取HTML5字符串](/cells/zh/cpp/get-html5-string-from-cell/)
{{< app/cells/assistant language="cpp" >}}
