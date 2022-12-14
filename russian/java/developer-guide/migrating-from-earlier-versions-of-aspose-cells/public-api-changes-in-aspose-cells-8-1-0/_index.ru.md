---
title: Общедоступный API Изменения в Aspose.Cells 8.1.0
type: docs
weight: 50
url: /ru/java/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.0.2 до 8.1.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство HtmlSaveOptions.ExportHiddenWorksheet.**
Класс HtmlSaveOptions предоставляет свойство ExportHiddenWorksheet, которое можно использовать для указания, экспортируются ли скрытые рабочие листы в формат HTML. Значение по умолчанию верно. тогда как если установлено значение false, Aspose.Cells не будет экспортировать скрытое содержимое рабочего листа.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Запретить экспорт скрытого рабочего листа](/cells/ru/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Добавлено свойство Cell.StringValueWithoutFormat.**
 Свойство StringValueWithoutFormat было добавлено в класс Cell, чтобы облегчить разработчикам извлечение значения ячейки без применения форматирования.

Приведенный ниже фрагмент кода демонстрирует использование метода Cell.getStringValueWithoutFormat по сравнению с cell.getDisplayStringValue путем создания электронной таблицы с нуля и применения числового формата к одной из ячеек.

**Java**

{{< highlight "csharp" >}}

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

Вывод приведенного выше кода выглядит следующим образом

Форматированное строковое значение: 123 456
Неформатированное строковое значение: 123456

{{% /alert %}}
## **Устаревшие байты, символы, символы с пробелами, строки, свойства абзацев**
 Начиная с Aspose.Cells for .NET 8.1.0, многие свойства из класса BuiltInDocumentPropertyCollection помечены как устаревшие. Эти свойства включают байты, символы, символы с пробелами, строки и абзацы. Причина в том, что вышеупомянутые свойства бесполезны для сохранения электронных таблиц Excel, потому что Excel их опускает. Хотя эти свойства изначально были написаны для документов Word и PowerPoint презентаций.
