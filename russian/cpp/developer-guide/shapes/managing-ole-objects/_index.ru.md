---
title: Управление объектами OLE с помощью C++
linktitle: Управление объектами OLE
type: docs
weight: 50
url: /ru/cpp/managing-ole-objects/
description: Узнайте, как добавлять, извлекать и управлять объектами OLE в рабочих листах с использованием Aspose.Cells и C++.
---

## **Введение**

OLE (Object Linking and Embedding) - это технология составного документа, разработанная Microsoft. Коротко говоря, составной документ представляет собой что-то вроде дисплейного рабочего стола, который может содержать визуальные и информационные объекты всех видов: текст, календари, анимации, звук, видео, 3D, постоянно обновляемые новости, элементы управления и т. д. Каждый объект рабочего стола является независимой программной сущностью, которая может взаимодействовать с пользователем и общаться с другими объектами на рабочем столе.

OLE (Object Linking and Embedding) поддерживается многими программами и используется для того, чтобы сделать контент, созданный в одной программе, доступным в другой. Например, вы можете вставить документ Microsoft Word в Microsoft Excel. Чтобы увидеть, какие типы содержимого можно вставить, щелкните ** Объект ** на меню ** Вставить **. В списке ** Тип объекта ** появляются только программы, установленные на компьютере и поддерживающие объекты OLE.

### **Вставка объектов OLE в лист**

Aspose.Cells поддерживает добавление, извлечение и управление объектами OLE в рабочих листах. Поэтому у Aspose.Cells есть класс [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/), который используется для добавления нового OLE-объекта в список коллекции. Другой класс, [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), представляет объект OLE. В нем есть важные члены:

- Свойство [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) задает изображение (иконку) в виде массива байтов. Это изображение отображается для отображения OLE-объекта в листе.
- Свойство [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) задает данные объекта в виде массива байтов. Эти данные будут отображаться в соответствующей программе при двойном щелчке по иконке OLE-объекта.

Нижеприведенный пример показывает, как добавить объект(ы) OLE в лист Excel.

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

### **Извлечение объектов OLE в книге**

В следующем примере показано, как извлекать объекты OLE в книге. Пример получает различные объекты OLE из существующего файла XLS и сохраняет различные файлы (DOC, XLS, PPT, PDF и т. д.) на основе типа формата файла объекта OLE.

После выполнения кода мы можем сохранить разные файлы на основе их соответствующих типов формата объектов OLE.

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

### **Извлечение встроенного файла MOL**

Aspose.Cells поддерживает извлечение объектов необычных типов, таких как MOL (файл данных молекул, содержащий информацию о атомах и связях). Следующий пример кода демонстрирует извлечение встроенного MOL файла и его сохранение на диск, используя этот [пример файла Excel](94896196.xlsx).

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

## **Дополнительные темы**
- [Доступ и изменение отображаемой метки связанного объекта OLE](/cells/ru/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells](/cells/ru/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Извлечение объектов OLE из книги](/cells/ru/cpp/extract-ole-objects-from-workbook/)
- [Получение или установка идентификатора класса встроенного объекта OLE](/cells/ru/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Вставка файла WAV в качестве объекта OLE](/cells/ru/cpp/inserting-a-wav-file-as-an-ole-object/)
