---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.1
type: docs
weight: 280
url: /de/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.8.0 zu 8.8.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Filtern Sie die Daten zum Laden**
Aspose.Cells for Java 8.8.1 hat die LoadDataFilterOptions-Enumeration zusammen mit der LoadOptions.LoadDataFilterOptions-Eigenschaft verfügbar gemacht, die verwendet werden kann, um den Datentyp anzugeben, der geladen werden soll, wenn die Arbeitsmappe aus einer Vorlagendatei erstellt wird. Das Filtern geladener Daten kann die Leistung für spezielle Zwecke verbessern, insbesondere bei Verwendung von LightCells-APIs.

Die LoadDataFilterOptions-Enumeration bietet die folgende Auswahl.

1. ALL, um alles aus der Tabelle zu laden.
1. NONE, um nichts aus der Tabelle zu laden.
1. CELL_BLANK lädt die Zellen, deren Werte leer sind.
1. CELL_BOOL lädt Zellen, deren Werte boolesch sind.
1. CELL_DATA lädt Zellendaten einschließlich Werte, Formeln und Formatierungen.
1. CELL_ERROR lädt Zellen, deren Werte fehlerhaft sind.
1. CELL_NUMERIC lädt Zellen, deren Werte numerisch sind (einschließlich Datum und Uhrzeit).
1. CELL_STRING lädt Zellen, deren Werte Text/String sind.
1. CELL_VALUE lädt nur Zellwerte (alle Typen).
1. CHART lädt nur Diagramme.
1. CONDITIONAL_FORMATTING lädt nur bedingte Formatierungsregeln.
1. DATA_VALIDATION lädt nur Datenvalidierungsregeln.
1. DOCUMENT_PROPERTIES lädt nur Dokumenteigenschaften.
1. FORMULA lädt Formeln mit definierten Namen.
1. MERGED_AREA lädt nur verbundene Zellen.
1. PIVOT_TABLE lädt Pivot-Tabellen.
1. EINSTELLUNGEN lädt nur Arbeitsmappen- und Arbeitsblatteinstellungen.
1. SHAPE lädt nur Shapes.
1. STYLE lädt die Zellenformatierung.
1. TABLE lädt Excel-Tabellen/Listenobjekte.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Daten zum Laden filtern](/cells/de/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Diagramm direkt in PDF konvertieren**
Aspose.Cells APIs haben bereits die Möglichkeit bereitgestellt, Diagramme unter Verwendung der Chart.toPdf-Methode in PDF zu rendern. Mit dieser Version hat API eine weitere überladene Version der genannten Methode verfügbar gemacht, die eine Instanz von OutputStream akzeptieren könnte, sodass die Benutzer das PDF des Diagramms in einer Instanz von ByteArrayOutputStream speichern können.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **WorkbookSettings.PaperSize-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.8.1 hat die WorkbookSettings.PaperSize-Eigenschaft verfügbar gemacht, um die standardmäßige Druckpapiergröße für die gesamte Tabelle festzulegen. Die WorkbookSettings.PaperSize-Eigenschaft akzeptiert einen Wert aus der PaperSizeType-Enumeration, die die vordefinierten Größen für die am häufigsten verwendeten Druckpapiertypen enthält.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Shape.TextBody-Eigenschaft hinzugefügt**
Diese Version von Aspose.Cells for Java API hat Shape.TextBody verfügbar gemacht, um die Aspekte des Textes in einer Form zu manipulieren. Das folgende Snippet verwendet die besagte Eigenschaft, um den Schatteneffekt des Textes in einer TextBox festzulegen.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Schatteneffekt für Text einstellen](/cells/de/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Eine Instanz von Workbook erstellen

Arbeitsmappenbuch = neue Arbeitsmappe();

//Zugriff auf das erste Arbeitsblatt der Arbeitsmappe

Arbeitsblatt sheet = book.getWorksheets().get(0);

//TextBox zur ShapeCollection hinzufügen

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Setzen Sie den Text der TextBox

textBox.setText("Dieser Text hat die folgenden Einstellungen.\n\nTexteffekte > Schatten > Versatz unten");

//Schatteneffekt für Text festlegen

 für (int i = 0; i< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Worksheet.calculateFormula(string formula, CalculationOptions opts) Methode hinzugefügt**
Aspose.Cells for Java 8.8.1 hat eine weitere Überladung für die Worksheet.calculateFormula-Methode verfügbar gemacht, die die Möglichkeit bietet, eine bestimmte Formel direkt mit benutzerdefinierten Optionen zu berechnen.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Direkte Berechnung der benutzerdefinierten Funktion](/cells/de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **GridCell.createValidation-Methode hinzugefügt**
Aspose.Cells. GridWeb bietet die Möglichkeit, die Validierungsregel direkt zu einer einzelnen Zelle hinzuzufügen, während die GridCell.createValidation-Methode verwendet wird. Das genannte Verfahren erfordert 2 Parameter. Der erste ist vom Typ GridValidationType, der den Validierungstyp bestimmt, während der zweite Parameter (isRequied) vom Typ Boolean ist.

**Java**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **GridCell.removeValidation-Methode hinzugefügt**
Aspose.Cells. GridWeb bietet auch die Möglichkeit, die Datenvalidierungsregel aus einer GridCell zu entfernen, während die GridCell.removeValidation-Methode verwendet wird.
## **Veraltete APIs**
### **Veraltete Shape.TextFrame-Eigenschaft**
Es wird empfohlen, stattdessen die Shape.TextBody.TextAlignment-Eigenschaft zu verwenden.
