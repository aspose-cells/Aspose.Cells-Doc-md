---
title: Aspose.Cells 8.4.2 de Genel API Değişiklikleri
type: docs
weight: 160
url: /tr/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Bu belge, uygulama geliştiricileri için Aspose.Cells API'sinde 8.4.1'den 8.4.2'ye yapılan değişiklikleri içermektedir. Sadece yeni ve güncellenmiş genel yöntemleri, [eklenmiş sınıfları vs.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-2/) değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki değişikliklerin de açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Geliştirilmiş Grafik Oluşturma Mekanizması**
com.aspose.cells.charts.Chart sınıfı, chart oluşturmanın görevini kolaylaştırmak için setChartDataRange methodunu kullanıma sunmuştur. setChartDataRange methodu, veri serilerini çizmek için hücre alanını belirten bir string türünden ve çizim yönlendirmesini (yani; veri serilerini satır veya sütun olarak çizmek) belirten Boolean türünden iki parametreyi kabul eder.

Aşağıdaki kod parçası, grafik sütunu oluşturmanın bir kaç satır kodla nasıl yapılacağını gösterir. Bu durumda çizelgenin grafiği hücre A1'den D4'e kadar aynı çalışma sayfasında bulunmalıdır.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **VbaModuleCollection.add Method Eklenmiş**
Aspose.Cells for Java 8.4.2, VbaModuleCollection.add yöntemini çalışma kitabına yeni bir VBA modülü eklemek için kullanıma sundu. VbaModuleCollection.add yöntemi, eklemek için bir çalışma sayfası türünde bir parametre kabul eder.

Aşağıdaki kod parçası, VbaModuleCollection.add yönteminin nasıl kullanılacağını gösterir.

**Java**

{{< highlight csharp >}}

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

### **Yüklenmiş Method Cells.copyColumns Eklendi**
Aspose.Cells for Java 8.4.2, Cells.copyColumns yönteminin aşırı yüklenmiş bir sürümünü kullanıma sundu. Yeni eklenen yöntem, toplamda 5 parametre kabul eder, ilk 4 parametre, standart Cells.copyColumns yöntemiyle aynıdır. Ancak, son parametre int tipindedir ve kaynak sütunların hedef üzerine tekrarlanacak sütun sayısını belirtir.

Aşağıdaki kod parçası, yeni eklenen Cells.copyColumns yönteminin nasıl kullanılacağını gösterir.

**Java**

{{< highlight csharp >}}

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
V8.4.2'nin yayınlanmasıyla, Aspose.Cells API'si PasteType için 2 yeni numaralandırma alanı ekledi.

- PasteType.DEFAULT: Hücre aralığını yapıştırmak için Excel'in "Hepsini" işleviyle benzer şekilde çalışır.
- PasteType.ALL_EXCEPT_BORDERS: Hücre aralığını yapıştırmak için Excel'in "Tüm sınırlar hariç" işleviyle benzer şekilde çalışır.

Aşağıdaki örnek kod, PasteType.DEFAULT alanının nasıl kullanılacağını gösterir.

**Java**

{{< highlight csharp >}}

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

Aspose.Cells for Java 8.4.2'den itibaren, PasteType.ALL numaralandırma alanı, Excel'in "Hepsini" işlevinden farklı olarak, artık sütun genişliklerini hedef aralığa kopyalar. Excel'in "Hepsini" işlevine benzetmek için, lütfen PasteType.DEFAULT kullanın.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
