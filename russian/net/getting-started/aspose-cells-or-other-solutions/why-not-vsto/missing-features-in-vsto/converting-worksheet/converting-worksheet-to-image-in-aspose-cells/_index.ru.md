﻿---
title: Преобразование рабочего листа в изображение в Aspose.Cells
type: docs
weight: 20
url: /ru/net/converting-worksheet-to-image-in-aspose-cells/
---
Этот документ предназначен для предоставления разработчикам подробного понимания того, как преобразовать рабочий лист в файл изображения и рабочий лист с несколькими страницами в файл изображения на странице.
 Иногда вам может понадобиться представить рабочие листы в виде изображений, например, чтобы использовать их в приложениях или на веб-страницах. Вам может понадобиться вставить изображения в документ Word,**PDF** файл, презентацию PowerPoint или использовать их в каком-либо другом сценарии. Просто вы хотите отобразить рабочий лист как изображение. Aspose.Cells поддерживает преобразование рабочих листов в файлах Excel Microsoft в изображения. Также,**Aspose.Cells** поддерживает преобразование книги в несколько файлов изображений, по одному на страницу.

Для этого можно использовать автоматизацию Office, но автоматизация Office имеет свои недостатки. Есть несколько причин и проблем: например, безопасность, стабильность, масштабируемость/скорость, цена и функции. Короче говоря, причин много, но главная из них заключается в том, что сами Microsoft настоятельно не рекомендуют автоматизировать Office.

В этой статье показано, как создать консольное приложение в Visual Studio.Net, преобразовать рабочий лист в изображение и рабочий лист в одно изображение для каждого рабочего листа с помощью нескольких простейших строк кода, используя Aspose.Cells API. Вам необходимо импортировать Aspose.Cells.Rendering пространство имен для вашей программы/проекта. Он имеет несколько ценных классов, например SheetRender, ImageOrPrintOptions, WorkbookRender и т. д. Aspose.Cells. Класс Rendering.SheetRender представляет рабочий лист для рендеринга изображений для рабочего листа, он имеет перегруженный**Изображать** метод, который может напрямую преобразовать рабочий лист в файл(ы) изображения, указанный с нужными атрибутами или параметрами. Он может вернуться**System.Drawing.Bitmap** объект, и вы можете сохранить файл изображения на диск/поток. Поддерживается несколько форматов изображений, например .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf и т. д.

{{< highlight "csharp" >}}

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
## **Скачать пример кода**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)