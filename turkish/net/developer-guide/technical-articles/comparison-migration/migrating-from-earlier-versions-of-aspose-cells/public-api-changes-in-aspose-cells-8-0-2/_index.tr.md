---
title: Genel API Aspose.Cells 8.0.2'deki değişiklikler
type: docs
weight: 30
url: /tr/net/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.0.1'den 8.0.2'ye modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **Shape Sınıfına TextDirection Özelliği Eklendi**
Shape sınıfı, Shape nesnesi için metin akışının yönünü almak veya ayarlamak için kullanılabilen TextDirection özelliğine sahiptir. TextDirection özelliği, aşağıda gösterildiği gibi bir elektronik tablodaki yorumlar için istenen metin yönünü ayarlamak için de kullanılabilir.

**C#**

{{< highlight "csharp" >}}

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

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Yorumun Metin Yönünü Değiştirme](/cells/tr/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **HTMLLoadOptions Sınıfına ConvertFormulasData Özelliği eklendi**
Geliştiricilerin HTML dosyalarından Excel formüllerini yüklemelerini kolaylaştırmak için HTMLLoadOptions Sınıfına ConvertFormulasData özelliği eklenmiştir. Boolean ConvertFormulasData özelliği, dize değeri '=' karakteriyle başladığında dizenin bir formüle dönüştürülüp dönüştürülmeyeceğini belirtir.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

ConvertFormulasData özelliğinin varsayılan değeri yanlıştır.

{{% /alert %}}
## **HtmlSaveOptions Sınıfına ImageOptions Özelliği eklendi**
HtmlSaveOptions Sınıfına ImageOptions özelliği eklendi. ImageOptions özelliğinin gösterilmesi, geliştiricilerin elektronik tabloları dışa aktarırken HTML'ye katıştırılmış resimler için tercihleri belirlemesine olanak sağlamıştır.
## **Eski HtmlSaveOptions.ExportChartImageFormat Özellik**
HtmlSaveOptions.ExportChartImageFormat, Aspose.Cells for .NET 8.0.2'den başlayarak geçersiz olarak işaretlendi. Elektronik tabloları HTML formatına dışa aktarırken resim formatı ayarları yerine HtmlSaveOptions.ImageOptions kullanılması tavsiye edilir.
