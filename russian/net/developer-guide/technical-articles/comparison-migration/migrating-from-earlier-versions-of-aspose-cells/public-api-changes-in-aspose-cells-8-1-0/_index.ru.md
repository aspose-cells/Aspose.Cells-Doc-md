---
title: Изменения в общедоступном API в Aspose.Cells 8.1.0
type: docs
weight: 40
url: /ru/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.0.2 до 8.1.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство HtmlSaveOptions.ExportHiddenWorksheet**
Класс HtmlSaveOptions имеет свойство ExportHiddenWorksheet, которое можно использовать для указания, будут ли скрытые листы экспортированы в формат HTML. Значение по умолчанию - true, тогда как если установлено false, Aspose.Cells не будет экспортировать содержимое скрытого листа.

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с подробной статьей по адресу [Предотвращение экспорта скрытого листа](/cells/ru/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Добавлено свойство Cell.StringValueWithoutFormat**
Добавлено свойство StringValueWithoutFormat в класс Cell, чтобы облегчить разработчикам получение значения ячейки без применения любого форматирования.

Приведенный ниже фрагмент кода демонстрирует использование свойства Cell.StringValueWithoutFormat по сравнению с cell.DisplayStringValue, создавая электронную таблицу с нуля и применяя числовой формат к одной из ячеек.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Результат работы вышеуказанного кода следующий

123,456

123456

{{% /alert %}}
## **Отмечены свойства Obsoleted Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs**
Многие свойства из класса BuiltInDocumentPropertyCollection были помечены как устаревшие, начиная с Aspose.Cells for .NET 8.1.0. К таким свойствам относятся Bytes, Characters, CharactersWithSpaces, Lines и Paragraphs. Причина заключается в том, что вышеперечисленные свойства не используются для сохранения электронных таблиц Excel, поскольку Excel их опускает. В то время как эти свойства были изначально написаны для документов Word и презентаций PowerPoint.
{{< app/cells/assistant language="csharp" >}}
