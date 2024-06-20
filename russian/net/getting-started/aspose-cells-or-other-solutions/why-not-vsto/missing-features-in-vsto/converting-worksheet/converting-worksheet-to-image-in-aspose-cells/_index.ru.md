---
title: Преобразование таблицы в изображение в Aspose.Cells
type: docs
weight: 20
url: /ru/net/converting-worksheet-to-image-in-aspose-cells/
---

Этот документ предназначен для предоставления разработчикам подробного понимания того, как преобразовать рабочий лист в файл изображения и рабочий лист с несколькими страницами в файл изображения для каждой страницы.
Иногда вам может понадобиться представить рабочие листы в виде изображений, например, чтобы использовать их в приложениях или веб-страницах. Возможно, вам потребуется вставить изображения в документ Word, файл **PDF**, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вы хотите отобразить рабочий лист в виде изображения. Aspose.Cells поддерживает преобразование рабочих листов в файлах Microsoft Excel в изображения. Кроме того, **Aspose.Cells** поддерживает преобразование книги в несколько файлов изображений, по одному на страницу.

Вы можете использовать автоматизацию Office для достижения этой цели, но у автоматизации Office есть свои недостатки. Существует несколько причин и проблем, например, безопасность, стабильность, масштабируемость/скорость, цена и функции. Короче говоря, есть много причин, но основная заключается в том, что сама компания Microsoft настоятельно рекомендует отказаться от автоматизации Office.

В этой статье показано, как создать консольное приложение в Visual Studio.Net, преобразовать рабочий лист в изображение и рабочий лист в одно изображение для каждого рабочего листа с помощью нескольких простых строк кода, используя API Aspose.Cells. Вам нужно импортировать пространство имен Aspose.Cells.Rendering в вашу программу/проект. В нем есть несколько ценных классов, например SheetRender, ImageOrPrintOptions, WorkbookRender и т. д. Класс Aspose.Cells.Rendering.SheetRender представляет рабочий лист для рендеринга изображений для рабочего листа, у него есть перегруженный метод **ToImage**, который может непосредственно преобразовывать рабочий лист в файл изображения с указанными желаемыми атрибутами или параметрами. Он может возвращать объект **System.Drawing.Bitmap**, и вы можете сохранить файл изображения на диск/поток. Поддерживается несколько форматов изображений, например .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf и т. д.

{{< highlight csharp >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
