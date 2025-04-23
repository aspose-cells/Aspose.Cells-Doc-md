---
title: 在加载 Excel 文件时解析数据透视缓存记录（C++）
linktitle: 解析数据透视缓存记录
type: docs
weight: 70
url: /zh/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: 学习如何在加载 Excel 文件时解析数据透视缓存记录，使用 Aspose.Cells for C++。
---

## **可能的使用场景**

创建透视表时，Microsoft Excel会复制源数据并将其存储在透视缓存中。透视缓存保存在Microsoft Excel的内存中。您看不到它，但这是建立透视表、更改切片选择或移动行/列时透视表引用的数据。这使得Microsoft Excel能够对透视表的更改做出非常灵敏的响应，但它也可能使文件的大小翻倍。毕竟，透视缓存只是源数据的副本，因此您的文件大小可能会翻倍。

在将Excel文件加载到Workbook对象中时，您可以决定是否也要加载透视缓存记录，使用[**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/)属性。此属性的默认值为**false**。如果透视缓存相当大，它会提高性能。但如果您也想加载透视缓存记录，应将此属性设置为**true**。

## **在加载Excel文件时解析透视缓存记录**

以下示例代码解释了[**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/)属性的用法。它在解析透视缓存记录时加载[示例Excel文件](61767773.xlsx)。然后刷新透视表并将其保存为[输出Excel文件](61767774.xlsx)。

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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
