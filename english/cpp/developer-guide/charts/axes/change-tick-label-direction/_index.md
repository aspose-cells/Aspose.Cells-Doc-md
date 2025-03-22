---
title: Change Tick Label Direction with C++
linktitle: Change Tick Label Direction
description: Learn how to change the direction of tick labels in Aspose.Cells for C++. Our guide will help you understand how to adjust the orientation of tick labels on axes, including horizontal, vertical, and angled orientations.
keywords: Aspose.Cells for C++, tick labels, direction, orientation, axes, horizontal, vertical, angled.
type: docs
weight: 170
url: /cpp/change-tick-label-direction/
---

## **Change Tick Label Direction**

Aspose.Cells provides you with the ability to change the chart tick label direction by using the [**TickLabels.DirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/properties/directiontype) property. The [**TickLabels.DirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/properties/directiontype) property accepts the [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) enumeration value. The [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) enumeration provides the following members:

- Horizontal
- Vertical
- Rotate90
- Rotate270
- Stacked

The following image compares the source and output files:

### **Source file image**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Output file image**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

The following code snippet changes the tick label direction from Rotate90 to Horizontal.

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

The source and output files can be downloaded from the following links.

[Source File](105480221.xlsx)

[Output File](105480223.xlsx)