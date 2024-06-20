---
title: Aspose.Cells 8.2.2 de Genel API Değişiklikleri
type: docs
weight: 90
url: /tr/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerin ilgisini çekebilecek Aspose.Cells API'sindeki 8.2.1'den 8.2.2'ye yapılan değişiklikleri açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **Eklendi - BuiltInDocumentPropertyCollection.Version Özelliği**
Yeni Version özelliği, belirli bir elektronik tabloyu oluşturan uygulamanın sürümünü geliştiricilere almak için BuiltInDocumentPropertyCollection sınıfına eklenmiştir.

{{% alert color="primary" %}} 

Daha fazla bilgi için lütfen [Elektronik Tabloyu Oluşturan Uygulamanın Sürümünü Alın](/cells/tr/net/get-the-version-number-of-the-application-that-created-the-excel-document/) detaylı makaleye bakın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Chart.Worksheet Özelliği Eklendi**
Aspose.Cells 8.2.2'den önce, bir Grafik nesnesinden çalışsayı oluşturmak mümkün değildi. Aspose.Cells 8.2.2, bu boşluğu doldurarak Chart.Worksheet özelliğini sağlayarak bu eksikliği giderdi.

{{% alert color="primary" %}} 

Daha fazla bilgi için lütfen [Grafik Elemanının Elektronik Tablosunu Alın](/cells/tr/net/get-worksheet-of-the-chart/) detaylı makaleye bakın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
