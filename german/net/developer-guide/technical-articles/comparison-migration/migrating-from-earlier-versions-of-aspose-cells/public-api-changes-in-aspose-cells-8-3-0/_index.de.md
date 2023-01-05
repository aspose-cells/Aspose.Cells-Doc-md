---
title: Öffentlich API Änderungen in Aspose.Cells 8.3.0
type: docs
weight: 100
url: /de/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.2.2 zu 8.3.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Eigenschaft WorkbookSettings.AutoRecover Hinzugefügt**
Die neue Eigenschaft AutoRecover wurde der WorkbookSettings-Klasse hinzugefügt, damit Entwickler die Option der automatischen Wiederherstellung für die Tabellenkalkulationen in ihren Anwendungen festlegen können.

{{% alert color="primary" %}} 

 Bitte überprüfen Sie den Artikel[Einstellen der automatischen Wiederherstellung der Tabellenkalkulation](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) für mehr Informationen.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Eigenschaft WorkbookSettings.CrashSave Hinzugefügt**
Der WorkbookSettings-Klasse wurde die Eigenschaft CrashSave vom booleschen Typ hinzugefügt, die angibt, ob die Anwendung die Arbeitsmappendatei zuletzt nach einem Absturz gespeichert hat.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Eigenschaft WorkbookSettings.DataExtractLoad Hinzugefügt**
Die Eigenschaft DataExtractLoad wurde der WorkbookSettings-Klasse hinzugefügt, damit die Entwickler Informationen zur letzten Wiederherstellung abrufen können. Wenn die Eigenschaft DataExtractLoad „true“ zurückgibt, bedeutet dies, dass die Datenwiederherstellung für das Arbeitsblatt durchgeführt wurde.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Eigenschaft WorkbookSettings.RepairLoad Hinzugefügt**
Die Eigenschaft RepairLoad gibt an, ob die Tabelle beim letzten Laden mit der Excel-Anwendung repariert wurde.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Eigenschaft TxtLoadOptions.KeepExactFormat hinzugefügt**
Der TxtLoadOptions-Klasse wurde die Eigenschaft KeepExactFormat hinzugefügt, die angibt, ob die exakte Formatierung für den Zellenwert beibehalten werden soll, wenn String/Text in Zahlen oder DateTime konvertiert wird. Diese Eigenschaft wurde hinzugefügt, um dem Verhalten der MS Excel-Anwendung beim Laden von DateTime- oder numerischen Werten aus CSV-Dateien zu entsprechen. Um das Verhalten von MS Excel zu simulieren, setzen Sie die KeepExactFormat-Eigenschaft auf „false“, während der Standardwert „true“ ist, sodass der Zellenwert als Zeichenfolge in der Datei „CSV“ formatiert wird.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Eigenschaft Shape.ID hinzugefügt**
Die Eigenschaft Id wurde der Shape-Klasse hinzugefügt, um jedes Shape-Objekt in einer bestimmten Tabelle eindeutig zu identifizieren. Diese neue Eigenschaft hilft auch beim Identifizieren von Diagrammobjekten in einer Tabellenkalkulation, wie unten gezeigt.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Methode PlotArea.SetPositionAuto Hinzugefügt**
Die Methode SetPositionAuto wurde der Klasse PlotArea hinzugefügt, die dabei hilft, den Plotbereich des Diagramms in den automatischen Modus zu versetzen.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
