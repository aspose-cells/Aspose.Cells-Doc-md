---
title: 用 C++ 管理OLE对象
linktitle: 管理OLE对象
type: docs
weight: 50
url: /zh/cpp/managing-ole-objects/
description: 学习如何使用 Aspose.Cells 和 C++ 在工作表中添加、提取和操作OLE对象。
---

## **介绍**

OLE (对象链接和嵌入) 是微软的复合文档技术框架。简而言之，复合文档类似于一个显示桌面，可以包含各种视觉和信息对象: 文本、日历、动画、声音、动态视频、3D、不断更新的新闻、控件等。每个桌面对象都是一个独立的程序实体，可以与用户交互，并与桌面上的其他对象进行通信。

OLE (对象链接和嵌入) 受到许多不同程序的支持，并用于使在一个程序中创建的内容在另一个程序中可用。例如，您可以将Microsoft Word文档插入Microsoft Excel。要查看可以插入的内容的类型，请单击**插入**菜单上的**对象**。只有安装在计算机上并支持OLE对象的程序才会出现在**对象类型**框中。

### **将OLE对象插入工作表**

Aspose.Cells支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells具有[**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/)类，用于向集合列表中添加新的OLE对象。另一个类，[**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/)，表示OLE对象。它具有一些重要成员：

- [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/)属性指定图像（图标）的字节数组数据。图像将显示在工作表中，用于展示OLE对象。
- [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)属性指定对象的数据，形式为字节数组。当双击OLE对象图标时，将在相关程序中显示这些数据。

下面的示例演示了如何将一个或多个OLE对象添加到工作表中。

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

### **从工作簿中提取OLE对象**

以下示例显示了如何从工作簿中提取OLE对象。该示例从现有的XLS文件中获取不同的OLE对象，并根据OLE对象的文件格式类型保存不同的文件(DOC、XLS、PPT、PDF等)。

运行代码后，我们可以根据各自OLE对象的格式类型保存不同的文件。

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
        U16String fileName = srcDir + u"ole_" + U16String(std::to_string(i).c_str()) + u".";

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
            Workbook oleBook(objectData);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **提取嵌入的MOL文件**

Aspose.Cells 支持提取不常见类型的对象，如 MOL（分子数据文件，包含关于原子和键的信息）。以下代码片段演示了如何利用此 [示例Excel文件](94896196.xlsx) 提取嵌入的 MOL 文件并保存到磁盘。

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

## **高级主题**
- [访问和修改链接的OLE对象的显示标签](/cells/zh/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [使用Aspose.Cells自动刷新OLE对象通过Microsoft Excel](/cells/zh/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [从工作簿中提取OLE对象](/cells/zh/cpp/extract-ole-objects-from-workbook/)
- [获取或设置嵌入的OLE对象的类标识符](/cells/zh/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [将WAV文件插入为一个OLE对象。](/cells/zh/cpp/inserting-a-wav-file-as-an-ole-object/)
