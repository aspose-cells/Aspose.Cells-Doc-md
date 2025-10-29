---
title: Настройки шрифта с Golang через C++
linktitle: Настройки шрифта
type: docs
weight: 30
url: /ru/go-cpp/cells-font-settings/
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает установку настроек шрифта ячеек, позволяя пользователям настраивать стиль и свойства шрифта. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для установки настроек шрифта ячеек.
keywords: Aspose.Cells, Ячейки, Настройки шрифта, Стили, Свойства
---

{{% alert color="primary" %}}

 Внешний вид текста можно контролировать, изменяя настройки шрифта. Настройки могут включать имя, стиль, размер, цвет и другие эффекты шрифта. Так же как в Microsoft Excel, Aspose.Cells поддерживает настройку шрифтов ячеек.

{{% /alert %}}

## **Настройка настроек шрифта**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Каждый элемент в коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells предоставляет методы класса [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) для получения и установки стиля форматирования ячейки. Класс [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) предоставляет свойства для настройки настроек шрифта.

### **Установка названия шрифта**

 Разработчики могут применять любой шрифт к тексту внутри ячейки, используя свойство [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **Установка стиля шрифта на жирный**

Разработчики могут сделать текст жирным, установив свойство [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) в **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **Установка размера шрифта**

Установите размер шрифта с помощью свойства [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **Установка цвета шрифта**

 Используйте свойство [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) для установки цвета шрифта. Выберите любой цвет из перечисления Color (часть C++ фреймворка) и присвойте его свойству [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **Установка типа подчеркивания шрифта**

Используйте свойство [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) для подчеркивания текста. Aspose.Cells предлагает различные предопределенные типы шрифтов в перечислении [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/).

|**Типы подчеркивания шрифта**|**Описание**|
| :- | :- |
|Accounting| Одиночная линия подчеркивания для учета
|Double| Двойное подчеркивание
|DoubleAccounting| Двойная линия подчеркивания для учета
|None| Без подчеркивания
|Single| Одиночная линия подчеркивания

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **Установка эффекта зачеркивания**

Примените зачеркивание, установив свойство [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) в **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **Установка эффекта нижнего индекса**

Примените нижний индекс, установив свойство [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) в **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **Установка верхнего индекса на шрифт**

Разработчики могут применить эффект верхнего индекса к шрифту, установив свойство [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) в **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **Продвинутые темы**
- [Применить эффект верхнего и нижнего индекса к шрифтам](/cells/ru/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Получение списка используемых шрифтов в электронной таблице или книге](/cells/ru/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
