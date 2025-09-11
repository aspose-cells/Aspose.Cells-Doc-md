---
title: AutoFit Row Height Automatically When Loading file with C++
linktitle: AutoFit Row Height Automatically When Loading file
type: docs
weight: 120
url: /cpp/autofit-row-height/
description: Learn how to fit the rows which height are not customed using Aspose.Cells with C++.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file.
---

## **Possible Usage Scenarios**
The height of the row automatically matches the font of the content, but when the height of the cached row does not match the height of the content in the file, MS Excel will automatically adjust the row height when loading the file, while Aspose.Cells will not automatically adjust it to improve performance. If you need to use the Aspose.Cells program to automatically match line heights when loading files, you can achieve the goal through the parameter [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

Please refer to the following image data. We can observe that the cache row height in line 11 is 15, but Excel automatically adjusted the row height when loading the file.
<br>
<img src="1.png" width=70% />

## **Adjust Row Height using Aspose.Cells**
If you directly load the file and save it to PDF, the data will not be fully displayed in PDF because its cache line height is only 15.
<br>
<img src="2.png" width=70% />
<br>
If you set the parameter [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) to true when loading the file, then Aspose.Cells will automatically adjust the row height. The adjusted line height can effectively meet the text display requirements.
<br>
<img src="3.png" width=70% />

## **C++ Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}