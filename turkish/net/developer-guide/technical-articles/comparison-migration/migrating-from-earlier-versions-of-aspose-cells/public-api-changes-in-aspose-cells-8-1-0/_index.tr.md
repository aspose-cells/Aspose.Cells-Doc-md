---
title: Genel API Aspose.Cells 8.1.0'daki değişiklikler
type: docs
weight: 40
url: /tr/net/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.0.2'den 8.1.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet Özelliği Eklendi**
HtmlSaveOptions sınıfı, gizli çalışma sayfalarının HTML biçimine dışa aktarılıp aktarılmadığını belirtmek için kullanılabilen ExportHiddenWorksheet özelliğine sahiptir. Varsayılan değer doğrudur. yanlış olarak ayarlanırsa Aspose.Cells, gizli çalışma sayfası içeriğini dışa aktarmaz.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Gizli Çalışma Sayfasını Dışa Aktarmayı Önle](/cells/tr/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Cell.StringValueWithoutFormat Özelliği eklendi**
Cell Sınıfına StringValueWithoutFormat özelliği eklenerek geliştiricilerin herhangi bir biçimlendirme uygulamadan hücre değerini almalarını kolaylaştırılmıştır.

Aşağıda verilen kod parçacığı, sıfırdan bir elektronik tablo oluşturarak ve hücrelerden birine sayı biçimi uygulayarak cell.DisplayStringValue ile karşılaştırıldığında Cell.StringValueWithoutFormat özelliğinin kullanımını göstermektedir.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Yukarıdaki kodun çıktısı aşağıdaki gibidir

123,456

123456

{{% /alert %}}
## **Eski Baytlar, Karakterler, CharactersWithSpaces, Satırlar, Paragraflar Özellikleri**
Aspose.Cells for .NET 8.1.0'dan başlayarak BuiltInDocumentPropertyCollection sınıfındaki birçok özellik geçersiz olarak işaretlendi. Bu özellikler arasında Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs bulunur. Nedeni, yukarıda belirtilen özelliklerin Excel elektronik tablolarının korunmasında hiçbir faydası yoktur çünkü Excel bunları atlar. Bu özellikler orijinal olarak Word belgeleri ve PowerPoint sunumları için yazılmıştır.
