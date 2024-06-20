---
title: Aspose.Cells 8.3.0 da Genel API Değişiklikleri
type: docs
weight: 110
url: /tr/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerin ilgisini çekebilecek Aspose.Cells API'sindeki 8.2.2'den 8.3.0'a yapılan değişiklikleri açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **WorkbookSettings.AutoRecover Özelliği Eklendi**
Getter/setter, uygulamalarının çalışma sayfaları için Otomatik Kurtarma seçeneğini ols/aan geliştiricilere getirilmiştir. 

{{% alert color="primary" %}} 

Daha fazla bilgi için [Çalışma Sayfası Otomatik Kurtarma Ayarı](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) üzerinde detaylı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **WorkbookSettings.CrashSave Özelliği Eklendi**
Getter/setter, CrashSave özelliği, uygulamanın son çökmesinden sonra çalışma kitabı dosyasını kurtarılıp kurtarılmadığını belirtir.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **WorkbookSettings.DataExtractLoad Özelliği Eklendi**
Getter/setter, DataExtractLoad özelliği, geliştiricilere çalışma kitabı dosyasında son kurtarmanın yapılıp yapılmadığı hakkında bilgi almak/ayarlamak için eklenmiştir. DataExtractLoad özelliği true döndürürse, bu, çalışma kitabı dosyasında veri kurtarımının yapıldığını belirtir.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **WorkbookSettings.RepairLoad Özelliği Eklendi**
Getter/setter, RepairLoad özelliği, uygulamanın son yükleme oturumunda elektronik tablonun onarıldığını belirtir.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **TxtLoadOptions.KeepExactFormat Özelliği Eklendi**
KeepExactFormat özelliği, metin/dizge sayıya veya TarihSaat'e dönüştürüldüğünde hücre değerinin tam biçiminin korunup korunmayacağını belirtir. Bu özellik, CSV dosyalarından TarihSaat veya sayısal değerleri yüklerken MS Excel programının davranışını eşleştirmek için eklenmiştir. MS Excel'in davranışını taklit etmek için KeepExactFormat özelliğini false olarak ayarlayın, varsayılan değer true olduğu için hücre değeri CSV dosyasındaki dize şeklinde biçimlendirilecektir.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Shape.Id Özelliği Eklendi**
V8.3.0, her bir şekil nesnesini benzersiz şekilde tanımlamak için Shape.Id özelliğinin getter/setter'ı eklenmiştir. Bu yeni özellik ayrıca bir elektronik tabloda Grafik nesnelerini benzersiz bir şekilde tanımlamada da yardımcı olur.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **PlotArea.setPositionAuto Yöntemi Eklendi**
setPositionAuto yöntemi PlotArea sınıfına eklendi ve bu, grafik alanının otomatik moda ayarlanmasına yardımcı olur.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
