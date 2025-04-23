---  
title: 使用C++移除工作簿中的未使用样式  
linktitle: 删除工作簿中的未使用样式  
type: docs  
weight: 340  
url: /zh/cpp/remove-unused-styles-inside-the-workbook/  
description: 使用Aspose.Cells和C++在Excel工作簿中移除未使用的样式。  
---  

{{% alert color="primary" %}}  

未使用的样式不仅占用空间，还会在转换为PDF、HTML等不同格式时引发性能问题。Aspose.Cells提供了[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/)以删除工作簿内所有未使用的样式。  

{{% /alert %}}  

以下代码说明了[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/)的用法。该代码加载了[模板Excel文件](5115520.xlsx)，可以通过提供的链接下载。它包含一个名为**AsposeStyle**的未使用样式；执行后，此样式及所有其他未使用样式将被删除。  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

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

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
