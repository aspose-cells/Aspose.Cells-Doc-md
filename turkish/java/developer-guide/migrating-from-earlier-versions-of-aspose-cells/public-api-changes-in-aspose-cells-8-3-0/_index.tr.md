---
title: Genel API Aspose.Cells 8.3.0'daki değişiklikler
type: docs
weight: 110
url: /tr/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.2.2'den 8.3.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır.

{{% /alert %}} 
## **Eklenen API'ler**
### **Özellik WorkbookSettings.AutoRecover Eklendi**
AutoRecover özelliği için alıcı/ayarlayıcı, geliştiricilerin uygulamalarında elektronik tablolar için Otomatik Kurtarma seçeneğini almalarına/ayarlamalarına izin vermek için WorkbookSettings sınıfına eklenmiştir.

{{% alert color="primary" %}} 

 Lütfen makaleyi kontrol edin[Elektronik Tablo Otomatik Kurtarmayı Ayarlama](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) daha fazla bilgi için.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Özellik WorkbookSettings.CrashSave Eklendi**
CrashSave özelliği için alıcı/ayarlayıcı, WorkbookSettings sınıfına eklendi. Boole tipi özelliği, uygulamanın çalışma kitabı dosyasını bir kilitlenmeden sonra en son kaydedip kaydetmediğini gösterir.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Özellik WorkbookSettings.DataExtractLoad Eklendi**
DataExtractLoad özelliği için alıcı/ayarlayıcı, geliştiricilerin son kurtarma ile ilgili bilgileri almasına/ayarlamasına izin vermek için WorkbookSettings sınıfına eklenmiştir. DataExtractLoad özelliği, çalışma kitabı dosyasında veri kurtarmanın gerçekleştirildiğini gösteren true değerini döndürürse.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Özellik WorkbookSettings.RepairLoad Eklendi**
RepairLoad özelliği için alıcı/ayarlayıcı, WorkbookSettings sınıfına eklendi. Boole tipi özelliği, elektronik tablonun Excel uygulamasıyla son yükleme oturumunda onarılıp onarılmadığını gösterir.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Özellik TxtLoadOptions.KeepExactFormat Eklendi**
TxtLoadOptions sınıfına, dize/metin sayılara veya DateTime'a dönüştürüldüğünde hücre değeri için tam biçimlendirmenin korunması gerekip gerekmediğini gösteren KeepExactFormat özelliği eklendi. Bu özellik, CSV dosyalarından DateTime veya sayısal değerleri yüklemek için MS Excel uygulamasının davranışını eşleştirmek için eklenmiştir. MS Excel'in davranışını simüle etmek için, KeepExactFormat özelliğini false olarak ayarlayın, varsayılan değer ise true'dur, böylece hücre değeri CSV dosyasında dize olarak biçimlendirilecektir.

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Özellik Shape.Id Eklendi**
v8.3.0, belirli bir elektronik tablodaki her bir şekil nesnesini benzersiz şekilde tanımlamak için Shape.Id özelliği için alıcı/ayarlayıcı eklemiştir. Bu yeni özellik, aşağıda gösterildiği gibi bir elektronik tablodaki Chart nesnelerini benzersiz bir şekilde tanımlamaya da yardımcı olur.

**Java**

{{< highlight "csharp" >}}

 Çalışma kitabı kitabı = yeni Çalışma Kitabı ("sample.xlsx");

ChartCollection çizelgeleri = book.getWorksheets().get(0).getCharts();

 for(int dizin = 0; dizin<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Yöntem PlotArea.setPositionAuto Eklendi**
Grafiğin çizim alanını otomatik moda ayarlamaya yardımcı olan PlotArea sınıfına setPositionAuto yöntemi eklendi.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
