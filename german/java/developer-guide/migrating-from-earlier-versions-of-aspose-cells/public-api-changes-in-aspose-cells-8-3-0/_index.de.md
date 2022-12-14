---
title: Öffentlich API Änderungen in Aspose.Cells 8.3.0
type: docs
weight: 110
url: /de/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.2.2 zu 8.3.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Eigenschaft WorkbookSettings.AutoRecover Hinzugefügt**
Der Getter/Setter für die Eigenschaft AutoRecover wurde der WorkbookSettings-Klasse hinzugefügt, damit Entwickler die Option der automatischen Wiederherstellung für die Tabellenkalkulationen in ihren Anwendungen abrufen/festlegen können.

{{% alert color="primary" %}} 

 Bitte überprüfen Sie den Artikel[Einstellen der automatischen Wiederherstellung der Tabellenkalkulation](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) für mehr Informationen.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Eigenschaft WorkbookSettings.CrashSave Hinzugefügt**
Die Getter/Setter für die Eigenschaft CrashSave wurden der WorkbookSettings-Klasse hinzugefügt. Die Eigenschaft des booleschen Typs gibt an, ob die Anwendung die Arbeitsmappendatei zuletzt nach einem Absturz gespeichert hat.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Eigenschaft WorkbookSettings.DataExtractLoad Hinzugefügt**
Die Getter/Setter für die Eigenschaft DataExtractLoad wurden der WorkbookSettings-Klasse hinzugefügt, damit die Entwickler die Informationen zur letzten Wiederherstellung abrufen/festlegen können. Wenn die Eigenschaft DataExtractLoad true zurückgibt, bedeutet dies, dass die Datenwiederherstellung für die Arbeitsmappendatei durchgeführt wurde.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Eigenschaft WorkbookSettings.RepairLoad Hinzugefügt**
Die Getter/Setter für die Eigenschaft RepairLoad wurden der WorkbookSettings-Klasse hinzugefügt. Die Eigenschaft des booleschen Typs gibt an, ob das Arbeitsblatt in der letzten Ladesitzung mit der Excel-Anwendung repariert wurde.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Eigenschaft TxtLoadOptions.KeepExactFormat Hinzugefügt**
Der TxtLoadOptions-Klasse wurde die Eigenschaft KeepExactFormat hinzugefügt, die angibt, ob die exakte Formatierung für den Zellenwert beibehalten werden soll, wenn String/Text in Zahlen oder DateTime konvertiert wird. Diese Eigenschaft wurde hinzugefügt, um dem Verhalten der MS Excel-Anwendung zum Laden von DateTime oder numerischen Werten aus CSV-Dateien zu entsprechen. Um das Verhalten von MS Excel zu simulieren, setzen Sie die KeepExactFormat-Eigenschaft auf „false“, während der Standardwert „true“ ist, sodass der Zellenwert als Zeichenfolge in der CSV-Datei formatiert wird.

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Eigenschaft Shape.ID hinzugefügt**
In v8.3.0 wurde der Getter/Setter für die Eigenschaft Shape.Id hinzugefügt, um jedes Formobjekt in einer bestimmten Tabelle eindeutig zu identifizieren. Diese neue Eigenschaft hilft auch bei der eindeutigen Identifizierung von Diagrammobjekten in einer Tabelle, wie unten gezeigt.

**Java**

{{< highlight "csharp" >}}

 Arbeitsbuch book = new Workbook("sample.xlsx");

ChartCollection-Diagramme = book.getWorksheets().get(0).getCharts();

 for(int index = 0; index<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Methode PlotArea.setPositionAuto Hinzugefügt**
Die Methode setPositionAuto wurde der Klasse PlotArea hinzugefügt, die dabei hilft, den Plotbereich des Diagramms in den automatischen Modus zu versetzen.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
