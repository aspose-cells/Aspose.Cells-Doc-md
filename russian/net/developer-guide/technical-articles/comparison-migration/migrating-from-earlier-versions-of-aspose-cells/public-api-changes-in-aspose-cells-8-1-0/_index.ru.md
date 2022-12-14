---
title: Общедоступный API Изменения в Aspose.Cells 8.1.0
type: docs
weight: 40
url: /ru/net/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.0.2 до 8.1.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство HtmlSaveOptions.ExportHiddenWorksheet.**
Класс HtmlSaveOptions предоставляет свойство ExportHiddenWorksheet, которое можно использовать для указания, экспортируются ли скрытые рабочие листы в формат HTML. Значение по умолчанию верно. тогда как если установлено значение false, Aspose.Cells не будет экспортировать скрытое содержимое рабочего листа.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Запретить экспорт скрытого рабочего листа](/cells/ru/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Добавлено свойство Cell.StringValueWithoutFormat.**
Свойство StringValueWithoutFormat было добавлено в класс Cell, чтобы облегчить разработчикам извлечение значения ячейки без применения форматирования.

Приведенный ниже фрагмент кода демонстрирует использование свойства Cell.StringValueWithoutFormat по сравнению с cell.DisplayStringValue путем создания электронной таблицы с нуля и применения числового формата к одной из ячеек.

**C#**

{{< highlight "csharp" >}}

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

Вывод приведенного выше кода выглядит следующим образом

123,456

123456

{{% /alert %}}
## **Устаревшие байты, символы, символы с пробелами, строки, свойства абзацев**
Начиная с Aspose.Cells for .NET 8.1.0, многие свойства из класса BuiltInDocumentPropertyCollection помечены как устаревшие. Эти свойства включают байты, символы, символы с пробелами, строки и абзацы. Причина в том, что вышеупомянутые свойства бесполезны для сохранения электронных таблиц Excel, потому что Excel их опускает. Хотя эти свойства изначально были написаны для документов Word и PowerPoint презентаций.
