---
title: Доступ и изменение метки отображения связанного Ole объекта с помощью C++
linktitle: Доступ и изменение отображаемой метки связанного объекта OLE
type: docs
weight: 100
url: /ru/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Узнайте, как получать и изменять метку отображения связанного Ole объекта в файлах Excel с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Microsoft Excel позволяет изменять метку отображения Ole-объекта, как показано на следующем скриншоте. Также можно получить или изменить метку отображения Ole-объекта с помощью API Aspose.Cells с методами [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) и [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Доступ и изменение отображаемой метки связанного объекта OLE**

Пожалуйста, ознакомьтесь с образцом кода ниже, который загружает [образец файла Excel](64716810.xlsx), содержащий объект OLE. Код получает доступ к объекту OLE и изменяет его метку с Sample APIs на Aspose APIs. Пожалуйста, обратите внимание на вывод консоли ниже, который показывает влияние образца кода на образец файла Excel в качестве примера.

## **Образец кода**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
