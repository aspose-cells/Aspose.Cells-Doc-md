---
title: Как масштабировать лист с помощью C++
linktitle: Как масштабировать лист
type: docs
weight: 130
url: /ru/cpp/how-to-scale-a-worksheet/
description: Эта статья показывает код, объясняющий, как масштабировать лист с помощью библиотеки Aspose.Cells на C++.
keywords: Масштабирование листа в C++, как масштабировать лист с помощью C++, масштабировать лист в C++.
---

## **Возможные сценарии использования**
Масштабирование листа может быть полезно по разным причинам, в зависимости от контекста работы. Вот несколько распространенных причин масштабирования листа:
1. Вписать в страницу: чтобы обеспечить умещание всего содержимого на одной странице или заданном количестве страниц при печати, облегчая чтение и управление без необходимости пролистывать несколько страниц.

1. Презентация: чтобы сделать лист более организованным и профессиональным, особенно при совместном использовании в заседаниях или отчетах.

1. Читаемость: чтобы настроить размер текста и других элементов для лучшей читаемости, особенно для людей с проблемами восприятия мелкого шрифта.

1. Управление пространством: чтобы оптимизировать использование пространства на листе, исключая ненужное пустое пространство и обеспечивая видимость всей важной информации без чрезмерной прокрутки.

1. Визуализация данных: для диаграмм и графиков масштаб может помочь сделать их более понятными, корректируя размер для соответствия доступному пространству.

1. Последовательность: чтобы поддерживать единый стиль и ощущение во многих листах или документах, что особенно важно в профессиональной и образовательной среде.

## **Как масштабировать лист в Excel**
Масштабирование листа в Excel помогает поместить содержимое на одну страницу или заданное количество страниц при печати. Вот шаги для масштабирования листа:

1. Откройте свой лист: откройте Excel-таблицу, которую хотите масштабировать.

1. Перейдите на вкладку Макет страницы: нажмите на вкладку Макет страницы в ленте.

1. Группа Масштаб для подгонки: в разделе Макет страницы найдите группу Масштаб для подгонки. Здесь есть параметры для регулировки масштабирования. Ширина: позволяет указать, сколько страниц по ширине будет занимать печатанный лист. Высота: позволяет указать, сколько страниц по высоте будет занимать печатанный лист. Масштаб: можно также установить пользовательский процент масштабирования.
<br>
<img src="1.png" width=60% />

1. Настройка ширины и высоты: задайте желаемое количество страниц по ширине и высоте. Например, оба по 1 странице, если хотите, чтобы лист помещался на одной странице.

1. Настройка процента масштабирования (при необходимости): если предпочитаете задать конкретный процент масштабирования, настройте поле Масштаб. Например, установка на 50% сделает всё в два раза меньше.


## **Как масштабировать лист с помощью C++**
Aspose.Cells — мощная библиотека для работы с файлами Excel программным путем. Чтобы масштабировать лист с помощью Aspose.Cells, выполните следующие шаги: загрузите [пример файла](sample.xlsx) и настройте параметры печати так, чтобы содержимое поместилось нужное количество страниц или определенный процент от первоначального размера.

### **Пример: Подгонка под страницу**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the worksheet to fit to 1 page wide and 1 page tall
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the modified workbook
    workbook.Save(u"output_fit_to_page.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
<br>
<img src="3.png" width=60% />

### **Пример: Масштабирование в процентное соотношение**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the scaling to a specific percentage (e.g., 75%)
    pageSetup.SetZoom(75);

    // Save the modified workbook
    workbook.Save(u"output_scaled_percentage.xlsx");

    // Clean up Aspose.Cells resources
    Aspose::Cells::Cleanup();

    return 0;
}
```
<br>
<img src="2.png" width=60% />
