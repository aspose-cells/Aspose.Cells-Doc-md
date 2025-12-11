---
title: Merge or Unmerge Range of Cells with C++
linktitle: Merge or Unmerge Range of Cells
type: docs
weight: 190
url: /cpp/merge-or-unmerge-range-of-cells/
description: Merge and Unmerge Cells in a Range in Excel with C++ code.
keywords: c++ merge and unmerge cells in a range, c++ merge and unmerge cells in range, merge and unmerge cells in range with c++, merge and unmerge cells in range using c++, merge and unmerge cells in excel using c++, merge and unmerge cells in excel with c++, c++ merge and unmerge cells in excel, c++ merge cells in excel, c++ unmerge cells in excel, merge cells in range with c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can use Aspose.Cells to merge or split a range of cells. Aspose.Cells provides the [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) and [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) methods for this purpose. This article explains how to merge a range of cells into a single cell.

{{% /alert %}}

## **Example**

The following sample code first creates a range (A1:D4), then merges the cells in the range into a single cell using the [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) method. Similarly, you can unmerge the cells by creating a range and calling the [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) method.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of the output Excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
