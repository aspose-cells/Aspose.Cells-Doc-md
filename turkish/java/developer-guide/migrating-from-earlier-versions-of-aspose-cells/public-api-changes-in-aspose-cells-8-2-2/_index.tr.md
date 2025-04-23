---
title: Aspose.Cells 8.2.2 de Genel API Değişiklikleri
type: docs
weight: 100
url: /tr/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerin ilgisini çekebilecek Aspose.Cells API'sindeki 8.2.1'den 8.2.2'ye yapılan değişiklikleri açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **BuiltInDocumentPropertyCollection Sınıfı için Version Özelliği Eklendi**
Yeni Version özelliği, geliştiricilerin belirli bir elektronik tablo için uygulamanın sürümünü almasına veya ayarlamasına izin vermek üzere BuiltInDocumentPropertyCollection sınıfına eklenmiştir.

{{% alert color="primary" %}} 

[Oluşturulan Elektronik Tablonun Sürüm Numarasını Almak](/cells/tr/java/get-the-version-number-of-the-application-that-created-the-excel-document/) üzerinde detaylı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Chart.Worksheet Özelliği Eklendi**
Aspose.Cells 8.2.2'nin yayınlanmasından önce, bir Grafik nesnesinden içerdiği Çalışma Sayfası örneğini almak mümkün değildi. Aspose.Cells 8.2.2, Chart.Worksheet özelliğini sağlayarak bu boşluğu doldurmuştur.

{{% alert color="primary" %}} 

Daha fazla bilgi için [Grafiğin Çalışma Sayfasını Al](/cells/tr/java/get-worksheet-of-the-chart/) üzerinde detaylı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
