---
title: Настройки шрифта
description: Aspose.Cells — это библиотека Python для работы с файлами электронных таблиц. Она поддерживает установку шрифтовых настроек ячеек, позволяя пользователям настраивать стиль и свойства шрифта ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для Python via .NET для установки настроек шрифта ячеек.
keywords: Aspose.Cells для Python via .NET, Ячейки, Настройки шрифтов, Стили, Свойства
type: docs
weight: 30
url: /ru/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

Внешний вид и ощущение текста можно контролировать, изменяя настройки шрифта. Настройки шрифтов могут включать имя, стиль, размер, цвет и другие эффекты шрифта. Как и в Microsoft Excel, Aspose.Cells для Python via .NET также поддерживает настройку шрифтовых свойств ячеек.

{{% /alert %}}

## **Настройка настроек шрифта**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая обеспечивает доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Каждый элемент коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells предоставляет методы класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) для получения и установки стиля форматирования ячейки. Класс [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) предоставляет свойства для настройки настроек шрифта.

### **Установка названия шрифта**

Разработчики могут применять любой шрифт к тексту внутри ячейки, используя свойство [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **Установка стиля шрифта на жирный**

Разработчики могут сделать текст жирным, установив свойство [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) в **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **Установка размера шрифта**

Установите размер шрифта с помощью свойства [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **Установка цвета шрифта**

Используйте свойство [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) для установки цвета шрифта. Выберите любой цвет из перечисления Color (часть .NET framework) и присвойте его свойству [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **Установка типа подчеркивания шрифта**

Используйте свойство [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font), чтобы подчеркнуть текст. Aspose.Cells для Python via .NET предлагает различные предопределённые типы подчеркивания шрифта в перечислении [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype).

|**Типы подчеркивания шрифта**|**Описание**|
| :- | :- |
|БЮЛЛЕТЕНИЙ|Одинарное подчеркивание бухгалтерии|
|ДВОЙНОЕ|Двойное подчеркивание|
|ДВОЙНОЕ_БЮЛЛЕТЕНИЕ|Двойное бухгалтерское подчеркивание|
|НИЧЕГО|Без подчеркивания|
|ОДИНАРНОЕ|Одно подчеркивание|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **Установка эффекта зачеркивания**

Примените зачеркивание, установив свойство [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) в **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **Установка эффекта нижнего индекса**

Примените нижний индекс, установив свойство [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) в **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **Установка верхнего индекса на шрифт**

Разработчики могут применить эффект верхнего индекса к шрифту, установив свойство [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) объекта [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) в **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **Продвинутые темы**
- [Применить эффект верхнего и нижнего индекса к шрифтам](/cells/ru/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Получение списка используемых шрифтов в электронной таблице или книге](/cells/ru/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


