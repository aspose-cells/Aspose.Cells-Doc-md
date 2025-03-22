---
title: Managing OLE Objects with C++
linktitle: Managing OLE Objects
type: docs
weight: 50
url: /cpp/managing-ole-objects/
description: Learn how to add, extract, and manipulate OLE objects in worksheets using Aspose.Cells with C++.
---

## **Introduction**

OLE (Object Linking and Embedding) is Microsoft's framework for a compound document technology. Briefly, a compound document is something like a display desktop that can contain visual and information objects of all kinds: text, calendars, animations, sound, motion video, 3D, continually updated news, controls, and so forth. Each desktop object is an independent program entity that can interact with a user and also communicate with other objects on the desktop.

OLE (Object Linking and Embedding) is supported by many different programs and is used to make content created in one program available in another. For example, you can insert a Microsoft Word document into Microsoft Excel. To see what types of content you can insert, click **Object** on the **Insert** menu. Only programs that are installed on the computer and that support OLE objects appear in the **Object type** box.

### **Inserting OLE Objects into the Worksheet**

Aspose.Cells supports adding, extracting, and manipulating OLE objects in worksheets. For this reason, Aspose.Cells has the [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/) class, used to add a new OLE Object to the collection list. Another class, [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), represents an OLE Object. It has some important members:

- The [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) property specifies the image (icon) data of byte array type. The image will be displayed to show the OLE Object in the worksheet.
- The [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) property specifies the object data in the form of a byte array. This data will be shown in its related program when you double-click on the OLE Object icon.

The following example shows how to add an OLE Object(s) into a worksheet.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::vector<uint8_t> ReadFileToVector(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (!file) return {};
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (size > 0)
        file.read(reinterpret_cast<char*>(buffer.data()), size);
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData = ReadFileToVector(imagePath);

    U16String objectPath = srcDir + u"book1.xls";
    std::vector<uint8_t> objectData = ReadFileToVector(objectPath);
    Vector<uint8_t> data(objectData.data(), static_cast<int32_t>(objectData.size()));
    sheet.GetOleObjects().Add(14, 3, 200, 220, data);
    if (sheet.GetOleObjects().GetCount() > 0) {
        sheet.GetOleObjects().Get(0).SetObjectData(data);
    }

    workbook.Save(outDir + u"output.out.xls");
    std::cout << "OLE object added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Extracting OLE Objects in the Workbook**

The following example shows how to extract OLE Objects in a Workbook. The example gets different OLE objects from an existing XLS file and saves different files (DOC, XLS, PPT, PDF, etc.) based on the OLE object’s file format type.

After running the code, we can save different files based on their respective OLE Objects format types.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"book1.xls");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object
    for (int32_t i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"ole_" + U16String(std::to_wstring(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Xlsx:
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
            auto ms = System::MakeObject<IO::MemoryStream>(objectData.ToArray());
            Workbook oleBook(ms);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_wstring(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetArray()), objectData.GetSize());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Extracting Embedded MOL File**

Aspose.Cells supports extracting objects of uncommon types like MOL (Molecular data file containing information about atoms and bonds). The following code snippet demonstrates extracting an embedded MOL file and saving it to disk by using this [sample excel file](94896196.xlsx).

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"EmbeddedMolSample.xlsx");

    int index = 1;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        OleObjectCollection oles = sheet.GetOleObjects();

        for (int j = 0; j < oles.GetCount(); j++)
        {
            OleObject ole = oles.Get(j);

            std::wstring indexWStr = std::to_wstring(index);
            U16String fileName = outDir + u"OleObject" + U16String(reinterpret_cast<const char16_t*>(indexWStr.c_str())) + u".mol";

            std::ofstream fs(fileName.ToUtf8(), std::ios::binary);
            if (fs.is_open())
            {
                Vector<uint8_t> objectData = ole.GetObjectData();
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
                index++;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Advance Topics**
- [Access and Modify the Display Label of the Linked Ole Object](/cells/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatically refresh OLE object via Microsoft Excel using Aspose.Cells](/cells/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extract OLE Objects from Workbook](/cells/cpp/extract-ole-objects-from-workbook/)
- [Get or Set the Class Identifier of the Embedded OLE Object](/cells/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Inserting a WAV file as an Ole Object](/cells/cpp/inserting-a-wav-file-as-an-ole-object/)