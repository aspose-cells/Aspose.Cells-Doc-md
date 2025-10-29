---
title: Вставить изображение на основе ссылки на ячейку с помощью C++
linktitle: Вставка изображения на основе ссылки на ячейку
type: docs
weight: 150
url: /ru/cpp/insert-a-picture-based-on-cell-reference/
description: Узнайте, как вставить изображение на основе ссылки на ячейку с использованием Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда у вас есть пустое изображение, и вам нужно показать данные или содержимое в изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).

{{% /alert %}}

## Вставка изображения на основе ссылки на ячейку

Aspose.Cells поддерживает отображение содержимого ячейки рабочего листа в виде изображения. Вы можете связать изображение с ячейкой, содержащей данные, которые вы хотите отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, которые вы вносите в данные в этой ячейке или диапазоне ячеек, автоматически отображаются в графическом объекте. Добавьте изображение на рабочий лист, вызвав метод [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Укажите диапазон ячеек, используя атрибут [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) объекта [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### Пример кода

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
