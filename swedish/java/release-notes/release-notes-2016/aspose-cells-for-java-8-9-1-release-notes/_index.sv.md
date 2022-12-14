---
title: Aspose.Cells för Java 8.9.1 Release Notes
type: docs
weight: 60
url: /sv/java/aspose-cells-for-java-8-9-1-release-notes/
---
## **1) Aspose.Cells**

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41925|Beräkningstiden har ökat med de senaste API-revisionerna|Ny funktion|
|CELLSJAVA-40958|Användarkonfigurerbar teckensnittsersättningsmekanism krävs|Ny funktion|
|CELLSJAVA-41936|Workbook.calculateFormula()-metoden avslutas aldrig för Excel-källfilen|Förbättring|
|CELLSJAVA-41928|Det gick inte att fånga bildresursen när kalkylbladet renderades till HTML med IStreamProvider|Insekt|
|CELLSJAVA-41841|Problem med att rendera kryssrutor till HTML|Insekt|
|CELLSJAVA-41932|Problem med getDisplayStringValue() för datumformaterade värden|Insekt|
|CELLSJAVA-41930|Genom att använda Light Cells API:er för att bearbeta en XLS-fil, bearbetas alltid den första cellen i det första arket|Insekt|
|CELLSJAVA-41931|Teckenavstånd och brytning är inte korrekta för vertikal text vid rendering av kalkylark till PDF|Insekt|
|CELLSJAVA-41709|Kolumnbredden är annorlunda på CentOS än på Windows|Insekt|
|CELLSJAVA-41933|Diagramskalan har ändrats vid rendering av kalkylark till PDF|Insekt|
|CELLSJAVA-41934|Justeringsproblem vid rendering av en Excel-fil till PDF|Insekt|
|CELLSJAVA-41935|Formatering av förklaringsposter störs när kalkylbladet renderas till PDF|Insekt|
|CELLSJAVA-41943|Horisontella axeletiketter har inte renderats helt, det vill säga; alla etiketter saknar visst innehåll i den renderade bilden.|Insekt|
|CELLSJAVA-41940|Filen är skadad efter formelberäkning och spara|Insekt|
|CELLSJAVA-41927|Undantag: "java.lang.OutOfMemoryError" när du sparar i HTML-filformat|Undantag|
|CELLSJAVA-41945|CellsException: Fel vid beräkning av Cell[0Sheet1!E5]at Workbook.CalculateFormula vid beräkning av TREND-funktionen|Undantag|
|CELLSJAVA-41946|Att öppna Excel-fil orsakar java.lang.NumberFormatException: För inmatningssträng: "80000020"|Undantag|
|CELLSJAVA-41922|IndexOutOfBoundsException vid kopiering av celler|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen CopyOptions.ReferToDestinationSheet och metoden Cells.CopyRows(Cells sourceCells, int sourceRowIndex, int destinationRowIndex, int rowNumber, CopyOptions copyOptions)**
Anger om det ska refereras till målarbetsbladet (som en datakälla för diagrammet) när rader/intervall kopieras.
När du kopierar intervallet och diagrammet hänvisar till källarket betyder False att det kopierade diagrammets datakälla inte kommer att ändras. Sant betyder att det kopierade diagrammets datakälla refererar till målarket.
### **Lägger till egenskapen HtmlSaveOptions.FilePathProvider**
Hämtar eller ställer in IFilePathProvider för export av arbetsblad till html separat.
### **Lägger till IFilePathProvider-gränssnitt**
Representerar den exporterade filsökvägen.
### **Lägger till FontConfigs-klassen**
Anger teckensnittsinställningar.
### **Lägger till FontSourceBase-klassen**
Detta är en abstrakt basklass för klasserna som låter användaren specificera olika teckensnittskällor.
### **Lägger till klassen FileFontSource**
Representerar den enda TrueType-teckensnittsfilen som är lagrad i filsystemet.
### **Lägger till klassen FolderFontSource**
Representerar mappen som innehåller TrueType-teckensnittsfiler.
### **Lägger till klassen MemoryFontSource**
Representerar den enda TrueType-teckensnittsfilen som är lagrad i minnet.
### **Lägger till FontSourceType enum**
Anger typen av en teckensnittskälla.
### **Lägger till CalculationOptions.Rekursiv egenskap**
Anger om de beroende cellerna ska beräknas rekursivt vid beräkning av en cell och det beror på andra celler.
### **Föråldrade CellsHelper.FontDir-egenskapen**
Använd metoden FontConfigs.SetFontFolder(sträng, bool) med mapp rekursiv till false istället.
### **Föråldrad CellsHelper.FontDirs egendom**
Använd metoden FontConfigs.SetFontFolders(string[], bool) med mapp rekursiv till false istället.
### **Obsoletes CellsHelper.FontFiles-egenskapen**
Använd FontConfigs.SetFontSources(FontSourceBase[]) istället.

{{% alert color="primary" %}} 

Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.9.1 också i denna Aspose.Cells för Java v8.9.1.

{{% /alert %}}
