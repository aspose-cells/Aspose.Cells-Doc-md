---
title: Genel API Aspose.Cells'deki değişiklikler 8.2.2
type: docs
weight: 90
url: /tr/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.2.1'den 8.2.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır.

{{% /alert %}} 
## **Eklenen API'ler**
### **Özellik BuiltInDocumentPropertyCollection.Version Eklendi**
Geliştiricilerin, belirli bir e-tabloyu oluşturan uygulamanın sürümünü almalarına olanak sağlamak için, yeni Version özelliği, BuiltInDocumentPropertyCollection sınıfına eklenmiştir.

{{% alert color="primary" %}} 

 Lütfen ayrıntılı makaleyi kontrol edin[Elektronik Tabloyu Oluşturan Uygulamanın Sürümünü Alın](/cells/tr/net/get-the-version-number-of-the-application-that-created-the-excel-document/) daha fazla bilgi için.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Özellik Tablosu.Çalışma Sayfası Eklendi**
Aspose.Cells 8.2.2 yayınlanmadan önce, Worksheet örneğini tuttuğu bir Chart nesnesinden almak mümkün değildi. Aspose.Cells 8.2.2, Chart.Worksheet özelliğini sağlayarak bu boşluğu doldurmuştur.

{{% alert color="primary" %}} 

 Lütfen ayrıntılı makaleyi kontrol edin[Grafiğin Çalışma Sayfasını Alın](/cells/tr/net/get-worksheet-of-the-chart/) daha fazla bilgi için.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
