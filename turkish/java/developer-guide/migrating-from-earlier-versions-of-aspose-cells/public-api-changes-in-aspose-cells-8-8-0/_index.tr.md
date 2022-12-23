---
title: Genel API Aspose.Cells 8.8.0'daki değişiklikler
type: docs
weight: 270
url: /tr/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.7.2'den 8.8.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Dış Bağlantı İçin Cell Referans Alın**
 Aspose.Cells for Java 8.8.0, elektronik tabloda saklanan harici bağlantılar için hedef ve çıkış hücresi referanslarının alınmasına yardımcı olan aşağıdaki yeni özellikleri ortaya çıkardı.

1. QueryTable.ConnectionId: Sorgu tablosunun bağlantı kimliğini alır.
1. ExternalConnection.Id: Harici bağlantının kimliğini alır.
1. ListObject.QueryTable: Bağlantılı QueryTable'ı alır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve Liste Nesnelerini Bulun](/cells/tr/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecision Özelliği eklendi**
Aspose.Cells for Java 8.8.0, HTML dosyalarını içe aktarırken uzun sayısal değerlerin üstel gösterime dönüştürülmesini kontrol etmek için HTMLLoadOptions.KeepPrecision özelliğini ekledi. Veriler HTML dizisinden veya dosyasından içe aktarılıyorsa, varsayılan olarak 15 basamaktan uzun herhangi bir değer üstel gösterime dönüştürülür. Ancak, artık kullanıcılar bu davranışı HTMLLoadOptions.KeepPrecision özelliğinin yardımıyla kontrol edebilir. Söz konusu özellik true olarak ayarlanırsa, değerler kaynakta olduğu gibi içe aktarılır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[ Büyük Sayısal Değerlerin Üstel Gösterime Dönüştürülmesinden Kaçının](/cells/tr/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

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
### **HTMLLoadOptions.DeleteRedundantSpaces Özelliği eklendi**
Aspose.Cells for Java 8.8.0, satır sonu etiketinden () sonraki fazladan boşlukları korumak veya silmek için HTMLLoadOptions.DeleteRedundantSpaces özelliğini kullanıma sundu.<br>Etiketi) HTML dizisinden veya dosyasından verileri içe aktarırken. HTMLLoadOptions.DeleteRedundantSpaces özelliği, false olarak varsayılan değere sahiptir; bu, tüm fazladan boşlukların korunacağı ve Workbook nesnesine aktarılacağı anlamına gelir, ancak, true olarak ayarlandığında, API, satır sonu etiketinden sonra gelen tüm gereksiz boşlukları siler.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[HTML'den Fazla Alanları Sil](/cells/tr/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

 Basit kullanım senaryosu aşağıdaki gibidir.

**Java**

{{< highlight "csharp" >}}

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

byte[]byteArray = html.getBytes();

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
 Aspose.Cells for Java 8.8.0, bir hücre değerinin tek tırnak simgesiyle başlayıp başlamadığını algılamak için Style.QuotePrefix özelliğini kullanıma sundu.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Cell Değerinin Başında Tek Alıntı Algıla](/cells/tr/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

 Basit kullanım senaryosu aşağıdaki gibidir.

**Java**

{{< highlight "csharp" >}}

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
## **Eski API'ler**
### **Eski LoadOptions.ConvertNumericData Özelliği**
Aspose.Cells 8.8.0, LoadOptions.ConvertNumericData özelliğini eskimiş olarak işaretledi. Lütfen HTMLLoadOptions veya TxtLoadOptions sınıflarından ilgili özelliği kullanın.
