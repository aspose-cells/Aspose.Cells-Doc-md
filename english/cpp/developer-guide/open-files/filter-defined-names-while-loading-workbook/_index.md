---
title: Filter Defined Names while loading Workbook with C++
linktitle: Filter Defined Names while loading Workbook
type: docs
weight: 50
url: /cpp/filter-defined-names-while-loading-workbook/
description: Learn to filter or remove defined names while loading a workbook with Aspose.Cells in C++.
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to filter or remove defined names present inside the workbook. Please use [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) to load defined names and use [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) to remove them while loading the workbook. Please note, if you remove defined names, then formulas inside the workbook may break up.

## **Filter Defined Names while loading Workbook**

The following sample code loads the [sample Excel file](61767860.xlsx) which has a formula in cell **C1** containing the defined names i.e. `=SUM(MyName1, MyName2)`. Since we are using [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) to remove the defined names while loading the workbook, the formula in cell C1 in the [output Excel file](61767861.xlsx) breaks up and you see `#NAME?` instead. Please see the following screenshot that shows the effect of the code on the sample Excel file.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Specify the load options
    LoadOptions opts;
    // We do not want to load defined names
    LoadFilter loadFilter(~LoadDataFilterOptions::DefinedNames);
    opts.SetLoadFilter(&loadFilter);

    // Load the workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx";
    Workbook wb(inputFilePath, opts);

    // Save the output Excel file, it will break the formula in C1
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"outputFilterDefinedNamesWhileLoadingWorkbook.xlsx";
    wb.Save(outputFilePath);

    std::cout << "FilterDefinedNamesWhileLoadingWorkbook executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```