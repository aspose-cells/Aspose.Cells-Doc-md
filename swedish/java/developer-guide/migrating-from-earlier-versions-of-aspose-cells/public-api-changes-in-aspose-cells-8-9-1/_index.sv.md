---
title: Offentliga API ändringar i Aspose.Cells 8.9.1
type: docs
weight: 320
url: /sv/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.9.0 till 8.9.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Konfigurerbara typsnittskällor**
Aspose.Cells for Java har exponerat ett antal klasser för att ge stöd för konfigurerbara typsnittskällor för att rendera kalkylblad. Här är listan över klasser som har lagts till med Aspose.Cells for Java 8.9.1.

1. FontConfigs-klassen specificerar typsnittsinställningarna.
1. FontSourceBase-klassen är en abstrakt basklass för klasser som tillåter användaren att specificera olika typsnittskällor.
1. FileFontSource-klassen representerar den enskilda TrueType-typsnittsfilen som lagras i filsystemet.
1. FolderFontSource-klassen representerar mappen som innehåller TrueType-typsnittsfilerna.
1. MemoryFontSource-klassen representerar den enskilda TrueType-typsnittsfilen som är lagrad i minnet.
1. FontSourceType-uppräkningen specificerar typen av typsnittskälla.

Med ovanstående nämnda ändringar på plats, tillåter Aspose.Cells for Java att ställa in typsnitten enligt följande.

1. Ange en anpassad typsnittsmapp medan du använder metoden FontConfigs.setFontFolder.
1. Ange flera anpassade typsnittsmappar medan du använder metoden FontConfigs.setFontFolders.
1. Ange typsnittskällor från en anpassad typsnittsmapp, en enskild typsnittsfil eller typsnittsdata från en byte-array medan du använder metoden FontConfigs.setFontSources.

Här finns ett enkelt användningsscenario för ovanstående metoder.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Både FontConfigs.setFontFolder & FontConfigs.setFontFolders-metoderna accepterar en Boolesk typ andra parameter. Genom att passera true som andra parameter kommer Aspose.Cells API:erna att söka igenom undermapparna efter typsnittsfilerna. 

{{% /alert %}} 

Aspose.Cells for Java tillåter också att konfigurera typsnittpåläggningen. Denna mekanism är användbar när ett krävt typsnitt inte är tillgängligt på maskinen där konverteringen ska äga rum. Användare kan ange en lista med typsnamn som alternativ till det ursprungligen krävda typsnittet. För att uppnå detta har Aspose.Cells API:erna exponerat metoden FontConfigs.setFontSubstitutes som accepterar 2 parametrar. Den första parametern är av typen sträng, vilken bör vara namnet på det typsnitt som behöver ersättas. Den andra parametern är en array av typen sträng. Användare kan ange en lista med typsnittsnamn som ersättning för det ursprungliga typsnittsnamnet (angeras i den första parametern).

Här är ett enkelt användningsscenario av metoden FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java har också tillhandahållit medel för att samla information om vilka källor och ersättningar som har ställts in.

1. FontConfigs.getFontSources-metoden returnerar en array av typen FontSourceBase som innehåller listan över specificerade typsnittskällor. Om inga källor har ställts in kommer FontConfigs.getFontSources-metoden att returnera en tom array.
1. FontConfigs.getFontSubstitutes-metoden accepterar en parameter av typen sträng som möjliggör att ange typsnittsnamnet för vilket en ersättning har ställts in. Om ingen ersättning har ställts in för det angivna typsnittsnamnet kommer FonConfigs.getFontSubstitutes-metoden att returnera null.

{{% alert color="primary" %}} 

För mer information om FontConfigs, vänligen granska artikeln om [Konfigurera typsnitt för att rendera kalkylblad](/cells/sv/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Lägg till IFilePathProvider-gränssnittet och HtmlSaveOptions.FilePathProvider-egenskapen**
Aspose.Cells for Java 8.9.1 tillåter att få/sätta IFilePathProvider för att exportera kalkylblad till separata HTML-filer. Dessa nya API:er är användbara i scenarier där hyperlänkar i ett kalkylblad pekar på en plats i ett annat kalkylblad, där applikationskravet är att rendera varje kalkylblad till en separat HTML-fil. Genom att implementera IFilePathProvider kan ovannämnda hyperlänkar behållas intakta oavsett om de pekar på en plats i en separat resulterande HTML-fil.

Följande är det enkla användningsscenario av HtmlSaveOptions.FilePathProvider-egenskapen.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

För mer information om denna förbättring, vänligen granska artikeln om [Implementera IFilePathProvider-gränssnittet](/cells/sv/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Lade till CopyOptions.ReferToDestinationSheet-egenskapen och överlagring för Cells.copyRows-metoden.**
Aspose.Cells for Java API har exponerat den Booleska typen CopyOptions.ReferToDestinationSheet-egenskapen tillsammans med en överlagring av Cells.copyRows-metoden för att underlätta kopieringsoperationen när rader som ska kopieras även innehåller en diagram och dess datakälla. Utvecklare kan använda dessa nya API:er för att peka diagrammets datakälla till käll- eller destinationskalkylbladen.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska artikeln om [Kontrollera datakällan för diagram när du kopierar rader](/cells/sv/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Tillagd CalculationOptions.Recursive Egendom**
Aspose.Cells for Java 8.9.1 har exponerat den booleska typen CalculationOptions.Recursive egendom. Att sätta CalculationOptions.Recursive egendomen till true och skicka objektet till Workbook.calculateFormula-metoden riktar Aspose.Cells API: erna att beräkna de beroende cellerna rekursivt när beräkning av celler som beror på andra celler.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska artikeln om [Optimera beräkningstiden](/cells/sv/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Obsoletterade API:er**
### **Föråldrad CellsHelper.FontDir Egendom**
Det rekommenderas att använda FontConfigs.setFontFolder(String, boolean) metoden med rekursiv mapp istället.
### **Föråldrad CellsHelper.FontDirs Egendom**
Använd FontConfigs.setFontFolders(String[], boolean) metoden med rekursiv mapp istället.
### **Föråldrad CellsHelper.FontFiles Egendom**
Använd FontConfigs.setFontSources(FontSourceBase[]) metoden istället.
