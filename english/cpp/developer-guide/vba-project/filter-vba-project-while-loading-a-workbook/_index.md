---
title: Filter VBA Project while loading a workbook with C++
linktitle: Filter VBA Project while loading a workbook
type: docs
weight: 140
url: /cpp/filter-vba-project-while-loading-a-workbook/
description: Learn how to filter VBA projects while loading an Excel workbook using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Filter VBA Project while loading an Excel workbook in C++**

Some .xlsm/.xslb files have an extremely large amount of macros (or very, very long macros). Aspose.Cells will unconditionally load this (meta) data when opening such workbooks. You may require to control this though [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) when you really only need to extract sheet names for a large number of workbooks thus skipping over such unneeded content. This filter is provided by introducing a new option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions).

## **Sample Code**

The following sample code loads a workbook such that only VBA is filtered. A sample file for testing this feature can be downloaded from the following link:

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
