---
title: Aspose.Cells 8.0.2 de Kamu API Değişiklikleri
type: docs
weight: 40
url: /tr/java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sındaki 8.0.1 sürümünden 8.0.2'ye kadar olan değişiklikleri açıklar, modül/uygulama geliştiricilerin ilgisini çekebilecek. Sadece yeni ve güncellenmiş kamusal yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Shape Sınıfına TextDirection Özelliği Eklendi**
Shape sınıfı, Shape nesnesinin metin akışının yönünü almak veya ayarlamak için kullanılabilecek TextDirection özelliğini açığa çıkardı. TextDirection özelliği, elektronik tablolardaki yorumlar için istenen metin yönünü ayarlamak için de kullanılabilir.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
## **HTMLLoadOptions Sınıfına ConvertFormulasData Özelliği Eklendi**
ConvertFormulasData özelliği, HTMLLoadOptions Sınıfına eklenmiş, geliştiricilerin HTML dosyalarından Excel formüllerini yüklemesini kolaylaştırmak için. Boolean ConvertFormulasData özelliği, dize değerinin '=' karakteri ile başlayıp başlamadığını dönüştürüp dönüştürmeyeceğini belirtir.

**Java**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

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
{{< app/cells/assistant language="java" >}}
