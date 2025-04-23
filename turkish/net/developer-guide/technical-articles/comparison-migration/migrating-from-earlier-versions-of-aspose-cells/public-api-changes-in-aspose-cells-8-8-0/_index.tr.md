---
title: Aspose.Cells 8.8.0 da Genel API Değişiklikleri
type: docs
weight: 260
url: /tr/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Bu belge, 8.7.2'den 8.8.0 sürümüne Aspose.Cells API'deki değişiklikleri modül/uygulama geliştiricilerin ilgisini çekebilecek herhangi bir değişikliği içermektedir. Yeni ve güncellenmiş genel yöntemler, eklendi ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içermektedir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Dış Bağlantı için Hücre Referanslarını Al**
Aspose.Cells for .NET 8.8.0, elektronik tablodaki dış bağlantılar için hedef ve çıktı hücre referanslarını almak için faydalı olan aşağıdaki yeni özellikleri açığa çıkardı.

1. QueryTable.ConnectionId: Sorgu tablosunun bağlantı kimliğini alır.
1. ExternalConnection.Id: Dış bağlantının kimliğini alır.
1. ListObject.QueryTable: Bağlantılı QueryTable'ı alır.

{{% alert color="primary" %}} 

Bu özelliğin daha fazla ayrıntısı için lütfen [Dış Veri Bağlantıları ile İlgili Sorgu Tablolarını ve List Nesnelerini Bulma](/cells/tr/net/find-query-tables-and-list-objects-related-to-external-data-connections/) üzerindeki detaylı makaleyi inceleyin

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecision Özelliği Eklendi**
Aspose.Cells for .NET 8.8.0, HTML dosyalarını içe aktarırken uzun sayısal değerlerin üstel gösterime dönüştürülmesini kontrol etmek için HTMLLoadOptions.KeepPrecision özelliğini ekledi. Varsayılan olarak, HTML dizgisi veya dosyasından veri içe aktarılıyorsa 15 haneden uzun herhangi bir değer üstel gösterime dönüştürülür. Ancak, artık kullanıcılar HTMLLoadOptions.KeepPrecision özelliğiyle bu davranışı kontrol edebilir. Söz konusu özellik true olarak ayarlanmışsa, değerler kaynağındaki gibi içe aktarılacaktır.

{{% alert color="primary" %}} 

Bu özelliğin daha fazla ayrıntısı için lütfen [Büyük Sayısal Değerlerin Üstel Gösterime Dönüştürülmesinin Engellenmesi](/cells/tr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/) üzerindeki detaylı makaleyi inceleyin

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **HTMLLoadOptions.DeleteRedundantSpaces Özelliği Eklendi**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Bu özelliğin daha fazla ayrıntısı için lütfen [HTML'den Redundant Boşlukları Silme](/cells/tr/net/delete-redundant-spaces-after-line-break-while-importing/) üzerindeki detaylı makaleyi inceleyin

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibi görünüyor.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Style.QuotePrefix Özelliği Eklendi**
Aspose.Cells for .NET 8.8.0, hücre değerinin tek tırnak sembolü ile başlayıp başlamadığını tespit etmek için Style.QuotePrefix özelliğini açığa çıkardı.

{{% alert color="primary" %}} 

Bu özelliğin daha fazla ayrıntısı için lütfen [Hücre Değeri'nin Başında Tek Tırnak İşareti Olup Olmadığını Bulma](/cells/tr/net/find-if-the-cell-value-starts-with-single-quote-mark/) üzerindeki detaylı makaleyi inceleyin

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibi görünüyor.

**C#**

{{< highlight csharp >}}

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
## **Eskimiş API'lar**
### **LoadOptions.ConvertNumericData Özelliği Eski Duruma Alındı**
Aspose.Cells 8.8.0, LoadOptions.ConvertNumericData özelliğini eski duruma aldı. Lütfen HTMLLoadOptions veya TxtLoadOptions sınıflarından karşılık gelen özelliği kullanın.
{{< app/cells/assistant language="csharp" >}}
