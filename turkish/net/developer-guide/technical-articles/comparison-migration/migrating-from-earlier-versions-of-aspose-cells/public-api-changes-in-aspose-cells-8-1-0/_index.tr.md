---
title: Aspose.Cells 8.1.0 Kamu API Değişiklikleri
type: docs
weight: 40
url: /tr/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sındaki 8.0.2'den 8.1.0'a kadar olan değişiklikleri açıklar, modül/uygulama geliştiricilerin ilgisini çekebilecek. Sadece yeni ve güncellenmiş kamusal yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet Özelliği Eklendi**
HtmlSaveOptions sınıfı, HTML biçimine gizli çalışma sayfalarının dışa aktarılıp aktarılmayacağını belirlemek için kullanılacak ExportHiddenWorksheet özelliğini açığa çıkardı. Varsayılan değer true'dur. false olarak ayarlansa, Aspose.Cells gizli çalışma sayfası içeriğini dışa aktarmaz.

{{% alert color="primary" %}} 

[Gizli Çalışma Sayfasını Dışa Aktarılmadı] (/hücreler/tr/net/kaydetme-şeklinde-gizli-çalışma-sayfası-içeriğini-dışa-aktarma/) üzerindeki detaylı makaleyi kontrol edin

{{% /alert %}}
## **Cell.StringValueWithoutFormat Özelliği Eklendi**
StringValueWithoutFormat özelliği, hücre Sınıfına eklenmiş, geliştiricilerin hücre değerini herhangi bir biçimlendirme uygulamadan almasını sağlamak için.

Yukarıdaki kod örneğinin çıktısı aşağıdaki gibidir:

**C#**

{{< highlight csharp >}}

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
## **Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs Özellikleri Geçersiz Kılındı**
BuiltInDocumentPropertyCollection sınıfından birçok özellik, Aspose.Cells for .NET 8.1.0'den itibaren geçersiz kılınmıştır. Bu özellikler, Bytes, Characters, CharactersWithSpaces, Lines ve Paragraphs'i içerir. Bu özellikler, Excel elektronik tablolarının korunmasında kullanışlı olmadığı için Excel tarafından atlanır. Bu özellikler aslında Word belgeleri ve PowerPoint sunuları için yazılmıştır.
