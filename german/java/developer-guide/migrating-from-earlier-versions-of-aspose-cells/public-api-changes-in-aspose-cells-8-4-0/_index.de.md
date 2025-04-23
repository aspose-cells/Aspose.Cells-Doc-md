---
title: Öffentliche API Änderungen in Aspose.Cells 8.4.0
type: docs
weight: 140
url: /de/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.3.2 auf 8.4.0, die für Modul-/Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-0/) und [entfernte Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-0/), sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Mechanismus zur Modifizierung des VBA-/Makro-Codes in Arbeitsblättern**
Um die Funktion [VBA-/Makro-Code-Manipulation](/cells/de/java/modifying-vba-or-macro-code-using-aspose-cells/) bereitzustellen, hat die Aspose.Cells for Java 8.4.0 eine Reihe neuer Klassen und Eigenschaften im com.aspose.cells.Vba-Paket freigegeben. Einige wichtige Details zu diesen neuen Klassen lauten wie folgt.

- Die VbaProject-Klasse kann verwendet werden, um das VBA-Projekt aus einem bestimmten Arbeitsblatt abzurufen.
- Die VbaModuleCollection-Klasse repräsentiert die Sammlung von VBA-Modulen, die Teil eines bestimmten VbaProject sind.
- Die VbaModule-Klasse repräsentiert ein einzelnes Modul aus der VbaModuleCollection.

Der folgende Code-Schnipsel zeigt, wie die VBA-Codeabschnitte dynamisch geändert werden.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **Fähigkeit, Pivot-Tabelle zu entfernen**
Aspose.Cells for Java 8.4.0 hat zwei Methoden für die PivotTableCollection freigegeben, um die Funktion der Pivot-Tabellenentfernung aus einem bestimmten Arbeitsblatt bereitzustellen. Die Details der genannten Methoden lauten wie folgt.

- Die Methode PivotTableCollection.remove akzeptiert ein Objekt von PivotTable und entfernt es aus der Sammlung.
- Die Methode PivotTableCollection.removeAt akzeptiert einen nullbasierten Integer-Wert und entfernt die bestimmte PivotTable aus der Sammlung.

Der folgende Code-Schnipsel zeigt, wie die PivotTable mithilfe beider oben genannter Methoden entfernt werden können.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Unterstützung für verschiedene Pivot-Tabellenlayouts**
Aspose.Cells for Java 8.4.0 bietet Unterstützung für verschiedene vordefinierte Layouts für Pivot-Tabellen. Um diese Funktion bereitzustellen, haben die Aspose.Cells-APIs drei Methoden für die PivotTable-Klasse freigegeben, wie nachstehend detailliert beschrieben.

- Die Methode PivotTable.showInCompactForm rendert die Pivot-Tabelle im Kompaktlayout.
- Die Methode PivotTable.showInOutlineForm rendert die Pivot-Tabelle im Gliederungslayout.
- Die Methode PivotTable.showInTabularForm rendert die Pivot-Tabelle im tabellarischen Layout.

{{% alert color="primary" %}} 

Es ist wichtig, nach dem Setzen eines der oben genannten Layouts die Methoden PivotTable.refreshData & PivotTable.calculateData aufzurufen. 

{{% /alert %}} 

Der folgende Beispielcode setzt verschiedene Layouts für eine Pivot-Tabelle und speichert das Ergebnis auf der Festplatte.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Die Klasse TxtLoadStyleStrategy & die Eigenschaft TxtLoadOptions.LoadStyleStrategy wurden hinzugefügt.**
Aspose.Cells for Java 8.4.0 hat die Klasse TxtLoadStyleStrategy und die Eigenschaft TxtLoadOptions.LoadStyleStrategy freigelegt, um die Strategie zur Formatierung der analysierten Werte beim Konvertieren von Zeichenfolgenwerten in Zahlen oder Datum/Uhrzeit anzugeben.
### **Methode 'DataBar.ToImage' hinzugefügt.**
Mit der Veröffentlichung von v8.4.0 hat die Aspose.Cells API die Methode DataBar.toImage bereitgestellt, um die bedingte formatierte DataBar im Bildformat zu speichern. Die Methode {DataBar.toImage} akzeptiert zwei Parameter, wie unten detailliert.

- Der erste Parameter ist vom Typ com.aspose.cells.Cell, auf den bedingte Formatierung angewendet wurde.
- Der zweite Parameter ist vom Typ com.aspose.cells.rendering.ImageOrPrintOptions, um verschiedene Parameter des resultierenden Bildes festzulegen.

Der folgende Beispielcode veranschaulicht die Verwendung der Methode DataBar.toImage, um die DataBar im Bildformat zu rendern.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Eigenschaft Border.ThemeColor hinzugefügt.**
Aspose.Cells APIs ermöglichen es, themenbezogene Daten aus den Tabellenkalkulationen zu extrahieren. Mit der Veröffentlichung von Aspose.Cells for Java 8.4.0 hat die API die Eigenschaft Border.ThemeColor freigelegt, die verwendet werden kann, um die themenbezogenen Farbeigenschaften von Zellgrenzen abzurufen.
### **Eigenschaft DrawObject.ImageBytes hinzugefügt.**
Aspose.Cells for Java 8.4.0 hat die Eigenschaft DrawObject.ImageBytes freigelegt, um die Bilddaten aus dem Diagramm oder der Form zu erhalten.
### **Eigenschaft HtmlSaveOptions.ExportBogusRowData hinzugefügt.**
Aspose.Cells for Java 8.4.0 hat die Eigenschaft {HtmlSaveOptions.ExportBogusRowData} bereitgestellt. Die Eigenschaft vom Typ Boolean bestimmt, ob die API falsche untere Zeilendaten beim Export der Tabellenkalkulation in das HTML-Format injiziert. 

{{% alert color="primary" %}} 

Der Standardwert ist true.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht die Verwendung der genannten Eigenschaft.

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Eigenschaft HtmlSaveOptions.CellCssPrefix hinzugefügt**
Die neu hinzugefügte Eigenschaft HtmlSaveOptions.CellCssPrefix ermöglicht das Festlegen des Präfix für die CSS-Dateien beim Export von Tabellenkalkulationen im HTML-Format.

{{% alert color="primary" %}} 

Der Standardwert ist "" (Leerzeichen).

{{% /alert %}}
## **Veraltete APIs**
### **Veraltete Cells.getCellByIndex & Row.getCellByIndex Methoden**
Verwenden Sie die getEnumerator-Methode, um alle Zellen zu durchlaufen.
### **Veraltete DrawObject.Image Eigenschaft**
Verwenden Sie stattdessen die DrawObject.ImageBytes-Eigenschaft, um Bilddaten zu erhalten.
{{< app/cells/assistant language="java" >}}
