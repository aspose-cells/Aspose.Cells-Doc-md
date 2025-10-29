---
title: 在加载工作簿时使用C++过滤VBA项目
linktitle: 在加载Excel工作簿时过滤VBA项目
type: docs
weight: 140
url: /zh/cpp/filter-vba-project-while-loading-a-workbook/
description: 了解如何在使用Aspose.Cells与C++加载Excel工作簿时过滤VBA项目。
---

## **用C++在加载Excel工作簿时过滤VBA项目**

一些.xlsm/.xslb文件包含大量宏（或非常长的宏）。Aspose.Cells在打开此类工作簿时会无条件加载这些（元）数据。当你只需要提取工作表名称时，可以通过[**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions)控制这个过程，以跳过不需要的内容。此过滤器通过引入新的选项[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions)实现。

## **示例代码**

以下示例代码加载工作簿，仅过滤 VBA。可以从以下链接下载用于测试此功能的示例文件：

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
