---
title: Как добавить/вставить TextBox на лист с помощью C++
linktitle: Добавить текстовое поле на лист
type: docs
weight: 10
url: /ru/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Как добавить/вставить TextBox на лист в Aspose.Cells с помощью C++.
keywords: добавить/вставить текстовое поле текстовое поле лист Excel Aspose
---

## Добавление текстового поля в лист Excel

В программе Excel (версия 07 и выше) есть два места, куда можно вставлять текстовые поля. Одно в "insert-shapes", другое — справа от верхнего меню опции "Insert".

### Метод первый:

![1](1.png)

### Метод второй:

![2](2.png)

## Как создать

Вы можете создавать текстовые поля с горизонтальным или вертикальным текстом.

- Выберите соответствующую опцию (горизонтальную или вертикальную)
- Щелкните левой кнопкой мыши на странице
- Удерживайте левую кнопку и перетаскивайте на странице
- Отпустите левую кнопку

Теперь у вас есть текстовое поле.

## Добавление текстового поля на листе рабочей книги в Aspose.Cells

Когда необходимо массово вставлять TextBox в лист, ручной метод вставки очевидно неудобен. Если это вас беспокоит, данный документ вам поможет. [Aspose.Cells](https://products.aspose.com/cells/) предоставляет API для быстрой массовой вставки в вашем коде.

В следующем примере кода создается текстовое поле.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Вы получите файл, похожий на [итоговый файл](result.xlsx). В файле вы увидите следующее:

![](52449.png)
