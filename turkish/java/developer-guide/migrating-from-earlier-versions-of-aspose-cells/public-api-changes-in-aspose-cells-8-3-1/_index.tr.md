---
title: Genel API Aspose.Cells 8.3.1'deki değişiklikler
type: docs
weight: 120
url: /tr/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.3.0'dan 8.3.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır.

{{% /alert %}} 
## **Eklenen API'ler**
### **Özellik DataLabels.ShowCellRange Eklendi**
ShowCellRange özelliğine ilişkin alıcı/ayarlayıcı, Excel'in çalışma zamanında Çizelgenin Veri Etiketlerini biçimlendirme işlevselliğini taklit etmek için DataLabels sınıfına eklenmiştir. Lütfen Excel'in bu özelliği aşağıdaki adımlarla sağladığını unutmayın.

1. Serinin Veri Etiketleri'ni seçin ve açılır menüyü açmak için sağ tıklayın.
1.  Tıkla**Veri Etiketlerini Biçimlendir...** ve gösterecek**Etiket Seçenekleri**.
1.  Onay kutusunu işaretleyin veya işaretini kaldırın**Etiket İçeriği - Cells'den itibaren değer**.

 Aşağıdaki örnek kod, Grafik Serisinin Veri Etiketlerine erişir ve ardından Excel'in şu özelliğini taklit etmek için DataLabels.setShowCellRange() yöntemini true olarak ayarlar.**Etiket İçeriği - Cells'den itibaren değer**.

**Java**

{{< highlight "csharp" >}}

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

 Lütfen makaleyi kontrol edin[Veri Etiketleri Olarak Cell Aralığı Gösteriliyor](/cells/tr/java/showing-cell-range-as-the-data-labels/) daha fazla bilgi için.

{{% /alert %}} 

### **Yöntemler Cell.getTable & ListObject.putCellValue Eklendi**
Cell.getTable & ListObject.putCellValue metodları Aspose.Cells for Java 8.3.1 ile eklenmiştir. Kullanıcıların ListObject'e bir hücreden erişmesini ve satır ve sütun ofsetlerini kullanarak içine değer eklemesini kolaylaştırmak için. Aşağıdaki örnek kod, kaynak e-tabloyu yükler ve tablonun içine değerler ekler.

**Java**

{{< highlight "csharp" >}}

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

 Lütfen makaleyi kontrol edin[Cell'den Tabloya Erişmek ve Satır ve Sütun Ofsetlerini Kullanarak İçerisine Değerler Eklemek](/cells/tr/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) daha fazla bilgi için.

{{% /alert %}} 

### **Yöntemler OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 Eklendi**
Geliştiricilerin elektronik tabloyu ODF v1.2 spesifikasyonuna uygun biçimde kaydetmelerine olanak sağlamak için isStrictSchema11 & setStrictSchema11 yöntemleri OdsSaveOptions sınıfına eklenmiştir. setStrictSchema11 özelliğinin varsayılan değeri yanlıştır; bu, Aspose.Cells API'lerinin 8.3.1 sürümünden itibaren ODS dosyalarının varsayılan olarak ODF biçimi sürüm 1.2 olarak kaydedileceği anlamına gelir.

Aşağıda sağlanan kod parçacığı, ODS dosyasını ODF 1.2 biçiminde kaydeder.

**Java**

{{< highlight "csharp" >}}

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

 Lütfen makaleyi kontrol edin[ODS dosyasını ODF 1.1 ve 1.2 Teknik Özelliklerine kaydedin](/cells/tr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) daha fazla bilgi için.

{{% /alert %}} 

### **Yöntem SparklineCollection.add Eklendi**
 Aspose.Cells API'ler, Sparkline Grubunun Veri Aralığını ve Konumunu belirtmek için SparklineCollection.add(String dataRange, int satır, int sütun) yöntemini kullanıma sunmuştur. Lütfen Excel'in aynı özelliği aşağıdaki adımlarla sağladığını unutmayın.

1. Sparkline'ınızı içeren hücreyi seçin.
1.  Seçme**Mini Grafikten Verileri Düzenleme** içindeki bölüm**Tasarım** sekme
1.  Seçmek**Grup Konumunu ve Verilerini Düzenle**.
1.  Belirtin**Veri aralığı** & **Konum**.

 Aşağıdaki örnek kod, kaynak e-tabloyu yükler, ilk mini grafik grubuna erişir ve mini grafik grubu için yeni veri aralıkları ve konumları ekler.

**Java**

{{< highlight "csharp" >}}

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

 Lütfen makaleyi kontrol edin[Mini Grafik Grubunun Veri Aralığını ve Konumunu Belirterek Mini Tabloyu Kopyalayın](/cells/tr/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) daha fazla bilgi için.

{{% /alert %}}
