---
title: Настройки шрифта
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц. Он поддерживает настройку параметров шрифта ячеек, позволяя пользователям настраивать стиль шрифта и свойства ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для установки настроек шрифта ячейки.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /ru/net/cells-font-settings/
---
{{% alert color="primary" %}}

Внешний вид текста можно контролировать, изменяя настройки шрифта. Настройки шрифта могут включать имя, стиль, размер, цвет и другие эффекты шрифтов. Как и Microsoft Excel, Aspose.Cells также поддерживает настройку шрифта ячеек.

{{% /alert %}}

##  **Настройка параметров шрифта**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

 Aspose.Cells обеспечивает[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) методы, которые используются для получения и установки стиля форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет свойства для настройки параметров шрифта.

###  **Установка имени шрифта**

 Разработчики могут применять любой шрифт к тексту внутри ячейки, используя[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) объекты[Имя](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **Установка стиля шрифта на полужирный**

 Разработчики могут сделать текст жирным, установив[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) объекты[**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)свойство в *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **Настройка размера шрифта**

Установите размер шрифта с помощью[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)объекты[**Размер**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **Настройка цвета шрифта**

Использовать[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) объекты[**Цвет**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)свойство для установки цвета шрифта. Выберите любой цвет из перечисления Цвет (часть структуры .NET) и назначьте его[**Цвет**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **Настройка типа подчеркивания шрифта**

Использовать[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)объекты[**Подчеркнуть**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)свойство подчеркивать текст. Aspose.Cells предлагает различные предопределенные типы подчеркивания шрифта в[**ШрифтUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) перечисление.

|**Типы подчеркивания шрифта**|**Описание**|
| :- | :- |
|Бухгалтерский учет|Единое бухгалтерское подчеркивание|
|Двойной|Двойное подчеркивание|
|Двойной учет|Двойное учетное подчеркивание|
|Никто|Без подчеркивания|
|Одинокий|Одно подчеркивание|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **Настройка эффекта вычеркивания**

Примените зачеркивание, установив[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) объекты[**Исчеркаут**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)свойство в *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **Настройка эффекта индекса**

Примените нижний индекс, установив[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)объекты[**Иссубскрипт**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)свойство в *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **Настройка эффекта надстрочного индекса для шрифта**

 Разработчики могут применить к шрифту эффект надстрочного индекса, установив параметр[**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) собственность[**Стиль.Шрифт**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)возражать против *истины**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **Предварительные темы**
- [Применение эффектов надстрочного и подстрочного индекса к шрифтам](/cells/ru/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Получите список шрифтов, используемых в электронной таблице или книге.](/cells/ru/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

