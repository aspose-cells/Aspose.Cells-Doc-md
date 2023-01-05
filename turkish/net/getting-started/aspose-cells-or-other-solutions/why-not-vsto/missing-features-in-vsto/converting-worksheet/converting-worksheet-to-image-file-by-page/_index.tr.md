---
title: Çalışma Sayfasını Sayfaya Göre Görüntü Dosyasına Dönüştürme
type: docs
weight: 10
url: /tr/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 Çalışma kitabı kitabı = new Workbook("Sayfadan Görüntüye Sayfa.xls");

Çalışma sayfası sayfası = kitap.Çalışma Sayfaları[0];

Aspose.Cells.Rendering.ImageOrPrintOptions seçenekleri = yeni Aspose.Cells.Rendering.ImageOrPrintOptions();

seçenekler.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image By Page dönüştürme

SheetRender sr = yeni SheetRender(sayfa, seçenekler);

 için (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
