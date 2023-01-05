---
title: Genel API Aspose.Cells'deki değişiklikler 8.2.2
type: docs
weight: 100
url: /tr/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.2.1'den 8.2.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır.

{{% /alert %}} 
## **Eklenen API'ler**
### **BuiltInDocumentPropertyCollection Sınıfı İçin Özellik Sürümü Eklendi**
Geliştiricilerin belirli bir e-tablo için uygulamanın sürümünü almalarına veya uygulama sürümünü ayarlamalarına olanak tanımak amacıyla, yeni Version özelliği, BuiltInDocumentPropertyCollection sınıfına eklenmiştir.

{{% alert color="primary" %}} 

 Lütfen ayrıntılı makaleyi kontrol edin.[Elektronik Tabloyu Oluşturan Uygulamanın Sürümünü Alın](/cells/tr/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Özellik Tablosu.Çalışma Sayfası Eklendi**
Aspose.Cells 8.2.2 sürümünden önce, Çalışma Sayfası örneğini içerdiği bir Grafik nesnesinden almak mümkün değildi. Aspose.Cells 8.2.2, Chart.Worksheet özelliğini sağlayarak bu boşluğu doldurmuştur.

{{% alert color="primary" %}} 

 Lütfen ayrıntılı makaleyi kontrol edin[Grafiğin Çalışma Sayfasını Alın](/cells/tr/java/get-worksheet-of-the-chart/) daha fazla bilgi için.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
