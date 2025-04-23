---
title: Доступ к полю ввода текста по имени с помощью C++
linktitle: Доступ к текстовому полю по имени
type: docs
weight: 230
url: /ru/cpp/access-the-text-box-by-the-name/
description: Узнайте, как получить доступ к полю ввода по его имени с помощью Aspose.Cells for C++.
---

## Доступ к текстовому полю по имени

Ранее текстовые поля получали по индексу из коллекции [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/), но теперь их также можно получить по имени из этой коллекции. Это удобный и быстрый способ доступа к вашему текстовому полю, если вы уже знаете его имя.

Следующий пример кода сначала создает поле ввода текста и присваивает ему некоторый текст и имя. Затем, в следующих строках, мы получаем тот же текстовый блок по его имени и выводим его текст.

### C++ код для доступа к полю ввода по имени

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### Вывод консоли, сгенерированный примерным кодом

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
