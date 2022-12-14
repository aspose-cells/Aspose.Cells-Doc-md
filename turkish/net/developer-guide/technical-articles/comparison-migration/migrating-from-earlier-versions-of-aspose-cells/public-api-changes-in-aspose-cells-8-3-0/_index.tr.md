---
title: Genel API Aspose.Cells 8.3.0'daki değişiklikler
type: docs
weight: 100
url: /tr/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.2.2'den 8.3.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır.

{{% /alert %}} 
## **Eklenen API'ler**
### **Özellik WorkbookSettings.AutoRecover Eklendi**
Geliştiricilerin uygulamalarında elektronik tablolar için Otomatik Kurtarma seçeneğini belirlemesine olanak sağlamak amacıyla WorkbookSettings sınıfına yeni AutoRecover özelliği eklenmiştir.

{{% alert color="primary" %}} 

 Lütfen makaleyi kontrol edin[Elektronik Tablo Otomatik Kurtarmayı Ayarlama](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) daha fazla bilgi için.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Özellik WorkbookSettings.CrashSave Eklendi**
WorkbookSettings sınıfına, uygulamanın çalışma kitabı dosyasını bir kilitlenmeden sonra en son kaydedip kaydetmediğini gösteren bir Boole türü özelliği CrashSave eklenmiştir.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Özellik WorkbookSettings.DataExtractLoad Eklendi**
Geliştiricilerin son kurtarma ile ilgili bilgileri alabilmeleri için WorkbookSettings sınıfına DataExtractLoad özelliği eklendi. DataExtractLoad özelliği true değerini döndürürse, bu, elektronik tabloda veri kurtarmanın gerçekleştirildiğini gösterir.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Özellik WorkbookSettings.RepairLoad Eklendi**
RepairLoad özelliği, elektronik tablonun Excel uygulamasıyla son yüklemede onarılıp onarılmadığını gösterir.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Özellik TxtLoadOptions.KeepExactFormat Eklendi**
TxtLoadOptions sınıfına, dize/metin sayılara veya DateTime'a dönüştürüldüğünde hücre değeri için tam biçimlendirmenin korunması gerekip gerekmediğini gösteren KeepExactFormat özelliği eklendi. Bu özellik, CSV dosyalarından DateTime veya sayısal değerleri yüklemek için MS Excel uygulamasının davranışını eşleştirmek için eklenmiştir. MS Excel'in davranışını simüle etmek için, KeepExactFormat özelliğini false olarak ayarlayın, varsayılan değer ise true'dur, böylece hücre değeri CSV dosyasında dize olarak biçimlendirilecektir.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Özellik Shape.Id Eklendi**
Belirli bir elektronik tablodaki her bir şekil nesnesini benzersiz şekilde tanımlamak için Shape sınıfına Id özelliği eklenmiştir. Bu yeni özellik, aşağıda gösterildiği gibi bir elektronik tablodaki Grafik nesnelerinin tanımlanmasına da yardımcı olur.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Yöntem PlotArea.SetPositionAuto Eklendi**
Grafiğin çizim alanını otomatik moda ayarlamaya yardımcı olan PlotArea sınıfına SetPositionAuto yöntemi eklendi.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
