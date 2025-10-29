---
title: Настройки номера с C++
linktitle: Настройки чисел
description: Aspose.Cells — это библиотека на C++, для работы с файлами электронных таблиц, поддерживающая множество различных настроек чисел в ячейках. В этой статье будет рассмотрено, как использовать библиотеку Aspose.Cells для управления настройками чисел в ячейках, чтобы пользователи могли при необходимости изменять формат чисел в таблице.
keywords: Aspose.Cells, библиотека C++, электронная таблица, настройки чисел ячеек, форматирование, управление, Форматы чисел и дат
type: docs
weight: 10
url: /ru/cpp/cells-number-settings/
---

## **Как установить отображаемые форматы чисел и дат**

Одной из важнейших особенностей Microsoft Excel является возможность установки отображаемых форматов числовых значений и дат. Мы знаем, что числовые данные могут использоваться для представления различных значений, включая десятичные, валютные, процентные, дробные или бухгалтерские значения и т. д. Все эти числовые значения отображаются в различных форматах в зависимости от типа информации, которую они представляют. Аналогично, существует множество форматов, в которых дата или время могут быть отображены.
Aspose.Cells поддерживает эту функциональность и позволяет разработчикам устанавливать отображаемый формат для числа или даты.

### **Как установить отображаемые форматы в Microsoft Excel**

Чтобы установить отображаемые форматы в Microsoft Excel:

1. Щелкните правой кнопкой мыши любую ячейку.
1. Выберите **Формат ячеек**. Появится диалоговое окно, которое используется для установки отображаемых форматов любого вида значений.

На левой стороне диалогового окна есть множество категорий значений, таких как **Общее**, **Число**, **Валюта**, **Бухгалтерский учет**, **Дата**, **Время**, **Процент**, и т. д. Aspose.Cells поддерживает все эти отображаемые форматы.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу Excel-файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells предоставляет методы [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) и [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Эти методы используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) предоставляет некоторые полезные свойства для работы с отображаемыми форматами чисел и дат.

### **Как использовать встроенные форматы чисел**

Aspose.Cells предлагает некоторые встроенные форматы чисел для настройки отображаемых форматов чисел и дат. Эти встроенные форматы чисел могут быть применены с использованием свойства [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Все встроенные форматы чисел имеют уникальные числовые значения. Разработчики могут назначить любое желаемое числовое значение свойству [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/), чтобы применить отображаемый формат. Этот подход быстр. Встроенные форматы чисел, поддерживаемые Aspose.Cells, перечислены ниже.

|**Значение**|**Тип**|**Строка формата**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::time_t now = std::time(nullptr);
    double excelDate = static_cast<double>(now) / 86400.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetNumber(15);
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetNumber(9);
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetNumber(6);
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как использовать пользовательские форматы чисел**

Чтобы определить свою собственную настраиваемую строку формата для установки отображаемого формата, используйте свойство [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) объекта [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Этот подход не так быстр, как использование заранее установленных форматов, но он более гибкий.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    auto hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    double excelDate = hours / 24.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetCustom(u"d-mmm-yy");
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetCustom(u"0.0%");
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetCustom(u"£#,##0;[Red]$-#,##0");
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Если вы используете свойство [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) для установки числового формата, любой предыдущий формат, установленный с использованием свойства [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/), переопределяется и наоборот.

{{% /alert %}}

## **Продвинутые темы**
- [Проверьте Пользовательский числовой формат при установке Свойства Custom.](/cells/ru/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [Список поддерживаемых форматов чисел](/cells/ru/cpp/list-of-supported-number-formats/)
- [Отображение пользовательского формата даты Шаблон g и ge mm dd](/cells/ru/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Укажите пользовательские разделители десятичных и групповых чисел для рабочей книги](/cells/ru/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Указание форматирования собственного шаблона DBNum](/cells/ru/cpp/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="cpp" >}}
