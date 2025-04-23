---
title: Öffentliche API Änderungen in Aspose.Cells 8.3.0
type: docs
weight: 100
url: /de/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.2.2 auf 8.3.0, die für Modul-/Anwendungs-Entwickler interessant sein könnten.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Eigenschaft WorkbookSettings.AutoRecover hinzugefügt**
Die neue Eigenschaft AutoRecover wurde der WorkbookSettings-Klasse hinzugefügt, um Entwicklern die Möglichkeit zu geben, die Option der automatischen Wiederherstellung für Tabellenkalkulationen in ihren Anwendungen festzulegen.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den Artikel [Einstellen der automatischen Tabellenwiederherstellung](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) für weitere Informationen.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Eigenschaft WorkbookSettings.CrashSave hinzugefügt**
Eine boolesche Typ-Eigenschaft CrashSave wurde der WorkbookSettings-Klasse hinzugefügt, die anzeigt, ob die Anwendung die Arbeitsmappe nach einem Absturz zuletzt gespeichert hat.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Eigenschaft WorkbookSettings.DataExtractLoad hinzugefügt**
Die Eigenschaft DataExtractLoad wurde der WorkbookSettings-Klasse hinzugefügt, um Entwicklern die Informationen zur letzten Wiederherstellung zu erhalten. Wenn die Eigenschaft DataExtractLoad true zurückgibt, deutet dies darauf hin, dass die Datenwiederherstellung auf der Tabelle durchgeführt wurde.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Eigenschaft WorkbookSettings.RepairLoad hinzugefügt**
Die RepairLoad-Eigenschaft zeigt an, ob die Tabelle beim letzten Laden mit der Excel-Anwendung repariert wurde.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Eigenschaft TxtLoadOptions.KeepExactFormat hinzugefügt**
Die Eigenschaft KeepExactFormat wurde der TxtLoadOptions-Klasse hinzugefügt, die angibt, ob das genaue Formatieren für den Zellwert beibehalten werden soll, wenn ein String/Text in Zahlen oder Datum/Uhrzeit konvertiert wird. Diese Eigenschaft wurde hinzugefügt, um das Verhalten der MS Excel-Anwendung beim Laden von Datum/Uhrzeit- oder numerischen Werten aus CSV-Dateien nachzubilden. Um das Verhalten von MS Excel zu simulieren, setzen Sie die Eigenschaft KeepExactFormat auf false, während der Standardwert true ist, sodass der Zellwert als String in der CSV-Datei formatiert wird.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Eigenschaft Shape.Id hinzugefügt**
Die Id-Eigenschaft wurde der Shape-Klasse hinzugefügt, um jedes Formobjekt in einer bestimmten Tabelle eindeutig zu identifizieren. Diese neue Eigenschaft hilft auch dabei, Diagrammobjekte in einer Tabelle zu identifizieren, wie unten gezeigt.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Hinzugefügte PlotArea.SetPositionAuto-Methode**
Die Methode SetPositionAuto wurde der PlotArea-Klasse hinzugefügt, die beim Einstellen des Diagrammbereichs auf den automatischen Modus hilft.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
