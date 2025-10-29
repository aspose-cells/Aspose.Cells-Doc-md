---
title: Работа с ContentTypeProperties с помощью C++
linktitle: Работа с ContentTypeProperties
type: docs
weight: 150
url: /ru/cpp/working-with-contenttypeproperties/
description: Добавляйте пользовательские ContentTypeProperties в Excel файл с помощью Aspose.Cells и C++.
---

Aspose.Cells предоставляет метод [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) для добавления пользовательских ContentTypeProperties в Excel файл. Также вы можете сделать свойство необязательным, установив свойство [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) в значение **true**. Следующий фрагмент кода демонстрирует добавление необязательных пользовательских ContentTypeProperties в Excel файл. На изображении показаны оба свойства, добавленных примером кода.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Выходной файл, сгенерированный образцов кода, прикреплен в качестве справки.

[Выходной файл](95584314.xlsx)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook with XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Add content type properties
    int index = workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(false);

    // Get current date and time
    time_t now = time(nullptr);
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%S", localtime(&now));
    U16String dateTime(buffer);

    // Add another content type property with current date and time
    index = workbook.GetContentTypeProperties().Add(u"MK32", dateTime, u"DateTime");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(true);

    // Save the workbook
    workbook.Save(outDir + u"WorkingWithContentTypeProperties_out.xlsx");

    std::cout << "Content type properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
