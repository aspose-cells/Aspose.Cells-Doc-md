---
title: Aspose.Cells 8.8.0 da Genel API Değişiklikleri
type: docs
weight: 270
url: /tr/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Bu belge, 8.7.2'den 8.8.0 sürümüne Aspose.Cells API'deki değişiklikleri modül/uygulama geliştiricilerin ilgisini çekebilecek herhangi bir değişikliği içermektedir. Yeni ve güncellenmiş genel yöntemler, eklendi ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içermektedir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Dış Bağlantı için Hücre Referanslarını Al**
Aspose.Cells for Java 8.8.0, elektronik tabloya kaydedilen dış bağlantılar için hedef ve çıkış hücre referanslarını almak için yardımcı olan aşağıdaki yeni özellikleri ortaya çıkardı. 

1. QueryTable.ConnectionId: Sorgu tablosunun bağlantı kimliğini alır.
1. ExternalConnection.Id: Dış bağlantının kimliğini alır.
1. ListObject.QueryTable: Bağlantılı QueryTable'ı alır.

{{% alert color="primary" %}} 

Bu özelliğe ilişkin daha fazla ayrıntı için lütfen [Uzak Veri Bağlantılarıyla İlgili Sorgu Tabloları ve List Objeleri Bulun](/cells/tr/java/find-query-tables-and-list-objects-related-to-external-data-connections/) başlıklı detaylı makaleye göz atın.

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecision Özelliği Eklendi**
Aspose.Cells for Java 8.8.0, HTML dosyalarını içe aktarırken uzun sayısal değerlerin üstel gösterimine dönüştürülmesini kontrol etmek için HTMLLoadOptions.KeepPrecision özelliğini ekledi. Varsayılan olarak, 15 haneden uzun herhangi bir değer, HTML dizesi veya dosyasından veri içe aktarılıyorsa üstel gösterime dönüştürülür. Ancak şimdi kullanıcılar, HTMLLoadOptions.KeepPrecision özelliğinin yardımıyla bu davranışı kontrol edebilir. Söz konusu özellik true olarak ayarlanmışsa, değerler kaynaktaki gibi içe aktarılacaktır.

{{% alert color="primary" %}} 

Bu özelliğe ilişkin daha fazla ayrıntı için lütfen [Büyük Sayısal Değerlerin Üstel Gösterimine Dönüştürülmesini Engelle](/cells/tr/java/avoid-exponential-notation-of-large-numbers-while-importing-from/) başlıklı detaylı makaleye göz atın.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **HTMLLoadOptions.DeleteRedundantSpaces Özelliği Eklendi**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Bu özelliğe ilişkin daha fazla ayrıntı için lütfen [HTML'den Redundant Boşlukları Silme](/cells/tr/java/delete-redundant-spaces-after-line-break-while-importing/) başlıklı detaylı makaleye göz atın.

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibi görünüyor. 

**Java**

{{< highlight csharp >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Style.QuotePrefix Özelliği Eklendi**
Aspose.Cells for Java 8.8.0, hücre değerinin tek tırnak işaretiyle başlayıp başlamadığını algılamak için Style.QuotePrefix özelliğini ortaya çıkardı. 

{{% alert color="primary" %}} 

Bu özelliğe ilişkin daha fazla ayrıntı için lütfen [Hücre Değerinin Başında Tek Tırnak İşareti Var Mı Bul](/cells/tr/java/find-if-the-cell-value-starts-with-single-quote-mark/) başlıklı detaylı makaleye göz atın.

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibi görünüyor. 

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **Eskimiş API'lar**
### **LoadOptions.ConvertNumericData Özelliği Eski Duruma Alındı**
Aspose.Cells 8.8.0, LoadOptions.ConvertNumericData özelliğini eski duruma aldı. Lütfen HTMLLoadOptions veya TxtLoadOptions sınıflarından karşılık gelen özelliği kullanın.
{{< app/cells/assistant language="java" >}}
