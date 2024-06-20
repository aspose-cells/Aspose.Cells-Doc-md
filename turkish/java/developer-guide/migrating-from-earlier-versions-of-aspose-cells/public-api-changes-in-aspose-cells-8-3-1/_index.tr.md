---
title: Aspose.Cells 8.3.1 de Genel API Değişiklikleri
type: docs
weight: 120
url: /tr/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.3.0 sürümünden 8.3.1'e olan değişiklikleri açıklar ve bu değişikliklerin modül / uygulama geliştiricileri için ilgi çekici olabileceğini açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **DataLabels.ShowCellRange Özelliği Eklendi**
DataLabels sınıfına, Grafik Veri Etiketlerinin çalışma zamanında biçimlendirilmesi Excel'in işlevselliğini taklit etmek için ShowCellRange özelliğinin getter/setter'ı eklenmiştir. Lütfen Excel, bu özelliği aşağıdaki adımlar aracılığıyla sağlar. 

1. Serinin Veri Etiketlerini seçin ve açılır menüyü açmak için sağ tıklayın.
1. **Veri Etiketlerini Biçimlendir...** öğesini tıklayın ve **Etiket Seçenekleri** görüntülenir.
1. **Etiket İçerir - Hücreden Değer** onay kutusunu işaretleyin veya işaretini kaldırın.

Aşağıdaki örnek kod, Grafik Serisinin Veri Etiketlerine erişir ve ardından Excel'in **Etiket İçerir - Hücreden Değer** özelliğini taklit etmek için DataLabels.setShowCellRange() yöntemini true olarak ayarlar.

**Java**

{{< highlight csharp >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için [Hücre Aralığını Veri Etiketleri Olarak Gösterme](/cells/tr/java/hucre-araligini-veri-etiketleri-olarak-gosterme/) makalesine bakın.

{{% /alert %}} 

### **Cell.getTable ve ListObject.putCellValue Yöntemleri Eklendi**
Aspose.Cells for Java 8.3.1 ile birlikte, Cell.getTable ve ListObject.putCellValue yöntemleri, kullanıcıların hücreden ListObject'e erişmesine ve satır ve sütun ofsetleri kullanarak içine değerler eklemesine olanak sağlamak üzere eklenmiştir. Aşağıdaki örnek kod, kaynak elektronik tabloyu yükler ve tablo içine değerler ekler.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için [Hücreden Tabloya Erişme ve Satır ve Sütun Ofsetleri Kullanarak Değer Ekleme](/cells/tr/java/hucreden-tabloya-erisme-ve-satir-ve-sutun-ofsetleri-kullanarak-deger-ekleme/) makalesine bakın.

{{% /alert %}} 

### **OdsSaveOptions.isStrictSchema11 ve OdsSaveOptions.setStrictSchema11 Yöntemleri Eklendi**
isStrictSchema11 ve setStrictSchema11 yöntemleri, OdsSaveOptions sınıfına ODF v1.2 belirtimine uygun biçimde elektronik tabloyu kaydetme olanağını sağlamak üzere eklenmiştir. setStrictSchema11 özelliğinin varsayılan değeri false'tur, yani Aspose.Cells API'lerinin 8.3.1 sürümüyle birlikte ODS dosyaları varsayılan olarak ODF formatı sürüm 1.2 olarak kaydedilecektir.

Aşağıdaki kod parçası, ODS dosyasını ODF 1.2 biçiminde kaydeder.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için [ODF 1.1 ve 1.2 Belirtimlerine Göre ODS Dosyasını Kaydetme](/cells/tr/java/odf-1-1-ve-1-2-belirtimlerine-gore-ods-dosyasini-kaydetme/) makalesine bakın.

{{% /alert %}} 

### **SparklineCollection.add Yöntemi Eklendi**
Aspose.Cells API'leri, SparklineCollection.add(String dataRange, int row, int column) yöntemini, Sparkline Grubunun Veri Aralığını ve Konumunu belirtmek için açığa çıkarmıştır. Lütfen Excel aynı özelliği aşağıdaki adımlar aracılığıyla sağlar. 

1. Sparkline içeren hücreyi seçin.
1. **Tasarım** sekmesi içindeki **Sparkline** bölümünden **Veri Düzenle**'yi seçin
1. **Grup Konumu ve Verisini Düzenle**'yi seçin.
1. **Veri Aralığı** ve **Konum** belirtin.

Aşağıdaki örnek kod, kaynak elektronik tabloyu yükler, ilk sparkline grubuna erişir ve sparkline grubu için yeni veri aralıkları ve konumlar ekler. 

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için [Sparkline Grubunun Veri Aralığını ve Konumunu Belirterek Sparkline Kopyalama](/cells/tr/java/sparkline-grubunun-veri-araligini-ve-konumunu-belirterek-sparkline-kopyalama/) makalesine bakın.

{{% /alert %}}
