---
title: Общедоступный API Изменения в Aspose.Cells 8.0.2
type: docs
weight: 40
url: /ru/java/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.0.1 до 8.0.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство TextDirection в класс Shape**
Класс Shape предоставляет свойство TextDirection, которое можно использовать для получения или установки направления потока текста для объекта Shape. Свойство TextDirection также можно использовать для установки нужного направления текста для комментариев в электронной таблице, как показано ниже.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
## **Добавлено свойство ConvertFormulasData в класс HTMLLoadOptions.**
Свойство ConvertFormulasData было добавлено в класс HTMLLoadOptions, чтобы облегчить разработчикам загрузку формул Excel из файлов HTML. Логическое свойство ConvertFormulasData указывает, следует ли преобразовывать строку в формулу, если строковое значение начинается с символа '='.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

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
