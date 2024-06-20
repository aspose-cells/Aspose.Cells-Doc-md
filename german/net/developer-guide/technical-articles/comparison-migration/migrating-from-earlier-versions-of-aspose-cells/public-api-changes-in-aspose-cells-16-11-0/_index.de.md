---
title: Öffentliche API Änderungen in Aspose.Cells 16.11.0
type: docs
weight: 350
url: /de/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 16.10.0 auf 16.11.0, die für Modul-/Anwendungsentwickler von Interesse sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Globalisierungseinstellungen**
Aspose.Cells 16.11.0 hat die GlobalizationSettings-Klasse zusammen mit der WorkbookSettings.GlobalizationSettings Eigenschaft freigegeben, um die Aspose.Cells APIs zu zwingen, benutzerdefinierte Bezeichnungen für Zwischensummen zu verwenden. Die GlobalizationSettings-Klasse verfügt über die folgenden Methoden, die in der benutzerdefinierten Implementierung überschrieben werden können, um gewünschte Namen für die Bezeichnungen **Gesamt** & **Gesamtsumme** zu liefern.

- GlobalizationSettings.GetTotalName: Ruft den Gesamtnamen der Funktion ab.
- GlobalizationSettings.GetGrandTotalName: Ruft den Gesamtnamen der Funktion ab.

Hier ist eine einfache benutzerdefinierte Klasse, die die GlobalizationSettings-Klasse erweitert und ihre oben genannten Methoden überschreibt, um benutzerdefinierte Bezeichnungen für die Konsolidierungsfunktion Durchschnitt zurückzugeben.

**C#**

{{< highlight csharp >}}

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



Der folgende Ausschnitt lädt eine vorhandene Tabellenkalkulation und fügt das Zwischenergebnis des Typs Durchschnitt zu den bereits in dem Arbeitsblatt vorhandenen Daten hinzu. Die CustomSettings-Klasse und ihre Methoden GetTotalName & GetGrandTotalName werden zur Zeit der Hinzufügung des Zwischenergebnisses zum Arbeitsblatt aufgerufen.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



Die GlobalizationSettings-Klasse bietet auch die Methode GetOtherName, die nützlich ist, um die Bezeichnung "Andere" für Tortendiagramme zu erhalten. Hier ist ein einfaches Anwendungsbeispiel der Methode GlobalizationSettings.GetOtherName.

**C#**

{{< highlight csharp >}}

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



Der folgende Ausschnitt lädt eine vorhandene Tabelle mit einem Kreisdiagramm und rendert das Diagramm als Bild, während die zuvor erstellte CustomSettings-Klasse genutzt wird.

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügte CellsFactory-Klasse**
Aspose.Cells 16.11.0 hat die Klasse CellsFactory freigelegt, die derzeit eine Methode, nämlich CreateStyle, enthält. Die Methode CellsFactory.CreateStyle kann verwendet werden, um eine Instanz der Klasse Style zu erstellen, ohne sie dem Pool der Arbeitsmappenstile hinzuzufügen.

Hier ist ein einfaches Anwendungsszenario der Methode CellsFactory.CreateStyle.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Hinzugefügtes Workbook.AbsolutePath-Eigenschaft**
Aspose.Cells 16.11.0 hat die Workbook.AbsolutePath-Eigenschaft freigelegt, die es ermöglicht, den absoluten Pfad des Arbeitsmappeninhalts zu erhalten oder festzulegen, der in der workbook.xml-Datei gespeichert ist. Diese Eigenschaft ist nützlich, wenn nur die externen Verknüpfungen aktualisiert werden.
### **Methode GridHyperlinkCollection.GetHyperlink hinzugefügt**
Aspose.Cells.GridWeb 16.11.0 hat die Methode GetHyperlink für die Klasse GridHyperlinkCollection freigelegt, die es ermöglicht, die Instanz von GridHyperlink zu erhalten, indem entweder eine Instanz von GridCell oder ein Paar von Ganzzahlen übergeben wird, die den Zeilen- und Spaltenindizes entsprechen.

{{% alert color="primary" %}} 

Wenn auf der angegebenen Zelle kein Hyperlink gefunden wurde, gibt die Methode GetHyperlink null zurück.

{{% /alert %}} 

Hier ist ein einfaches Anwendungsszenario der Methode GetHyperlink.

**C#**

{{< highlight csharp >}}

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
### **Veralteter Style-Konstruktor**
Bitte verwenden Sie die Methode cellsFactory.CreateStyle als Alternative.
## **Gelöschte APIs**
### **Gelöschte Cell.GetConditionalStyle-Methode**
Bitte verwenden Sie stattdessen die Methode Cell.GetConditionalFormattingResult.
### **Gelöschte Cells.MaxDataRowInColumn(int column)-Methode**
Bitte verwenden Sie die Methode Cells.GetLastDataRow(int) als Alternative.
### **Gelöschte PageSetup.Draft-Eigenschaft**
Es wird empfohlen, die PageSetup.PrintDraft-Eigenschaft stattdessen zu verwenden.
### **Gelöschte AutoFilter.FilterColumnCollection-Eigenschaft**
Bitte verwenden Sie die AutoFilter.FilterColumns-Eigenschaft, um dasselbe Ziel zu erreichen.
### **Gelöschte TickLabels.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die TickLabels.RotationAngle-Eigenschaft.
