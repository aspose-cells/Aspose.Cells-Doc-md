---
title: تحويل ورقة العمل إلى ملف صورة حسب الصفحة
type: docs
weight: 10
url: /ar/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 كتاب المصنف = مصنف جديد ("ورقة إلى صورة بواسطة Page.xls") ؛

ورقة العمل = book.Worksheets [0] ؛

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions ()؛

خيارات أفقية الدقة = 200 ؛

options.VerticalResolution = 200 ؛

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff ؛

// Sheet2Image حسب تحويل الصفحة

SheetRender sr = new SheetRender (ورقة ، خيارات) ؛

 لـ (int j = 0 ؛ j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
