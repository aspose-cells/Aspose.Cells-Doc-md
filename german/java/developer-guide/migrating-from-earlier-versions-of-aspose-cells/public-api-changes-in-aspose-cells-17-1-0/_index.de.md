---
title: Öffentliche API Änderungen in Aspose.Cells 17.1.0
type: docs
weight: 380
url: /de/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 16.12.0 auf 17.1.0, die für Modulentwickler/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Excel 2016 Diagramme**
Aspose.Cells APIs haben die Unterstützung für einige Excel 2016 Diagramme hinzugefügt, indem sie die ChartType-Enumeration verbessert haben. Mit der Veröffentlichung von Aspose.Cells 17.1.0 wurden folgende neue Felder hinzugefügt.

- ChartType.BOX_WHISKER: Die Serie ist als Box- und-Whisker-Diagramm angelegt.
- ChartType.FUNNEL: Die Serie ist als Trichterdiagramm angelegt.
- ChartType.PARETO_LINE: Die Serie ist als Pareto-Linien angelegt.
- ChartType.SUNBURST: Die Serie ist als Sonnenstrahl-Diagramm angelegt.
- ChartType.TREEMAP: Die Serie ist als TreeMap-Diagramm angelegt.
- ChartType.WATERFALL: Die Serie ist als Wasserfalldiagramm angelegt.
- ChartType.HISTOGRAM: Die Serie ist als Histogramm angelegt.

{{% alert color="primary" %}} 

Prüfen Sie den ausführlichen Artikel zu [Lesen von Excel 2016 Diagrammtypen](/cells/de/java/lesen-und-manipulieren-von-excel-2016-diagrammen/)

{{% /alert %}} 
### **Hinzugefügter Setter für LoadFilter.LoadDataFilterOptions Eigenschaft**
Aspose.Cells 17.1.0 hat einen Setter für die LoadFilter.LoadDataFilterOptions-Eigenschaft hinzugefügt, um die Instanzvariable m_LoadDataFilterOptions zu ersetzen. Benutzer können die LoadDataFilterOptions-Eigenschaft in ihrer eigenen Implementierung der LoadFilter-Klasse ändern, um das Ladeverhalten von Vorlagendateien zu ändern.

Hier ist ein einfaches Anwendungsbeispiel.

{{% alert color="primary" %}} 

Prüfen Sie den ausführlichen Artikel zu [Benutzerdefinierter Vorlagenfilterung](/cells/de/java/filter-objekte-beim-laden-einer-arbeitsmappe-oder-arbeitsblatts/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **Hinzugefügte CellsHelper.SignificantDigits Eigenschaft**
Aspose.Cells 17.1.0 hat die SignificantDigits-Eigenschaft aus der CellsHelper-Klasse freigelegt, die es erlaubt, die Anzahl der signifikanten Stellen für numerische Werte in einer Tabellenkalkulation zu erhalten oder festzulegen. Der Standardwert der CellsHelper.SignificantDigits-Eigenschaft beträgt 17 und ist nur anwendbar, wenn das Ergebnis im XLSX-Dateiformat gespeichert werden soll.

Hier ist ein einfaches Szenario zur Demonstration der Verwendung der CellsHelper.SignificantDigits-Eigenschaft.

{{% alert color="primary" %}} 

Prüfen Sie den ausführlichen Artikel zu [Festlegen der Anzahl der signifikanten Stellen](/cells/de/java/festlegen-der-anzahl-der-signifikanten-stellen-die-in-einer-excel-datei-gespeichert-werden-sollen/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Hinzugefügtes GlowEffect.Color-Eigenschaft**
Aspose.Cells 17.1.0 hat die GlowEffect.Color-Eigenschaft hinzugefügt, die zur Abrufung der Farbe des Leuchteffekts verwendet werden kann.

Der folgende Ausschnitt verwendet die GlowEffect.Color-Eigenschaft.

{{% alert color="primary" %}} 

Lesen Sie den ausführlichen Artikel über [das Lesen der Glow-Farbe der Form](/cells/de/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **Hinzugefügte PaperWidth- & PaperHeight-Eigenschaften für PageSetup**
Aspose.Cells 17.1.0 hat die PaperWidth- und PaperHeight-Eigenschaften für die PageSetup-Klasse freigegeben. Die PaperWidth- und PaperHeight-Eigenschaften von PageSetup sind vom Typ double und repräsentieren die Papierbreite und -höhe in Zoll, unter Berücksichtigung der Seitenorientierung.

{{% alert color="primary" %}} 

Lesen Sie den ausführlichen Artikel über [das Abrufen der Papiergröße des Arbeitsblatts](/cells/de/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Hinzugefügtes CheckCustomNumberFormat-Eigenschaft für WorkbookSettings**
Aspose.Cells 17.1.0 hat die CheckCustomNumberFormat-Eigenschaft für die WorkbookSettings-Klasse hinzugefügt. Die CheckCustomNumberFormat ist nützlich, um zu überprüfen, ob die Style.Custom-Eigenschaft ordnungsgemäß festgelegt wurde oder nicht. Falls die Style.Custom-Eigenschaft auf unkorrekte Weise festgelegt wurde, d.h. der Wert nicht dem gültigen Muster entspricht, werden die Aspose.Cells-APIs eine CellsException mit entsprechender Meldung auslösen.

{{% alert color="primary" %}} 

Lesen Sie den ausführlichen Artikel über [die Überprüfung des benutzerdefinierten Formats](/cells/de/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **Hinzugefügtes PERCENTAGE-Feld für DisplayUnitType**
Aspose.Cells 17.1.0 hat auch das PERCENTAGE-Feld für die DisplayUnitType-Aufzählung freigegeben. Das DisplayUnitType.PERCENTAGE-Feld gibt an, dass die Werte auf dem Diagramm durch 0,01 dividiert werden sollen.
## **Entfernte APIs**
### **Instanzvariable m_LoadDataFilterOptions wurde entfernt**
In diesem Release wurde die Instanzvariable m_LoadDataFilterOptions entfernt. Es wird empfohlen, stattdessen die LoadFilter.LoadDataFilterOptions-Eigenschaft zu verwenden.
{{< app/cells/assistant language="java" >}}
