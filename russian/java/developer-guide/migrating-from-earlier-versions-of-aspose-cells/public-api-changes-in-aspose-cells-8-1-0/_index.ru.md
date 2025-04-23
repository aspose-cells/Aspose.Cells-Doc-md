---
title: Изменения в общедоступном API в Aspose.Cells 8.1.0
type: docs
weight: 50
url: /ru/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.0.2 до 8.1.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство HtmlSaveOptions.ExportHiddenWorksheet**
Класс HtmlSaveOptions имеет свойство ExportHiddenWorksheet, которое можно использовать для указания, будут ли скрытые листы экспортированы в формат HTML. Значение по умолчанию - true, тогда как если установлено false, Aspose.Cells не будет экспортировать содержимое скрытого листа.

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со подробной статьей по теме [Предотвращение экспорта скрытого листа](/cells/ru/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Добавлено свойство Cell.StringValueWithoutFormat**
Добавлено свойство StringValueWithoutFormat в класс Cell, чтобы облегчить разработчикам получение значения ячейки без применения любого форматирования. 

Ниже предоставлен фрагмент кода, демонстрирующий использование метода Cell.getStringValueWithoutFormat по сравнению с методом cell.getDisplayStringValue путем создания электронной таблицы с нуля и применения числового формата к одной из ячеек. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Результат работы вышеуказанного кода следующий

Форматированное строковое значение: 123,456
Неформатированное строковое значение: 123456

{{% /alert %}}
## **Отмечены свойства Obsoleted Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs**
Многие свойства из класса BuiltInDocumentPropertyCollection были помечены как устаревшие, начиная с Aspose.Cells for .NET 8.1.0. К таким свойствам относятся Bytes, Characters, CharactersWithSpaces, Lines и Paragraphs. Причина заключается в том, что вышеперечисленные свойства не используются для сохранения электронных таблиц Excel, поскольку Excel их опускает. В то время как эти свойства были изначально написаны для документов Word и презентаций PowerPoint. 
{{< app/cells/assistant language="java" >}}
