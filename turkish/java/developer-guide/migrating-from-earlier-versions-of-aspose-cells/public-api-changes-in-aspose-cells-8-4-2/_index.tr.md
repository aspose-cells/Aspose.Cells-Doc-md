---
title: Genel API Aspose.Cells 8.4.2'deki değişiklikler
type: docs
weight: 160
url: /tr/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.4.1'den 8.4.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-2/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Geliştirilmiş Grafik Oluşturma Mekanizması**
com.aspose.cells.charts.Chart sınıfı, grafik oluşturma görevini kolaylaştırmak için setChartDataRange yöntemini kullanıma sunmuştur. setChartDataRange yöntemi iki parametre kabul eder; burada ilk parametre, veri serisinin çizileceği hücre alanını belirten dize türündedir. İkinci parametre, çizim yönünü belirten Boolean türündedir, yani; grafik veri serisinin bir dizi hücre değeri aralığından satıra mı yoksa sütunlara göre mi çizileceğini belirler.

Aşağıdaki kod parçacığı, grafiğin arsa serisi verilerinin A1 hücresinden D4'e kadar aynı çalışma sayfasında bulunduğunu varsayarak birkaç satır kod içeren bir sütun grafiğinin nasıl oluşturulacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Yöntem VbaModuleCollection.add Eklendi**
Aspose.Cells for Java 8.4.2, Workbook örneğine yeni bir VBA modülü eklemek için VbaModuleCollection.add yöntemini kullanıma sundu. VbaModuleCollection.add yöntemi, çalışma sayfasına özel bir modül eklemek için Çalışma Sayfası türünde bir parametre kabul eder.

Aşağıdaki kod parçacığı, VbaModuleCollection.add yönteminin nasıl kullanılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Aşırı Yüklenmiş Yöntem Cells.copyColumns Eklendi**
Aspose.Cells for Java 8.4.2, hedefte kaynak sütunları tekrarlamak için Cells.copyColumns yönteminin aşırı yüklenmiş bir sürümünü kullanıma sundu. Yeni kullanıma sunulan yöntem toplamda 5 parametre kabul eder ve ilk 4 parametre ortak Cells.copyColumns yöntemiyle aynıdır. Ancak int türündeki son parametre, kaynak sütunların üzerinde tekrarlanması gereken hedef sütunların sayısını belirtir.

Aşağıdaki kod parçacığı, yeni kullanıma sunulan Cells.copyColumns yönteminin nasıl kullanılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Numaralandırma Alanları PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS Eklendi**
v8.4.2 sürümüyle birlikte Aspose.Cells API, PasteType için aşağıda ayrıntıları verilen 2 yeni numaralandırma alanı ekledi.

- PasteType.DEFAULT: Hücre aralığını yapıştırmak için Excel'in "Tümü" işlevine benzer şekilde çalışır.
- YapıştırTürü.TÜMÜ_HARİÇ_KENARLAR: Hücre aralığını yapıştırmak için Excel'in "Kenarlıklar hariç tümü" işlevine benzer şekilde çalışır.

Aşağıdaki örnek kod, PasteType.DEFAULT alanının kullanımını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Aspose.Cells for Java 8.4.2 sürümünden başlayarak, PasteType.ALL dosyalanan numaralandırma, hücre aralığını yapıştırmak için Excel'in "Tümü" işlevine kıyasla farklı davranır. Artık PasteType.ALL, Excel'in "Tümü" işlevinin aksine, sütun genişliklerini hedef aralığa da kopyalar. Excel'in "Tümü" davranışını taklit etmek için lütfen PasteType.DEFAULT'u kullanın.

{{% /alert %}}
