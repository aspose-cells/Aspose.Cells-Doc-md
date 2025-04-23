---
title: Изменения в общедоступном API в Aspose.Cells 8.0.2
type: docs
weight: 40
url: /ru/java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.0.1 до 8.0.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлено свойство TextDirection в класс Shape**
Класс Shape имеет свойство TextDirection, которое можно использовать для получения или установки направления потока текста для объекта Shape. Свойство TextDirection также может использоваться для установки желаемого направления текста для комментариев в электронной таблице, как показано ниже.

**Java**

{{< highlight csharp >}}

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
## **Добавлено свойство ConvertFormulasData в класс HTMLLoadOptions**
Добавлено свойство ConvertFormulasData в класс HTMLLoadOptions, чтобы облегчить разработчикам загрузку формул Excel из HTML-файлов. Логическое свойство ConvertFormulasData указывает, следует ли преобразовать строку в формулу, когда строковое значение начинается с символа '='.

**Java**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

Значение по умолчанию свойства ConvertFormulasData - false.

{{% /alert %}}
## **Добавлено свойство ImageOptions в класс HtmlSaveOptions**
В классе HtmlSaveOptions появилось свойство ImageOptions. Публичное предоставление свойства ImageOptions позволяет разработчикам устанавливать предпочтения для изображений, встроенных в HTML при экспорте электронных таблиц. 
## **Устаревшее свойство HtmlSaveOptions.ExportChartImageFormat**
HtmlSaveOptions.ExportChartImageFormat помечен как устаревший, начиная с Aspose.Cells for .NET 8.0.2. Рекомендуется использовать HtmlSaveOptions.ImageOptions вместо настройки формата изображения при экспорте электронных таблиц в формат HTML.
{{< app/cells/assistant language="java" >}}
