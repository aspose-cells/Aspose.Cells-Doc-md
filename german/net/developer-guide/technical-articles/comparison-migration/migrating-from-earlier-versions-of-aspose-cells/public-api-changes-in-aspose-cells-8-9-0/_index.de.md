---
title: Öffentliche API Änderungen in Aspose.Cells 8.9.0
type: docs
weight: 300
url: /de/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.8.3 bis 8.9.0, die für Modul-/Anwendungs-Entwickler interessant sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung von etwaigen Änderungen im Arbeitsablauf hinter den Kulissen bei Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügte HtmlSaveOptions.DefaultFontName Eigenschaft**
Aspose.Cells for .NET 8.9.0 hat die DefaultFontName-Eigenschaft für die HtmlSaveOptions-Klasse freigegeben, die es ermöglicht, den Standard-Schriftartnamen beim Rendern von Tabellenkalkulationen im HTML-Format anzugeben. Die Standard-Schriftart wird nur dann verwendet, wenn die Schriftart des Stils nicht vorhanden ist. Der Standardwert der HtmlSaveOptions.DefaultFontName-Eigenschaft ist null, das bedeutet, dass die Aspose.Cells for .NET-API die Universalschriftart verwenden wird, die dieselbe Familie wie die ursprüngliche Schriftart hat.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den Artikel [Festlegen der Standard-Schriftart für das Rendern von Tabellenkalkulationen im HTML-Format](/cells/de/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Hinzugefügte ImageOrPrintOptions.DefaultFont Eigenschaft**
Aspose.Cells for .NET 8.9.0 ermöglicht es, den Standard-Schriftartnamen für die ImageOrPrintOptions-Klasse durch Freigabe der DefaultFont-Eigenschaft festzulegen. Die genannte Eigenschaft kann verwendet werden, wenn Unicode-Zeichen in der Tabellenkalkulation nicht mit der korrekten Schriftart im Zellstil festgelegt sind. Solche Zeichen können daher in den resultierenden Bildern als Blöcke erscheinen.

{{% alert color="primary" %}} 

Legen Sie die DefaultFont-Eigenschaft auf MingLiu oder MS Gothic fest, um Unicode-Zeichen anzuzeigen. Wenn die genannte Eigenschaft nicht festgelegt ist, verwendet Aspose.Cells die Standardschriftart des Systems, um Unicode-Zeichen anzuzeigen.

{{% /alert %}} {{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den Artikel [Festlegen der Standard-Schriftart für das Rendern von Tabellenkalkulationen in Bildformaten](/cells/de/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügte PivotTable.IsExcel2003Compatible-Eigenschaft**
Aspose.Cells for .NET-API hat die boolesche IsExcel2003Compatible-Eigenschaft für die PivotTable-Klasse freigegeben, die es ermöglicht anzugeben, ob die PivotTable für Auffrischungszwecke mit Excel 2003 kompatibel ist. Der Standardwert der IsExcel2003Compatible-Eigenschaft ist true, das bedeutet, dass ein String kleiner oder gleich 255 Zeichen sein muss. Wenn der String größer als 255 Zeichen ist, wird er abgeschnitten. Wenn false, wird die oben genannte Einschränkung nicht durchgesetzt.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den Artikel [Kompatibilität für Excel 2003 für das Aktualisieren von Pivot-Tabellen](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügter GridWeb.GetVersion-Methode**
Aspose.Cells.GridWeb für .NET 8.9.0 hat die {GetVersion}}-Factory-Methode freigegeben, die die Versionsnummer des GridWeb-Komponenten zurückgibt.
{{< app/cells/assistant language="csharp" >}}
