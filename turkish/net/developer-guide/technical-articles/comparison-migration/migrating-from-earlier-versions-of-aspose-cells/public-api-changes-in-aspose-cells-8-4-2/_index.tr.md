---
title: Genel API Aspose.Cells 8.4.2'deki değişiklikler
type: docs
weight: 150
url: /tr/net/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.4.1'den 8.4.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-2/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Geliştirilmiş Grafik Oluşturma Mekanizması**
Aspose.Cells.Charts.Chart sınıfı, grafik oluşturma görevini kolaylaştırmak için SetChartDataRange yöntemini kullanıma sunmuştur. SetChartDataRange yöntemi iki parametre kabul eder; burada ilk parametre, veri serisinin çizileceği hücre alanını belirten dize türündedir. İkinci parametre, çizim yönünü belirten Boolean türündedir, yani; grafik veri serisinin bir dizi hücre değeri aralığından satıra mı yoksa sütunlara göre mi çizileceğini belirler.

Aşağıdaki kod parçacığı, grafiğin arsa serisi verilerinin A1 hücresinden D4'e kadar aynı çalışma sayfasında bulunduğunu varsayarak birkaç satır kod içeren bir sütun grafiğinin nasıl oluşturulacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Yöntem VbaModuleCollection.Add Eklendi**
Aspose.Cells for .NET 8.4.2, Workbook örneğine yeni bir VBA modülü eklemek için VbaModuleCollection.Add yöntemini kullanıma sundu. VbaModuleCollection.Add yöntemi, çalışma sayfasına özel bir modül eklemek için Worksheet türünde bir parametre kabul eder.

Aşağıdaki kod parçacığı, VbaModuleCollection.Add yönteminin nasıl kullanılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **Aşırı Yüklenmiş Yöntem Cells.CopyColumns Eklendi**
Aspose.Cells for .NET 8.4.2, kaynak sütunları hedefte tekrarlamak için Cells.CopyColumns yönteminin aşırı yüklenmiş bir sürümünü kullanıma sundu. Yeni kullanıma sunulan yöntem toplamda 5 parametre kabul eder ve ilk 4 parametre ortak Cells.CopyColumns yöntemiyle aynıdır. Ancak int türündeki son parametre, kaynak sütunların üzerinde tekrarlanması gereken hedef sütunların sayısını belirtir.

Aşağıdaki kod parçacığı, yeni kullanıma sunulan Cells.CopyColumns yönteminin nasıl kullanılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Numaralandırma Alanları PasteType.Default & PasteType.DefaultExceptBorders Eklendi**
v8.4.2 sürümüyle birlikte Aspose.Cells API, PasteType için aşağıda ayrıntıları verilen 2 yeni numaralandırma alanı ekledi.

- PasteType.Default: Hücre aralığını yapıştırmak için Excel'in "Tümü" işlevine benzer şekilde çalışır.
- PasteType.DefaultExceptBorders: Hücre aralığını yapıştırmak için Excel'in "Kenarlıklar hariç tümü" işlevine benzer şekilde çalışır.

Aşağıdaki örnek kod, PasteType.Default alanının kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Aspose.Cells for .NET 8.4.2 sürümünden başlayarak, PasteType.All dosyalanan numaralandırma, hücre aralığını yapıştırmak için Excel'in "Tümü" işlevine kıyasla farklı davranır. Şimdi PasteType.All, Excel'in "Tümü" işlevselliğinin aksine sütun genişliklerini hedef aralığa da kopyalar. Excel'in "Tümü" davranışını taklit etmek için lütfen PasteType.Default'u kullanın.

{{% /alert %}}
