---
title: Aspose.Cells 8.0.2 de Kamu API Değişiklikleri
type: docs
weight: 30
url: /tr/net/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sındaki 8.0.1 sürümünden 8.0.2'ye kadar olan değişiklikleri açıklar, modül/uygulama geliştiricilerin ilgisini çekebilecek. Sadece yeni ve güncellenmiş kamusal yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Shape Sınıfına TextDirection Özelliği Eklendi**
Shape sınıfı, Shape nesnesinin metin akışının yönünü almak veya ayarlamak için kullanılabilecek TextDirection özelliğini açığa çıkardı. TextDirection özelliği, elektronik tablolardaki yorumlar için istenen metin yönünü ayarlamak için de kullanılabilir.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

[Yorumun Metin Yönünü Değiştirme] (/hücreler/tr/net/yorumun-metin-yönünü-değiştirme/) üzerindeki detaylı makaleyi kontrol edin

{{% /alert %}}
## **HTMLLoadOptions Sınıfına ConvertFormulasData Özelliği Eklendi**
ConvertFormulasData özelliği, HTMLLoadOptions Sınıfına eklenmiş, geliştiricilerin HTML dosyalarından Excel formüllerini yüklemesini kolaylaştırmak için. Boolean ConvertFormulasData özelliği, dize değerinin '=' karakteri ile başlayıp başlamadığını dönüştürüp dönüştürmeyeceğini belirtir.

**C#**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

ConvertFormulasData özelliğinin varsayılan değeri false'tur

{{% /alert %}}
## **HtmlSaveOptions Sınıfına ImageOptions Özelliği Eklendi**
ImageOptions özelliği, HtmlSaveOptions Sınıfına eklenmiş. ImageOptions özelliğine erişmek, geliştiricilerin elektronik tabloları HTML olarak dışa aktarırken gömülü olan resimler için tercihleri belirlemesine olanak tanımıştır.
## **HtmlSaveOptions.ExportChartImageFormat Özelliği Kaldırıldı**
HtmlSaveOptions.ExportChartImageFormat, Aspose.Cells for .NET 8.0.2'den itibaren geçersiz kılınmıştır. Elektronik tabloları HTML biçimine dışa aktarırken resim biçim ayarları için HtmlSaveOptions.ImageOptions yerine kullanılması önerilir.
