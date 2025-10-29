---
title: Извлечение Ole объектов из книги с помощью C++
linktitle: Извлечение объектов OLE из книги
type: docs
weight: 110
url: /ru/cpp/extract-ole-objects-from-workbook/
description: Узнайте, как извлекать Ole объекты из книги с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Иногда необходимо извлекать Ole-объекты из книги. Aspose.Cells поддерживает извлечение и сохранение этих Ole-объектов.

Эта статья показывает, как создать консольное приложение в Visual Studio и извлечь различные Ole-объекты из книги с помощью нескольких простых строк кода.

{{% /alert %}}

## **Извлечение объектов OLE из книги**

### **Создание шаблонной книги Excel**

1. Создайте рабочую книгу в Microsoft Excel.
1. Добавьте документ Microsoft Word, рабочую книгу Excel и PDF-документ как OLE объекты на первый лист.

|**Образец документа с объектами OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Затем извлеките OLE объекты и сохраните их на жесткий диск с их соответствующими типами файлов.

### **Загрузите и установите Aspose.Cells**

1. [Скачать Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Установите его на вашем компьютере для разработки.

Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.

### **Создайте проект**

Запустите **Visual Studio** и создайте новое консольное приложение. В этом примере показано создание консольного приложения на C++.

1. Добавьте ссылки.
   1. Добавьте ссылку на компонент Aspose.Cells в проект, например, добавьте ссылку на ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Извлечение объектов OLE**

Следующий код выполняет фактическую работу по поиску и извлечению объектов OLE. Объекты OLE (DOC, XLS и PDF файлы) сохраняются на диск.

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
