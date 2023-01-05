---
title: Aspose.Cells for Java 17.02.0 Release Notes
type: docs
weight: 110
url: /sv/java/aspose-cells-for-java-17-02-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 17.02.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.02.0/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42009|Stöd MS Excel 2016 TreeMap-diagram|Ny funktion|
|CELLSJAVA-42008|Stöd MS Excel 2016 Waterfall Chart|Ny funktion|
|CELLSJAVA-41521|Stöd för att konvertera text till kolumner MS Excel-funktionen|Ny funktion|
|CELLSJAVA-42165|Dataförlust när intervall med dolda rader och kolumner kopieras till ny arbetsbok och konverteras till HTML|Insekt|
|CELLSJAVA-42164|Dataförlust när intervall med dolda rader och kolumner kopieras till ny arbetsbok och konverteras till HTML - II|Insekt|
|CELLSJAVA-42162|Dataförlust när intervall med dolda rader och kolumner kopieras till ny arbetsbok och konverteras till HTML - III|Insekt|
|CELLSJAVA-40251|Spara som PDF bevarar inte formateringen|Insekt|
|CELLSJAVA-42187|Excel-formeln fungerar inte och visas som "#DIV/0!"|Insekt|
|CELLSJAVA-42184|Problem med att spara samtidigt|Insekt|
|CELLSJAVA-42156|De övre och nedre gränserna för celler försvinner vid konvertering till HTML|Insekt|
|CELLSJAVA-42147|Excel-formeln fungerar inte korrekt|Insekt|
|CELLSJAVA-42131|Omräkning av ett antal formler med Aspose Cells API:er resulterar i "#NUM!" fel|Insekt|
|CELLSJAVA-42188|Demosidan för matematik läses inte in korrekt i GridWeb (Java) demoprojekt|Insekt|
|CELLSJAVA-41565|Listdatavalidering rullgardinsmenyn stängs inte när data laddas om|Insekt|
|CELLSJAVA-42159|PageSetup.BlackAndWhite verkar inte fungera|Insekt|
|CELLSNET-45106|Bugg in try catch and re-throw undantag där ExceptionType ändras|Insekt|
|CELLSJAVA-42189|Vattenfallsdiagram, när calculate() anropas, återställs färgerna i diagramserien.|Insekt|
|CELLSJAVA-42160|Logaritmisk skala bugg i Excel gör att Aspose Cells hänger sig|Insekt|
|CELLSJAVA-42158|Vertikal axel bundna värden ändrades under rendering av kalkylark till PDF|Insekt|
|CELLSJAVA-42157|Horisontella och vertikala axelbundna värden ändrades under rendering av diagram till EMF|Insekt|
|CELLSJAVA-42133|Hebreiska - Mellanslagstecken saknas i PDF|Insekt|
|CELLSJAVA-42107|Diagram undertrycks vertikalt under rendering till bild|Insekt|
|CELLSJAVA-42105|DataTable-serier saknas vid export av diagram till bild|Insekt|
|CELLSJAVA-42090|Saknar understrykning i rubriken när diagram konverteras till bild|Insekt|
|CELLSJAVA-42086|Bakgrundsbilden i diagrammet är fel|Insekt|
|CELLSJAVA-42084|Mellanslag s/v-diagrammets axel (hebreiska) etiketter/legend saknas i utdatafilen PDF|Insekt|
|CELLSJAVA-41831|Innehållet i rektangelformen återges inte vid konvertering av kalkylark till HTML|Insekt|
|CELLSJAVA-42095|Diagrammet har ändrats när kalkylbladet konverterades till HTML|Insekt|
|CELLSJAVA-42096|Formeln i diagrammet har ändrat position när kalkylbladet konverterades till HTML|Insekt|
|CELLSJAVA-42169|Excel till PDF konvertering - arabisk text är omvänd|Insekt|
|CELLSJAVA-42193|Arknamnet får versaler när formeln infogas|Insekt|
|CELLSJAVA-42191|Anrop för att uppdateraSelectedValue ändringar activeSheetIndex|Insekt|
|CELLSJAVA-42181|Skyddad vy efter att ha sparat en XLS-fil igen|Insekt|
|CELLSJAVA-42180|Att kopiera en arbetsbok ändrar standardhöjden|Insekt|
|CELLSJAVA-42177|Formel i anpassad validering saknas när arbetsboken sparas i formatet XLS|Insekt|
|CELLSJAVA-42173|Excel måste återställa filen efter enkel spara via Aspose.Cells|Insekt|
|CELLSJAVA-42171|Kalkylarket blir skadat efter att ha ändrat teckensnitt för formerna|Insekt|
|CELLSJAVA-42168|Det går inte att ändra teckensnittet för några få former i samlingen|Insekt|
|CELLSJAVA-42166|Lösenordsskyddad Excel-fil ger undantag vid laddning|Insekt|
|CELLSJAVA-42163|Storleken på målarbetsboken är nästan dubbelt så stor som källarbetsboken|Insekt|
|CELLSJAVA-42161|Genom att kopiera ark över arbetsböcker ändras formeln|Insekt|
|CELLSJAVA-42154|Det går inte att läsa kryssrutans textvärde|Insekt|
|CELLSJAVA-42150|Metoden GetNames() returnerar inte alla namn|Insekt|
|CELLSJAVA-40511|Sidorna i PDF genererade av Aspose.Cells är helt svarta|Insekt|
|CELLSJAVA-42179|NullPointerException på Workbook ctor när du laddar en HTML|Undantag|
|CELLSJAVA-42174|NullPointerException vid Workbook ctor när du laddar en HTML - II|Undantag|
|CELLSJAVA-42192|CellsException: Ogiltig hålstorlek: den måste vara mellan 10 och 90|Undantag|
|CELLSJAVA-42190|Undantag: "java.lang.IndexOutOfBoundsException" vid inläsning av ett XLSX filformat|Undantag|
|CELLSJAVA-42185|Undantag - ReadElementString kunde endast anropas - inträffade när arbetsboken öppnades|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Tillagd HTMLLoadOptions.AutoFitColsAndRows-egenskap**
Den här versionen av Aspose.Cells for Java API har lagt till egenskapen HTMLLoadOptions.AutoFitColsAndRows som indikerar om API automatiskt ska anpassa kolumner och rader medan HTML importeras i objektläget. Egenskapen boolesk typ har standardvärdet som false, vilket innebär att cellhöjderna och -bredderna kommer att importeras som de är, men när den tidigare nämnda egenskapen är inställd på true, försöker API justera kolumnbredderna och radhöjderna enligt innehållet .

Här är det enkla användningsscenariot för HTMLLoadOptions.AutoFitColsAndRows-egenskapen.

{{< highlight "java" >}}

 // Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

// Set the AutoFitColsAndRows property to true

loadOptions.setAutoFitColsAndRows(true);

// Create an instance of Workbook and load HTML while passing

// the object of HTMLLoadOptions class created above

Workbook book = new Workbook(dir + "sample.htm", loadOptions);

{{< /highlight >}}
### **Lade till WorkbookSettings.WarningCallback & LoadOptions.WarningCallback Properties**
Aspose.Cells for Java 17.02.0 har exponerat egenskapen WarningCallback för klasserna LoadOptions och WorkbookSettings för att få eller ställa in varningsåteruppringningen. Utvecklare måste implementera IWarningCallback-gränssnittet för att få anpassade varningar i sina applikationer.

Här är ett enkelt användningsscenario för LoadOptions.WarningCallback-egenskapen för att få varningar när ett indatakalkylblad innehåller dubbletter av namngivna intervall.

{{< highlight "java" >}}

 public class WarningCallback implements IWarningCallback

{

	public void warning(WarningInfo warningInfo)

    {

        if (warningInfo.getWarningType() == WarningType.DUPLICATE_DEFINED_NAME)

        {

            System.out.println("Duplicate Defined Names Found as " + warningInfo.getDescription());

        }

    }

}

{{< /highlight >}}

Så här använder du den anpassade klassen som definierats ovan.

{{< highlight "java" >}}

 // Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

// Set the WarningCallback property to custom class

options.setWarningCallback(new WarningCallback());

// Load a sample spreadsheet in an instance of Workbook while 

// passing the object of LoadOptions class as defined above

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **Lade till Cells.textToColumns Method**
Senaste revisionen av Aspose.Cells for Java API:er har exponerat metoden Cells.textToColumns för att efterlikna Excels**Text till kolumner**funktion. Excel tillhandahåller den här funktionen från**Dataverktyg**under**Data**flik. Observera att för att dela upp innehållet i en kolumn till flera kolumner bör data innehålla en specifik avgränsare som ett kommatecken (eller något annat tecken) baserat på vilket API försöker dela upp innehållet i en cell till flera celler.

Här är ett enkelt användningsscenario för att demonstrera användningen av nyligen exponerade API.

{{< highlight "java" >}}

 // Create an instance of Workbook and load a sample

Workbook book = new Workbook(dir + "sample.xlsx");

// Retrieve the cells collection of the first worksheet in the sample

Cells cells = book.getWorksheets().get(0).getCells();

// Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

// Specify the separator

options.setSeparator(',');

// Split the data in range B2:B4

cells.textToColumns(1, 1, 3, options);

{{< /highlight >}}
### **Lade till Workbook.getFonts-metoden**
Aspose.Cells for Java 17.02.0 har exponerat getFonts-metoden för klassen Workbook. Metoden Workbook.getFonts returnerar listan över individuella teckensnitt som används för att formatera cellinnehållet i ett visst kalkylblad. Returtypen för ovannämnda metod är en array av typFont-klassen.

Följande kodavsnitt visar hur Workbook.getFonts-metoden används.

{{< highlight "java" >}}

 // Skapa en instans av Workbook och ladda ett exempel

Workbook book = new Workbook(dir + "sample.xlsx");

// Hämta listan över teckensnitt som används i kalkylbladet

Font[]fonts = book.getFonts();

// Iterera listan och skriv teckensnittsnamnet

 för (int i = 0; i< fonts.length; i ++)

{

	Font font = fonts[i];

	System.out.println(font.getName());

}

{{< /highlight >}}
### **Lagt till egenskapen TxtSaveOptions.TrimLeadingBlankRowAndColumn**
Denna revidering av Aspose.Cells for Java har exponerat den booleska typen TrimLeadingBlankRowAndColumn för klassen TxtSaveOptions som anger om ledande tomma rader och kolumner ska trimmas som Excel gör när man exporterar data till CSV eller tabbavgränsade egenskapsformat för falsement. Om data i kalkylbladet inte startar från den första cellen, det vill säga: A1, tar Excel-applikationen bort de inledande tomma raderna och kolumnerna medan data exporteras till CSV eller tabbavgränsade format, men Aspose.Cells API:er som standard behåller de tomma raderna och kolumnerna för samma prov för att behålla dataplatsen om de exporterade CSV eller tabbavgränsade filerna måste importeras tillbaka med Aspose.Cells API:er.

Här är ett enkelt användningsscenario för egenskapen TrimLeadingBlankRowAndColumn.

{{< highlight "java" >}}

 // Create an instance of Workbook and load a sample

Workbook book = new Workbook(dir + "sample.xlsx");

// Create an instance of TxtSaveOptions

TxtSaveOptions options = new TxtSaveOptions();

// Set TrimLeadingBlankRowAndColumn property to true

options.setTrimLeadingBlankRowAndColumn(true);

// Export to CSV format while removing the leading blank rows & columns

book.save(dir + "output.csv", options);

{{< /highlight >}}
### **Lade till egenskapen BuiltInDocumentPropertyCollection.Revision och föråldrad egendom BuiltInDocumentPropertyCollection.RevisionNumber**
Använd egenskapen BuiltInDocumentPropertyCollection.Revision istället.
### **Lade till Shape.TextShapeType-egenskap**
Egenskapen Shape.TextShapeType hämtar eller ställer in den förinställda textformtypen från en lista med fördefinierade typer lagrade i AutoShapeType-uppräkning.
### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

1. [Autopassa kolumner och rader när HTML laddas i arbetsboken](/cells/sv/java/autofit-columns-and-rows-while-loading-html-in-workbook/)
1. [Konvertera text till kolumner med Aspose.Cells](/cells/sv/java/convert-text-to-columns-using-aspose-cells/)
1. [Få en lista över teckensnitt som används i ett kalkylblad eller en arbetsbok](/cells/sv/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
1. [Få varningar när du laddar Excel-fil](/cells/sv/java/get-warnings-while-loading-excel-file/)
1. [Läs och manipulera Excel 2016-diagram](/cells/sv/java/read-and-manipulate-excel-2016-charts/)
1. [Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till formatet CSV](/cells/sv/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
