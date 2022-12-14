---
title: Öffentlich API Änderungen in Aspose.Cells 8.3.2
type: docs
weight: 130
url: /de/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.3.1 zu 8.3.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-3-2/) und[Klassen entfernt usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-3-2/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Mechanismus zum Festlegen der absoluten Position von PivotItem**
 Um die Funktion bereitzustellen[Absolute Positionierung des PivotItems](/cells/de/java/specifying-the-absolute-position-of-the-pivot-item/), die Aspose.Cells for Java 8.3.2 hat eine Reihe von Eigenschaften und eine Methode wie unten aufgeführt ausgesetzt.

- PivotItem.setPosition kann verwendet werden, um den Positionsindex in allen PivotItems unabhängig vom übergeordneten Knoten festzulegen.
- PivotItem.setPositionInSameParentNode kann verwendet werden, um den Positionsindex in den PivotItems unter demselben übergeordneten Knoten festzulegen.
- Die PivotItem.move(int count, bool isSameParent)-Methode kann verwendet werden, um das Element basierend auf dem count-Wert nach oben oder unten zu verschieben, wobei count die Nummer der Position ist, um das PivotItem nach oben oder unten zu verschieben. Wenn der Zählwert kleiner als null ist, wird das Element nach oben verschoben, während das PivotItem nach unten verschoben wird, wenn der Zählwert größer als null ist. Der isSameParent-Parameter vom booleschen Typ gibt an, ob der Verschiebevorgang im selben übergeordneten Knoten ausgeführt werden muss oder nicht.

{{% alert color="primary" %}} 

Bitte beachten Sie, dass die Methoden PivotTable.refreshData und PivotTable.calculateData aufgerufen werden müssen, bevor die Eigenschaften PivotItem.setPosition, PivotItem.setPositionInSameParentNode und die Methode PivotItem.move(int count, bool isSameParent) verwendet werden.

{{% /alert %}} 
### **Klasse SignatureLine hinzugefügt**
Aspose.Cells 8.3.2 bietet Unterstützung für die Signaturzeile, um die entsprechende Funktion von MS Excel nachzuahmen. Diese Version hat zu diesem Zweck die SignatureLine-Klasse und die Picture.SignatureLine-Eigenschaft verfügbar gemacht.

Der folgende Beispielcode fügt der Arbeitsmappe eine Signaturzeile mit der Picture.SignatureLine-Eigenschaft hinzu.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Methode Chart.hasAxis hinzugefügt**
Mit der Veröffentlichung von v8.3.2 hat der Aspose.Cells API die Methode Chart.hasAxis(AxisType axisType, bool isPrimary) bereitgestellt, um zu bestimmen, ob das Diagramm eine bestimmte Achse hat oder nicht.

Der folgende Beispielcode demonstriert die Verwendung der Chart.hasAxis-Methode, um zu bestimmen, ob das Beispieldiagramm eine Primär-, Sekundär- und Wertachse hat.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **Methode WorkbookSettings.checkWriteProtectedPassword hinzugefügt**
Die Methode WorkbookSettings.checkWriteProtectedPassword ermöglicht es den Entwicklern zu überprüfen, ob ein gegebenes Passwort zum Ändern der Tabelle korrekt ist oder nicht.

**Java**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Überladungsmethoden WorkbookRender.toPrinter & SheetRender.toPrinter Hinzugefügt**
Aspose.Cells 8.3.2 hat die Methoden WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) und SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) bereitgestellt, um den Seitenbereich der Arbeitsmappe bzw. des Arbeitsblatts zu drucken.

Der folgende Beispielcode veranschaulicht die Verwendung der oben genannten Methoden zum Drucken der Seiten 2-5 der Arbeitsmappe und des Arbeitsblatts.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Methode Worksheet.refreshPivotTables Hinzugefügt**
Die neu hinzugefügte Methode Worksheet.refreshPivotTables ermöglicht es, alle Pivot-Tabellen in einer bestimmten Tabelle in einem einzigen Aufruf zu aktualisieren.

**Java**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Methode Workbook.getNamedStyle hinzugefügt**
Aspose.Cells 8.3.2 hat die Workbook.getNamedStyle-Methode verfügbar gemacht, die die Zeichenfolge als Parameter akzeptiert und das Style-Objekt basierend auf dem übergebenen Parameter abruft.
### **Methode Cells.importTwoDimensionArray hinzugefügt**
Aspose.Cells API hat es ermöglicht, zweidimensionale Arrays in Tabellenkalkulationszellen zu importieren, indem die Methode Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) bereitgestellt wird. Die genannte Methode importiert ein zweidimensionales Array von Daten in ein Arbeitsblatt mit flexibleren Optionen, die in TxtLoadOptions definiert sind.
### **Eigenschaften OnePagePerSheet, PageIndex & PageCount hinzugefügt**
Aspose.Cells for Java 8.3.2 hat die OnePagePerSheet-, PageIndex- und PageCount-Eigenschaften für die XpsSaveOptions-Klasse verfügbar gemacht. Der Benutzer kann den gesamten Inhalt einer Tabelle mithilfe der OnePagePerSheet-Eigenschaft auf eine einzelne XPS-Seite packen und/oder die Anzahl der zu druckenden Seiten mithilfe der PageCount-Eigenschaft abrufen. Die PageIndex-Eigenschaft ruft/legt den 0-basierten Index der ersten zu speichernden Seite fest.
### **Eigenschaften NumberDecimalSeparator & NumberGroupSeparator hinzugefügt**
Aspose.Cells for Java 8.3.2 hat NumberDecimalSeparator- und NumberGroupSeparator-Eigenschaften eingeführt, mit denen die benutzerdefinierten Trennzeichen abgerufen/festgelegt werden können, die zum Formatieren und Analysieren der numerischen Werte in Tabellenkalkulationen verwendet werden.

Der folgende Beispielcode veranschaulicht, wie die benutzerdefinierten Trennzeichen mithilfe von Aspose.Cells API angegeben werden. Der folgende Code gibt die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt bzw. Leerzeichen an.

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Eigenschaft PdfSaveOptions.setFontSubstitutionCharGranularity Hinzugefügt**
Aspose.Cells for Java 8.3.2 hat die PdfSaveOptions.setFontSubstitutionCharGranularity-Eigenschaft verfügbar gemacht, um das Problem zu lösen, bei dem einige Unicode-Zeichen nicht mit einer bestimmten Schriftartfamilie angezeigt werden können. Wenn die Eigenschaft PdfSaveOptions.setFontSubstitutionCharGranularity auf „true“ gesetzt ist, wird nur die Schriftart bestimmter Zeichen, die nicht angezeigt werden können, in eine anzeigbare Schriftart geändert, und der Rest des Wortes oder Satzes sollte in der ursprünglichen Schriftart bleiben.

**Java**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Entfernte APIs**
### **Veraltete Methoden entfernt**
Die folgenden Methoden wurden aus dem öffentlichen API entfernt.

- Workbook.open- und Workbook.save-Methoden.
- Workbook.setOleSize-Methode.
- Workbook.loadData-Methode.
- Methoden WorkbookDesigner.open & WorkbookDesigner.save.
- WorksheetCollection.deleteName-Methode.
### **Veraltete Eigenschaften entfernt**
Die folgenden Eigenschaften wurden aus der öffentlichen API entfernt.

- Workbook.isProtected-Eigenschaft.
- Workbook.Language-Eigenschaft.
- Workbook.Region-Eigenschaft.
- WorkbookSettings.ReCalcOnOpen-Eigenschaft.
- WorkbookSettings.Language-Eigenschaft.
- WorkbookSettings.Encoding-Eigenschaft.
- WorkbookSettings.ConvertNumericData-Eigenschaft.
- WorksheetCollection.HidePivotFieldList-Eigenschaft.
- WorksheetCollection.EnableHTTPCompression-Eigenschaft.
- WorksheetCollection.isMinimized-Eigenschaft.
- WorksheetCollection.isHidden-Eigenschaft.
- WorksheetCollection.SheetTabBarWidth-Eigenschaft.
- WorksheetCollection.WindowLeft-Eigenschaft.
- WorksheetCollection.WindowLeftInch-Eigenschaft.
- WorksheetCollection.WindowLeftCM-Eigenschaft.
- WorksheetCollection.WindowTop-Eigenschaft.
- WorksheetCollection.WindowTopInch-Eigenschaft.
- WorksheetCollection.WindowTopCM-Eigenschaft.
- WorksheetCollection.WindowWidth-Eigenschaft.
- WorksheetCollection.WindowWidthInch-Eigenschaft.
- WorksheetCollection.WindowWidthCM-Eigenschaft.
- WorksheetCollection.WindowHeight-Eigenschaft.
- WorksheetCollection.WindowHeightInch-Eigenschaft.
- WorksheetCollection.WindowHeightCM-Eigenschaft.
- Worksheet.HPageBreaks-Eigenschaft.
- Worksheet.VPageBreaks-Eigenschaft.
- HtmlSaveOptions.DisplayHTMLCrossString-Eigenschaft.
- HtmlSaveOptions.ExportChartImageFormat-Eigenschaft.
- SaveOptions.ExpCellNameToXLSX-Eigenschaft.
- SaveOptions.DefaultFont-Eigenschaft.
- SaveOptions.Compliance-Eigenschaft.
- SaveOptions.PdfBookmark-Eigenschaft.
- SaveOptions.PdfImageCompression-Eigenschaft.
- TxtSaveOptions.AlwaysQuoted-Eigenschaft.
## **Veraltete APIs**
### **Eigenschaft Workbook.saveOptions Veraltet**
 Ein Objekt von SaveOptions muss an die Workbook.Save-Methode übergeben werden, nachdem die richtigen SaveOptions-Eigenschaften festgelegt wurden.
### **Eigenschaft Workbook.Styles & Class StyleCollection Veraltet**
Es wird empfohlen, die Workbook.createStyle-Methode zu verwenden, um den Stil für die Workbook-Instanz zu erstellen und zu bearbeiten, anstatt einen Stil mit der StyleCollection.add-Methode zu erstellen. Darüber hinaus kann die Workbook.getNamedStyle(string)-Methode verwendet werden, um einen benannten Stil anstelle von StyleCollection.get(string) zu erhalten.
### **Methode PivotItem.move(int count) Veraltet**
 Mit der Veröffentlichung von Aspose.Cells 8.3.2 hat API eine weitere Überladung der PivotItem.move-Methode eingeführt, die den ganzzahligen Parameter für die Anzahl und den booleschen Parameter akzeptiert, um ein PivotItem innerhalb des übergeordneten Knotens zu verschieben.
