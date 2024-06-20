---
title: تحويل ورقة عمل إلى ملف صورة حسب الصفحة
type: docs
weight: 10
url: /ar/net/converting-worksheet-to-image-file-by-page/
---

{{< highlight csharp >}}

 Workbook book = new Workbook("Sheet to Image by Page.xls");

Worksheet sheet = book.Worksheets[0];

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

options.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image By Page conversion

SheetRender sr = new SheetRender(sheet, options);

for (int j = 0; j < sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
