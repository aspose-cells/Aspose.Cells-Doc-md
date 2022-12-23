---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.1
type: docs
weight: 270
url: /de/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.8.0 zu 8.8.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Filtern Sie die Daten zum Laden**
Aspose.Cells for .NET 8.8.1 hat die LoadDataFilterOptions-Enumeration zusammen mit der LoadOptions.LoadDataFilterOptions-Eigenschaft verfügbar gemacht, die verwendet werden kann, um den Datentyp anzugeben, der geladen werden soll, wenn die Arbeitsmappe aus einer Vorlagendatei erstellt wird. Das Filtern geladener Daten kann die Leistung für spezielle Zwecke verbessern, insbesondere bei Verwendung von LightCells-APIs.

Die LoadDataFilterOptions-Enumeration bietet die folgende Auswahl.

1. Alle, um alles aus der Tabelle zu laden.
1. Keine, um nichts aus der Tabelle zu laden.
1. CellBlank lädt die Zellen, deren Werte leer sind.
1. CellBool lädt Zellen, deren Werte boolesch sind.
1. CellData lädt Zellendaten einschließlich Werte, Formeln und Formatierungen.
1. CellError lädt Zellen, deren Werte fehlerhaft sind.
1. CellNumeric lädt Zellen, deren Werte numerisch sind (einschließlich Datum und Uhrzeit).
1. CellString lädt Zellen, deren Werte Text/String sind.
1. CellValue lädt nur Zellwerte (alle Typen).
1. Diagramm lädt nur Diagramme.
1. ConditionalFormatting lädt nur bedingte Formatierungsregeln.
1. DataValidation lädt nur Datenvalidierungsregeln.
1. DocumentProperties lädt nur Dokumenteigenschaften.
1. Formel lädt Formeln einschließlich definierter Namen.
1. MergedArea lädt nur verbundene Zellen.
1. PivotTable lädt Pivot-Tabellen.
1. Einstellungen lädt nur Arbeitsmappen- und Arbeitsblatteinstellungen.
1. Form lädt nur Formen.
1. Stil lädt die Zellenformatierung.
1. Tabelle lädt Excel-Tabellen/Listenobjekte.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Daten zum Laden filtern](/cells/de/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Konvertieren Sie das Diagramm direkt in PDF**
Aspose.Cells-APIs haben bereits die Möglichkeit bereitgestellt, Diagramme in PDF zu rendern, während die Chart.ToPdf-Methode verwendet wird. Mit dieser Version hat API eine weitere überladene Version der genannten Methode bereitgestellt, die eine Instanz von Stream akzeptieren könnte, sodass Benutzer PDF des Diagramms in einer Instanz von MemoryStream speichern können.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

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


### **WorkbookSettings.PaperSize-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.8.1 hat die WorkbookSettings.PaperSize-Eigenschaft verfügbar gemacht, um die standardmäßige Druckpapiergröße für die gesamte Tabelle festzulegen. Die WorkbookSettings.PaperSize-Eigenschaft akzeptiert einen Wert aus der PaperSizeType-Enumeration, die die vordefinierten Größen für die am häufigsten verwendeten Druckpapiertypen enthält.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Shape.TextBody-Eigenschaft hinzugefügt**
Diese Version von Aspose.Cells for .NET API hat Shape.TextBody verfügbar gemacht, um die Aspekte des Textes in einer Form zu manipulieren. Das folgende Snippet verwendet die besagte Eigenschaft, um den Schatteneffekt des Textes in einer TextBox festzulegen.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Schatteneffekt für Text einstellen](/cells/de/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 //Eine Instanz von Workbook erstellen

var book = neue Arbeitsmappe ();

//Zugriff auf das erste Arbeitsblatt der Arbeitsmappe

var sheet = book.Worksheets[0];

//TextBox zur ShapeCollection hinzufügen

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Setzen Sie den Text der TextBox

textBox.Text = "Dieser Text hat die folgenden Einstellungen.\n\nTexteffekte > Schatten > Versatz unten";

//Schatteneffekt für Text festlegen

 für (int i = 0; i< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Worksheet.CalculateFormula(string formula, CalculationOptions opts) Methode hinzugefügt**
Aspose.Cells for .NET 8.8.1 hat eine weitere Überladung für die CalculateFormula-Methode verfügbar gemacht, die die Möglichkeit bietet, eine bestimmte Formel direkt mit benutzerdefinierten Optionen zu berechnen.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Direkte Berechnung der benutzerdefinierten Funktion](/cells/de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **GridCell.CreateValidation-Methode hinzugefügt**
Aspose.Cells. GridWeb bietet die Möglichkeit, die Validierungsregel direkt einer einzelnen Zelle hinzuzufügen, während die GridCell.CreateValidation-Methode verwendet wird. Das genannte Verfahren erfordert 2 Parameter. Der erste ist vom Typ GridValidationType, der den Validierungstyp bestimmt, während der zweite Parameter (isRequied) vom Typ Boolean ist.



**C#**

{{< highlight "csharp" >}}

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


### **GridCell.RemoveValidation-Methode hinzugefügt**
Aspose.Cells.GridWeb bietet auch die Möglichkeit, die Datenvalidierungsregel aus einer GridCell zu entfernen, während die GridCell.RemoveValidation-Methode verwendet wird.
## **Veraltete APIs**
### **Veraltete Shape.TextFrame-Eigenschaft**
Es wird empfohlen, stattdessen die Shape.TextBody.TextAlignment-Eigenschaft zu verwenden.
