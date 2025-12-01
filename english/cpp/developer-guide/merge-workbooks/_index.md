---
title: Combine Multiple Workbooks into a Single Workbook with C++
linktitle: Workbook Merger
type: docs
weight: 66
url: /cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Learn how to combine multiple workbooks into a single workbook using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to combine workbooks with various content like images, charts, and data into a single workbook. Aspose.Cells supports this feature. This article shows how to create a console application in Visual Studio and combine workbooks with a few, simple lines of code using Aspose.Cells.

{{% /alert %}}

## **Combining Workbooks with Images and Charts**

The example code combines two workbooks into a single workbook using Aspose.Cells. The code loads the source workbooks, uses the [**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) method to combine them and saves the output workbook.

### **Source Workbooks**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Output Workbooks**

- [combined.xlsx](5473095.xlsx)

### **Screenshots**

Below are screenshots of the source and output workbooks.

{{% alert color="primary" %}}

You can use any source workbooks. These images are just for illustration purposes.

{{% /alert %}}

**The first worksheet of the charts workbook - stacked** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Second worksheet of charts workbook - line** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**First worksheet of the picture workbook - picture** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**All three worksheets in the combined workbook - stacked, line, picture** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

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

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";
    
    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Combine Multiple Worksheets into a Single Worksheet](/cells/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Merge Files](/cells/cpp/merge-files/)
{{< app/cells/assistant language="cpp" >}}
