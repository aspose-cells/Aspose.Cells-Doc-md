---
title: Aspose.Cells 8.1.0 Kamu API Değişiklikleri
type: docs
weight: 50
url: /tr/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sındaki 8.0.2'den 8.1.0'a kadar olan değişiklikleri açıklar, modül/uygulama geliştiricilerin ilgisini çekebilecek. Sadece yeni ve güncellenmiş kamusal yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet Özelliği Eklendi**
HtmlSaveOptions sınıfı, HTML biçimine gizli çalışma sayfalarının dışa aktarılıp aktarılmayacağını belirlemek için kullanılacak ExportHiddenWorksheet özelliğini açığa çıkardı. Varsayılan değer true'dur. false olarak ayarlansa, Aspose.Cells gizli çalışma sayfası içeriğini dışa aktarmaz.

{{% alert color="primary" %}} 

[Gizli Çalışma Sayfasının Dışa Aktarılmasını Engelleme](/cells/tr/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/) konusundaki detaylı makaleyi kontrol edin

{{% /alert %}}
## **Cell.StringValueWithoutFormat Özelliği Eklendi**
StringValueWithoutFormat özelliği, hücre Sınıfına eklenmiş, geliştiricilerin hücre değerini herhangi bir biçimlendirme uygulamadan almasını sağlamak için. 

Aşağıdaki sağlanan kod parçası, bir elektronik tablo oluşturarak ve hücrelerden birine numara biçimini uygulayarak Cell.getStringValueWithoutFormat yönteminin kullanımını cell.getDisplayStringValue ile karşılaştırmaktadır. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Yukarıdaki kodun çıktısı aşağıdaki gibidir

Biçimlendirilmiş Dize Değeri: 123,456
Biçimsiz Dize Değeri: 123456

{{% /alert %}}
## **Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs Özellikleri Geçersiz Kılındı**
BuiltInDocumentPropertyCollection sınıfındaki birçok özellik Aspose.Cells for Java 8.1.0’den itibaren eski kabul edilmiştir. Bu özellikler Bytes, Characters, CharactersWithSpaces, Lines ve Paragraphs’i içerir. Sebep ise, bahsi geçen özelliklerin Excel tablolarının korunmasında kullanılmamasıdır çünkü Excel bunları atlar. Bu özellikler başlangıçta Word belgeleri ve PowerPoint sunumları için yazılmıştır. 
{{< app/cells/assistant language="java" >}}
