---
title: Öffentlich API Änderungen in Aspose.Cells 16.11.0
type: docs
weight: 350
url: /de/net/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.10.0 zu 16.11.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Globalisierungseinstellungen**
Aspose.Cells 16.11.0 hat die GlobalizationSettings-Klasse zusammen mit der WorkbookSettings.GlobalizationSettings-Eigenschaft verfügbar gemacht, um die Aspose.Cells-APIs zur Verwendung benutzerdefinierter Bezeichnungen für Zwischensummen zu erzwingen. Die GlobalizationSettings-Klasse verfügt über die folgenden Methoden, die in der benutzerdefinierten Implementierung überschrieben werden können, um den Beschriftungen die gewünschten Namen zu geben**Gesamt** & **Gesamtsumme**.

- GlobalizationSettings.GetTotalName: Ruft den Gesamtnamen der Funktion ab.
- GlobalizationSettings.GetGrandTotalName: Ruft den Gesamtsummennamen der Funktion ab.

Hier ist eine einfache benutzerdefinierte Klasse, die die GlobalizationSettings-Klasse erweitert und ihre oben genannten Methoden überschreibt, um benutzerdefinierte Bezeichnungen für die Konsolidierungsfunktion Average zurückzugeben.

**C#**

{{< highlight "csharp" >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



Das folgende Snippet lädt ein vorhandenes Arbeitsblatt und fügt die Zwischensumme des Typs „Durchschnitt“ zu Daten hinzu, die bereits im Arbeitsblatt verfügbar sind. Die CustomSettings-Klasse und ihre GetTotalName- und GetGrandTotalName-Methoden werden zum Zeitpunkt des Hinzufügens von Subtotal zum Arbeitsblatt aufgerufen.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[]{ 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



Die GlobalizationSettings-Klasse bietet auch die GetOtherName-Methode, die nützlich ist, um den Namen von „Anderen“-Beschriftungen für Kreisdiagramme abzurufen. Hier ist ein einfaches Verwendungsszenario der Methode GlobalizationSettings.GetOtherName.

**C#**

{{< highlight "csharp" >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



Der folgende Codeausschnitt lädt eine vorhandene Tabelle mit einem Kreisdiagramm und rendert das Diagramm in ein Bild, während die oben erstellte CustomSettings-Klasse verwendet wird.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **CellsFactory-Klasse hinzugefügt**
Aspose.Cells 16.11.0 hat die CellsFactory-Klasse verfügbar gemacht, die derzeit eine Methode hat, das heißt; CreateStyle. Die CellsFactory.CreateStyle-Methode kann verwendet werden, um eine Instanz der Style-Klasse zu erstellen, ohne sie dem Pool von Arbeitsmappenstilen hinzuzufügen.

Hier ist ein einfaches Anwendungsszenario der CellsFactory.CreateStyle-Methode.

**C#**

{{< highlight "csharp" >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Workbook.AbsolutePath-Eigenschaft hinzugefügt**
Aspose.Cells 16.11.0 hat die Workbook.AbsolutePath-Eigenschaft verfügbar gemacht, die es ermöglicht, den absoluten Arbeitsmappenpfad abzurufen oder festzulegen, der in der Datei workbook.xml gespeichert ist. Diese Eigenschaft ist nur beim Aktualisieren der externen Links nützlich.
### **GridHyperlinkCollection.GetHyperlink-Methode hinzugefügt**
Aspose.Cells.GridWeb 16.11.0 hat die GetHyperlink-Methode für die GridHyperlinkCollection-Klasse verfügbar gemacht, die es ermöglicht, die Instanz von GridHyperlink abzurufen, indem entweder eine Instanz GridCell oder ein Paar Ganzzahlen übergeben wird, die den Zeilenspaltenindizes entsprechen.

{{% alert color="primary" %}} 

Falls in der angegebenen Zelle kein Hyperlink gefunden wurde, gibt die GetHyperlink-Methode null zurück.

{{% /alert %}} 

Hier ist ein einfaches Anwendungsszenario der GetHyperlink-Methode.

**C#**

{{< highlight "csharp" >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **Veraltete APIs**
### **Veralteter Stilkonstruktor**
Bitte verwenden Sie alternativ die Methode cellsFactory.CreateStyle.
## **Gelöschte APIs**
### **Cell.GetConditionalStyle-Methode gelöscht**
Bitte verwenden Sie stattdessen die Methode Cell.GetConditionalFormattingResult.
### **Methode Cells.MaxDataRowInColumn(int column) gelöscht**
Bitte verwenden Sie alternativ die Methode Cells.GetLastDataRow(int).
### **PageSetup.Draft-Eigenschaft gelöscht**
Es wird empfohlen, stattdessen die Eigenschaft PageSetup.PrintDraft zu verwenden.
### **Gelöschte AutoFilter.FilterColumnCollection-Eigenschaft**
Bitte erwägen Sie die Verwendung der AutoFilter.FilterColumns-Eigenschaft, um dasselbe Ziel zu erreichen.
### **Gelöschte TickLabels.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die Eigenschaft TickLabels.RotationAngle.
