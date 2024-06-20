---
title: Öffentliche API Änderungen in Aspose.Cells 8.3.1
type: docs
weight: 120
url: /de/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.3.0 auf 8.3.1, die für Modul-/Anwendungs-Entwickler interessant sein könnten.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügtes DataLabels.ShowCellRange-Eigenschaft**
Der Getter/Setter für die Eigenschaft ShowCellRange wurde der DataLabels-Klasse hinzugefügt, um die Funktionalität von Excels Formatierung von Diagrammdatenaufklebern zur Laufzeit zu imitieren. Bitte beachten Sie, dass Excel diese Funktion durch die folgenden Schritte bereitstellt. 

1. Wählen Sie Datenetiketten der Serie aus und klicken Sie mit der rechten Maustaste, um das Popup-Menü zu öffnen.
1. Klicken Sie auf **Datenetiketten formatieren...** und es wird **Beschriftungsoptionen** angezeigt.
1. Aktivieren oder deaktivieren Sie das Kontrollkästchen **Beschriftung enthält – Wert aus Zellen**.

Der nachstehende Beispielcode greift auf die Datenetiketten der Diagrammserie zu und setzt dann die Methode DataLabels.setShowCellRange() auf true, um die Funktion von Excel **Beschriftung enthält – Wert aus Zellen** zu imitieren.

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

Bitte überprüfen Sie den Artikel [Anzeigen des Zellenbereichs als Datenetiketten](/cells/de/java/showing-cell-range-as-the-data-labels/) für weitere Informationen.

{{% /alert %}} 

### **Hinzugefügte Cell.getTable & ListObject.putCellValue Methoden**
Die Methoden Cell.getTable & ListObject.putCellValue wurden mit Aspose.Cells for Java 8.3.1 hinzugefügt, um den Benutzern den Zugriff auf das ListObject von einer Zelle aus und das Hinzufügen von Werten darin mithilfe der Zeilen- und Spaltenversätze zu erleichtern. Der folgende Beispielcode lädt die Quelltabelle und fügt Werte innerhalb der Tabelle hinzu.

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

Bitte überprüfen Sie den Artikel [Zugriff auf Tabelle von Zelle aus und Hinzufügen von Werten mithilfe von Zeilen- und Spaltenversätzen](/cells/de/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) für weitere Informationen.

{{% /alert %}} 

### **Hinzugefügte OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 Methoden**
Die Methoden isStrictSchema11 & setStrictSchema11 wurden der OdsSaveOptions-Klasse hinzugefügt, um den Entwicklern das Speichern der Tabelle im Format gemäß der ODF v1.2-Spezifikation zu ermöglichen. Der Standardwert der Eigenschaft setStrictSchema11 ist false, das heißt, ab der Version 8.3.1 der Aspose.Cells-APIs werden die ODS-Dateien standardmäßig als ODF-Format Version 1.2 gespeichert.

Der unten bereitgestellte Codeschnipsel speichert die ODS-Datei im ODF 1.2-Format.

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

Bitte überprüfen Sie den Artikel [Speichern von ODS-Datei in ODF 1.1 und 1.2-Spezifikationen](/cells/de/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) für weitere Informationen.

{{% /alert %}} 

### **Hinzugefügte SparklineCollection.add Methode**
Aspose.Cells-APIs haben die Methode SparklineCollection.add(String dataRange, int row, int column) freigegeben, um den Datenbereich und den Standort der Sparkline-Gruppe anzugeben. Bitte beachten Sie, dass Excel dieselbe Funktion durch folgende Schritte bereitstellt. 

1. Wählen Sie die Zelle mit Ihrer Sparkline aus.
1. Wählen Sie **Daten bearbeiten** im Bereich **Entwurf** aus.
1. Wählen Sie **Gruppenposition & Daten bearbeiten** aus.
1. Geben Sie den **Datenbereich** & **Ort** an.

Der folgende Beispielcode lädt die Quellentabelle, greift auf die erste Sparkline-Gruppe zu und fügt neue Datenbereiche und Positionen für die Sparkline-Gruppe hinzu. 

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

Bitte überprüfen Sie den Artikel [Kopieren von Sparkline durch Angabe von Datenbereich und Position der Sparkline-Gruppe](/cells/de/java/kopieren-von-sparkline-durch-angabe-von-datenbereich-und-position-der-sparkline-gruppe/) für weitere Informationen.

{{% /alert %}}
