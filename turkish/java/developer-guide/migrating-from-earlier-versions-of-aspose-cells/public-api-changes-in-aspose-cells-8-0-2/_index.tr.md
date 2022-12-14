---
title: Genel API Aspose.Cells 8.0.2'deki değişiklikler
type: docs
weight: 40
url: /tr/java/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.0.1'den 8.0.2'ye modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **Shape Sınıfına TextDirection Özelliği Eklendi**
Shape sınıfı, Shape nesnesi için metin akışının yönünü almak veya ayarlamak için kullanılabilen TextDirection özelliğine sahiptir. TextDirection özelliği, aşağıda gösterildiği gibi bir elektronik tablodaki yorumlar için istenen metin yönünü ayarlamak için de kullanılabilir.

**Java**

{{< highlight "csharp" >}}

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
## **HTMLLoadOptions Sınıfına ConvertFormulasData Özelliği eklendi**
Geliştiricilerin HTML dosyalarından Excel formüllerini yüklemelerini kolaylaştırmak için HTMLLoadOptions Sınıfına ConvertFormulasData özelliği eklenmiştir. Boolean ConvertFormulasData özelliği, dize değeri '=' karakteriyle başladığında dizenin bir formüle dönüştürülüp dönüştürülmeyeceğini belirtir.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

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
