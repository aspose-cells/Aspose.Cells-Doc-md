---
title: Aspose.Cells 8.4.2 de Genel API Değişiklikleri
type: docs
weight: 150
url: /tr/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.4.1'den 8.4.2'ye yapılan değişiklikleri, modül/uygulama geliştiricilerinin ilgisini çekebilecek herhangi yeni ve güncellenmiş genel yöntemleri [eklendi sınıflar, vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-2/) ve aynı zamanda Aspose.Cells'in arka planındaki herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Geliştirilmiş Grafik Oluşturma Mekanizması**
Aspose.Cells.Charts.Chart sınıfı, grafik oluşturmanın görevini kolaylaştırmak için SetChartDataRange yöntemini açığa çıkardı. SetChartDataRange yöntemi, veri serilerini çizmek için hücre alanını belirten string türünde ilk parametre ve grafik veri serilerini işaret eden hücre değerlerinin satır veya sütun tarafından çizilip çizilmeyeceğini belirten Boolean türünde ikinci bir parametre kabul eder.

Aşağıdaki kod parçası, grafik sütunu oluşturmanın bir kaç satır kodla nasıl yapılacağını gösterir. Bu durumda çizelgenin grafiği hücre A1'den D4'e kadar aynı çalışma sayfasında bulunmalıdır.

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **VbaModuleCollection.Add Method Eklendi**
Aspose.Cells for .NET 8.4.2, Bir çalışma kitabı örneğine yeni bir VBA modül eklemek için VbaModuleCollection.Add yöntemini kullanıma sunmuştur. VbaModuleCollection.Add yöntemi, eklenecek bir Çalışsayfaları türündeki parametreyi kabul eder.

Aşağıdaki kod bloğu, VbaModuleCollection.Add yöntemini nasıl kullanacağını gösterir.

**C#**

{{< highlight csharp >}}

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


### **Overloaded Method Cells.CopyColumns Eklendi**
Aspose.Cells for .NET 8.4.2, Kaynak sütunları hedefe tekrarlamak için Cells.CopyColumns yönteminin aşırı yüklenmiş bir sürümünü kullanıma sunmuştur. Yeni eklenen yöntem, toplamda 5 parametre kabul eder, ilk 4 parametre ortak Cells.CopyColumns yöntemiyle aynıdır. Ancak, tamsayı türünden son parametre, kaynak sütunlarının tekrarlanacağı hedef sütunların sayısını belirtir.

Aşağıdaki kod bloğu, yeni eklenen Cells.CopyColumns yöntemini nasıl kullanacağını gösterir.

**C#**

{{< highlight csharp >}}

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


### **Enumerasyon Fields PasteType.Default & PasteType.DefaultExceptBorders Eklendi**
V8.4.2'nin yayınlanmasıyla, Aspose.Cells API'si PasteType için 2 yeni numaralandırma alanı ekledi.

- PasteType.Default: Hücre aralığını yapıştırma işlevselliği Excel'in "Tümü" işlevselliğine benzer şekilde çalışır.
- PasteType.DefaultExceptBorders: Hücre aralığını yapıştırma işlevselliği Excel'in "Kenarlıklar hariç tümü" işlevselliğine benzer şekilde çalışır.

Aşağıdaki örnek kod, PasteType.Default alanının kullanımını gösterir.

**C#**

{{< highlight csharp >}}

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

Aspose.Cells for .NET 8.4.2'den başlayarak, PasteType.All enumerasyon alanı, Excel'in "Tümü" işlevselliğine kıyasla farklı şekilde davranır. Artık PasteType.All, hedef aralığa sütun genişliklerini de kopyalar, Excel'in "Tümü" işlevselliğinin aksine. Excel'in "Tümü" davranışını taklit etmek için, lütfen PasteType.Default'i kullanın.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
