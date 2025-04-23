---
title: Aspose.Cells 8.3.1 de Genel API Değişiklikleri
type: docs
weight: 110
url: /tr/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.3.0 sürümünden 8.3.1'e olan değişiklikleri açıklar ve bu değişikliklerin modül / uygulama geliştiricileri için ilgi çekici olabileceğini açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **DataLabels.ShowCellRange Özelliği Eklendi**
DataLabels sınıfına ShowCellRange özelliği eklenmiştir, bu özellikle Excel'in çalışma zamanında Grafik Veri Etiketlerini biçimlendirme işlevini taklit etmek içindir. Lütfen Excel, bu özelliği aşağıdaki adımlarla sağlar. 

1. Serinin Veri Etiketlerini seçin ve açılır menüyü açmak için sağ tıklayın.
1. **Veri Etiketlerini Biçimlendir...** öğesini tıklayın ve **Etiket Seçenekleri** görüntülenir.
1. **Etiket İçerir - Hücreden Değer** onay kutusunu işaretleyin veya işaretini kaldırın.

Aşağıdaki örnek kod, Grafik Serisinin Data Labels'larına erişir ve sonra DataLabels.ShowCellRange yöntemini true olarak ayarlar ki bu Excel'in **Etiket İçerir - Hücre Değerinden** özelliğini taklit etmek içindir.

**C#**

{{< highlight csharp >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için lütfen [Hücre Aralığını Veri Etiketleri Olarak Gösterme](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) makalesini kontrol edin.

{{% /alert %}} 

### **Cell.GetTable & ListObject.PutCellValue Metodları Eklendi**
Cell.GetTable & ListObject.PutCellValue yöntemleri, kullanıcıların bir hücreden ListObject'e erişmelerini ve satır ve sütun ofsetleri kullanarak içine değer eklemelerini kolaylaştırmak için Aspose.Cells for .NET 8.3.1 ile eklenmiştir. Aşağıdaki örnek kod, kaynak elektronik tabloyu yükler ve tabloya içinde değerler ekler.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için lütfen [Hücreden Tabloya Erişme ve Satır ve Sütun Ofsetleri Kullanarak İçine Değer Eklemesi](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) makalesini kontrol edin.

{{% /alert %}} 

### **OdsSaveOptions.IsStrictSchema11 Özelliği Eklendi**
IsStrictSchema11 özelliği, geliştiricilere elektronik tabloyu ODF v1.2 özelliklerine uygun olarak kaydetmelerine izin vermek için OdsSaveOptions sınıfına eklenmiştir. IsStrictSchema11 özelliğinin varsayılan değeri false'dur, bu da Aspose.Cells API'nin 8.3.1 sürümünden itibaren ODS dosyalarının varsayılan olarak ODF format sürüm 1.2 olarak kaydedileceği anlamına gelir.

Aşağıdaki kod parçası, ODS dosyasını ODF 1.2 biçiminde kaydeder.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için lütfen [ODS Dosyasını ODF 1.1 ve 1.2 Özelliklerine Göre Kaydetme](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) makalesini kontrol edin.

{{% /alert %}} 

### **SparklineCollection.Add Metodu Eklendi**
Aspose.Cells API'ları, SparklineCollection.Add(string dataRange, int row, int column) yöntemini Kısa Çizgi Grubunun Veri Aralığını ve Konumunu belirtmek için açıklayarak sunmuştur. Lütfen Excel, aynı özelliği aşağıdaki adımlarla sağlar. 

1. Sparkline içeren hücreyi seçin.
1. **Tasarım** sekmesi içindeki **Sparkline** bölümünden **Veri Düzenle**'yi seçin
1. **Grup Konumu ve Verisini Düzenle**'yi seçin.
1. **Veri Aralığı** ve **Konum** belirtin.

Aşağıdaki örnek kod, kaynak elektronik tabloyu yükler, ilk sparkline grubuna erişir ve sparkline grubu için yeni veri aralıkları ve konumlar ekler. 

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için lütfen [Kısa Çizgi Grubunun Veri Aralığını ve Konumunu Belirtme](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) makalesini kontrol edin.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
