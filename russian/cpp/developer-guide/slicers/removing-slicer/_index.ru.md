---
title: Удаление Слайсера с помощью C++
linktitle: Удаление срезки
type: docs
weight: 30
url: /ru/cpp/removing-slicer/
description: Узнайте, как программно удалять слайсер для файлов Excel, используя API Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Если вы хотите удалить слайсер в Microsoft Excel, просто выберите его и нажмите кнопку *Delete*. Аналогично, чтобы удалить его программно с помощью API Aspose.Cells, используйте метод [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/). Он удалит слайсер с рабочего листа.

## **Удаление срезки**

Следующий образец кода загружает [образец файла Excel](67338478.xlsx), содержащий существующую срезку. Он получает доступ к срезке, а затем удаляет ее. Наконец, он сохраняет книгу как [выходной файл Excel](67338477.xlsx). На следующем скриншоте показано, что срезка будет удалена после выполнения образца кода.

![todo:image_alt_text](removing-slicer_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
