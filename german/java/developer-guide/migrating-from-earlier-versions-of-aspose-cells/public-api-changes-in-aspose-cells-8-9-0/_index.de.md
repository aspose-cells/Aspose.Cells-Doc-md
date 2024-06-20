---
title: Öffentliche API Änderungen in Aspose.Cells 8.9.0
type: docs
weight: 310
url: /de/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.8.3 bis 8.9.0, die für Modul-/Anwendungs-Entwickler interessant sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung von etwaigen Änderungen im Arbeitsablauf hinter den Kulissen bei Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügte HtmlSaveOptions.DefaultFontName Eigenschaft**
Aspose.Cells for Java 8.9.0 hat die Eigenschaft DefaultFontName für die Klasse HtmlSaveOptions freigelegt, die es ermöglicht, den Standardschriftartnamen beim Rendern von Tabellenkalkulationen im HTML-Format anzugeben. Die Standardschriftart wird nur verwendet, wenn die Schriftart des Stils nicht existiert. Der Standardwert der Eigenschaft HtmlSaveOptions.DefaultFontName ist null, was bedeutet, dass Aspose.Cells for Java API die universelle Schriftart verwenden wird, die dieselbe Familie wie die Originalschriftart hat.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den Artikel zu [Festlegen der Standardschriftart beim Rendern von Tabellenkalkulationen im HTML-Format](/cells/de/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Hinzugefügte ImageOrPrintOptions.DefaultFont Eigenschaft**
Aspose.Cells for Java 8.9.0 ermöglicht es, den Standardschriftartnamen für die Klasse ImageOrPrintOptions durch Freigabe der Eigenschaft DefaultFont festzulegen. Die genannte Eigenschaft kann verwendet werden, wenn Unicode-Zeichen in der Tabellenkalkulation im Zellstil nicht mit der richtigen Schriftart festgelegt sind und daher in den resultierenden Bildern als Blöcke angezeigt werden können. 

{{% alert color="primary" %}} 

Legen Sie die DefaultFont-Eigenschaft auf MingLiu oder MS Gothic fest, um Unicode-Zeichen anzuzeigen. Wenn die genannte Eigenschaft nicht festgelegt ist, verwendet Aspose.Cells die Standardschriftart des Systems, um Unicode-Zeichen anzuzeigen. 

{{% /alert %}} {{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den Artikel über [Festlegen der Standardschriftart beim Rendern von Tabellenkalkulationen in Bildformaten](/cells/de/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **Hinzugefügte PivotTable.Excel2003Compatible Eigenschaft**
Aspose.Cells for Java API hat die boolesche Eigenschaft Excel2003Compatible für die Klasse PivotTable freigelegt, die es ermöglicht festzulegen, ob die Pivot-Tabelle für Aktualisierungszwecke kompatibel mit Excel 2003 ist. Der Standardwert der Eigenschaft Excel2003Compatible ist true, das bedeutet, dass ein Zeichenfolgenwert kleiner oder gleich 255 Zeichen sein muss. Wenn die Zeichenfolge größer als 255 Zeichen ist, wird sie abgeschnitten. Wenn false, wird die genannte Beschränkung nicht auferlegt.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den Artikel über [Kompatibilität für Excel 2003 bei der Aktualisierung von Pivot-Tabellen](/cells/de/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
