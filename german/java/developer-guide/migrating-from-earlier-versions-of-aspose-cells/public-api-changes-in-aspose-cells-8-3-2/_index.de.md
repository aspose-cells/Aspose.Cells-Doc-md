---
title: Öffentliche API Änderungen in Aspose.Cells 8.3.2
type: docs
weight: 130
url: /de/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.3.1 auf 8.3.2, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/java/öffentliche-api-änderungen-in-aspose-cells-8-3-2/) und [entfernte Klassen usw.](/cells/de/java/öffentliche-api-änderungen-in-aspose-cells-8-3-2/), sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Mechanismus zum Festlegen der absoluten Position des PivotItems**
Um die Funktion [Absolute Positionierung von PivotItem](/cells/de/java/festlegen-der-absoluten-position-des-pivot-items/) bereitzustellen, hat die Aspose.Cells for Java 8.3.2 eine Reihe von Eigenschaften und eine Methode wie unten aufgelistet freigelegt.

- PivotItem.setPosition kann verwendet werden, um den Positionisindex in allen PivotItems unabhängig vom übergeordneten Knoten festzulegen.
- PivotItem.setPositionInSameParentNode kann verwendet werden, um den Positionisindex in den PivotItems unter demselben übergeordneten Knoten festzulegen.
- Die Methode PivotItem.move(int count, bool isSameParent) kann verwendet werden, um das Element basierend auf dem count-Wert nach oben oder unten zu verschieben, wobei count die Anzahl der Positionen angibt, um das PivotItem nach oben oder unten zu verschieben. Wenn der count-Wert kleiner als null ist, wird das Element nach oben verschoben, und wenn der count-Wert größer als null ist, wird das PivotItem nach unten verschoben. Der boolesche Typ isSameParent legt fest, ob die Verschiebungsoperation im selben übergeordneten Knoten durchgeführt werden muss oder nicht.

{{% alert color="primary" %}} 

Bitte beachten Sie, dass es notwendig ist, die Methoden PivotTable.refreshData und PivotTable.calculateData aufzurufen, bevor PivotItem.setPosition, PivotItem.setPositionInSameParentNode-Eigenschaften und die PivotItem.move(int count, bool isSameParent)-Methode verwendet werden.

{{% /alert %}} 
### **Klasse SignatureLine hinzugefügt**
Aspose.Cells 8.3.2 bietet Unterstützung für die Signaturlinie, um die dem MS Excel-Äquivalent entsprechende Funktion zu imitieren. Diese Version hat die SignatureLine-Klasse und die Picture.SignatureLine-Eigenschaft für diesen Zweck freigelegt.

Der folgende Beispielcode fügt eine Signaturlinie mithilfe der Picture.SignatureLine-Eigenschaft zum Arbeitsblatt hinzu.

**Java**

{{< highlight csharp >}}

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
Mit der Version v8.3.2 hat die Aspose.Cells-API die Methode Chart.hasAxis(AxisType axisType, bool isPrimary) bereitgestellt, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.

Der folgende Beispielcode zeigt die Verwendung der Methode Chart.hasAxis, um festzustellen, ob das Beispieldiagramm Primär-, Sekundär- und Wertachse hat.

**Java**

{{< highlight csharp >}}

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
Methode WorkbookSettings.checkWriteProtectedPassword ermöglicht es den Entwicklern zu überprüfen, ob ein angegebenes Passwort zur Bearbeitung der Tabelle korrekt ist oder nicht.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Überladungsmethoden WorkbookRender.toPrinter & SheetRender.toPrinter hinzugefügt**
Aspose.Cells 8.3.2 hat die Methoden WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) und SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) bereitgestellt, um den Bereich von Seiten des Arbeitsblatts und des Tabellenblatts zu drucken.

Der folgende Beispielcode veranschaulicht die Verwendung der genannten Methoden zum Drucken der Seiten 2-5 des Arbeitsmappens und des Arbeitsblatts.

**Java**

{{< highlight csharp >}}

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
### **Methode Worksheet.refreshPivotTables hinzugefügt**
Die neu hinzugefügte Methode Worksheet.refreshPivotTables ermöglicht das Aktualisieren aller Pivot-Tabellen in einer bestimmten Tabelle in einem einzigen Aufruf.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Methode Workbook.getNamedStyle hinzugefügt**
Aspose.Cells 8.3.2 hat die Methode Workbook.getNamedStyle freigegeben, die den String als Parameter akzeptiert und das Style-Objekt basierend auf dem übergebenen Parameter abruft.
### **Methode Cells.importTwoDimensionArray hinzugefügt**
Es ist mit der Aspose.Cells-API möglich, zweidimensionale Arrays in Tabellenzellen zu importieren, indem die Methode Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) freigegeben wird. Die genannte Methode importiert ein zweidimensionales Array von Daten in ein Arbeitsblatt mit flexibleren Optionen, die in TxtLoadOptions definiert sind.
### **Eigenschaften OnePagePerSheet, PageIndex & PageCount hinzugefügt**
Aspose.Cells for Java 8.3.2 hat die Eigenschaften OnePagePerSheet, PageIndex & PageCount für die Klasse XpsSaveOptions freigegeben. Der Benutzer kann mit der Eigenschaft OnePagePerSheet alle Inhalte einer Tabelle auf einer einzigen Seite von XPS anpassen und/oder die Anzahl der zu druckenden Seiten mit der Eigenschaft PageCount abrufen. Die Eigenschaft PageIndex ruft den 0-basierten Index der ersten zu speichernden Seite ab/setzt diesen.
### **Eigenschaften NumberDecimalSeparator & NumberGroupSeparator hinzugefügt**
Aspose.Cells for Java 8.3.2 hat die Eigenschaften NumberDecimalSeparator & NumberGroupSeparator eingeführt, die die benutzerdefinierten Trennzeichen für das Formatieren & Parsen von numerischen Werten in Tabellenblättern abrufen/setzen können.

Der folgende Beispielcode veranschaulicht, wie die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells-API festgelegt werden. Der folgende Code legt die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt und Leerzeichen fest.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Eigenschaft PdfSaveOptions.setFontSubstitutionCharGranularity hinzugefügt**
Aspose.Cells for Java 8.3.2 hat die Eigenschaft PdfSaveOptions.setFontSubstitutionCharGranularity freigegeben, um das Problem zu überwinden, dass einige Unicode-Zeichen nicht mit einer bestimmten Schriftart angezeigt werden können. Wenn die Eigenschaft PdfSaveOptions.setFontSubstitutionCharGranularity auf true gesetzt ist, wird nur die Schriftart des spezifischen Zeichens, das nicht darstellbar ist, geändert. Der Rest des Wortes oder Satzes sollte in der Originalschrift bleiben.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Entfernte APIs**
### **Veraltete Methoden entfernt**
Folgende Methoden wurden aus der öffentlichen API entfernt:

- Workbook.open & Workbook.save Methoden.
- Workbook.setOleSize Methode.
- Workbook.loadData Methode.
- WorkbookDesigner.open & WorkbookDesigner.save Methoden.
- Die Methode WorksheetCollection.deleteName.
### **Entfernte veraltete Eigenschaften**
Folgende Eigenschaften wurden aus der öffentlichen API entfernt.

- Die Eigenschaft Workbook.isProtected.
- Die Eigenschaft Workbook.Language.
- Die Eigenschaft Workbook.Region.
- Die Eigenschaft WorkbookSettings.ReCalcOnOpen.
- Die Eigenschaft WorkbookSettings.Language.
- Die Eigenschaft WorkbookSettings.Encoding.
- Die Eigenschaft WorkbookSettings.ConvertNumericData.
- Die Eigenschaft WorksheetCollection.HidePivotFieldList.
- Die Eigenschaft WorksheetCollection.EnableHTTPCompression.
- Die Eigenschaft WorksheetCollection.isMinimized.
- Die Eigenschaft WorksheetCollection.isHidden.
- Die Eigenschaft WorksheetCollection.SheetTabBarWidth.
- Die Eigenschaft WorksheetCollection.WindowLeft.
- Die Eigenschaft WorksheetCollection.WindowLeftInch.
- Die Eigenschaft WorksheetCollection.WindowLeftCM.
- Die Eigenschaft WorksheetCollection.WindowTop.
- Die Eigenschaft WorksheetCollection.WindowTopInch.
- Eigenschaft WorksheetCollection.WindowTopCM.
- Eigenschaft WorksheetCollection.WindowWidth.
- Eigenschaft WorksheetCollection.WindowWidthInch.
- Eigenschaft WorksheetCollection.WindowWidthCM.
- Eigenschaft WorksheetCollection.WindowHeight.
- Eigenschaft WorksheetCollection.WindowHeightInch.
- Eigenschaft WorksheetCollection.WindowHeightCM.
- Eigenschaft Worksheet.HPageBreaks.
- Eigenschaft Worksheet.VPageBreaks.
- Eigenschaft HtmlSaveOptions.DisplayHTMLCrossString.
- Eigenschaft HtmlSaveOptions.ExportChartImageFormat.
- Eigenschaft SaveOptions.ExpCellNameToXLSX.
- Eigenschaft SaveOptions.DefaultFont.
- Eigenschaft SaveOptions.Compliance.
- Eigenschaft SaveOptions.PdfBookmark.
- Eigenschaft SaveOptions.PdfImageCompression.
- Eigenschaft TxtSaveOptions.AlwaysQuoted.
## **Veraltete APIs**
### **Überholte Workbook.saveOptions Eigenschaft**
Ein Objekt von SaveOptions muss an die Workbook.Save Methode übergeben werden, nachdem die entsprechenden SaveOptions-Eigenschaften festgelegt wurden. 
### **Veraltete Workbook.Styles & Class StyleCollection-Eigenschaft**
Es wird empfohlen, die Workbook.createStyle-Methode zu verwenden, um Stile für die Workbook-Instanz zu erstellen und zu manipulieren, anstatt einen Stil mit der StyleCollection.add-Methode zu erstellen. Darüber hinaus kann die Workbook.getNamedStyle(string)-Methode verwendet werden, um benannte Styles zu erhalten, anstelle von StyleCollection.get(string).
### **Veraltete PivotItem.move(int count)-Methode**
Mit der Veröffentlichung von Aspose.Cells 8.3.2 hat die API eine weitere Überladung der PivotItem.move-Methode eingeführt, die den Integer-Parameter für die Anzahl und den Boolean-Parameter zum Verschieben eines PivotItem innerhalb des übergeordneten Knotens akzeptiert. 
{{< app/cells/assistant language="java" >}}
