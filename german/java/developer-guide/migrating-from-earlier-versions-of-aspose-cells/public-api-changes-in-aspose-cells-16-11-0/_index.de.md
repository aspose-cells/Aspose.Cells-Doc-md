---
title: Öffentliche API Änderungen in Aspose.Cells 16.11.0
type: docs
weight: 360
url: /de/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 16.10.0 auf 16.11.0, die für Modul-/Anwendungsentwickler von Interesse sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Globalisierungseinstellungen**
Aspose.Cells 16.11.0 hat die GlobalizationSettings-Klasse zusammen mit der WorkbookSettings.GlobalizationSettings Eigenschaft freigegeben, um die Aspose.Cells APIs zu zwingen, benutzerdefinierte Bezeichnungen für Zwischensummen zu verwenden. Die GlobalizationSettings-Klasse verfügt über die folgenden Methoden, die in der benutzerdefinierten Implementierung überschrieben werden können, um gewünschte Namen für die Bezeichnungen **Gesamt** & **Gesamtsumme** zu liefern.

- GlobalizationSettings.getTotalName: Ruft den Gesamtnamen der Funktion ab.
- GlobalizationSettings.getGrandTotalName: Ruft den Gesamtnamen der Funktion ab.

Hier ist eine einfache benutzerdefinierte Klasse, die die GlobalizationSettings-Klasse erweitert und ihre oben genannten Methoden überschreibt, um benutzerdefinierte Bezeichnungen für die Konsolidierungsfunktion Durchschnitt zurückzugeben.

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

Der folgende Ausschnitt lädt eine vorhandene Tabelle und fügt das Zwischenergebnis des Typs Durchschnitt zu den bereits auf dem Arbeitsblatt vorhandenen Daten hinzu. Die Klasse CustomSettings und ihre getTotalName & getGrandTotalName Methoden werden zum Zeitpunkt des Hinzufügens des Zwischenergebnisses zum Arbeitsblatt aufgerufen.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

Die GlobalizationSettings-Klasse bietet auch die getOtherName Methode, die nützlich ist, um den Namen von "Anderen" Bezeichnungen für Tortendiagramme zu erhalten. Hier ist ein einfaches Anwendungsbeispiel der GlobalizationSettings.getOtherName Methode.

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

Der folgende Ausschnitt lädt eine vorhandene Tabelle mit einem Kreisdiagramm und rendert das Diagramm als Bild, während die zuvor erstellte CustomSettings-Klasse genutzt wird.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **Hinzugefügte CellsFactory-Klasse**
Aspose.Cells 16.11.0 hat die CellsFactory-Klasse freigelegt, die derzeit eine Methode namens createStyle enthält. Die Methode CellsFactory.createStyle kann genutzt werden, um eine Instanz der Style-Klasse zu erstellen, ohne sie zu den Tabellenblatt-Stilen hinzuzufügen.

Hier ist ein einfaches Anwendungsbeispiel für die Methode CellsFactory.createStyle.

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Hinzugefügtes Workbook.AbsolutePath-Eigenschaft**
Aspose.Cells 16.11.0 hat die Workbook.AbsolutePath-Eigenschaft freigelegt, die es ermöglicht, den absoluten Pfad des Arbeitsmappeninhalts zu erhalten oder festzulegen, der in der workbook.xml-Datei gespeichert ist. Diese Eigenschaft ist nützlich, wenn nur die externen Verknüpfungen aktualisiert werden.
### **Hinzugefügte GridHyperlinkCollection.getHyperlink-Methode**
Aspose.Cells.GridWeb 16.11.0 hat die Methode getHyperlink für die GridHyperlinkCollection-Klasse freigelegt, die es ermöglicht, die Instanz von GridHyperlink zu erhalten, indem entweder eine Instanz von GridCell oder ein Paar ganzer Zahlen übergeben wird, die den Zeilen- und Spaltenindizes entsprechen.

{{% alert color="primary" %}} 

Falls keine Verknüpfungszelle gefunden wurde, würde die getHyperlink-Methode null zurückgeben.

{{% /alert %}} 

Hier ist ein einfaches Anwendungsbeispiel für die getHyperlink-Methode.

**Java**

{{< highlight csharp >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **Veraltete APIs**
### **Veralteter Style-Konstruktor**
Bitte verwenden Sie die cellsFactory.createStyle-Methode als Alternative.
## **Gelöschte APIs**
### **Gelöschte Cell.getConditionalStyle-Methode**
Bitte verwenden Sie die Cell.getConditionalFormattingResult-Methode stattdessen.
### **Gelöschte Cells.getMaxDataRowInColumn(int column)-Methode**
Bitte verwenden Sie die Cells.getLastDataRow(int)-Methode als Alternative.
### **Gelöschte PageSetup.Draft-Eigenschaft**
Es wird empfohlen, die PageSetup.PrintDraft-Eigenschaft stattdessen zu verwenden.
### **Gelöschte AutoFilter.FilterColumnCollection-Eigenschaft**
Bitte verwenden Sie die AutoFilter.FilterColumns-Eigenschaft, um dasselbe Ziel zu erreichen.
### **Gelöschte TickLabels.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die TickLabels.RotationAngle-Eigenschaft.
{{< app/cells/assistant language="java" >}}
