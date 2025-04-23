---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.1
type: docs
weight: 280
url: /de/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.8.0 auf 8.8.1, die für Modul-/Anwendungsentwickler relevant sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Daten für das Laden filtern**
Aspose.Cells for Java 8.8.1 hat die Enumeration LoadDataFilterOptions zusammen mit der LoadOptions.LoadDataFilterOptions-Eigenschaft freigegeben, die verwendet werden kann, um den Datentyp anzugeben, der beim Erstellen der Arbeitsmappe aus einer Vorlagendatei geladen werden sollte. Das Filtern von geladenen Daten kann für spezielle Zwecke die Leistung verbessern, insbesondere beim Verwenden von LightCells-APIs.

Die Enumeration LoadDataFilterOptions bietet die folgenden Auswahlmöglichkeiten.

1. ALLES, um alles aus der Tabelle zu laden.
1. NICHTS, um nichts aus der Tabelle zu laden.
1. CELL_BLANK lädt die Zellen, deren Werte leer sind.
1. CELL_BOOL lädt Zellen, deren Werte Boolean sind.
1. CELL_DATA lädt Zellendaten, einschließlich Werten, Formeln und Formatierungen.
1. CELL_ERROR lädt Zellen, deren Werte Fehler sind.
1. CELL_NUMERIC lädt Zellen, deren Werte numerisch sind (einschließlich Datum & Uhrzeit).
1. CELL_STRING lädt Zellen, deren Werte Text/String sind.
1. CELL_VALUE lädt nur Zellwerte (alle Typen).
1. CHART lädt nur Diagramme.
1. CONDITIONAL_FORMATTING lädt nur bedingte Formatierungsregeln.
1. DATA_VALIDATION lädt nur Datenüberprüfungsregeln.
1. DOCUMENT_PROPERTIES lädt nur Dokumenteigenschaften.
1. FORMULA lädt Formeln einschließlich definierter Namen.
1. MERGED_AREA lädt nur zusammengeführte Zellen.
1. PIVOT_TABLE lädt Pivot-Tabellen.
1. SETTINGS lädt nur Arbeitsmappen- und Arbeitsblatteinstellungen.
1. SHAPE lädt nur Formen.
1. STYLE lädt Zellformatierungen.
1. TABLE lädt Excel-Tabellen/Listobjekte.

{{% alert color="primary" %}} 

Weitere Details zu diesem Feature finden Sie im detaillierten Artikel zu [Filtern von Daten beim Laden](/cells/de/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Konvertieren Sie das Diagramm direkt in PDF um**
Die Aspose.Cells-APIs haben bereits die Möglichkeit zum Rendern von Diagrammen in PDF mittels der Methode Chart.toPdf bereitgestellt. Mit diesem Release hat die API eine weitere überladene Version dieser Methode freigegeben, die eine Instanz von OutputStream akzeptieren kann, was es den Benutzern ermöglicht, das PDF des Diagramms in einer Instanz von ByteArrayOutputStream zu speichern.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

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
### **Eigenschaft WorkbookSettings.PaperSize hinzugefügt**
Aspose.Cells for Java 8.8.1 hat die Eigenschaft WorkbookSettings.PaperSize freigegeben, um die Standardpapiergröße für das gesamte Tabellenblatt festzulegen. Die Eigenschaft WorkbookSettings.PaperSize akzeptiert einen Wert aus dem Aufzählungstyp PaperSizeType, der die vordefinierten Größen für die am häufigsten verwendeten Druckerpapiertypen enthält.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Eigenschaft Shape.TextBody hinzugefügt**
Dieses Release von Aspose.Cells for Java API hat die Eigenschaft Shape.TextBody freigegeben, um die Aspekte des Textes in Formen zu manipulieren. Der folgende Code-Schnipsel verwendet diese Eigenschaft, um den Schatteneffekt des Textes in einem TextBox zu setzen.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über [Einstellung des Schatteneffekts für Text](/cells/de/java/einstellen-von-schatten-des-texteffekts-von-form-oder-textbox/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Methode Worksheet.calculateFormula(string formula, CalculationOptions opts) hinzugefügt**
Aspose.Cells for Java 8.8.1 hat eine weitere Überlastung für die Methode Worksheet.calculateFormula freigegeben, die die Möglichkeit bietet, eine gegebene Formel direkt mit benutzerdefinierten Optionen zu berechnen.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über [Direkte Berechnung der benutzerdefinierten Funktion](/cells/de/java/direkte-berechnung-der-benutzerdefinierten-funktion-ohne-sie-im-arbeitsblatt-zu-schreiben/).

{{% /alert %}} 
### **Methode GridCell.createValidation hinzugefügt**
Aspose.Cells.GridWeb hat die Möglichkeit bereitgestellt, die Validierungsregel direkt zu einer einzelnen Zelle hinzuzufügen, während die Methode GridCell.createValidation verwendet wird. Die besagte Methode erfordert 2 Parameter. Der erste ist vom Typ GridValidationType, der den Validierungstyp bestimmt, während der zweite Parameter (isRequied) vom Typ Boolean ist.

**Java**

{{< highlight csharp >}}

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
### **Methode GridCell.removeValidation hinzugefügt**
Aspose.Cells.GridWeb hat auch die Möglichkeit bereitgestellt, die Datenvalidierungsregel aus einer GridCell zu entfernen, während die Methode GridCell.removeValidation verwendet wird.
## **Veraltete APIs**
### **Eigenschaft Shape.TextFrame obsolet**
Es wird empfohlen, stattdessen die Eigenschaft Shape.TextBody.TextAlignment zu verwenden.
{{< app/cells/assistant language="java" >}}
