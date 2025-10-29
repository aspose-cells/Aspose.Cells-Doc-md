---
title: 使用C++在HtmlSaveOptions.TableCssId属性前缀表元素样式
linktitle: 使用HtmlSaveOptions.TableCssId属性前缀表元素样式
type: docs
weight: 110
url: /zh/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: 学习如何使用HtmlSaveOptions.TableCssId属性前缀表元素样式，示例ID为Aspose.Cells for C++。
---

## **可能的使用场景**

Aspose.Cells允许您使用[**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)属性前缀表元素样式。假设将此属性设置为某个值，如**MyTest_TableCssId**，那么您将找到类似下面显示的表元素样式

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

以下屏幕截图显示了使用 [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) 属性对输出 HTML 的影响。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## ** 使用HtmlSaveOptions.TableCssId属性前缀表元素样式**

以下示例代码演示了如何利用[**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)属性。请查看代码生成的[output HTML](60489790.zip) 以供参考。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - specify table css id
    HtmlSaveOptions opts;
    opts.SetTableCssId(u"MyTest_TableCssId");

    // Save the workbook in html
    wb.Save(u"outputTableCssId.html", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
