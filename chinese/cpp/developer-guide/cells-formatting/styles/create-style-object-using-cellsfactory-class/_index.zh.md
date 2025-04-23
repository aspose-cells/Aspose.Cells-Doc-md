---  
title: 使用CellsFactory类在C++中创建样式对象  
description: Aspose.Cells是一个支持使用样式对象对单元格进行样式设置的C++库。本文将介绍如何使用Aspose.Cells中的CellsFactory类创建单元格样式对象，以便用户根据需要自定义单元格的外观。  
keywords: Aspose.Cells，C++库，电子表格，样式对象，单元格样式，定制化  
type: docs  
weight: 70  
url: /zh/cpp/create-style-object-using-cellsfactory-class/  
---  

## **使用CellsFactory类创建Style对象**  
以下示例代码使用CellsFactory类创建[样式](https://reference.aspose.com/cells/cpp/aspose.cells/style)对象，然后设置工作簿的默认样式。请下载[输出Excel文件](5115153.xlsx)，以查看此代码的结果供您参考。  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
