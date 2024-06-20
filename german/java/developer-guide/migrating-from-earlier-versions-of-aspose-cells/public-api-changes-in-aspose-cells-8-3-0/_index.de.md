---
title: Öffentliche API Änderungen in Aspose.Cells 8.3.0
type: docs
weight: 110
url: /de/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.2.2 auf 8.3.0, die für Modul-/Anwendungs-Entwickler interessant sein könnten.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Eigenschaft WorkbookSettings.AutoRecover hinzugefügt**
Der Getter/Setter für die Eigenschaft AutoRecover wurde der WorkbookSettings-Klasse hinzugefügt, um Entwicklern zu ermöglichen, die Option der automatischen Wiederherstellung für ihre Tabellenkalkulationen in ihren Anwendungen zu erhalten/setzen. 

{{% alert color="primary" %}} 

Bitte prüfen Sie den Artikel [Einstellen der Tabellenkalkulation für automatische Wiederherstellung](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) für weitere Informationen.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Eigenschaft WorkbookSettings.CrashSave hinzugefügt**
Der Getter/Setter für die Eigenschaft CrashSave wurde der WorkbookSettings-Klasse hinzugefügt. Diese boolesche Eigenschaft gibt an, ob die Anwendung die Arbeitsmappe nach einem Absturz zuletzt gespeichert hat.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Eigenschaft WorkbookSettings.DataExtractLoad hinzugefügt**
Der Getter/Setter für die Eigenschaft DataExtractLoad wurde der WorkbookSettings-Klasse hinzugefügt, um den Entwicklern die Information zur letzten Wiederherstellung zu erhalten/setzen. Wenn die Eigenschaft DataExtractLoad true zurückgibt, deutet dies darauf hin, dass die Datenwiederherstellung in der Arbeitsmappendatei durchgeführt wurde.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Eigenschaft WorkbookSettings.RepairLoad hinzugefügt**
Der Getter/Setter für die Eigenschaft RepairLoad wurde der WorkbookSettings-Klasse hinzugefügt. Diese boolesche Eigenschaft gibt an, ob die Tabellenkalkulation in der letzten Ladesitzung mit der Excel-Anwendung repariert wurde.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Eigenschaft TxtLoadOptions.KeepExactFormat hinzugefügt**
Die Eigenschaft KeepExactFormat wurde der TxtLoadOptions-Klasse hinzugefügt, die angibt, ob das genaue Formatieren für den Zellwert beibehalten werden soll, wenn ein String/Text in Zahlen oder Datum/Uhrzeit konvertiert wird. Diese Eigenschaft wurde hinzugefügt, um das Verhalten der MS Excel-Anwendung beim Laden von Datum/Uhrzeit- oder numerischen Werten aus CSV-Dateien nachzubilden. Um das Verhalten von MS Excel zu simulieren, setzen Sie die Eigenschaft KeepExactFormat auf false, während der Standardwert true ist, sodass der Zellwert als String in der CSV-Datei formatiert wird.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Eigenschaft Shape.Id hinzugefügt**
Die v8.3.0 hat den Getter/Setter für die Eigenschaft Shape.Id hinzugefügt, um jedes Formobjekt in einer bestimmten Tabellenkalkulation eindeutig zu identifizieren. Diese neue Eigenschaft hilft auch dabei, Diagrammobjekte in einer Tabellenkalkulation eindeutig zu identifizieren, wie unten dargestellt.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Methode setPositionAuto zur PlotArea-Klasse hinzugefügt**
Die Methode setPositionAuto wurde der PlotArea-Klasse hinzugefügt, die beim Einstellen des Diagrammbereichs auf den automatischen Modus hilft.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
