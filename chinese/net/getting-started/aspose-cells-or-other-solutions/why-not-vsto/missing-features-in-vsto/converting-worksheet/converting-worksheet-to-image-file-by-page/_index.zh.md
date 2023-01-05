---
title: 按页将工作表转换为图像文件
type: docs
weight: 10
url: /zh/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

工作簿 book = new Workbook("Sheet to Image by Page.xls");

工作表 sheet = book.Worksheets[0];

Aspose.Cells.Rendering.ImageOrPrintOptions 选项 = 新 Aspose.Cells.Rendering.ImageOrPrintOptions();

options.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image按页转换

SheetRender sr = new SheetRender(sheet, options);

对于 (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
