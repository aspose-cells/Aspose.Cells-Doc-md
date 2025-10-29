---
title: Как повернуть текст ячейки на C++
linktitle: Как повернуть текст ячейки
type: docs
weight: 80
url: /ru/cpp/how-to-rotate-text-of-cell/
description: Код C++ для поворота текста ячейки с помощью API Aspose.Cells for C++
keywords: C++ повернуть текст ячейки, программное изменение угла поворота текста в рабочей книге, как повернуть текст ячейки в Excel на C++
---

## **Поворот текста ячейки в Aspose.Cells**

Aspose.Cells — мощный компонент на C++, который позволяет разработчикам работать с таблицами Excel программным способом. Одной из функций Aspose.Cells является возможность поворачивать ячейки, позволяя настраивать ориентацию текста и улучшать визуальное представление данных. В этом документе мы рассмотрим, как поворачивать ячейки с помощью Aspose.Cells.

## **Как вращать текст ячейки в Excel**
Для вращения ячейки в Excel вы можете использовать следующие шаги:
1. Откройте Excel и выберите ячейку или диапазон ячеек, которые вы хотите повернуть.
1. Щелкните правой кнопкой мыши на выбранной ячейке(ях) и выберите "Формат ячеек" в контекстном меню. В качестве альтернативы вы можете перейти на вкладку "Главная" в ленте Excel, нажать на выпадающий список "Формат" в группе "Ячейки" и выбрать "Формат ячеек".
1. В диалоговом окне "Формат ячеек" перейдите на вкладку "Выравнивание".
1. В разделе "Ориентация" вы увидите варианты вращения текста. Вы можете непосредственно ввести желаемый угол поворота в градусах в поле "Градусы". Положительные значения вращают текст против часовой стрелки, а отрицательные - по часовой.
<br>
![todo:image_alt_text](alignment.png)
1. После выбора желаемого угла поворота нажмите "OK", чтобы применить изменения. Выбранные ячейки теперь будут повернуты в соответствии с выбранным углом поворота или ориентацией.

## **Как вращать текст ячейки с использованием API Aspose.Cells**

Свойство [**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) упрощает вращение ячеек. Чтобы вращать ячейки в Aspose.Cells, вам нужно выполнить следующие шаги:
1. Загрузите книгу Excel
<br>
Сначала вам нужно загрузить книгу Excel с помощью Aspose.Cells. Вы можете использовать класс Workbook для открытия существующего файла Excel или создания нового. 

1. Получите доступ к листу
<br>
После загрузки книги вам нужно получить доступ к листу, на котором вы хотите повернуть ячейки. Вы можете получить доступ к листу по его индексу или имени. 

1. Поверните текст ячейки
<br>
Теперь, когда у вас есть доступ к листу, вы можете повернуть ячейки, модифицируя объект Style нужных ячеек. Объект Style позволяет устанавливать различные варианты форматирования, включая вращение. 

1. Сохраните книгу
<br>
После вращения ячеек вы можете сохранить измененную книгу обратно в файл или поток, используя метод Save.

## **Пример кода на C++**

Пожалуйста, ознакомьтесь с приведенным ниже кодом, он создает объект книги и задает различные углы вращения для нескольких ячеек. На снимке экрана показан результат выполнения примера кода.
<br>
<img src="rotation.png" width=80% />

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
