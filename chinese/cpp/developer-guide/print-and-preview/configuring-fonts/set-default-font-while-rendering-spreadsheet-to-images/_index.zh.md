---
title: 使用C++将工作表渲染为图像时设置默认字体
linktitle: 设置默认字体
type: docs
weight: 360
url: /zh/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: 了解如何使用Aspose.Cells与C++在将工作表渲染为图像时设置默认字体。
---

{{% alert color="primary" %}}

请使用[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性将默认字体设置为渲染电子表格为图像时的默认字体。仅当工作簿的默认字体无法呈现您的字符时，才会使用[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性指定的默认字体。指定的默认字体将用于所有缺少或不存在的字体的单元格。

{{% /alert %}}

## 渲染电子表格为图像时设置默认字体

下面的示例代码创建一个工作簿，在第一个工作表的A4单元格中添加一些文本，并将其字体设置为无效或不存在的字体。然后，它会获取工作表的两个图像。第一张图片是通过将[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性设置为Courier New获取的，第二张图片是通过将[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性设置为Times New Roman获取的。

将[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性设置为Courier New后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

将[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性设置为Times New Roman后的输出图像。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## 示例代码

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Set default font of the workbook to none
    Style s = wb.GetDefaultStyle();
    s.GetFont().SetName(u"");
    wb.SetDefaultStyle(s);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"A4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell A4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    st.SetIsTextWrapped(true);
    cell.SetStyle(st);

    // Set first column width and fourth column height
    ws.GetCells().SetColumnWidth(0, 80);
    ws.GetCells().SetRowHeight(3, 60);

    // Create image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    // Render worksheet image with Courier New as default font
    opts.SetDefaultFont(u"Courier New");
    SheetRender sr(ws, opts);
    sr.ToImage(0, outDir + u"out_courier_new_out.png");

    // Render worksheet image again with Times New Roman as default font
    opts.SetDefaultFont(u"Times New Roman");
    SheetRender sr2(ws, opts);
    sr2.ToImage(0, outDir + u"times_new_roman_out.png");

    Aspose::Cells::Cleanup();
    return 0;
}
```
