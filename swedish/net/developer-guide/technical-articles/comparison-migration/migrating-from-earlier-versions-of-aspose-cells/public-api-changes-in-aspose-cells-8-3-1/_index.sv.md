---
title: Förändringar i den offentliga API en i Aspose.Cells 8.3.1
type: docs
weight: 110
url: /sv/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.3.0 till 8.3.1 som kan vara av intresse för modul-/applikationsutvecklare.

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagd DataLabels.ShowCellRange Egenskap**
Egenskapen ShowCellRange har lagts till i DataLabels-klassen för att härma Excels funktionalitet att formatera diagrammets datamärken under körning. Observera att Excel tillhandahåller denna funktion genom följande steg. 

1. Välj Data Labels för serien och högerklicka för att öppna snabbmenyn.
1. Klicka på **Formatera Data Labels...** och det kommer att visa **Märkets alternativ**.
1. Markera eller avmarkera kryssrutan **Märket innehåller - Värde från celler**.

Exemplet nedan får åtkomst till Data Labels för diagramserien och ställer sedan in DataLabels.ShowCellRange-metoden till true för att härma Excels funktion **Märket innehåller - Värde från celler**.

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

Vänligen kontrollera artikeln [Visa cellintervall som datamärken](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) för mer information.

{{% /alert %}} 

### **Tillagd Cell.GetTable & ListObject.PutCellValue Metoder**
Metoderna Cell.GetTable & ListObject.PutCellValue har lagts till med Aspose.Cells for .NET 8.3.1 för att underlätta för användarna att komma åt ListObject från en cell och lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar. Exempelkoden nedan laddar källkalkylarket och lägger till värden inne i tabellen.

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

Vänligen kontrollera artikeln [Åtkomst till tabell från cell och lägga till värden inne i den med rad- och kolumnförskjutningar](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) för mer information.

{{% /alert %}} 

### **Tillagd OdsSaveOptions.IsStrictSchema11 Egenskap**
Egenskapen IsStrictSchema11 har lagts till i OdsSaveOptions-klassen för att tillåta utvecklare att spara kalkylarket i format som överensstämmer med ODF v1.2-specifikationen. Standardvärdet för Egenskapen IsStrictSchema11 är falskt, vilket innebär att från version 8.3.1 av Aspose.Cells API:er kommer ODS-filer att sparas som ODF-format version 1.2 som standard.

Nedan följer kodsnutt som sparar ODS-filen i ODF 1.2-format.

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

Vänligen kontrollera artikeln [Spara ODS-fil enligt ODF 1.1- och 1.2-specifikationerna](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) för mer information.

{{% /alert %}} 

### **Tillagd SparklineCollection.Add Metod**
Aspose.Cells API:er har exponerat SparklineCollection.Add(string dataRange, int row, int column) metoden för att ange Data Range och Location för Sparkline Group. Observera att Excel tillhandahåller samma funktion genom följande steg. 

1. Välj cellen som innehåller din Sparkline.
1. Välj **Redigera data** från avsnittet **Design** inne i fliken **Design**
1. Välj **Redigera gruppläge och data**.
1. Ange **Data Range** & **Location**.

Exempelkoden nedan laddar källkalkylarket, får åtkomst till den första sparkline gruppen och lägger till nya dataområden och platser för sparkline gruppen. 

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

Vänligen kontrollera artikeln [Kopiera Sparkline genom att ange Data Range och Location för Sparkline Group](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) för mer information.

{{% /alert %}}
