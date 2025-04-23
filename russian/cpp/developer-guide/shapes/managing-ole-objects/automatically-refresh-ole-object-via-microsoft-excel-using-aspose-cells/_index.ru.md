---
title: Автоматическое обновление Ole объекта через Microsoft Excel с помощью C++
linktitle: Автоматическое обновление Ole объекта
type: docs
weight: 270
url: /ru/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Узнайте, как автоматически обновлять Ole объекты в Microsoft Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) для обновления Ole-объекта при открытии файла Excel в Microsoft Excel. Благодаря этому свойству Ole-объект будет отображать правильное изображение Ole, созданное Microsoft Excel.

{{% /alert %}}

Следующий пример кода загружает [образец файла Excel](5115231.xlsx), в котором есть нереальное Ole-изображение. Ole-объект на самом деле — документ Microsoft Word, но образец файла Excel показывает изображение животного вместо изображения Word. Однако, если открыть [выходной файл Excel](5115225.xlsx), вы увидите, что Microsoft Excel отображает правильное Ole-изображение.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
