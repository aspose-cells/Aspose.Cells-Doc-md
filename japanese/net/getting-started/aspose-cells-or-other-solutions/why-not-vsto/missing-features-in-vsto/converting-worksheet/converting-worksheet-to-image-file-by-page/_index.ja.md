---
title: ワークシートをページごとに画像ファイルに変換する
type: docs
weight: 10
url: /ja/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

Workbook book = new Workbook("Page.xls によるシートから画像へ");

ワークシート sheet = book.Worksheets[0];

Aspose.Cells.Rendering.ImageOrPrintOptions オプション = 新しい Aspose.Cells.Rendering.ImageOrPrintOptions();

options.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image By Page 変換

SheetRender sr = new SheetRender(シート, オプション);

 for (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
