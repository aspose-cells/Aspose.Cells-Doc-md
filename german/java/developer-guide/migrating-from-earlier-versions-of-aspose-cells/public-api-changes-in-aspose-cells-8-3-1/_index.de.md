---
title: Öffentlich API Änderungen in Aspose.Cells 8.3.1
type: docs
weight: 120
url: /de/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.3.0 zu 8.3.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Eigenschaft DataLabels.ShowCellRange hinzugefügt**
Der Getter/Setter für die Eigenschaft ShowCellRange wurde der DataLabels-Klasse hinzugefügt, um die Excel-Funktionalität zum Formatieren der Datenbeschriftungen von Chart zur Laufzeit nachzuahmen. Bitte beachten Sie, dass Excel diese Funktion durch die folgenden Schritte bereitstellt.

1. Wählen Sie Datenetiketten der Serie und klicken Sie mit der rechten Maustaste, um das Popup-Menü zu öffnen.
1.  Drücke den**Datenbeschriftungen formatieren...** und es wird sich zeigen**Beschriftungsoptionen**.
1.  Aktivieren oder deaktivieren Sie das Kontrollkästchen**Etikett enthält - Wert von Cells**.

 Der folgende Beispielcode greift auf die Datenbeschriftungen der Diagrammreihe zu und setzt dann die Methode DataLabels.setShowCellRange() auf true, um die Funktion von Excel nachzuahmen**Etikett enthält - Wert von Cells**.

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

 Bitte überprüfen Sie den Artikel[Anzeige des Bereichs Cell als Datenbeschriftung](/cells/de/java/showing-cell-range-as-the-data-labels/) für mehr Informationen.

{{% /alert %}} 

### **Methoden Cell.getTable & ListObject.putCellValue hinzugefügt**
Die Methoden Cell.getTable & ListObject.putCellValue wurden mit Aspose.Cells for Java 8.3.1 hinzugefügt, um den Benutzern den Zugriff auf das ListObject von einer Zelle aus zu erleichtern und darin mithilfe der Zeilen- und Spaltenoffsets Werte hinzuzufügen. Der folgende Beispielcode lädt die Quelltabelle und fügt Werte in die Tabelle ein.

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

 Bitte überprüfen Sie den Artikel[Zugriff auf die Tabelle von Cell und Hinzufügen von Werten darin mithilfe von Zeilen- und Spalten-Offsets](/cells/de/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) für mehr Informationen.

{{% /alert %}} 

### **Methoden OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 Hinzugefügt**
Die Methoden isStrictSchema11 und setStrictSchema11 wurden der OdsSaveOptions-Klasse hinzugefügt, damit die Entwickler die Tabelle in einem Format speichern können, das der ODF v1.2-Spezifikation entspricht. Der Standardwert der Eigenschaft setStrictSchema11 ist false, d. h. ab Version 8.3.1 der Aspose.Cells-APIs werden die ODS-Dateien standardmäßig im ODF-Format Version 1.2 gespeichert.

Das unten bereitgestellte Code-Snippet speichert die Datei ODS im ODF 1.2-Format.

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

 Bitte überprüfen Sie den Artikel[Speichern Sie die Datei ODS in den ODF 1.1- und 1.2-Spezifikationen](/cells/de/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) für mehr Informationen.

{{% /alert %}} 

### **Methode SparklineCollection.add Hinzugefügt**
 Aspose.Cells APIs haben die SparklineCollection.add(String dataRange, int row, int column)-Methode verfügbar gemacht, um den Datenbereich und den Speicherort der Sparkline-Gruppe anzugeben. Bitte beachten Sie, dass Excel die gleiche Funktion durch die folgenden Schritte bietet.

1. Wählen Sie die Zelle aus, die Ihre Sparkline enthält.
1.  Wählen**Bearbeiten Sie Daten aus der Sparkline** Abschnitt innerhalb der**Design** Tab
1.  Wählen**Standort und Daten der Gruppe bearbeiten**.
1.  Angeben**Datenreichweite** & **Standort**.

 Der folgende Beispielcode lädt die Quelltabelle, greift auf die erste Sparkline-Gruppe zu und fügt neue Datenbereiche und Positionen für die Sparkline-Gruppe hinzu.

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

 Bitte überprüfen Sie den Artikel[Kopieren Sie die Sparkline, indem Sie den Datenbereich und den Speicherort der Sparkline-Gruppe angeben](/cells/de/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) für mehr Informationen.

{{% /alert %}}
