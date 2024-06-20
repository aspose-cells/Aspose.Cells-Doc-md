---
title: Настройки чисел
description: Aspose.Cells  это библиотека .NET для работы с файлами электронных таблиц, которая поддерживает множество различных настроек чисел в ячейках. В этой статье будет рассмотрено, как использовать библиотеку Aspose.Cells для управления настройками чисел в ячейках, чтобы пользователи могли настраивать числовой формат в электронной таблице по мере необходимости.
keywords: Aspose.Cells, библиотека .NET, электронные таблицы, настройки чисел в ячейках, форматирование, управление, форматы чисел и дат
type: docs
weight: 10
url: /ru/net/cells-number-settings/
---

## **Как установить отображаемые форматы чисел и дат**

Одной из важнейших особенностей Microsoft Excel является возможность установки отображаемых форматов числовых значений и дат. Мы знаем, что числовые данные могут использоваться для представления различных значений, включая десятичные, валютные, процентные, дробные или бухгалтерские значения и т. д. Все эти числовые значения отображаются в различных форматах в зависимости от типа информации, которую они представляют. Аналогично, существует множество форматов, в которых дата или время могут быть отображены.
Aspose.Cells поддерживает эту функциональность и позволяет разработчикам устанавливать отображаемый формат для числа или даты.

### **Как установить отображаемые форматы в Microsoft Excel**

Чтобы установить отображаемые форматы в Microsoft Excel:

1. Щелкните правой кнопкой мыши любую ячейку.
1. Выберите **Формат ячеек**. Появится диалоговое окно, которое используется для установки отображаемых форматов любого вида значений.

На левой стороне диалогового окна есть множество категорий значений, таких как **Общее**, **Число**, **Валюта**, **Бухгалтерский учет**, **Дата**, **Время**, **Процент**, и т. д. Aspose.Cells поддерживает все эти отображаемые форматы.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу Excel-файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells предоставляет методы [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Эти методы используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) предоставляет некоторые полезные свойства для работы с отображаемыми форматами чисел и дат.

### **Как использовать встроенные форматы чисел**

Aspose.Cells предлагает некоторые встроенные форматы чисел для настройки отображаемых форматов чисел и дат. Эти встроенные форматы чисел могут быть применены с использованием свойства [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Все встроенные форматы чисел имеют уникальные числовые значения. Разработчики могут назначить любое желаемое числовое значение свойству [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style), чтобы применить отображаемый формат. Этот подход быстр. Встроенные форматы чисел, поддерживаемые Aspose.Cells, перечислены ниже.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **Как использовать пользовательские форматы чисел**

Чтобы определить свою собственную настраиваемую строку формата для установки отображаемого формата, используйте свойство [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) объекта [**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom). Этот подход не так быстр, как использование заранее установленных форматов, но он более гибкий.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

Если вы используете свойство [**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) для установки числового формата, любой предыдущий формат, установленный с использованием свойства [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number), переопределяется и наоборот.

{{% /alert %}}

## **Продвинутые темы**
- [Проверьте Пользовательский числовой формат при установке Свойства Custom.](/cells/ru/net/check-custom-number-format-when-setting-style-custom-property/)
- [Список поддерживаемых форматов чисел](/cells/ru/net/list-of-supported-number-formats/)
- [Отображение пользовательского формата даты Шаблон g и ge mm dd](/cells/ru/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Укажите пользовательские разделители десятичных и групповых чисел для рабочей книги](/cells/ru/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Указание форматирования собственного шаблона DBNum](/cells/ru/net/specifying-dbnum-custom-pattern-formatting/)
