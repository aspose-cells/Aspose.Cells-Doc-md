---
title: Настройки номера
type: docs
weight: 10
url: /ru/net/cells-number-settings/
---
## **Настройка форматов отображения Numbers и дат**

Очень сильной стороной Microsoft Excel является то, что он позволяет пользователям устанавливать форматы отображения числовых значений и дат. Мы знаем, что числовые данные могут использоваться для представления различных значений, включая десятичные, денежные, процентные, дробные или бухгалтерские значения и т. д. Все эти числовые значения отображаются в разных форматах в зависимости от типа информации, которую они представляют. Точно так же существует множество форматов, в которых может отображаться дата или время.
Aspose.Cells поддерживает эту функцию и позволяет разработчикам устанавливать любой формат отображения числа или даты.

### **Настройка форматов отображения в Microsoft Excel**

Чтобы установить форматы отображения в Microsoft Excel:

1. Щелкните правой кнопкой мыши любую ячейку.
1.  Выбирать**Формат Cells**. Появится диалоговое окно, которое используется для установки форматов отображения любых значений.

 В левой части диалогового окна есть много категорий значений, таких как**Общий**, **Число**, **Валюта**, **Бухгалтерский учет**, **Датировать**, **Время**, **Процент,**и т. д. Aspose.Cells поддерживает все эти форматы отображения.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.

 Aspose.Cells предоставляет[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) методы для[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс. Эти методы используются для получения и установки форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)class предоставляет некоторые полезные свойства для работы с форматами отображения чисел и дат.

### **Использование встроенных числовых форматов**

 Aspose.Cells предлагает несколько встроенных форматов чисел для настройки форматов отображения чисел и дат. Эти встроенные числовые форматы можно применять с помощью[**Число**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) собственность[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объект. Всем встроенным числовым форматам присваиваются уникальные числовые значения. Разработчики могут присвоить любое желаемое числовое значение[**Число**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) собственность[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект для применения формата отображения. Этот подход быстрый. Ниже перечислены встроенные числовые форматы, поддерживаемые Aspose.Cells.

|**Стоимость**|**Тип**|**Строка формата**|
|:- |:- |:- |
|0|Общий|Общий|
|1|Десятичный|0|
|2|Десятичный|0.00|
|3|Десятичный|# ,##0
|
|4|Десятичный|# ,##0.00
|
|5|Валюта|$#,##0;$-#,##0|
|6|Валюта|$#,##0;[Красный]$-#,##0|
|7|Валюта|$#,##0.00;$-#,##0.00|
|8|Валюта|$#,##0.00;[Красный]$-#,##0.00|
|9|Процент|0%|
|10|Процент|0.00%|
|11|Научный|0.00E+00|
|12|Доля|# ?/?
|
|13|Доля|# */*
|
|14|Датировать|м/д/гг|
|15|Датировать|д-ммм-гг|
|16|Датировать|д-ммм|
|17|Датировать|ммм-гг|
|18|Время|ч:мм AM/PM|
|19|Время|ч:мм:сс AM/PM|
|20|Время|хм|
|21|Время|ч:мм:сс|
|22|Время|м/д/гг ч:мм|
|37|Валюта|# ,##0;-#,##0
|
|38|Валюта|# ,##0;[Красный]-#,##0
|
|39|Валюта|# ,##0.00;-#,##0.00
|
|40|Валюта|# ,##0.00;[Красный]-#,##0.00
|
|41|Бухгалтерский учет|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Бухгалтерский учет|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Бухгалтерский учет|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Бухгалтерский учет|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Время|мм:сс|
|46|Время|ч:мм:сс|
|47|Время|мм:сс.0|
|48|Научный|## 0.0E+00
|
|49|Текст|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **Использование пользовательских числовых форматов**

Чтобы определить собственную строку пользовательского формата для настройки формата отображения, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Обычай**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)имущество. Этот подход не такой быстрый, как использование предустановленных форматов, но он более гибкий.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Если вы используете[**Обычай**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) свойство, чтобы установить числовой формат, любой предыдущий формат, установленный с помощью[**Число**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)свойство переопределяется и наоборот.

{{% /alert %}}

## **Предварительные темы**
- [Проверьте пользовательский числовой формат при настройке свойства Style.Custom](/cells/ru/net/check-custom-number-format-when-setting-style-custom-property/)
- [Список поддерживаемых числовых форматов](/cells/ru/net/list-of-supported-number-formats/)
- [Рендеринг шаблона пользовательского формата даты g и ge mm dd](/cells/ru/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Укажите пользовательские десятичные числа и разделители групп для книги](/cells/ru/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Указание форматирования пользовательского шаблона DBNum](/cells/ru/net/specifying-dbnum-custom-pattern-formatting/)
