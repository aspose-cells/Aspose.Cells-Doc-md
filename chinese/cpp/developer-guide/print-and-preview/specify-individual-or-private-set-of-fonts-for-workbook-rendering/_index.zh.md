---
title: 使用 C++ 指定工作簿渲染的单独或私有字体集
linktitle: 指定工作簿渲染的个体或私有字体集
type: docs
weight: 40
url: /zh/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: 学习如何使用 Aspose.Cells for C++为工作簿渲染指定单独或私有的字体集。
---

## **可能的使用场景**

 通常，你为所有工作簿指定字体目录或字体列表，但有时你必须为你的工作簿指定单独或私有的字体集。Aspose.Cells 提供了 [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) 类，可以用来为你的工作簿指定单独或私有的字体集。

## **指定工作簿渲染的个体或私有字体集**

 以下示例代码加载了带有其单独或私有字体集的[示例Excel文件](67338268.xlsx)，这些字体通过 [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) 类指定。请参阅代码中使用的[示例字体](67338271.zip)以及它生成的[输出PDF](67338269.pdf)。以下截图显示了如果成功找到字体，输出PDF的外观。

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
