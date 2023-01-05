---
title: Genel API Aspose.Cells 8.3.1'deki değişiklikler
type: docs
weight: 110
url: /tr/net/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.3.0'dan 8.3.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır.

{{% /alert %}} 
## **Eklenen API'ler**
### **Özellik DataLabels.ShowCellRange Eklendi**
 ShowCellRange özelliği, çalışma zamanında Çizelgenin Veri Etiketlerini biçimlendirme Excel'in işlevselliğini taklit etmek için DataLabels sınıfına eklenmiştir. Lütfen Excel'in bu özelliği aşağıdaki adımlarla sağladığını unutmayın.

1. Serinin Veri Etiketleri'ni seçin ve açılır menüyü açmak için sağ tıklayın.
1.  Tıkla**Veri Etiketlerini Biçimlendir...** ve gösterecek**Etiket Seçenekleri**.
1.  Onay kutusunu işaretleyin veya işaretini kaldırın**Etiket İçeriği - Cells'den itibaren değer**.

 Aşağıdaki örnek kod, Grafik Serisinin Veri Etiketlerine erişir ve ardından Excel'in şu özelliğini taklit etmek için DataLabels.ShowCellRange yöntemini true olarak ayarlar.**Etiket İçeriği - Cells'den itibaren değer**.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}



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

 Lütfen makaleyi kontrol edin[Veri Etiketleri Olarak Cell Aralığı Gösteriliyor](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) daha fazla bilgi için.

{{% /alert %}} 

### **Yöntemler Cell.GetTable & ListObject.PutCellValue Eklendi**
Cell.GetTable & ListObject.PutCellValue metodları Aspose.Cells for .NET 8.3.1 ile eklenmiştir. Kullanıcıların ListObject'e bir hücreden erişmesini ve satır ve sütun ofsetlerini kullanarak içine değer eklemesini kolaylaştırmak için. Aşağıdaki örnek kod, kaynak e-tabloyu yükler ve tablonun içine değerler ekler.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 Lütfen makaleyi kontrol edin[Cell'den Tabloya Erişmek ve Satır ve Sütun Ofsetlerini Kullanarak İçerisine Değerler Eklemek](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) daha fazla bilgi için.

{{% /alert %}} 

### **Özellik OdsSaveOptions.IsStrictSchema11 Eklendi**
IsStrictSchema11 özelliği, geliştiricilerin elektronik tabloyu ODF v1.2 spesifikasyonuna uygun biçimde kaydetmesine izin vermek için OdsSaveOptions sınıfına eklenmiştir. IsStrictSchema11 özelliğinin varsayılan değeri yanlıştır; bu, Aspose.Cells API'lerinin 8.3.1 sürümünden itibaren ODS dosyalarının varsayılan olarak ODF formatı sürüm 1.2 olarak kaydedileceği anlamına gelir.

Aşağıda sağlanan kod parçacığı, ODS dosyasını ODF 1.2 biçiminde kaydeder.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 Lütfen makaleyi kontrol edin[ODS dosyasını ODF 1.1 ve 1.2 Teknik Özelliklerine kaydedin](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) daha fazla bilgi için.

{{% /alert %}} 

### **Yöntem SparklineCollection.Add Eklendi**
 Aspose.Cells API'ler, Sparkline Grubunun Veri Aralığını ve Konumunu belirtmek için SparklineCollection.Add(string dataRange, int row, int column) yöntemini kullanıma sunmuştur. Lütfen Excel'in aynı özelliği aşağıdaki adımlarla sağladığını unutmayın.

1. Sparkline'ınızı içeren hücreyi seçin.
1.  Seçme**Mini Grafikten Verileri Düzenleme** içindeki bölüm**Tasarım** sekme
1.  Seçmek**Grup Konumunu ve Verilerini Düzenle**.
1.  Belirtin**Veri aralığı** & **Konum**.

 Aşağıdaki örnek kod, kaynak e-tabloyu yükler, ilk mini grafik grubuna erişir ve mini grafik grubu için yeni veri aralıkları ve konumları ekler.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 Lütfen makaleyi kontrol edin[Mini Grafik Grubunun Veri Aralığını ve Konumunu Belirterek Mini Tabloyu Kopyalayın](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) daha fazla bilgi için.

{{% /alert %}}
