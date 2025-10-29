---
title: 使用C++在保存为HTML时禁用CSS
linktitle: 禁用CSS在保存为HTML时
type: docs
weight: 320
url: /zh/cpp/disable-css-while-saving-to-html/
description: 了解如何在使用Aspose.Cells for C++将Excel文件保存为HTML时禁用CSS。
---

## **可能的使用场景**

 当你将Excel文件保存为单页HTML时，CSS元素通常会嵌入到HTML文件中，并位于HEAD部分。如果将此文件作为内容/正文附加到电子邮件中，大多数电子邮件客户端会删除这些CSS元素，导致渲染不正确。Aspose.Cells的24.12版本引入了一个选项，允许你选择性禁用CSS，从而使样式直接应用于HTML元素本身。如果你希望将HTML用作电子邮件的内容/正文，请使用[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/)属性并设置为**true**。

## ** 禁用CSS在保存为HTML时**

 下面的示例代码展示了[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/)属性的用法。

## **示例代码**

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
