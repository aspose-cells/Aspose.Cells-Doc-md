---
title: Offentliga API ändringar i Aspose.Cells 8.9.1
type: docs
weight: 310
url: /sv/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.9.0 till 8.9.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Konfigurerbara typsnittskällor**
Aspose.Cells for .NET har exponerat ett antal klasser för att ge stöd för konfigurerbara fontkällor för att rendera kalkylblad. Här är listan över klasser som har lagts till med Aspose.Cells for .NET 8.9.1.

1. FontConfigs-klassen specificerar typsnittsinställningarna.
1. FontSourceBase-klassen är en abstrakt basklass för klasser som tillåter användaren att specificera olika typsnittskällor.
1. FileFontSource-klassen representerar den enskilda TrueType-typsnittsfilen som lagras i filsystemet.
1. FolderFontSource-klassen representerar mappen som innehåller TrueType-typsnittsfilerna.
1. MemoryFontSource-klassen representerar den enskilda TrueType-typsnittsfilen som är lagrad i minnet.
1. FontSourceType-uppräkningen specificerar typen av typsnittskälla.

Med ovan nämnda ändringar på plats, tillåter Aspose.Cells for .NET att ställa in fonterna enligt nedan beskrivet.

1. Ange en anpassad fontmapp medan du använder FontConfigs.SetFontFolder-metoden.
1. Ange flera anpassade fontmappar medan du använder FontConfigs.SetFontFolders-metoden.
1. Ange fontkällor från en anpassad fontmapp, en enskild fontfil eller fontdata från en matris av byte medan du använder FontConfigs.SetFontSources-metoden.

Här finns ett enkelt användningsscenario för ovanstående metoder.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Både FontConfigs.SetFontFolder & FontConfigs.SetFontFolders-metoder accepterar en andra parameter av typen Boolean. Genom att skicka true som andra parameter kommer Aspose.Cells API att söka i undermapparna efter fontfiler.

{{% /alert %}} 

Aspose.Cells for .NET tillåter även att konfigurera fontsubstitution. Denna mekanism är användbar när en nödvändig font inte är tillgänglig på den maskin där konvertering ska ske. Användare kan ange en lista med fontnamn som alternativ till den ursprungligen nödvändiga fonten. För att uppnå detta har Aspose.Cells API exponerat FontConfigs.SetFontSubstitutes-metoden som accepterar 2 parametrar. Den första parametern är av typen sträng, som ska vara namnet på den font som behöver ersättas. Den andra parametern är en matris av typen sträng. Användare kan ange en lista med fontnamn som substitut till det ursprungliga fontnamnet (anger i den första parametern).

Här är ett enkelt användningsscenario av metoden FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET har också tillhandahållit medel för att samla information om vilka källor och substitutioner som har ställts in.

1. Metoden FontConfigs.GetFontSources returnerar en array av typen FontSourceBase som innehåller listan över specifierade typsnittskällor. Om inga källor har angetts kommer metoden FontConfigs.GetFontSources att returnera en tom array.
1. Metoden FontConfigs.GetFontSubstitutes accepterar en parameter av typen string som låter dig ange typsnittets namn för vilket en ersättning har angetts. Om ingen ersättning har angetts för det angivna typsnittsnamnet kommer metoden FontConfigs.GetFontSubstitutes att returnera null.

{{% alert color="primary" %}} 

För mer information om FontConfigs, vänligen granska artikeln om [Konfigurering av typsnitt för rendering av kalkylblad](/cells/sv/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Lägg till IFilePathProvider-gränssnittet och HtmlSaveOptions.FilePathProvider-egenskapen**
Aspose.Cells for .NET 8.9.1 gör att du kan hämta/ställa in IFilePathProvider för att exportera kalkylblad till separata HTML-filer. Dessa nya API:er är användbara i scenarier där hyperlänkar i ett kalkylblad pekar på en plats i ett annat kalkylblad, där programkravet är att rendera varje kalkylblad till en separat HTML-fil. Genom att implementera IFilePathProvider kan du behålla de tidigare nämnda hyperlänkarna intakta oavsett om de pekar på en plats i en separat resulterande HTML-fil.

Följande är det enkla användningsscenario av HtmlSaveOptions.FilePathProvider-egenskapen.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

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



Så här implementerar du gränssnittet IFilePathProvider.

**C#**

{{< highlight csharp >}}

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

För mer information om den här förbättringen, vänligen granska artikeln om [Implementering av gränssnittet IFilePathProvider](/cells/sv/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Lade till CopyOptions.ReferToDestinationSheet Egenskap & Overload för Cells.CopyRows Metod**
Aspose.Cells for .NET API har exponerat den booleska typen CopyOptions.ReferToDestinationSheet egenskap tillsammans med en överbelastning av Cells.CopyRows metoden för att underlätta kopiering av rader när raderna som ska kopieras också innehåller en tabell och dess datakälla. Utvecklare kan använda dessa nya API:er för att peka grafens datakälla till käll- eller destinationskalkylbladen.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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

För mer information om den här funktionen, vänligen granska artikeln om [Kontrollera Datakällan för Diagram vid Kopiering av Rader](/cells/sv/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Tillagd CalculationOptions.Recursive Egendom**
Aspose.Cells for .NET 8.9.1 har exponerat den booleska typen CalculationOptions.Recursive egenskap. Att ställa in CalculationOptions.Recursive-egenskapen till true och skicka objektet till Workbook.CalculateFormula-metoden riktar Aspose.Cells API:er att beräkna de beroende cellerna rekursivt när de beräknar celler som är beroende av andra celler.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska artikeln om [Optimera Beräkningstiden](/cells/sv/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Obsoletterade API:er**
### **Föråldrad CellsHelper.FontDir Egendom**
Det rekommenderas att använda metoden FontConfigs.SetFontFolder(string, bool) med rekursiv inställd på false istället.
### **Föråldrad CellsHelper.FontDirs Egendom**
Använd FontConfigs.SetFontFolders(string[], bool) metoden med rekursiv inställd på false istället.
### **Föråldrad CellsHelper.FontFiles Egendom**
Använd FontConfigs.SetFontSources(FontSourceBase[]) metoden istället.
{{< app/cells/assistant language="csharp" >}}
