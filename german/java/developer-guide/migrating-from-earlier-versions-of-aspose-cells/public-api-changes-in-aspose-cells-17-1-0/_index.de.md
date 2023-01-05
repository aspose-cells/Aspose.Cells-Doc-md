---
title: Öffentlich API Änderungen in Aspose.Cells 17.1.0
type: docs
weight: 380
url: /de/java/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.12.0 zu 17.1.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Excel 2016-Diagramme**
Aspose.Cells APIs haben die Unterstützung für einige Excel 2016-Diagramme hinzugefügt, indem sie die ChartType-Enumeration erweitert haben. Die folgenden neuen Felder wurden mit der Veröffentlichung von Aspose.Cells 17.1.0 hinzugefügt.

- ChartType.BOX_WHISKER: Die Reihe wird als Box und Whisker angelegt.
- ChartType.FUNNEL: Die Reihe ist als Trichter angelegt.
- ChartType.PARETO_LINE: Die Reihe wird als Pareto-Linien angelegt.
- ChartType.SUNBURST: Die Serie ist als Sunburst angelegt.
- ChartType.TREEMAP: Die Serie wird als Treemap angelegt.
- ChartType.WATERFALL: Die Reihe wird als Wasserfall angelegt.
- ChartType.HISTOGRAM: Die Reihe wird als Histogramm dargestellt.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Diagrammtypen in Excel 2016 lesen](/cells/de/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter für LoadFilter.LoadDataFilterOptions-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat Setter für die Eigenschaft LoadFilter.LoadDataFilterOptions hinzugefügt, um die Instanzvariable m_LoadDataFilterOptions zu ersetzen. Benutzer können die LoadDataFilterOptions-Eigenschaft in ihrer eigenen Implementierung der LoadFilter-Klasse ändern, um das Verhalten beim Laden von Vorlagendateien zu ändern.

Hier ist ein einfaches Nutzungsszenario.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Benutzerdefinierte Vorlagenfilterung](/cells/de/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **CellsHelper.SignificantDigits-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat die SignificantDigits-Eigenschaft der CellsHelper-Klasse verfügbar gemacht, die es ermöglicht, die Anzahl signifikanter Stellen für numerische Werte in einer Tabelle abzurufen oder festzulegen. Der Standardwert der Eigenschaft CellsHelper.SignificantDigits ist 17, wobei er nur anwendbar ist, wenn das Ergebnis im Dateiformat XLSX gespeichert werden muss.

Hier ist ein einfaches Szenario, um die Verwendung der Eigenschaft CellsHelper.SignificantDigits zu demonstrieren.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Einstellen der Anzahl signifikanter Stellen](/cells/de/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **GlowEffect.Color-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat die Eigenschaft GlowEffect.Color hinzugefügt, die verwendet werden kann, um die Farbe des Glüheffekts abzurufen.

Das folgende Snippet verwendet die GlowEffect.Color-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Lesen der Leuchtfarbe der Form](/cells/de/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **PageSetup.PaperWidth- und PaperHeight-Eigenschaften hinzugefügt**
Aspose.Cells 17.1.0 hat die PaperWidth- und PaperHeight-Eigenschaften für die PageSetup-Klasse verfügbar gemacht. Die Eigenschaften PageSetup.PaperWidth und PageSetup.PaperHeight sind vom Typ Double und repräsentieren die Papierbreite und -höhe in der Einheit Zoll, wobei die Seitenausrichtung berücksichtigt wird.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Abrufen der Papiergröße des Arbeitsblatts](/cells/de/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat die CheckCustomNumberFormat-Eigenschaft zur WorkbookSettings-Klasse hinzugefügt. Das CheckCustomNumberFormat ist nützlich, um zu überprüfen, ob die Style.Custom-Eigenschaft richtig festgelegt wurde oder nicht. Falls die Style.Custom-Eigenschaft falsch eingestellt wurde, das heißt; Der Wert entspricht keinem gültigen Muster, dann lösen die Aspose.Cells-APIs CellsException mit der entsprechenden Meldung aus.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Überprüfen des benutzerdefinierten Formulars](/cells/de/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **DisplayUnitType.PERCENTAGE-Feld hinzugefügt**
Aspose.Cells 17.1.0 hat auch das PERCENTAGE-Feld für die DisplayUnitType-Enumeration verfügbar gemacht. Das Feld DisplayUnitType.PERCENTAGE gibt an, dass die Werte im Diagramm durch 0,01 geteilt werden sollen.
## **Entfernte APIs**
### **Instanzvariable m_LoadDataFilterOptions entfernt**
In dieser Version wurde die Instanzvariable m_LoadDataFilterOptions entfernt. Es wird empfohlen, stattdessen die Eigenschaft LoadFilter.LoadDataFilterOptions zu verwenden.
