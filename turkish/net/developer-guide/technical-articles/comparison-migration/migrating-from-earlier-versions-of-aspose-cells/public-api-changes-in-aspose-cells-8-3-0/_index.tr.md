---
title: Aspose.Cells 8.3.0 da Genel API Değişiklikleri
type: docs
weight: 100
url: /tr/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerin ilgisini çekebilecek Aspose.Cells API'sindeki 8.2.2'den 8.3.0'a yapılan değişiklikleri açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **WorkbookSettings.AutoRecover Özelliği Eklendi**
Yeni AutoRecover özelliği, uygulamalarındaki elektronik tablolar için Otomatik Kurtarma seçeneğini ayarlamak için WorkbookSettings sınıfına eklenmiştir.

{{% alert color="primary" %}} 

Daha fazla bilgi için lütfen [Elektronik Tablo Oto Kurtarma Ayarı](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) makalesine bakın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **WorkbookSettings.CrashSave Özelliği Eklendi**
WorkbookSettings sınıfına, uygulamanın son çökmesinden sonra elektronik tablo dosyasını kaydedip kaydetmediğini gösteren Boolean tipi bir CrashSave özelliği eklenmiştir.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **WorkbookSettings.DataExtractLoad Özelliği Eklendi**
DataExtractLoad özelliği, geliştiricilere elektronik tabloya en son yapılan kurtarma hakkında bilgi alınmasını sağlamak için WorkbookSettings sınıfına eklenmiştir. DataExtractLoad özelliği true döndürürse, bu, elektronik tabloda veri kurtarımının gerçekleştirildiğini gösterir.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **WorkbookSettings.RepairLoad Özelliği Eklendi**
RepairLoad özelliği, elektronik tablonun Excel uygulamasıyla son yüklemede onarıldığını gösterir.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **TxtLoadOptions.KeepExactFormat Özelliği Eklendi**
KeepExactFormat özelliği, metin/dizge sayıya veya TarihSaat'e dönüştürüldüğünde hücre değerinin tam biçiminin korunup korunmayacağını belirtir. Bu özellik, CSV dosyalarından TarihSaat veya sayısal değerleri yüklerken MS Excel programının davranışını eşleştirmek için eklenmiştir. MS Excel'in davranışını taklit etmek için KeepExactFormat özelliğini false olarak ayarlayın, varsayılan değer true olduğu için hücre değeri CSV dosyasındaki dize şeklinde biçimlendirilecektir.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Shape.Id Özelliği Eklendi**
Shape sınıfına her bir şekil nesnesini benzersiz olarak tanımlamak için Id özelliği eklenmiştir. Bu yeni özellik ayrıca elektronik tabloda Grafik nesnelerini tanımlamada da yardımcı olur.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Eklendi - PlotArea.SetPositionAuto Metodu**
SetPositionAuto metodu, Grafik bölgesinin otomatik moda ayarlanmasına yardımcı olan PlotArea sınıfına eklenmiştir.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
