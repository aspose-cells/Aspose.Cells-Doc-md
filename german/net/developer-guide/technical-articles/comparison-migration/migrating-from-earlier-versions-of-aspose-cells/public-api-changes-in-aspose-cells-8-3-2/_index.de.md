---
title: Öffentliche API Änderungen in Aspose.Cells 8.3.2
type: docs
weight: 120
url: /de/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.3.1 bis 8.3.2, die für Modul-/Anwendungs-Entwickler interessant sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen etc.](/cells/de/net/public-api-changes-in-aspose-cells-8-3-2/) und [entfernte Klassen etc.](/cells/de/net/public-api-changes-in-aspose-cells-8-3-2/), sondern auch eine Beschreibung etwaiger Änderungen im Hintergrundverhalten von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Mechanismus zum Festlegen der absoluten Position des PivotItems**
Um die Funktion [Absolute Positionierung des Pivot-Elements](/cells/de/net/specifying-the-absolute-position-of-the-pivot-item/) bereitzustellen, wurden im Aspose.Cells for .NET 8.3.2 eine Reihe von Eigenschaften und Hilfsmethoden wie folgt freigegeben.

- Die Eigenschaft PivotItem.Position kann verwendet werden, um den Positionsinde x aller Pivot-Elemente unabhängig vom übergeordneten Knoten festzulegen.
- Die Eigenschaft PivotItem.PositionInSameParentNode kann verwendet werden, um den Positionsinde x der Pivot-Elemente unter demselben übergeordneten Knoten festzulegen.
- Die Methode PivotItem.Move(int count, bool isSameParent) kann verwendet werden, um das Element basierend auf dem Wert von count nach oben oder unten zu verschieben, wobei count die Anzahl der Positionen angibt, um das Pivot-Element nach oben oder unten zu verschieben. Wenn der Wert von count kleiner als null ist, wird das Element nach oben verschoben, wenn der Wert von count größer als null ist, wird das Pivot-Element nach unten verschoben. Der boolesche Typ isSameParent gibt an, ob die Verschiebungsoperation im selben übergeordneten Knoten durchgeführt werden soll oder nicht.

{{% alert color="primary" %}} 

Bitte beachten Sie, dass es erforderlich ist, die Methoden PivotTable.RefreshData und PivotTable.CalculateData aufzurufen, bevor die Eigenschaften PivotItem.Position, PivotItem.PositionInSameParentNode und die Methode PivotItem.Move(int count, bool isSameParent) verwendet werden.

{{% /alert %}} 
### **Klasse SignatureLine hinzugefügt**
Aspose.Cells for .NET 8.3.2 bietet Unterstützung für die Signaturzeile, um das äquivalente Feature von MS Excel nachzuahmen. Zu diesem Zweck wurde in dieser Version von Aspose.Cells for .NET die Klasse SignatureLine und die Eigenschaft Picture.SignatureLine bereitgestellt.

Der folgende Beispielcode fügt eine Signaturlinie mithilfe der Picture.SignatureLine-Eigenschaft zum Arbeitsblatt hinzu.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Hinzugefügte Methode Chart.HasAxis**
Mit der Version v8.3.2 hat die Aspose.Cells-API die Methode Chart.HasAxis(AxisType axisType, bool isPrimary) bereitgestellt, um zu bestimmen, ob das Diagramm eine bestimmte Achse oder nicht hat.

Der folgende Beispielcode zeigt die Verwendung der Methode Chart.HasAxis, um festzustellen, ob das Beispiel-Diagramm Primär-, Sekundär- und Wertachsen hat.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **Methode WorkbookSettings.CheckWriteProtectedPassword hinzugefügt**
Die Methode WorkbookSettings.CheckWriteProtectedPassword ermöglicht es Entwicklern zu prüfen, ob ein gegebenes Passwort zur Änderung der Kalkulationstabelle korrekt ist oder nicht.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Überladene Methoden WorkbookRender.ToPrinter & SheetRender.ToPrinter hinzugefügt**
Mit der Version Aspose.Cells for .NET 8.3.2 wurden die Methoden WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) und SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) bereitgestellt, um den Bereich der Seiten des Arbeitsbuchs und des Arbeitsblatts jeweils zu drucken.

Der folgende Beispielcode veranschaulicht die Verwendung der genannten Methoden zum Drucken der Seiten 2-5 des Arbeitsmappens und des Arbeitsblatts.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Methode Worksheet.RefreshPivotTables hinzugefügt**
Die neu hinzugefügte Methode Worksheet.RefreshPivotTables ermöglicht das Aktualisieren aller Pivot-Tabellen in einer bestimmten Kalkulationstabelle in einem einzigen Aufruf.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Methode Workbook.GetNamedStyle hinzugefügt**
Das API Aspose.Cells for .NET hat die Methode Workbook.GetNamedStyle freigelegt, die den String als Parameter akzeptiert und das Style-Objekt basierend auf dem übergebenen Parameter abruft.
### **Methode Cells.ImportTwoDimensionArray hinzugefügt**
Das API Aspose.Cells for .NET hat es ermöglicht, zweidimensionale Arrays in Zellen des Tabellenkalkulationsblatts zu importieren, indem die Methode Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) freigelegt wurde. Die genannte Methode importiert ein zweidimensionales Array von Daten in ein Arbeitsblatt mit flexibleren Optionen, die in TxtLoadOptions definiert sind.
### **Eigenschaften OnePagePerSheet, PageIndex & PageCount hinzugefügt**
Das API Aspose.Cells for .NET 8.3.2 hat die Eigenschaften OnePagePerSheet, PageIndex & PageCount für die XpsSaveOptions-Klasse freigelegt. Der Benutzer kann alle Inhalte einer Tabellenkalkulation auf einer einzigen Seite des XPS mit der Eigenschaft OnePagePerSheet anpassen und/oder die Anzahl der zu druckenden Seiten mit der Eigenschaft PageCount abrufen. Die Eigenschaft PageIndex ruft den 0-basierten Index der ersten zu speichernden Seite ab/legt ihn fest.
### **Eigenschaften NumberDecimalSeparator & NumberGroupSeparator hinzugefügt**
Das API Aspose.Cells for .NET 8.3.2 hat die Eigenschaften NumberDecimalSeparator & NumberGroupSeparator eingeführt, die die benutzerdefinierten Trennzeichen für das Formatieren und Analysieren numerischer Werte in Tabellenkalkulationen abrufen/legen können.

Der folgende Beispielcode veranschaulicht, wie die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells API festgelegt werden. Der folgende Code legt die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt bzw. Leerzeichen fest.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Hinzugefügte Eigenschaft PdfSaveOptions.IsFontSubstitutionCharGranularity**
Das API Aspose.Cells for .NET 8.3.2 hat die Eigenschaft PdfSaveOptions.IsFontSubstitutionCharGranularity freigelegt, um das Problem zu lösen, dass einige Unicode-Zeichen mit einer bestimmten Schriftart nicht angezeigt werden können. Wenn PdfSaveOptions.IsFontSubstitutionCharGranularity auf true gesetzt ist, wird nur die Schriftart des spezifischen nicht darstellbaren Zeichens zu einer darstellbaren Schriftart geändert, während der Rest des Worts oder Satzes in der Originalschriftart verbleiben sollte.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Entfernte APIs**
### **Veraltete Methoden entfernt**
Folgende Methoden wurden aus der öffentlichen API entfernt:

- Workbook.Open & Workbook.Save Methoden.
- Workbook.SetOleSize Methode.
- Workbook.LoadData Methode.
- WorkbookDesigner.Open & WorkbookDesigner.Save Methoden.
- WorksheetCollection.DeleteName Methode.
### **Entfernte veraltete Eigenschaften**
Folgende Eigenschaften wurden aus der öffentlichen API entfernt.

- Workbook.IsProtected Eigenschaft.
- Die Eigenschaft Workbook.Language.
- Die Eigenschaft Workbook.Region.
- Die Eigenschaft WorkbookSettings.ReCalcOnOpen.
- Die Eigenschaft WorkbookSettings.Language.
- Die Eigenschaft WorkbookSettings.Encoding.
- Die Eigenschaft WorkbookSettings.ConvertNumericData.
- Die Eigenschaft WorksheetCollection.HidePivotFieldList.
- Die Eigenschaft WorksheetCollection.EnableHTTPCompression.
- WorksheetCollection.IsMinimized-Eigenschaft.
- WorksheetCollection.IsHidden-Eigenschaft.
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
### **Veraltete Workbook.SaveOptions-Eigenschaft**
Ein Objekt von SaveOptions muss an die Workbook.Save Methode übergeben werden, nachdem die entsprechenden SaveOptions-Eigenschaften festgelegt wurden.
### **Veraltete Workbook.Styles-Eigenschaft und Klassen StyleCollection**
Es wird empfohlen, die Workbook.CreateStyle-Methode zu verwenden, um einen Stil für eine Workbook-Instanz zu erstellen und zu manipulieren, anstelle eines Stils mit der StyleCollection.Add-Methode zu erstellen. Außerdem kann die Workbook.GetNamedStyle(string)-Methode verwendet werden, um benannten Stil zu erhalten, anstatt StyleCollection[string].
### **Veraltete PivotItem.Move(int count)-Methode**
Mit der Veröffentlichung von Aspose.Cells 8.3.2 hat die API eine weitere Überladung der PivotItem.Move-Methode eingeführt, die den ganzzahligen Parameter für den Count und den booleschen Parameter akzeptiert, um ein PivotItem innerhalb des übergeordneten Knotens zu verschieben.
{{< app/cells/assistant language="csharp" >}}
