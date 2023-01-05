---
title: Общедоступный API Изменения в Aspose.Cells 8.0.2
type: docs
weight: 30
url: /ru/net/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.0.1 до 8.0.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство TextDirection в класс Shape**
Класс Shape предоставляет свойство TextDirection, которое можно использовать для получения или установки направления потока текста для объекта Shape. Свойство TextDirection также можно использовать для установки нужного направления текста для комментариев в электронной таблице, как показано ниже.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Изменение направления текста комментария](/cells/ru/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **Добавлено свойство ConvertFormulasData в класс HTMLLoadOptions.**
Свойство ConvertFormulasData было добавлено в класс HTMLLoadOptions, чтобы облегчить разработчикам загрузку формул Excel из файлов HTML. Логическое свойство ConvertFormulasData указывает, следует ли преобразовывать строку в формулу, если строковое значение начинается с символа '='.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

Значение свойства ConvertFormulasData по умолчанию — false.

{{% /alert %}}
## **Добавлено свойство ImageOptions в класс HtmlSaveOptions.**
Свойство ImageOptions добавлено в класс HtmlSaveOptions. Предоставление свойства ImageOptions позволило разработчикам установить предпочтения для изображений, встроенных в HTML, при экспорте электронных таблиц.
## **Устаревшее свойство HtmlSaveOptions.ExportChartImageFormat**
HtmlSaveOptions.ExportChartImageFormat помечен как устаревший, начиная с Aspose.Cells for .NET 8.0.2. Вместо этого рекомендуется использовать HtmlSaveOptions.ImageOptions для настроек формата изображения при экспорте электронных таблиц в формат HTML.
