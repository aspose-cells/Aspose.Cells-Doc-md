---
title: Genel API Aspose.Cells 8.8.0'daki değişiklikler
type: docs
weight: 260
url: /tr/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.7.2'den 8.8.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Dış Bağlantı İçin Cell Referans Alın**
Aspose.Cells for .NET 8.8.0, elektronik tabloda saklanan harici bağlantılar için hedef ve çıkış hücresi referanslarının alınmasına yardımcı olan aşağıdaki yeni özellikleri ortaya çıkardı.

1. QueryTable.ConnectionId: Sorgu tablosunun bağlantı kimliğini alır.
1. ExternalConnection.Id: Harici bağlantının kimliğini alır.
1. ListObject.QueryTable: Bağlantılı QueryTable'ı alır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve Liste Nesnelerini Bulun](/cells/tr/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecision Özelliği eklendi**
Aspose.Cells for .NET 8.8.0, HTML dosyalarını içe aktarırken uzun sayısal değerlerin üstel gösterime dönüştürülmesini kontrol etmek için HTMLLoadOptions.KeepPrecision özelliğini ekledi. Veriler HTML dizisinden veya dosyasından içe aktarılıyorsa, varsayılan olarak 15 basamaktan uzun herhangi bir değer üstel gösterime dönüştürülür. Ancak, artık kullanıcılar bu davranışı HTMLLoadOptions.KeepPrecision özelliğinin yardımıyla kontrol edebilir. Söz konusu özellik true olarak ayarlanırsa, değerler kaynakta olduğu gibi içe aktarılır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[ Büyük Sayısal Değerlerin Üstel Gösterime Dönüştürülmesinden Kaçının](/cells/tr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **HTMLLoadOptions.DeleteRedundantSpaces Özelliği eklendi**
Aspose.Cells for .NET 8.8.0, satır sonu etiketinden () sonraki fazladan boşlukları korumak veya silmek için HTMLLoadOptions.DeleteRedundantSpaces özelliğini kullanıma sundu.<br>Etiket) HTML dizisinden veya dosyasından verileri içe aktarırken. HTMLLoadOptions.DeleteRedundantSpaces özelliği, false olarak varsayılan değere sahiptir; bu, tüm fazladan boşlukların korunacağı ve Workbook nesnesine aktarılacağı anlamına gelir, ancak, true olarak ayarlandığında, API, satır sonu etiketinden sonra gelen tüm gereksiz boşlukları siler.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Gereksiz Boşlukları HTML'den Sil](/cells/tr/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibidir.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Style.QuotePrefix Özelliği Eklendi**
Aspose.Cells for .NET 8.8.0, bir hücre değerinin tek tırnak simgesiyle başlayıp başlamadığını algılamak için Style.QuotePrefix özelliğini kullanıma sundu.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Cell Değerinin Başında Tek Alıntı Algıla](/cells/tr/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibidir.

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **Eski API'ler**
### **Eski LoadOptions.ConvertNumericData Özelliği**
Aspose.Cells 8.8.0, LoadOptions.ConvertNumericData özelliğini eskimiş olarak işaretledi. Lütfen HTMLLoadOptions veya TxtLoadOptions sınıflarından ilgili özelliği kullanın.
