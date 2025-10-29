---
title: 在使用C++将Excel保存为HTML时禁用Downlevel Revealed Comments
linktitle: 禁用Downlevel Revealed Comments
type: docs
weight: 20
url: /zh/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: 使用Aspose.Cells和C++在将Excel文件保存为HTML时，消除Downlevel Revealed Comments。
---

## **可能的使用场景**

将Excel文件保存为HTML时，Aspose.Cells显示了下层条件注释。这些条件注释主要与旧版本的Internet Explorer相关，与现代网页浏览器无关。你可以在以下链接详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells允许你通过将[**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/)属性设置为**true**来消除这些下层显示的注释。

## **在保存为HTML时禁用下级可见的批注**

以下示例代码展示了[**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/)属性的用法。截图显示了当未将此属性设置为true时的效果。请下载此代码中使用的[样本Excel文件](50528257.xlsx)以及它生成的[输出HTML](50528258.zip)作为参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
