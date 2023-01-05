---
title: Преобразование рабочего листа в файл изображения на странице
type: docs
weight: 10
url: /ru/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 Книга книги = новая книга («Лист в изображение по Page.xls»);

Рабочий лист = book.Worksheets[0];

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

options.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Конвертация Sheet2Image по страницам

SheetRender sr = новый SheetRender (лист, параметры);

 для (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
