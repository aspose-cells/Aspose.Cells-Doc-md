---
title: Öffentlich API Änderungen in Aspose.Cells 8.4.0
type: docs
weight: 130
url: /de/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.3.2 zu 8.4.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-0/) und[Klassen entfernt usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-0/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Mechanismus zum Ändern des VBA/Makrocodes in Tabellenkalkulationen**
 Um die Funktion bereitzustellen[VBA/Makrocode-Manipulation](/cells/de/net/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for .NET 8.4.0 hat eine Reihe neuer Klassen und Eigenschaften im Aspose.Cells.VBA-Namespace verfügbar gemacht. Einige der wichtigen Details dieser neuen Klassen sind wie folgt.

- Die VbaProject-Klasse kann verwendet werden, um das VBA-Projekt aus einer bestimmten Tabelle abzurufen.
- Die VbaModuleCollection-Klasse stellt die Sammlung von VBA-Modulen dar, die Teil eines bestimmten VbaProject sind.
- Die VbaModule-Klasse repräsentiert ein einzelnes Modul aus der VbaModuleCollection.

Der folgende Codeausschnitt zeigt, wie die VBA-Codesegmente dynamisch geändert werden.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Möglichkeit zum Entfernen der Pivot-Tabelle**
Aspose.Cells for .NET 8.4.0 hat zwei Methoden für die PivotTableCollection bereitgestellt, um die Funktion zum Entfernen von Pivot-Tabellen aus einer bestimmten Tabelle bereitzustellen. Die Einzelheiten der oben genannten Verfahren sind wie folgt.

- Die PivotTableCollection.Remove-Methode akzeptiert ein PivotTable-Objekt und entfernt es aus der Auflistung.
- Die PivotTableCollection.RemoveAt-Methode akzeptiert einen nullindexbasierten ganzzahligen Wert und entfernt die bestimmte PivotTable aus der Auflistung.

Der folgende Codeausschnitt zeigt, wie die PivotTable mit den beiden oben genannten Methoden entfernt wird.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Unterstützung für verschiedene Pivot-Tabellen-Layouts**
Aspose.Cells for .NET 8.4.0 bietet Unterstützung für verschiedene vordefinierte Layouts für Pivot-Tabellen. Um diese Funktion bereitzustellen, haben die Aspose.Cells-APIs drei Methoden für die PivotTable-Klasse verfügbar gemacht, wie unten beschrieben.

- Die PivotTable.ShowInCompactForm-Methode rendert die Pivot-Tabelle im kompakten Layout.
- Die PivotTable.ShowInOutlineForm-Methode rendert die Pivot-Tabelle im Gliederungslayout.
- Die PivotTable.ShowInTabularForm-Methode rendert die Pivot-Tabelle im tabellarischen Layout.

{{% alert color="primary" %}} 

Es ist wichtig, PivotTable.RefreshData & PivotTable.CalculateData aufzurufen, nachdem eines der oben genannten Layouts festgelegt wurde.

{{% /alert %}} 

Der folgende Beispielcode legt verschiedene Layouts für eine Pivot-Tabelle fest und speichert das Ergebnis auf dem Datenträger.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Klasse TxtLoadStyleStrategy & Eigenschaft TxtLoadOptions.LoadStyleStrategy Hinzugefügt**
Aspose.Cells for .NET 8.4.0 hat die TxtLoadStyleStrategy-Klasse und die TxtLoadOptions.LoadStyleStrategy-Eigenschaft verfügbar gemacht, um die Strategie zum Formatieren der geparsten Werte beim Konvertieren des Zeichenfolgenwerts in eine Zahl oder Datumszeit anzugeben.
### **Methode DataBar.ToImage Hinzugefügt**
Mit der Veröffentlichung von v8.4.0 hat der Aspose.Cells API die DataBar.ToImage-Methode bereitgestellt, um die bedingt formatierten DataBars im Bildformat zu speichern. Die Methode {DataBar.ToImage}} akzeptiert zwei Parameter, wie unten beschrieben.

- Der erste Parameter ist vom Typ Aspose.Cells.Cell, auf den bedingte Formatierung angewendet wurde.
- Der zweite Parameter ist vom Typ Aspose.Cells.Rendering.ImageOrPrintOptions, um verschiedene Parameter des resultierenden Bildes einzustellen.

Der folgende Beispielcode veranschaulicht die Verwendung der DataBar.ToImage-Methode zum Rendern des DataBar im Bildformat.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Eigenschaft Border.ThemeColor hinzugefügt**
Aspose.Cells APIs ermöglichen das Extrahieren themenbezogener Formatierungsdaten aus den Tabellenkalkulationen. Mit der Veröffentlichung von Aspose.Cells for .NET 8.4.0 hat API die Border.ThemeColor-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die Themenfarbattribute von Cell-Rahmen abzurufen.
### **Eigenschaft DrawObject.ImageBytes hinzugefügt**
Aspose.Cells for .NET 8.4.0 hat die DrawObject.ImageBytes-Eigenschaft bereitgestellt, um die Bilddaten von Chart oder Shape abzurufen.
### **Eigenschaft HtmlSaveOptions.ExportBogusRowData Hinzugefügt**
Aspose.Cells for .NET 8.4.0 hat die Eigenschaft {HtmlSaveOptions.ExportBogusRowData}} bereitgestellt. Die Eigenschaft Boolescher Typ bestimmt, ob API beim Exportieren der Tabelle in das HTML-Format falsche Daten in der unteren Zeile einfügt.

{{% alert color="primary" %}} 

Der Standardwert ist wahr.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht die Verwendung der oben genannten Eigenschaft.

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Eigenschaft HtmlSaveOptions.CellCssPrefix Hinzugefügt**
Die neu hinzugefügte Eigenschaft HtmlSaveOptions.CellCssPrefix ermöglicht das Festlegen des Präfixes für die CSS-Dateien beim Exportieren von Tabellenkalkulationen in das Format HTML.

{{% alert color="primary" %}} 

Der Standardwert ist "" (leerer String).

{{% /alert %}}
## **Veraltete APIs**
### **Methoden Cells.GetCellByIndex & Row.GetCellByIndex Veraltet**
Verwenden Sie stattdessen die GetEnumerator-Methode, um alle Zellen zu durchlaufen.
### **Eigenschaft DrawObject.Image Veraltet**
Verwenden Sie stattdessen die DrawObject.ImageBytes-Eigenschaft, um Bilddaten abzurufen.
