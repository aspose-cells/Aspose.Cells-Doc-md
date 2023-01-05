---
title: Öffentlich API Änderungen in Aspose.Cells 16.11.0
type: docs
weight: 360
url: /de/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.10.0 zu 16.11.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Globalisierungseinstellungen**
Aspose.Cells 16.11.0 hat die GlobalizationSettings-Klasse zusammen mit der WorkbookSettings.GlobalizationSettings-Eigenschaft verfügbar gemacht, um die Aspose.Cells-APIs zur Verwendung benutzerdefinierter Bezeichnungen für Zwischensummen zu erzwingen. Die GlobalizationSettings-Klasse verfügt über die folgenden Methoden, die in der benutzerdefinierten Implementierung überschrieben werden können, um den Beschriftungen die gewünschten Namen zu geben**Gesamt** & **Gesamtsumme**.

- GlobalizationSettings.getTotalName: Ruft den Gesamtnamen der Funktion ab.
- GlobalizationSettings.getGrandTotalName: Ruft den Gesamtsummennamen der Funktion ab.

Hier ist eine einfache benutzerdefinierte Klasse, die die GlobalizationSettings-Klasse erweitert und ihre oben genannten Methoden überschreibt, um benutzerdefinierte Bezeichnungen für die Konsolidierungsfunktion Average zurückzugeben.

**Java**

{{< highlight "csharp" >}}

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

Das folgende Snippet lädt ein vorhandenes Arbeitsblatt und fügt die Zwischensumme des Typs „Durchschnitt“ zu Daten hinzu, die bereits im Arbeitsblatt verfügbar sind. Die CustomSettings-Klasse und ihre getTotalName- und getGrandTotalName-Methoden werden zum Zeitpunkt des Hinzufügens von Subtotal zum Arbeitsblatt aufgerufen.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

Die GlobalizationSettings-Klasse bietet auch die getOtherName-Methode, die nützlich ist, um den Namen von „Anderen“-Beschriftungen für Kreisdiagramme abzurufen. Hier ist ein einfaches Verwendungsszenario der Methode GlobalizationSettings.getOtherName.

**Java**

{{< highlight "csharp" >}}

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

Der folgende Codeausschnitt lädt eine vorhandene Tabelle mit einem Kreisdiagramm und rendert das Diagramm in ein Bild, während die oben erstellte CustomSettings-Klasse verwendet wird.

**Java**

{{< highlight "csharp" >}}

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
### **CellsFactory-Klasse hinzugefügt**
Aspose.Cells 16.11.0 hat die CellsFactory-Klasse verfügbar gemacht, die derzeit eine Methode hat, das heißt; createStyle. Die CellsFactory.createStyle-Methode kann verwendet werden, um eine Instanz der Style-Klasse zu erstellen, ohne sie dem Pool von Arbeitsmappenstilen hinzuzufügen.

Hier ist ein einfaches Anwendungsszenario der CellsFactory.createStyle-Methode.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Workbook.AbsolutePath-Eigenschaft hinzugefügt**
Aspose.Cells 16.11.0 hat die Workbook.AbsolutePath-Eigenschaft verfügbar gemacht, die es ermöglicht, den absoluten Arbeitsmappenpfad abzurufen oder festzulegen, der in der Datei workbook.xml gespeichert ist. Diese Eigenschaft ist nur beim Aktualisieren der externen Links nützlich.
### **GridHyperlinkCollection.getHyperlink-Methode hinzugefügt**
Aspose.Cells.GridWeb 16.11.0 hat die getHyperlink-Methode für die GridHyperlinkCollection-Klasse verfügbar gemacht, die es ermöglicht, die Instanz von GridHyperlink abzurufen, indem entweder eine Instanz GridCell oder ein Paar Ganzzahlen übergeben wird, die den Zeilen-Spalten-Indizes entsprechen.

{{% alert color="primary" %}} 

Falls in der angegebenen Zelle kein Hyperlink gefunden wurde, gibt die getHyperlink-Methode null zurück.

{{% /alert %}} 

Hier ist ein einfaches Nutzungsszenario der getHyperlink-Methode.

**Java**

{{< highlight "csharp" >}}

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
### **Veralteter Stilkonstruktor**
Bitte verwenden Sie alternativ die Methode cellsFactory.createStyle.
## **Gelöschte APIs**
### **Cell.getConditionalStyle-Methode gelöscht**
Bitte verwenden Sie stattdessen die Methode Cell.getConditionalFormattingResult.
### **Methode Cells.getMaxDataRowInColumn(int column) gelöscht**
Bitte verwenden Sie alternativ die Methode Cells.getLastDataRow(int).
### **PageSetup.Draft-Eigenschaft gelöscht**
Es wird empfohlen, stattdessen die Eigenschaft PageSetup.PrintDraft zu verwenden.
### **Gelöschte AutoFilter.FilterColumnCollection-Eigenschaft**
Bitte erwägen Sie die Verwendung der AutoFilter.FilterColumns-Eigenschaft, um dasselbe Ziel zu erreichen.
### **Gelöschte TickLabels.Rotation-Eigenschaft**
Bitte verwenden Sie stattdessen die Eigenschaft TickLabels.RotationAngle.
