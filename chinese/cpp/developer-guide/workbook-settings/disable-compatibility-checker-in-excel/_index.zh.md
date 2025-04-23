---
title: 在Excel中禁用兼容性检查器，使用C++
linktitle: 禁用兼容性检查器
type: docs
weight: 170
url: /zh/cpp/disable-compatibility-checker-in-excel/
description: 本文介绍如何通过Aspose.Cells for C++ API禁用兼容性检查器。
keywords: 用C++禁用兼容性检查器，Excel禁用兼容性检查器，禁用兼容性检查器在工作簿中。 
---

## 在C++中禁用Excel工作表的兼容性检查器

{{% alert color="primary" %}}

Microsoft Excel的兼容性检查器在将文件保存为较早文件格式时可能会出现功能问题或保真度丢失。 兼容性检查器是Microsoft Office Excel 2007和Microsoft Excel 2010的功能。

当您从Excel 2007或Excel 2010将工作簿保存在较早的版本中（Excel 97至Excel 2003），兼容性检查程序将扫描工作簿，以查看它是否包含较早版本不支持的功能。为了帮助您决定如何处理兼容性问题，兼容性检查程序显示带有选项的对话框。它还可用于创建有关工作簿中任何问题的报告，或者禁用该功能。

有时，您需要为特定电子表格禁用兼容性检查器。通过Aspose.Cells的API，您可以以编程方式执行此操作，使用户在手动在Microsoft Excel中重新保存文件时不会因兼容性检查器对话框的弹出而感到沮丧或困惑。

{{% /alert %}}

## **如何使用Microsoft Excel禁用兼容性检查器**

要在Microsoft Excel中禁用兼容性检查程序（例如Microsoft Excel 2007/2010）：

- （Excel 2007）在办公按钮上，单击**准备**，然后单击**运行兼容性检查**，然后清除**保存此工作簿时检查兼容性**选项。
- （Excel 2010）单击“文件”选项卡，然后单击**信息**，再单击“检查问题”，再单击“检查兼容性”，最后清除“保存此工作簿时检查兼容性”选项。

## **如何使用Aspose.Cells API禁用兼容性检查器**

将[**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcompatibility/)属性设置为**False**以禁用Microsoft Excel的兼容性检查程序。

### **代码示例**

以下代码示例展示如何使用Aspose.Cells for C++禁用兼容性检查器。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open a template file
    U16String templateFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(templateFilePath);

    // Disable the compatibility checker
    workbook.GetSettings().SetCheckCompatibility(false);

    // Path to save the output file
    U16String outputFilePath = srcDir + u"Output_BK_CompCheck.out.xlsx";

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
