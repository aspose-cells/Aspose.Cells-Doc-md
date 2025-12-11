---
title: AutoFit Row Height Automatically When Loading a File with C++
linktitle: AutoFit Row Height Automatically When Loading a File
type: docs
weight: 120
url: /cpp/autofit-row-height/
description: Learn how to fit rows whose height is not customized using Aspose.Cells with C++.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening Excel file.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The height of a row automatically matches the font of its content, but when the height of the cached row does not match the height of the content in the file, MS Excel will automatically adjust the row height when loading the file, whereas Aspose.Cells will not automatically adjust it in order to improve performance. If you need Aspose.Cells to automatically match row heights when loading files, you can achieve this by using the parameter [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

Please refer to the following image. We can observe that the cached row height in row 11 is 15, but Excel automatically adjusts the row height when loading the file.  
<br>
<img src="1.png" width=70% />

## **Adjust Row Height using Aspose.Cells**
If you load the file directly and save it to PDF, the data will not be fully displayed in the PDF because the cached row height is only 15.  
<br>
<img src="2.png" width=70% />
<br>
If you set the parameter [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) to **true** when loading the file, Aspose.Cells will automatically adjust the row height. The adjusted row height can effectively meet the text‑display requirements.  
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
