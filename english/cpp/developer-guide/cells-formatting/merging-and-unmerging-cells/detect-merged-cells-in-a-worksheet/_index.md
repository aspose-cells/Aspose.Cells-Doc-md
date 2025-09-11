---
title: Detect Merged Cells in a Worksheet with C++
linktitle: Detect Merged Cells
description: Aspose.Cells is a C++ library for working with spreadsheet files. It supports detecting merged cells in a worksheet, making it easy for users to identify and manipulate these cells. This article will introduce how to use the Aspose.Cells library to detect merged cells.
keywords: Aspose.Cells, Worksheet, Merge Cells, Detect, Identify, Operate
type: docs
weight: 80
url: /cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

This article provides information on how to get merged cell areas in a worksheet.

Aspose.Cells allows you to get merged cell areas in a worksheet. You can unmerge (split) them too. This article shows the simplest code using **Aspose.Cells API** to perform the task.

{{% /alert %}}

The component provides the [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) method which can get all merged cells. The following code sample shows you how to detect merged cells in a worksheet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}