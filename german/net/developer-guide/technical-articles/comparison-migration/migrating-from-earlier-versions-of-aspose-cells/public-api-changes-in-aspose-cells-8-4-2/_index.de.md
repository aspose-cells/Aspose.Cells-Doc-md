---
title: Öffentliche API Änderungen in Aspose.Cells 8.4.2
type: docs
weight: 150
url: /de/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.4.1 bis 8.4.2, die für Modul-/Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen etc.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-2/), sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Verbessertes Diagrammerstellungsmechanismus**
Die Aspose.Cells.Charts.Chart-Klasse hat die SetChartDataRange-Methode freigelegt, um die Aufgabe der Diagrammerstellung zu erleichtern. Die SetChartDataRange-Methode akzeptiert zwei Parameter, wobei der erste Parameter vom Typ String den Zellenbereich angibt, aus dem die Datenreihen geplottet werden sollen. Der zweite Parameter vom Typ Boolean gibt die Plot-Ausrichtung an, d.h. ob die Diagrammdatenreihen aus einem Bereich von Zellwerten nach Zeilen oder Spalten geplottet werden sollen.

Der folgende Codeausschnitt zeigt, wie Sie mit wenigen Zeilen Code ein Säulendiagramm erstellen können, wobei angenommen wird, dass die Diagrammseriendaten auf demselben Arbeitsblatt von Zelle A1 bis D4 vorhanden sind.

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Methode VbaModuleCollection.Add hinzugefügt**
Aspose.Cells for .NET 8.4.2 hat die VbaModuleCollection.Add-Methode freigegeben, um ein neues VBA-Modul zur Instanz der Arbeitsmappe hinzuzufügen. Die VbaModuleCollection.Add-Methode akzeptiert einen Parameter vom Typ Arbeitsblatt, um ein arbeitsblattspezifisches Modul hinzuzufügen.

Der folgende Codeausschnitt zeigt, wie die VbaModuleCollection.Add-Methode verwendet wird.

**C#**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **Überladene Methode Cells.CopyColumns hinzugefügt**
Aspose.Cells for .NET 8.4.2 hat eine überladene Version der Cells.CopyColumns-Methode freigegeben, um die Quellspalten auf das Ziel zu wiederholen. Die neu freigegebene Methode akzeptiert insgesamt 5 Parameter, wobei die ersten 4 Parameter dasselbe sind wie bei der üblichen Cells.CopyColumns-Methode. Der letzte Parameter vom Typ int gibt die Anzahl der Zielspalten an, auf die die Quellspalten wiederholt werden sollen.

Der folgende Codeausschnitt zeigt, wie die neu freigegebene Cells.CopyColumns-Methode verwendet wird.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Enumeration Felder PasteType.Default & PasteType.DefaultExceptBorders hinzugefügt**
Mit der Version 8.4.2 hat die Aspose.Cells-API 2 neue Enumerationsfelder für PasteType hinzugefügt.

- PasteType.Default: Funktioniert ähnlich wie die "Alle"-Funktion von Excel zum Einfügen eines Zellbereichs.
- PasteType.DefaultExceptBorders: Funktioniert ähnlich wie die "Alle außer Rahmen"-Funktion von Excel zum Einfügen eines Zellbereichs.

Der folgende Beispielcode zeigt die Verwendung des Feldes PasteType.Default.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Ab der Veröffentlichung von Aspose.Cells for .NET 8.4.2 verhält sich das Enumerationsfeld PasteType.All im Vergleich zur "Alle"-Funktion von Excel zum Einfügen von Zellenbereichen anders. Jetzt kopiert PasteType.All auch die Spaltenbreiten auf den Zielbereich, im Gegensatz zur "Alle"-Funktion von Excel. Um das Verhalten von Excel "Alle" nachzuahmen, verwenden Sie bitte das PasteType.Default.

{{% /alert %}}
