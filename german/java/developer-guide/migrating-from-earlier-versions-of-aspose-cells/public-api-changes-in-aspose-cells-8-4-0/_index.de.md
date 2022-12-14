---
title: Öffentlich API Änderungen in Aspose.Cells 8.4.0
type: docs
weight: 140
url: /de/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.3.2 zu 8.4.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-0/) und[Klassen entfernt usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-0/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Mechanismus zum Ändern des VBA/Makrocodes in Tabellenkalkulationen**
 Um die Funktion bereitzustellen[VBA/Makrocode-Manipulation](/cells/de/java/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for Java 8.4.0 hat eine Reihe neuer Klassen und Eigenschaften im com.aspose.cells.Vba-Paket verfügbar gemacht. Einige der wichtigen Details dieser neuen Klassen sind wie folgt.

- Die VbaProject-Klasse kann verwendet werden, um das VBA-Projekt aus einer bestimmten Tabelle abzurufen.
- Die VbaModuleCollection-Klasse stellt die Sammlung von VBA-Modulen dar, die Teil eines bestimmten VbaProject sind.
- Die VbaModule-Klasse repräsentiert ein einzelnes Modul aus der VbaModuleCollection.

Der folgende Codeausschnitt zeigt, wie die VBA-Codesegmente dynamisch geändert werden.

**Java**

{{< highlight "csharp" >}}

 Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe("source.xlsm");

//Ändern Sie den VBA-Modulcode

VbaModuleCollection-Module = workbook.getVbaProject().getModules();

 for(int i=0; i< modules.getCount(); i++)

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
### **Möglichkeit zum Entfernen der Pivot-Tabelle**
Aspose.Cells for Java 8.4.0 hat zwei Methoden für die PivotTableCollection bereitgestellt, um die Funktion zum Entfernen von Pivot-Tabellen aus einer bestimmten Tabelle bereitzustellen. Die Einzelheiten der oben genannten Verfahren sind wie folgt.

- Die PivotTableCollection.remove-Methode akzeptiert ein PivotTable-Objekt und entfernt es aus der Auflistung.
- Die PivotTableCollection.removeAt-Methode akzeptiert einen nullindexbasierten ganzzahligen Wert und entfernt die bestimmte PivotTable aus der Sammlung.

Der folgende Codeausschnitt zeigt, wie die PivotTable mit den beiden oben genannten Methoden entfernt wird.

**Java**

{{< highlight "csharp" >}}

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
### **Unterstützung für verschiedene Pivot-Tabellen-Layouts**
Aspose.Cells for Java 8.4.0 bietet Unterstützung für verschiedene vordefinierte Layouts für Pivot-Tabellen. Um diese Funktion bereitzustellen, haben die Aspose.Cells-APIs drei Methoden für die PivotTable-Klasse verfügbar gemacht, wie unten beschrieben.

- Die PivotTable.showInCompactForm-Methode rendert die Pivot-Tabelle im kompakten Layout.
- Die PivotTable.showInOutlineForm-Methode rendert die Pivot-Tabelle im Gliederungslayout.
- Die PivotTable.showInTabularForm-Methode rendert die Pivot-Tabelle im tabellarischen Layout.

{{% alert color="primary" %}} 

 Es ist wichtig, PivotTable.refreshData & PivotTable.calculateData aufzurufen, nachdem eines der oben genannten Layouts festgelegt wurde.

{{% /alert %}} 

Der folgende Beispielcode legt verschiedene Layouts für eine Pivot-Tabelle fest und speichert das Ergebnis auf dem Datenträger.

**Java**

{{< highlight "csharp" >}}

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
### **Klasse TxtLoadStyleStrategy & Eigenschaft TxtLoadOptions.LoadStyleStrategy Hinzugefügt**
Aspose.Cells for Java 8.4.0 hat die TxtLoadStyleStrategy-Klasse und die TxtLoadOptions.LoadStyleStrategy-Eigenschaft verfügbar gemacht, um die Strategie zum Formatieren der geparsten Werte beim Konvertieren des Zeichenfolgenwerts in eine Zahl oder Datumszeit anzugeben.
### **Methode DataBar.ToImage Hinzugefügt**
Mit der Veröffentlichung von v8.4.0 hat der Aspose.Cells API die DataBar.toImage-Methode bereitgestellt, um den bedingt formatierten DataBar im Bildformat zu speichern. Die Methode {DataBar.toImage}} akzeptiert zwei Parameter, wie unten beschrieben.

- Der erste Parameter ist vom Typ com.aspose.cells.Cell, auf den bedingte Formatierung angewendet wurde.
- Der zweite Parameter ist vom Typ com.aspose.cells.rendering.ImageOrPrintOptions, um verschiedene Parameter des resultierenden Bildes einzustellen.

Der folgende Beispielcode veranschaulicht die Verwendung der DataBar.toImage-Methode zum Rendern des DataBar im Bildformat.

**Java**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Eigenschaft Border.ThemeColor hinzugefügt**
Aspose.Cells APIs ermöglichen es, themenbezogene Daten aus den Tabellenkalkulationen zu extrahieren. Mit der Veröffentlichung von Aspose.Cells for Java 8.4.0 hat API die Border.ThemeColor-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die Themenfarbattribute von Cell-Rahmen abzurufen.
### **Eigenschaft DrawObject.ImageBytes hinzugefügt**
Aspose.Cells for Java 8.4.0 hat die DrawObject.ImageBytes-Eigenschaft bereitgestellt, um die Bilddaten von Chart oder Shape abzurufen.
### **Eigenschaft HtmlSaveOptions.ExportBogusRowData Hinzugefügt**
 Aspose.Cells for Java 8.4.0 hat die Eigenschaft {HtmlSaveOptions.ExportBogusRowData}} bereitgestellt. Die Eigenschaft Boolescher Typ bestimmt, ob API beim Exportieren der Tabelle in das HTML-Format falsche Daten in der unteren Zeile einfügt.

{{% alert color="primary" %}} 

Der Standardwert ist wahr.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht die Verwendung der oben genannten Eigenschaft.

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Eigenschaft HtmlSaveOptions.CellCssPrefix Hinzugefügt**
Die neu hinzugefügte Eigenschaft HtmlSaveOptions.CellCssPrefix ermöglicht das Festlegen des Präfixes für die CSS-Dateien beim Exportieren von Tabellenkalkulationen in das HTML-Format.

{{% alert color="primary" %}} 

Der Standardwert ist "" (leerer String).

{{% /alert %}}
## **Veraltete APIs**
### **Methoden Cells.getCellByIndex & Row.getCellByIndex Veraltet**
Verwenden Sie stattdessen die getEnumerator-Methode, um alle Zellen zu durchlaufen.
### **Eigenschaft DrawObject.Image Veraltet**
Verwenden Sie stattdessen die DrawObject.ImageBytes-Eigenschaft, um Bilddaten abzurufen.
