---
title: Offentliga API ändringar i Aspose.Cells 17.1.0
type: docs
weight: 380
url: /sv/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

I detta dokument beskrivs ändringarna i Aspose.Cells API från version 16.12.0 till 17.1.0 som kan vara intressanta för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tilläggade och borttagna klasser, etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Support för Excel 2016-diagram**
Aspose.Cells API har lagt till stöd för några Excel 2016-diagram genom att förbättra ChartType-uppräkningen. Följande nya fält har lagts till med utgivningen av Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: Serien är utlagd som box och whisker.
- ChartType.FUNNEL: Serien är utlagd som en tratt.
- ChartType.PARETO_LINE: Serien är utlagd som paretolinjer.
- ChartType.SUNBURST: Serien är utlagd som en solfjäder.
- ChartType.TREEMAP: Serien är utlagd som ett trädkarta.
- ChartType.WATERFALL: Serien är utlagd som ett vattenfall.
- ChartType.HISTOGRAM: Serien är utlagd som ett histogram.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Läsning av Excel 2016 Diagramtyper](/cells/sv/java/läs-och-manipulera-excel-2016-diagram/)

{{% /alert %}} 
### **Tillagd Setter for LoadFilter.LoadDataFilterOptions Property**
Aspose.Cells 17.1.0 har lagt till setter för LoadFilter.LoadDataFilterOptions-egendomen för att ersätta variabeln m_LoadDataFilterOptions. Användare kan ändra LoadDataFilterOptions-egendomen i sin egen implementation av LoadFilter-klassen för att ändra beteendet för att ladda mallfiler.

Här är ett enkelt användningsscenario.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Anpassad Mallfiltrering](/cells/sv/java/filtreringsobjekt-vid-laddning-av-kalkylblad-eller-arbetsblad/)

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
### **Tillagd CellsHelper.SignificantDigits-egendom**
Aspose.Cells 17.1.0 har exponerat SignificantDigits-egendomen från CellsHelper-klassen vilket gör att man kan hämta eller ställa in antalet signifikanta siffror för numeriska värden i ett kalkylark. Standardvärdet för CellsHelper.SignificantDigits-egendomen är 17, och den är tillämplig endast om resultatet ska lagras i XLSX-filformatet.

Här är ett enkelt scenario för att demonstrera användningen av CellsHelper.SignificantDigits-egendomen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Angivande av Antal Signifikanta Siffror](/cells/sv/java/ange-antal-signifikanta-siffror-att-lagra-i-excel-fil/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Tillagd GlowEffect.Color-egendom**
Aspose.Cells 17.1.0 har lagt till GlowEffect.Color-egendomen som kan användas för att hämta färgen på glödeffekten.

Följande utdrag använder GlowEffect.Color-egendomen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Läsning av färg för formens glöd](/cells/sv/java/read-color-of-the-shape-s-glow-effect/)
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
### **Tillagd PageSetup.PaperWidth & PaperHeight-egendom**
Aspose.Cells 17.1.0 har exponerat PaperWidth & PaperHeight-egendomen för PageSetup-klassen. PageSetup.PaperWidth & PageSetup.PaperHeight-egendomen är av typen double och representerar pappersbredden och höjden i tum med hänsyn till sidorienteringen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Hämta arbetsbladets pappersstorlek](/cells/sv/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Tillagt WorkbookSettings.CheckCustomNumberFormat Egendom**
Aspose.Cells 17.1.0 har lagt till egenskapen CheckCustomNumberFormat till klassen WorkbookSettings. CheckCustomNumberFormat är användbar för att kontrollera om egendomen Style.Custom har ställts in korrekt eller inte. Om egenskapen Style.Custom har ställts in felaktigt, det vill säga om värdet inte överensstämmer med ett giltigt mönster, kommer Aspose.Cells API:erna att kasta CellsException med lämpligt meddelande.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Verifiering av anpassat format](/cells/sv/java/check-custom-number-format-when-setting-style-custom-property/)

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
### **Lagt till DisplayUnitType.PERCENTAGE-fältet**
Aspose.Cells 17.1.0 har också exponerat PERCENTAGE-fältet för DisplayUnitType-uppräkningen. DisplayUnitType.PERCENTAGE-fältet indikerar att värdena på diagrammet ska delas med 0,01.
## **Borttagen API:er**
### **Instans Variabel m_LoadDataFilterOptions Borttagen**
Denna version har tagit bort instansvariabeln m_LoadDataFilterOptions. Det rekommenderas att istället använda egenskapen LoadFilter.LoadDataFilterOptions.
{{< app/cells/assistant language="java" >}}
