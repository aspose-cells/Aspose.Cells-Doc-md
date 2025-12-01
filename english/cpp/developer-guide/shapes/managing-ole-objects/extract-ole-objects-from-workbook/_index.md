---
title: Extract OLE Objects from Workbook with C++
linktitle: Extract OLE Objects from Workbook
type: docs
weight: 110
url: /cpp/extract-ole-objects-from-workbook/
description: Learn how to extract OLE objects from a workbook using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to extract OLE objects from a workbook. Aspose.Cells supports extracting and saving those OLE objects.

This article shows how to create a console application in Visual Studio and extract different OLE objects from a workbook with a few simple lines of code.

{{% /alert %}}

## **Extract OLE Objects from a Workbook**

### **Creating a Template Workbook**

1. Create a workbook in Microsoft Excel.
1. Add a Microsoft Word document, an Excel workbook, and a PDF document as OLE objects on the first worksheet.

|**Template document with OLE objects (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Next, extract the OLE objects and save them to the hard disk with their respective file types.

### **Download and Install Aspose.Cells**

1. [Download Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Install it on your development computer.

All Aspose components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.

### **Create a Project**

Start **Visual Studio** and create a new console application. This example will show a C++ console application.

1. Add References
   1. Add a reference to the Aspose.Cells component to your project, for example, add a reference to ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Extract OLE Objects**

The code below does the actual work of finding and extracting OLE objects. The OLE objects (DOC, XLS, and PDF files) are saved to disk.

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"oleFile.xlsx");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object in the worksheet
    for (int i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Excel97To2003:
                fileName += u"Xlsx";
                break;
            case FileFormatType::Ppt:
                fileName += u"Ppt";
                break;
            case FileFormatType::Pdf:
                fileName += u"Pdf";
                break;
            case FileFormatType::Unknown:
                fileName += u"Jpg";
                break;
            default:
                // Handle other formats if needed
                break;
        }

        // Save the oleobject as a new excel file if the object type is xls
        if (ole.GetFileFormatType() == FileFormatType::Xlsx)
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                Workbook oleBook(objectData);
                oleBook.GetSettings().SetIsHidden(false);
                oleBook.Save(srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
            }
        }
        // Create the files based on the oleobject format types
        else
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
