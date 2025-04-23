---
title: Настройки шрифта
description: Aspose.Cells  это .NET библиотека для работы с файлами электронных таблиц. Она поддерживает настройку шрифтов ячеек, позволяя пользователям настраивать стиль и свойства шрифта ячеек. В этой статье будет рассмотрено, как использовать библиотеку Aspose.Cells для настройки шрифта ячейки.
keywords: Aspose.Cells, Ячейки, Настройки шрифта, Стили, Свойства
type: docs
weight: 30
url: /ru/net/cells-font-settings/
---

{{% alert color="primary" %}}

Внешний вид и ощущение текста могут быть управляемыми путем изменения настроек шрифта. Настройки шрифта могут включать имя, стиль, размер, цвет и другие эффекты шрифтов. Как и Microsoft Excel, Aspose.Cells также поддерживает настройку шрифта ячеек.

{{% /alert %}}

## **Настройка настроек шрифта**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells предоставляет методы класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) для получения и установки стиля форматирования ячейки. Класс [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) предоставляет свойства для настройки настроек шрифта.

### **Установка названия шрифта**

Разработчики могут применить любой шрифт к тексту внутри ячейки, используя свойство [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Установка стиля шрифта на жирный**

Разработчики могут сделать текст жирным, установив свойство [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) в **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Установка размера шрифта**

Установите размер шрифта с помощью свойства [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Установка цвета шрифта**

Используйте свойство [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) для установки цвета шрифта. Выберите любой цвет из перечисления Color (часть .NET framework) и присвойте его свойству [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Установка типа подчеркивания шрифта**

Используйте свойство [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) для подчеркивания текста. Aspose.Cells предлагает различные предопределенные типы шрифтов в перечислении [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype).

|**Типы подчеркивания шрифта**|**Описание**|
| :- | :- |
|Accounting| Одиночная линия подчеркивания для учета
|Double| Двойное подчеркивание
|DoubleAccounting| Двойная линия подчеркивания для учета
|None| Без подчеркивания
|Single| Одиночная линия подчеркивания

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Установка эффекта зачеркивания**

Примените зачеркивание, установив свойство [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) в **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Установка эффекта нижнего индекса**

Примените нижний индекс, установив свойство [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) в **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Установка верхнего индекса на шрифт**

Разработчики могут применить эффект верхнего индекса к шрифту, установив свойство [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) объекта [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) в **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Продвинутые темы**
- [Применить эффект верхнего и нижнего индекса к шрифтам](/cells/ru/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Получение списка используемых шрифтов в электронной таблице или книге](/cells/ru/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

{{< app/cells/assistant language="csharp" >}}
