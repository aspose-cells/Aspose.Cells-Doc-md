---
title: Saving File to Response Object with C++
linktitle: Saving File to Response Object
type: docs
weight: 50
url: /cpp/saving-file-to-response-object/
description: Learn how to save files dynamically and send them directly to a client browser using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to manipulate files. This article explains the various ways in which files can be saved to a response object.

{{% /alert %}}

## **Saving File to Response Object**

It is also possible to generate a file dynamically and send it directly to a client browser. In order to do so, use a special overloaded version of the [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method that accepts the following parameters:

- **HttpResponse** object.
- File name.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/), the content-disposition type of the output file.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), the file format type.

The [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) enumeration determines whether the file being sent to the browser provides the option to open by itself directly in the browser or in an application associated with .xls/.xlsx or another extension.

The enumeration contains the following pre-defined save types:

|**Type**|**Description**|
| :- | :- |
|Attachment|Sends the spreadsheet to the browser and opens in an application as an attachment associated with .xls/.xlsx or other extensions|
|Inline|Sends the document to the browser and presents an option to save the spreadsheet to disk or open inside the browser|

### **XLS Files**

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **XLSX Files**

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Simulate HttpResponse object (assuming it's a placeholder in the original code)
    HttpResponse* Response = nullptr;

    if (Response != nullptr)
    {
        // Save in Xlsx format
        OoxmlSaveOptions saveOptions;
        workbook.Save(*Response, outputFilePath, ContentDisposition::Attachment, saveOptions);
        Response->End();
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PDF Files**

```c++
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

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Note**

Due to the object "System.Web.HttpResponse" which is not included in .NET5 and .Netstandard,
So this function does not exist in Aspose.Cells .NET5 and .Netstandard version, you can refer to the following code to save the file to the stream, then do operation to the stream.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```