---
title: Öffentlich API Änderungen in Aspose.Cells 8.9.0
type: docs
weight: 300
url: /de/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.8.3 zu 8.9.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **HtmlSaveOptions.DefaultFontName-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.9.0 hat die DefaultFontName-Eigenschaft für die HtmlSaveOptions-Klasse verfügbar gemacht, die es ermöglicht, den Standardschriftartnamen anzugeben, während Tabellen im HTML-Format gerendert werden. Die Standardschriftart wird nur verwendet, wenn die Schriftart des Stils nicht vorhanden ist. Der Standardwert der Eigenschaft HtmlSaveOptions.DefaultFontName ist null, was bedeutet, dass Aspose.Cells for .NET API die universelle Schriftart verwendet, die dieselbe Familie wie die ursprüngliche Schriftart hat.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im Artikel auf[Festlegen der Standardschriftart zum Rendern von Tabellenkalkulationen im HTML-Format](/cells/de/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **ImageOrPrintOptions.DefaultFont-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.9.0 ermöglicht das Festlegen des Standardschriftartnamens für die ImageOrPrintOptions-Klasse durch Verfügbarmachen der DefaultFont-Eigenschaft. Die besagte Eigenschaft kann verwendet werden, wenn Unicode-Zeichen in der Tabelle nicht mit der richtigen Schriftart im Zellenstil gesetzt sind, daher können solche Zeichen als Blöcke in den resultierenden Bildern erscheinen.

{{% alert color="primary" %}} 

Legen Sie die DefaultFont-Eigenschaft auf MingLiu oder MS Gothic fest, um Unicode-Zeichen anzuzeigen. Wenn die genannte Eigenschaft nicht gesetzt ist, verwendet Aspose.Cells die Standardschriftart des Systems, um Unicode-Zeichen anzuzeigen.

{{% /alert %}} {{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im Artikel auf[Festlegen der Standardschriftart zum Rendern von Tabellenkalkulationen in Bildformaten](/cells/de/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **PivotTable.IsExcel2003Compatible-Eigenschaft hinzugefügt**
Aspose.Cells for .NET API hat die IsExcel2003Compatible-Eigenschaft des booleschen Typs für die PivotTable-Klasse verfügbar gemacht, mit der angegeben werden kann, ob die PivotTable zu Aktualisierungszwecken mit Excel 2003 kompatibel ist. Der Standardwert der Eigenschaft IsExcel2003Compatible ist „true“, was bedeutet, dass eine Zeichenfolge kleiner oder gleich 255 Zeichen sein muss. Wenn die Zeichenfolge länger als 255 Zeichen ist, wird sie abgeschnitten. Wenn falsch, wird die oben genannte Beschränkung nicht auferlegt.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im Artikel auf[Kompatibilität für Excel 2003 zum Aktualisieren von Pivot-Tabellen](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **GridWeb.GetVersion-Methode hinzugefügt**
Aspose.Cells.GridWeb for .NET 8.9.0 hat die Factory-Methode {GetVersion}} verfügbar gemacht, die die Release-Version der GridWeb-Komponente zurückgibt.
