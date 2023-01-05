---
title: Offentlig API Ändringar i Aspose.Cells 8.9.1
type: docs
weight: 320
url: /sv/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.9.0 till 8.9.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Konfigurerbara teckensnittskällor**
Aspose.Cells for Java har exponerat ett antal klasser för att ge stöd för konfigurerbara teckensnittskällor för rendering av kalkylblad. Här är listan över klasser som har lagts till med Aspose.Cells for Java 8.9.1.

1. FontConfigs-klassen anger teckensnittsinställningarna.
1. FontSourceBase-klassen är en abstrakt basklass för klasserna som låter användaren specificera olika teckensnittskällor.
1. FileFontSource-klassen representerar den enda TrueType-teckensnittsfilen som är lagrad i filsystemet.
1. FolderFontSource-klassen representerar mappen som innehåller TrueType-teckensnittsfiler.
1. MemoryFontSource-klassen representerar den enda TrueType-teckensnittsfilen som är lagrad i minnet.
1. FontSourceType-uppräkning anger typen av en teckensnittskälla.

Med ovan nämnda ändringar på plats, tillåter Aspose.Cells for Java att ställa in typsnitten enligt nedan.

1. Ställ in en anpassad typsnittsmapp när du använder metoden FontConfigs.setFontFolder.
1. Ställ in flera anpassade teckensnittsmappar när du använder metoden FontConfigs.setFontFolders.
1. Ställ in teckensnittskällor från en anpassad teckensnittsmapp, en enskild teckensnittsfil eller teckensnittsdata från en mängd byte medan du använder metoden FontConfigs.setFontSources.

Här är ett enkelt användningsscenario för ovannämnda metoder.

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 Både FontConfigs.setFontFolder och FontConfigs.setFontFolders metoder accepterar en andra parameter av boolesk typ. Genom att skicka true som andra parameter kommer Aspose.Cells API:erna att söka i undermapparna efter teckensnittsfilerna.

{{% /alert %}} 

Aspose.Cells for Java gör det också möjligt att konfigurera teckensnittsersättningen. Denna mekanism är användbar när ett önskat teckensnitt inte är tillgängligt på maskinen där konvertering måste ske. Användare kan tillhandahålla en lista med teckensnittsnamn som alternativ till det ursprungliga teckensnittet. För att uppnå detta har API:erna Aspose.Cells exponerat metoden FontConfigs.setFontSubstitutes som accepterar 2 parametrar. Den första parametern är av typen string, som ska vara namnet på teckensnittet som måste ersättas. Den andra parametern är en array av typen sträng. Användare kan tillhandahålla en lista med teckensnittsnamn som ersättning för det ursprungliga teckensnittsnamnet (anges i den första parametern).

Här är ett enkelt användningsscenario för metoden FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java har också tillhandahållit medel för att samla information om vilka källor och ersättningar som har ställts in.

1. Metoden FontConfigs.getFontSources returnerar en array av typen FontSourceBase som innehåller listan över angivna teckensnittskällor. Om inga källor har ställts in kommer metoden FontConfigs.getFontSources att returnera en tom array.
1. Metoden FontConfigs.getFontSubstitutes accepterar en parameter av typen sträng som gör det möjligt att ange teckensnittsnamnet för vilket en ersättning har ställts in. Om ingen ersättning har ställts in för det angivna teckensnittsnamnet kommer FontConfigs.getFontSubstitutes-metoden att returnera null.

{{% alert color="primary" %}} 

 För mer information om FontConfigs, läs artikeln om[Konfigurera teckensnitt för rendering av kalkylblad](/cells/sv/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Lade till IFilePathProvider Interface & HtmlSaveOptions.FilePathProvider egendom**
Aspose.Cells for Java 8.9.1 gör det möjligt att hämta/ställa in IFilePathProvider för export av kalkylblad till separata HTML-filer. Dessa nya API:er är användbara i scenarier där hyperlänkar i ett kalkylblad pekar till en plats i ett annat kalkylblad, där applikationskravet är att rendera varje kalkylblad till en separat HTML-fil. Genom att implementera IFilePathProvider kan de ovannämnda hyperlänkarna hållas intakta oavsett det faktum att de pekar på en plats i en separat resulterande HTML-fil.

Följande är det enkla användningsscenariot för egenskapen HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight "csharp" >}}

 //Ladda ett kalkylblad i en instans av Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Spara varje kalkylblad till separat HTML-fil

 för (int i = 0; i< book.getWorksheets().getCount(); i++)

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

 För mer information om denna förbättring, läs artikeln om[Implementering av IFilePathProvider Interface](/cells/sv/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Lade till CopyOptions.ReferToDestinationSheet Property & Overload för Cells.copyRows Method**
Aspose.Cells for Java API har avslöjat den booleska typen CopyOptions.ReferToDestinationSheet-egenskapen tillsammans med en överbelastning av Cells.copyRows-metoden för att underlätta kopieringsoperationen av rader när rader innehåller datakälla ett diagram och dess datakälla. Utvecklare kan använda dessa nya API:er för att peka diagrammets datakälla till käll- eller målarbetsbladen.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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

 För mer information om den här funktionen, läs artikeln om[Kontrollera diagrammets datakälla medan du kopierar rader](/cells/sv/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Lade till CalculationOptions.Rekursiv egenskap**
Aspose.Cells for Java 8.9.1 har exponerat den booleska typen CalculationOptions.Rekursiv egenskap. Genom att ställa in egenskapen CalculationOptions.Recursive till true och skicka objektet till Workbook.calculateFormula-metoden styrs API:erna Aspose.Cells att beräkna de beroende cellerna rekursivt vid beräkning av celler som beror på andra celler.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Optimera beräkningstid](/cells/sv/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Föråldrade API:er**
### **Föråldrad CellsHelper.FontDir-egenskap**
Det rekommenderas att använda metoden FontConfigs.setFontFolder(String, boolean) med mapp rekursiv till false istället.
### **Föråldrad CellsHelper.FontDirs-egenskap**
Använd metoden FontConfigs.setFontFolders(String[], boolean) med mapp rekursiv till false istället.
### **Föråldrad CellsHelper.FontFiles-egenskap**
Använd metoden FontConfigs.setFontSources(FontSourceBase[]) istället.
