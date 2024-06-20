---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.1
type: docs
weight: 270
url: /de/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.8.0 auf 8.8.1, die für Modul-/Anwendungsentwickler relevant sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Daten für das Laden filtern**
Aspose.Cells for .NET 8.8.1 hat die Enumeration LoadDataFilterOptions zusammen mit der Eigenschaft LoadOptions.LoadDataFilterOptions freigegeben, die verwendet werden kann, um den Datentyp anzugeben, der beim Erstellen des Arbeitsmappendatei aus einer Vorlagendatei geladen werden soll. Das Filtern der geladenen Daten kann die Leistung für spezielle Zwecke verbessern, insbesondere bei Verwendung von LightCells APIs.

Die Enumeration LoadDataFilterOptions bietet die folgenden Auswahlmöglichkeiten.

1. All, um alles aus der Tabelle zu laden.
1. None, um nichts aus der Tabelle zu laden.
1. CellBlank lädt die Zellen, deren Werte leer sind.
1. CellBool lädt Zellen, deren Werte Boolean sind.
1. CellData lädt Zellendaten einschließlich Werten, Formeln und Formatierungen.
1. CellError lädt Zellen, deren Werte Fehler sind.
1. CellNumeric lädt Zellen, deren Werte numerisch sind (einschließlich Datum & Uhrzeit).
1. CellString lädt Zellen, deren Werte Text/String sind.
1. CellValue lädt nur Zellwerte (alle Typen).
1. Chart lädt nur Diagramme.
1. ConditionalFormatting lädt nur bedingte Formatierungsregeln.
1. DataValidation lädt nur Datenüberprüfungsregeln.
1. DocumentProperties lädt nur Dokumenteigenschaften.
1. Formula lädt Formeln einschließlich definierter Namen.
1. MergedArea lädt nur zusammengeführte Zellen.
1. PivotTable lädt Pivot-Tabellen.
1. Settings lädt nur Arbeitsmappe & Arbeitsblatt-Einstellungen.
1. Shape lädt nur Formen.
1. Style lädt Zellformatierungen.
1. Table lädt Excel-Tabellen/Listeobjekte.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Filtern von Daten beim Laden](/cells/de/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Konvertieren Sie das Diagramm direkt in PDF um**
Aspose.Cells APIs haben bereits die Möglichkeit bereitgestellt, Diagramme unter Verwendung der Chart.ToPdf-Methode in PDF zu rendern. Mit dieser Version hat die API eine weitere überladene Version dieser Methode freigelegt, die eine Instanz von Stream akzeptieren könnte, so dass die Benutzer das Diagramm-PDF in einer Instanz von MemoryStream speichern können.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **Eigenschaft WorkbookSettings.PaperSize hinzugefügt**
Aspose.Cells for .NET 8.8.1 hat das WorkbookSettings.PaperSize-Attribut freigelegt, um die Standarddruckpapiergröße für die gesamte Tabelle festzulegen. Das WorkbookSettings.PaperSize-Attribut akzeptiert einen Wert aus der Aufzählung PaperSizeType, die die vordefinierten Größen für die am weitesten verbreiteten Druckpapiertypen enthält.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Eigenschaft Shape.TextBody hinzugefügt**
Diese Version der Aspose.Cells for .NET-API hat das Shape.TextBody-Attribut freigelegt, um die Aspekte des Texts in Formen zu manipulieren. Der folgende Ausschnitt verwendet das genannte Attribut, um den Schatteffekt des Texts in einem TextBox festzulegen.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Festlegen des Schatteffekts für Text](/cells/de/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Hinzugefügter Worksheet.CalculateFormula Method**
Aspose.Cells for .NET 8.8.1 hat eine weitere Überladung für die CalculateFormula-Methode freigelegt, die die Möglichkeit bietet, eine bestimmte Formel direkt mit benutzerdefinierten Optionen zu berechnen.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über [Direkte Berechnung der benutzerdefinierten Funktion](/cells/de/net/direkte-berechnung-der-benutzerdefinierten-funktion-ohne-sie-in-einem-arbeitsblatt-zu-schreiben/).

{{% /alert %}} 
### **Hinzugefügte GridCell.CreateValidation Methode**
Aspose.Cells.GridWeb bietet die Möglichkeit, die Validierungsregel direkt zu einer einzelnen Zelle hinzuzufügen, während die GridCell.CreateValidation-Methode verwendet wird. Die genannte Methode erfordert 2 Parameter. Der erste ist vom Typ GridValidationType, der den Validierungstyp bestimmt, während der zweite Parameter (isRequied) vom Typ Boolean ist.



**C#**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **Hinzugefügte GridCell.RemoveValidation Methode**
Aspose.Cells.GridWeb bietet auch die Möglichkeit, die Datenvalidierungsregel aus einer GridCell zu entfernen, während die GridCell.RemoveValidation-Methode verwendet wird.
## **Veraltete APIs**
### **Eigenschaft Shape.TextFrame obsolet**
Es wird empfohlen, stattdessen die Eigenschaft Shape.TextBody.TextAlignment zu verwenden.
