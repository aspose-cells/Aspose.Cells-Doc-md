---
title: Öffentliche API Änderungen in Aspose.Cells 8.3.1
type: docs
weight: 110
url: /de/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.3.0 auf 8.3.1, die für Modul-/Anwendungs-Entwickler interessant sein könnten.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügtes DataLabels.ShowCellRange-Eigenschaft**
Die Eigenschaft ShowCellRange wurde der DataLabels-Klasse hinzugefügt, um die Funktionalität von Excel zur Formatierung von Diagrammdatenbeschriftungen zur Laufzeit nachzuahmen. Bitte beachten Sie, dass Excel diese Funktion über die folgenden Schritte bereitstellt. 

1. Wählen Sie Datenetiketten der Serie aus und klicken Sie mit der rechten Maustaste, um das Popup-Menü zu öffnen.
1. Klicken Sie auf **Datenetiketten formatieren...** und es wird **Beschriftungsoptionen** angezeigt.
1. Aktivieren oder deaktivieren Sie das Kontrollkästchen **Beschriftung enthält – Wert aus Zellen**.

Der unten stehende Beispielscode greift auf die Datenbeschriftungen der Diagrammreihe zu und setzt dann die Methode DataLabels.ShowCellRange auf true, um die Funktion von Excel **Etikett enthält - Wert aus Zellen** nachzuahmen.

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

Bitte lesen Sie den Artikel [Anzeigen des Zellenbereichs als Datenbeschriftungen](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) für weitere Informationen.

{{% /alert %}} 

### **Hinzugefügte Methoden Cell.GetTable & ListObject.PutCellValue**
Die Methoden Cell.GetTable & ListObject.PutCellValue wurden mit Aspose.Cells for .NET 8.3.1 hinzugefügt, um den Benutzern den Zugriff auf das ListObject von einer Zelle aus und das Hinzufügen von Werten darin mithilfe der Zeilen- und Spaltenoffsets zu erleichtern. Der folgende Beispielscode lädt die Quellentabelle und fügt Werte in die Tabelle ein.

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

Bitte lesen Sie den Artikel [Zugriff auf Tabelle aus Zelle und Hinzufügen von Werten mithilfe von Zeilen- und Spaltenoffsets](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) für weitere Informationen.

{{% /alert %}} 

### **Hinzugefügte Eigenschaft OdsSaveOptions.IsStrictSchema11**
Die Eigenschaft IsStrictSchema11 wurde der Klasse OdsSaveOptions hinzugefügt, um den Entwicklern das Speichern der Arbeitsmappe in einem Format gemäß der ODF v1.2-Spezifikation zu ermöglichen. Der Standardwert der Eigenschaft IsStrictSchema11 ist false, das bedeutet, dass ab Version 8.3.1 der Aspose.Cells-APIs die ODS-Dateien standardmäßig als ODF-Format Version 1.2 gespeichert werden.

Der unten bereitgestellte Codeschnipsel speichert die ODS-Datei im ODF 1.2-Format.

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

Bitte lesen Sie den Artikel [Speichern von ODS-Dateien in den ODF 1.1- und 1.2-Spezifikationen](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) für weitere Informationen.

{{% /alert %}} 

### **Hinzugefügte SparklineCollection.Add-Methode**
Aspose.Cells-APIs haben die Methode SparklineCollection.Add(string dataRange, int row, int column) freigegeben, um den Datenbereich und den Speicherort der Sparkline-Gruppe anzugeben. Bitte beachten Sie, dass Excel die gleiche Funktion durch folgende Schritte bereitstellt. 

1. Wählen Sie die Zelle mit Ihrer Sparkline aus.
1. Wählen Sie **Daten bearbeiten** im Bereich **Entwurf** aus.
1. Wählen Sie **Gruppenposition & Daten bearbeiten** aus.
1. Geben Sie den **Datenbereich** & **Ort** an.

Der folgende Beispielcode lädt die Quellentabelle, greift auf die erste Sparkline-Gruppe zu und fügt neue Datenbereiche und Positionen für die Sparkline-Gruppe hinzu. 

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

Bitte lesen Sie den Artikel [Sparkline kopieren, indem der Datenbereich und der Speicherort der Sparkline-Gruppe angegeben werden](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) für weitere Informationen.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
