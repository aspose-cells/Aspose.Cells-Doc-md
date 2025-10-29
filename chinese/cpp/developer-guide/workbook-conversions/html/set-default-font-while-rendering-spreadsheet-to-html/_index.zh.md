---
title: 在渲染电子表格为HTML时设置默认字体，使用C++
linktitle: 在将电子表格渲染为HTML时设置默认字体
type: docs
weight: 370
url: /zh/cpp/set-default-font-while-rendering-spreadsheet-to/
description: 学习如何使用Aspose.Cells for C++在渲染电子表格为HTML时设置默认字体。
---

{{% alert color="primary" %}}

Aspose.Cells允许在将电子表格渲染为HTML时设置默认字体。请使用[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/)实现此功能。当电子表格中的某些单元格字体无效或不存在时，这些单元格将以由[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/)属性指定的字体呈现。

{{% /alert %}}

## 在将电子表格渲染为HTML时设置默认字体

以下示例代码创建一个工作簿，并在第一个工作表的B4单元格中添加了一些文本，并将其字体设置为某个未知/不存在的字体。然后，它通过设置不同的默认字体名称，如Courier New、Arial、Times New Roman等，将工作簿保存为HTML。

截图显示通过[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/)属性设置不同默认字体名的效果。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成了使用Courier New的[output HTML文件](5115516), 使用Arial的[output HTML文件](5115518), 以及使用Times New Roman的[output HTML文件](5115517).

## 示例代码

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

    // Create workbook object and access first worksheet
    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"B4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell B4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    cell.SetStyle(st);

    // Now save the workbook in html format and set the default font to Courier New
    HtmlSaveOptions opts;
    opts.SetDefaultFontName(u"Courier New");
    wb.Save(outDir + u"out_courier_new_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Arial
    opts.SetDefaultFontName(u"Arial");
    wb.Save(outDir + u"out_arial_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Times New Roman
    opts.SetDefaultFontName(u"Times New Roman");
    wb.Save(outDir + u"times_new_roman_out.htm", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
