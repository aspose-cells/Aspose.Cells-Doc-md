---
title: Настройки номера
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц, которая поддерживает множество различных настроек номеров ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для управления параметрами числа ячеек, чтобы пользователи могли при необходимости настраивать числовой формат в электронной таблице.
keywords: Aspose.Cells, .NET library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /ru/net/cells-number-settings/
---
##  **Как установить форматы отображения Numbers и дат**

Очень сильной особенностью Microsoft Excel является то, что он позволяет пользователям устанавливать форматы отображения числовых значений и дат. Мы знаем, что числовые данные могут использоваться для представления различных значений, включая десятичные, денежные, процентные, дробные или учетные значения и т. д. Все эти числовые значения отображаются в разных форматах в зависимости от типа информации, которую они представляют. Аналогично, существует множество форматов отображения даты и времени.
Aspose.Cells поддерживает эту функциональность и позволяет разработчикам устанавливать любой формат отображения числа или даты.

###  **Как установить форматы отображения в Microsoft Excel**

Чтобы установить форматы отображения в Microsoft Excel:

1. Щелкните правой кнопкой мыши любую ячейку.
1. Выберите *Формат Cells**. Появится диалог, который используется для установки форматов отображения любого вида значений.

 В левой части диалогового окна есть множество категорий значений, например**Общие**, **Число**, **Валюта**, **Учет**, **Дата**, **Время**, **Процент,**и т. д. Aspose.Cells поддерживает все эти форматы отображения.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

 Aspose.Cells обеспечивает[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) методы для[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) сорт. Эти методы используются для получения и установки форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет некоторые полезные свойства для работы с форматами отображения чисел и дат.

###  **Как использовать встроенные числовые форматы**

 Aspose.Cells предлагает несколько встроенных числовых форматов для настройки форматов отображения чисел и дат. Эти встроенные числовые форматы можно применять с помощью[**Число**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) собственность[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объект. Всем встроенным числовым форматам присваиваются уникальные числовые значения. Разработчики могут присвоить любому желаемому числовому значению[**Число**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) собственность[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)объект для применения формата отображения. Этот подход быстрый. Ниже перечислены встроенные числовые форматы, поддерживаемые Aspose.Cells.

|**Ценить**|**Тип**|**Форматировать строку**|
| :- | :- | :- |
|0|General|Общий|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Красный]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Красный]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|м/д/гггг|
|15|Date|д-ммм-гг|
|16|Date|д-ммм|
|17|Date|ммм-гг|
|18|Time|ч:мм до полудня/после полудня|
|19|Time|ч:мм:сс AM/PM|
|20|Time|хм|
|21|Time|ч:мм:сс|
|22|Time|м/д/гг ч:мм|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[Красный]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[Красный]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|мм:сс|
|46|Time|ч :мм:сс|
|47|Time|мм:сс.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

###  **Как использовать пользовательские числовые форматы**

 Чтобы определить собственную строку формата для настройки формата отображения, используйте команду[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Обычай**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)свойство. Этот подход не такой быстрый, как использование предустановленных форматов, но он более гибкий.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Если вы используете[**Обычай**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) свойство для установки числового формата, любой предыдущий формат, установленный с помощью[**Число**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)свойство переопределяется и наоборот.

{{% /alert %}}

##  **Предварительные темы**
- [Проверьте формат произвольного номера при настройке свойства Style.Custom](/cells/ru/net/check-custom-number-format-when-setting-style-custom-property/)
- [Список поддерживаемых числовых форматов](/cells/ru/net/list-of-supported-number-formats/)
- [Визуализация пользовательского формата даты Шаблон g и ge мм дд](/cells/ru/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Укажите пользовательские десятичные числа и разделители групп для книги](/cells/ru/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Указание пользовательского форматирования шаблона DBNum](/cells/ru/net/specifying-dbnum-custom-pattern-formatting/)
