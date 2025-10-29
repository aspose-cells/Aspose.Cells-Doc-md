---
title: Обновление значений связанных фигур с помощью C++
linktitle: Обновить значения связанных форм
type: docs
weight: 3200
url: /ru/cpp/refresh-values-of-linked-shapes/
description: Узнайте, как обновлять значения связанных фигур в Excel файлах с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда у вас есть связанная форма в файле Excel, связанная с какой-то ячейкой. В Microsoft Excel, изменение значения связанной ячейки также изменяет значение связанной формы. Это также работает отлично с Aspose.Cells, если вы хотите сохранить свою книгу в формате XLS или XLSX. Однако, если вы хотите сохранить свою книгу в формате PDF или HTML, тогда вам придется вызвать метод [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) для обновления значения связанной формы.

{{% /alert %}}

## Пример

Следующий скриншот показывает исходный файл Excel, использованный в приведенном ниже примере кода. В нем есть связанная картинка, связанная с ячейками A1 до E4. Мы изменим значение ячейки B4 с помощью Aspose.Cells и вызовем метод [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) для обновления значения картинки и сохранения его в PDF-формате.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Вы можете скачать [исходный файл Excel](95584291.xlsx) и [итоговый PDF](95584292.pdf) по указанным ссылкам.

### C++ код для обновления значений связанных фигур

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
