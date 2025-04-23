---
title: Сохранение файла в объект Response с помощью C++
linktitle: Сохранение файла в объект ответа
type: docs
weight: 50
url: /ru/cpp/saving-file-to-response-object/
description: Узнайте, как динамически сохранять файлы и отправлять их напрямую в браузер клиента с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells делает возможным манипулирование файлами. В этой статье объясняются различные способы сохранения файлов в объект ответа.

{{% /alert %}}

## **Сохранение файла в объект ответа**

Также возможно динамически создавать файл и направлять его непосредственно в браузер клиента. Для этого используйте специальную перегруженную версию метода [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/), принимающую следующие параметры:

- Объект `HttpResponse`.
- Имя файла.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/), тип содержания выводимого файла.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), тип формата файла.

Перечисление [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) определяет, предоставляет ли файл, отправляемый в браузер, возможность открыть его непосредственно в браузере или в приложении, связанном с .xls/.xlsx или другим расширением.

Перечисление содержит следующие предопределенные типы сохранения:

|**Тип**|**Описание**|
| :- | :- |
|Attachment|Отправляет электронную таблицу в браузер и открывает ее в приложении в качестве вложения, связанного с .xls/.xlsx или другими расширениями|
|Inline|Отправляет документ в браузер и предоставляет возможность сохранить электронную таблицу на диск или открыть внутри браузера|

### **XLS Файлы**

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

### **XLSX Файлы**

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

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PDF Файлы**

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

### **Примечание**

Из-за объекта"System.Web.HttpResponse", который не включен в .NET5 и .Netstandard,
Поэтому данная функция не существует в Aspose.Cells .NET5 и Netstandard версии, вы можете обратиться к следующему коду, чтобы сохранить файл в поток, а затем выполнить операцию с потоком.

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
