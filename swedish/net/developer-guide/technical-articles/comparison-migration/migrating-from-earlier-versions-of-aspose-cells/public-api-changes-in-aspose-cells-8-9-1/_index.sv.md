---
title: Offentlig API Ändringar i Aspose.Cells 8.9.1
type: docs
weight: 310
url: /sv/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.9.0 till 8.9.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Konfigurerbara teckensnittskällor**
Aspose.Cells for .NET har exponerat ett antal klasser för att ge stöd för konfigurerbara teckensnittskällor för rendering av kalkylblad. Här är listan över klasser som har lagts till med Aspose.Cells for .NET 8.9.1.

1. FontConfigs-klassen anger teckensnittsinställningarna.
1. FontSourceBase-klassen är en abstrakt basklass för klasserna som låter användaren specificera olika teckensnittskällor.
1. FileFontSource-klassen representerar den enda TrueType-teckensnittsfilen som är lagrad i filsystemet.
1. FolderFontSource-klassen representerar mappen som innehåller TrueType-teckensnittsfiler.
1. MemoryFontSource-klassen representerar den enda TrueType-teckensnittsfilen som är lagrad i minnet.
1. FontSourceType-uppräkning anger typen av en teckensnittskälla.

Med ovan nämnda ändringar på plats, tillåter Aspose.Cells for .NET att ställa in typsnitten enligt nedan.

1. Ställ in en anpassad typsnittsmapp när du använder metoden FontConfigs.SetFontFolder.
1. Ställ in flera anpassade teckensnittsmappar medan du använder metoden FontConfigs.SetFontFolders.
1. Ställ in teckensnittskällor från en anpassad teckensnittsmapp, en enskild teckensnittsfil eller teckensnittsdata från en mängd byte medan du använder metoden FontConfigs.SetFontSources.

Här är ett enkelt användningsscenario för ovannämnda metoder.

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Både FontConfigs.SetFontFolder och FontConfigs.SetFontFolders metoder accepterar en andra parameter av boolesk typ. Genom att skicka true som andra parameter kommer Aspose.Cells API:erna att söka i undermapparna efter teckensnittsfilerna.

{{% /alert %}} 

Aspose.Cells for .NET gör det också möjligt att konfigurera teckensnittsersättningen. Denna mekanism är användbar när ett önskat teckensnitt inte är tillgängligt på maskinen där konvertering måste ske. Användare kan tillhandahålla en lista med teckensnittsnamn som alternativ till det ursprungliga teckensnittet. För att uppnå detta har API:erna Aspose.Cells exponerat metoden FontConfigs.SetFontSubstitutes som accepterar 2 parametrar. Den första parametern är av typen string, som ska vara namnet på teckensnittet som måste ersättas. Den andra parametern är en array av typen sträng. Användare kan tillhandahålla en lista med teckensnittsnamn som ersättning för det ursprungliga teckensnittsnamnet (anges i den första parametern).

Här är ett enkelt användningsscenario för metoden FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET har också tillhandahållit medel för att samla information om vilka källor och ersättningar som har ställts in.

1. Metoden FontConfigs.GetFontSources returnerar en array av typen FontSourceBase som innehåller listan över angivna teckensnittskällor. Om inga källor har ställts in kommer metoden FontConfigs.GetFontSources att returnera en tom array.
1. Metoden FontConfigs.GetFontSubstitutes accepterar en parameter av typen sträng som gör det möjligt att ange teckensnittsnamnet för vilket en ersättning har ställts in. Om ingen ersättning har ställts in för det angivna teckensnittsnamnet kommer FontConfigs.GetFontSubstitutes-metoden att returnera null.

{{% alert color="primary" %}} 

 För mer information om FontConfigs, läs artikeln om[Konfigurera teckensnitt för rendering av kalkylblad](/cells/sv/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Lade till IFilePathProvider Interface & HtmlSaveOptions.FilePathProvider egendom**
Aspose.Cells for .NET 8.9.1 gör det möjligt att hämta/ställa in IFilePathProvider för att exportera kalkylblad till separata HTML-filer. Dessa nya API:er är användbara i scenarier där hyperlänkar i ett kalkylblad pekar till en plats i ett annat kalkylblad, där applikationskravet är att rendera varje kalkylblad till en separat HTML-fil. Genom att implementera IFilePathProvider kan de ovannämnda hyperlänkarna hållas intakta oavsett att de pekar på en plats i en separat resulterande HTML-fil.

Följande är det enkla användningsscenariot för egenskapen HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight "csharp" >}}

 // Ladda ett kalkylblad i en instans av Workbook

var book = new Workbook(dir + "sample.xlsx");

// Spara varje kalkylblad till separat HTML-fil

 för (int i = 0; i< book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



Så här implementerar du gränssnittet IFlePathProvider.

**C#**

{{< highlight "csharp" >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

 För mer information om denna förbättring, läs artikeln om[Implementering av IFilePathProvider Interface](/cells/sv/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Lade till CopyOptions.ReferToDestinationSheet Property & Overload för Cells.CopyRows Method**
Aspose.Cells for .NET API har avslöjat den booleska typen CopyOptions.ReferToDestinationSheet-egenskapen tillsammans med en överbelastning på Cells.CopyRows-metoden för att underlätta kopieringsoperationen av rader när rader innehåller datakälla ett diagram och dess datakälla. Utvecklare kan använda dessa nya API:er för att peka diagrammets datakälla till käll- eller målarbetsbladen.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Kontrollera diagrammets datakälla medan du kopierar rader](/cells/sv/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Lade till CalculationOptions.Rekursiv egenskap**
Aspose.Cells for .NET 8.9.1 har exponerat den booleska typen CalculationOptions.Rekursiv egenskap. Att ställa in egenskapen CalculationOptions.Recursive till true och skicka objektet till Workbook.CalculateFormula-metoden styr API:erna Aspose.Cells att beräkna de beroende cellerna rekursivt vid beräkning av celler som beror på andra celler.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Optimera beräkningstid](/cells/sv/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Föråldrade API:er**
### **Föråldrad CellsHelper.FontDir-egenskap**
Det rekommenderas att använda metoden FontConfigs.SetFontFolder(string, bool) med mapp rekursiv till false istället.
### **Föråldrad CellsHelper.FontDirs-egenskap**
Använd metoden FontConfigs.SetFontFolders(string[], bool) med mapp rekursiv till false istället.
### **Föråldrad CellsHelper.FontFiles-egenskap**
Använd metoden FontConfigs.SetFontSources(FontSourceBase[]) istället.
