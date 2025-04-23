---
title: Öffentliche API Änderungen in Aspose.Cells 8.4.0
type: docs
weight: 130
url: /de/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.3.2 auf 8.4.0, die für Modulentwickler/Anwendungsprogrammierer interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-0/) und [entfernte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-0/), sondern auch eine Beschreibung möglicher Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Mechanismus zur Modifizierung des VBA-/Makro-Codes in Arbeitsblättern**
Um die Funktion zur [Manipulation des VBA/Makro-Codes](/cells/de/net/modifying-vba-or-macro-code-using-aspose-cells/) bereitzustellen, hat die Aspose.Cells for .NET 8.4.0 eine Reihe neuer Klassen und Eigenschaften im Namensraum Aspose.Cells.Vba freigelegt. Einige wichtige Details dieser neuen Klassen sind wie folgt.

- Die VbaProject-Klasse kann verwendet werden, um das VBA-Projekt aus einem bestimmten Arbeitsblatt abzurufen.
- Die VbaModuleCollection-Klasse repräsentiert die Sammlung von VBA-Modulen, die Teil eines bestimmten VbaProject sind.
- Die VbaModule-Klasse repräsentiert ein einzelnes Modul aus der VbaModuleCollection.

Der folgende Code-Schnipsel zeigt, wie die VBA-Codeabschnitte dynamisch geändert werden.

**C#**

{{< highlight csharp >}}

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


### **Fähigkeit, Pivot-Tabelle zu entfernen**
Aspose.Cells for .NET 8.4.0 hat zwei Methoden für die PivotTableCollection freigelegt, um die Funktion zum Entfernen von Pivot-Tabellen aus einer bestimmten Tabelle bereitzustellen. Die Details der genannten Methoden sind wie folgt.

- Die Methode PivotTableCollection.Remove akzeptiert ein Objekt von PivotTable und entfernt es aus der Sammlung.
- Die Methode PivotTableCollection.RemoveAt akzeptiert einen nullbasierten ganzzahligen Wert und entfernt die jeweilige PivotTabelle aus der Sammlung.

Der folgende Code-Schnipsel zeigt, wie die PivotTable mithilfe beider oben genannter Methoden entfernt werden können.

**C#**

{{< highlight csharp >}}

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


### **Unterstützung für verschiedene Pivot-Tabellenlayouts**
Aspose.Cells for .NET 8.4.0 bietet Unterstützung für verschiedene vordefinierte Layouts für Pivot-Tabellen. Um diese Funktion bereitzustellen, haben die Aspose.Cells-APIs drei Methoden für die PivotTable-Klasse freigelegt, wie unten detailliert beschrieben.

- Die Methode PivotTable.ShowInCompactForm rendert die Pivot-Tabelle im kompakten Layout.
- Die Methode PivotTable.ShowInOutlineForm rendert die Pivot-Tabelle im Gliederungs-Layout.
- Die Methode PivotTable.ShowInTabularForm rendert die Pivot-Tabelle im tabellarischen Layout.

{{% alert color="primary" %}} 

Es ist wichtig, die Methoden PivotTable.RefreshData und PivotTable.CalculateData aufzurufen, nachdem eines der oben genannten Layouts festgelegt wurde.

{{% /alert %}} 

Der folgende Beispielcode setzt verschiedene Layouts für eine Pivot-Tabelle und speichert das Ergebnis auf der Festplatte.

**C#**

{{< highlight csharp >}}

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


### **Die Klasse TxtLoadStyleStrategy & die Eigenschaft TxtLoadOptions.LoadStyleStrategy wurden hinzugefügt.**
Aspose.Cells for .NET 8.4.0 hat die Klasse TxtLoadStyleStrategy und das Attribut TxtLoadOptions.LoadStyleStrategy freigelegt, um die Strategie zur Formatierung der analysierten Werte beim Konvertieren von Zeichenfolgen in Zahlen oder Datum/Zeit festzulegen.
### **Methode 'DataBar.ToImage' hinzugefügt.**
Mit der Version v8.4.0 bietet die Aspose.Cells API die Methode DataBar.ToImage zum Speichern der bedingt formatierten DataBars im Bildformat an. Die Methode {DataBar.ToImage}} akzeptiert zwei Parameter wie unten detailliert.

- Der erste Parameter ist vom Typ Aspose.Cells.Cell, auf den die bedingte Formatierung angewendet wurde.
- Der zweite Parameter ist vom Typ Aspose.Cells.Rendering.ImageOrPrintOptions, um verschiedene Parameter des resultierenden Bildes festzulegen.

Der folgende Beispielcode zeigt die Verwendung der Methode DataBar.ToImage zum Rendern der DataBar im Bildformat an.

**C#**

{{< highlight csharp >}}

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

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Eigenschaft Border.ThemeColor hinzugefügt.**
Aspose.Cells APIs erlauben das Extrahieren von themenbezogenen Formatierungsdaten aus den Tabellenkalkulationen. Mit der Version Aspose.Cells for .NET 8.4.0 hat die API die Eigenschaft Border.ThemeColor freigelegt, die genutzt werden kann, um die Themafarbeigenschaften der Zellgrenzen abzurufen.
### **Eigenschaft DrawObject.ImageBytes hinzugefügt.**
Aspose.Cells for .NET 8.4.0 hat die Eigenschaft DrawObject.ImageBytes freigelegt, um die Bilddaten von Diagramm oder Form zu erhalten.
### **Eigenschaft HtmlSaveOptions.ExportBogusRowData hinzugefügt.**
Aspose.Cells for .NET 8.4.0 hat die {HtmlSaveOptions.ExportBogusRowData}}-Eigenschaft bereitgestellt. Die Eigenschaft vom Typ Boolean bestimmt, ob die API falsche untere Zeilendaten einfügt, während die Tabelle in das HTML-Format exportiert wird.

{{% alert color="primary" %}} 

Der Standardwert ist true.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht die Verwendung der genannten Eigenschaft.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Eigenschaft HtmlSaveOptions.CellCssPrefix hinzugefügt**
Die neu hinzugefügte Eigenschaft HtmlSaveOptions.CellCssPrefix ermöglicht das Festlegen des Präfix für die CSS-Dateien beim Export von Tabellenkalkulationen im HTML-Format.

{{% alert color="primary" %}} 

Der Standardwert ist "" (Leerzeichen).

{{% /alert %}}
## **Veraltete APIs**
### **Veraltete Methoden Cells.GetCellByIndex & Row.GetCellByIndex**
Verwenden Sie die GetEnumerator-Methode, um alle Zellen iterativ zu durchlaufen.
### **Veraltete DrawObject.Image Eigenschaft**
Verwenden Sie stattdessen die DrawObject.ImageBytes-Eigenschaft, um Bilddaten zu erhalten.
{{< app/cells/assistant language="csharp" >}}
