---
title: Настройки чисел
description: Aspose.Cells — это библиотека Python для работы с файлами электронных таблиц, поддерживающая множество настроек чисел в ячейках. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для управления числовыми настройками ячеек, чтобы пользователи могли при необходимости изменять формат чисел в таблице.
keywords: Aspose.Cells, библиотека Python, электронная таблица, настройки чисел в ячейках, форматирование, управление, Форматы чисел и дат
type: docs
weight: 10
url: /ru/python-net/cells-number-settings/
---

## **Как установить отображаемые форматы чисел и дат**

Одной из важнейших особенностей Microsoft Excel является возможность установки отображаемых форматов числовых значений и дат. Мы знаем, что числовые данные могут использоваться для представления различных значений, включая десятичные, валютные, процентные, дробные или бухгалтерские значения и т. д. Все эти числовые значения отображаются в различных форматах в зависимости от типа информации, которую они представляют. Аналогично, существует множество форматов, в которых дата или время могут быть отображены.
Aspose.Cells для Python via .NET поддерживает эту функциональность и позволяет разработчикам задавать любой отображаемый формат для числа или даты.

### **Как установить отображаемые форматы в Microsoft Excel**

Чтобы установить отображаемые форматы в Microsoft Excel:

1. Щелкните правой кнопкой мыши любую ячейку.
1. Выберите **Формат ячеек**. Появится диалоговое окно, которое используется для установки отображаемых форматов любого вида значений.

На левой стороне диалога расположено множество категорий значений, таких как **Общие**, **Число**, **Деньги**, **Бухгалтерия**, **Дата**, **Время**, **Процент** и др. Aspose.Cells для Python via .NET поддерживает все эти форматы отображения.

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Каждый элемент в коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells для Python via .NET предоставляет методы [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) и [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) для класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Эти методы используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) предоставляет некоторые полезные свойства для работы с форматами отображения чисел и дат.

### **Как использовать встроенные форматы чисел**

Aspose.Cells для Python via .NET предлагает встроенные форматы чисел для настройки отображения чисел и дат. Эти встроенные форматы можно применять с помощью свойства [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Все встроенные форматы чисел имеют уникальные числовые значения. Разработчики могут присвоить любое желаемое числовое значение свойству [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) для применения формата отображения. Этот подход быстрый. Ниже перечислены поддерживаемые Aspose.Cells встроенные числовые форматы.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **Как использовать пользовательские форматы чисел**

Чтобы определить свою собственную настраиваемую строку формата для установки отображаемого формата, используйте свойство [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) объекта [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Этот подход не так быстр, как использование заранее установленных форматов, но он более гибкий.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

Если вы используете свойство [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) для установки числового формата, любой предыдущий формат, установленный с использованием свойства [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number), переопределяется и наоборот.

{{% /alert %}}

## **Продвинутые темы**
- [Проверьте Пользовательский числовой формат при установке Свойства Custom.](/cells/ru/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [Список поддерживаемых форматов чисел](/cells/ru/python-net/list-of-supported-number-formats/)
- [Отображение пользовательского формата даты Шаблон g и ge mm dd](/cells/ru/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Укажите пользовательские разделители десятичных и групповых чисел для рабочей книги](/cells/ru/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Указание форматирования собственного шаблона DBNum](/cells/ru/python-net/specifying-dbnum-custom-pattern-formatting/)

{{< app/cells/assistant language="python-net" >}}
