---
title: Öppna filer med olika format
linktitle: Öppna filer
type: docs
weight: 10
url: /sv/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

Utvecklare använder Aspose.Cells för att öppna filer för olika ändamål. Öppna till exempel en fil för att hämta data från den, eller använd en fördefinierad designarkfil för att påskynda utvecklingsprocessen. Aspose.Cells tillåter utvecklare att öppna olika typer av källfiler. Dessa källfiler kan vara Microsoft Excel-rapporter, SpreadsheetML, kommaseparerade värden (CSV), tabbavgränsade eller tabbavgränsade värden (TSV) filer. Den här artikeln diskuterar att öppna dessa olika källfiler med Aspose.Cells.

Om du behöver veta alla filformat som stöds, se följande sidor:
[Filformat som stöds](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Enkla sätt att öppna Excel-filer**

### **Öppning genom vägen**

För att öppna en Microsoft Excel-fil med hjälp av filsökvägen, skicka sökvägen till filen som en parameter medan du skapar instansen av**[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Arbetsbok)**klass. Följande exempelkod visar hur du öppnar en Excel-fil med hjälp av filsökvägen.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Öppnas genom Stream**

Ibland lagras Excel-filen som du vill öppna som en ström. I så fall, på samma sätt som att öppna en fil med hjälp av filsökvägen, skicka strömmen som en parameter medan du instansierar**[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Arbetsbok)**klass. Följande exempelkod visar hur du öppnar en Excel-fil med stream.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Öppna filer av olika Microsoft Excel-versioner**

 Användaren kan använda**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** klass för att ange formatet för Excel-filen med hjälp av**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

 De**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkningen innehåller många fördefinierade filformat av vilka några ges nedan.

|**Formattyper**|**Beskrivning**|
|:- |:- |
|Csv|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003-fil|
|Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-fil|
|Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM-fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX-fil|
|Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM-fil|
|Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB-fil|
|SpreadsheetML|Representerar en SpreadsheetML-fil|
|Tsv|Representerar en tabbseparerad värdefil|
|TabDelimited|Representerar en tabbavgränsad textfil|
|Odds|Representerar en ODS-fil|
|Html|Representerar en HTML-fil|
|Mhtml|Representerar en MHTML-fil|

### **Öppnar Microsoft Excel 95/5.0-filer**

 För att öppna Microsoft Excel 95-filer, instansiera**[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Arbetsbok)**instans med sökvägen eller strömmen till mallfilen. Exempelfil för att testa koden kan laddas ner från följande länk:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Öppna Microsoft Excel 97 eller senare versioner av XLS-filer**

 För att öppna XLS-filer av Microsoft Excel XLS 97 eller senare versioner, instansiera**[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Arbetsbok)** instans med sökvägen eller strömmen till mallfilen. Eller använd**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** metod och välj**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** värde i**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Öppna Microsoft Excel 2007 eller senare versioner av XLSX-filer**

 För att öppna XLSX-filer av Microsoft Excel 2007 eller senare versioner, instansiera**[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Arbetsbok)**instans med sökvägen eller strömmen till mallfilen. Eller använd**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** klass och välj**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** värde i**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Öppna filer med olika format**

Aspose.Cells tillåter utvecklare att öppna kalkylarksfiler med olika format som SpreadsheetML, CSV, Tab Delimited filer. För att öppna sådana filer kan utvecklare använda samma metod som de använder för att öppna filer av olika Microsoft Excel-versioner.

### **Öppna SpreadsheetML-filer**

SpreadsheetML-filer är XML-representationer av dina kalkylblad inklusive all information om kalkylarket som formatering, formler etc. Sedan Microsoft Excel XP har ett XML-exportalternativ lagts till i Microsoft Excel som exporterar dina kalkylblad till SpreadsheetML-filer.

För att öppna SpreadsheetML-filer, använd**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** klass och välj**[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** värde i**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Öppna CSV-filer**

CSV-filer (Comma Separated Values) innehåller poster vars värden är avgränsade eller separerade med kommatecken. I CSV-filer lagras data i ett tabellformat som har fält separerade med kommatecken och citerade med dubbla citattecken. Om ett fälts värde innehåller ett dubbelcitattecken escapes det med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera dina kalkylbladsdata till en CSV-fil.

För att öppna CSV-filer, använd**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** klass och välj**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** värde, fördefinierat i**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Öppnar CSV-filer och ersätter ogiltiga tecken**

I Excel, när CSV-fil med specialtecken öppnas, ersätts tecknen automatiskt. Detsamma görs av Aspose.Cells API vilket visas i kodexemplet nedan.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Öppna CSV-filer med föredragen parser**

Detta är inte alltid nödvändigt för att använda standardparserinställningar för att öppna CSV-filerna. Ibland skapar import av CSV-fil inte förväntad utdata som att datumformatet inte är som förväntat eller tomma fält hanteras annorlunda. För det här syftet**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**är tillgänglig för att tillhandahålla en egen föredragen parser för att analysera olika datatyper enligt kravet. Följande exempelkod visar användningen av den föredragna parsern.

Exempel på källfiler och utdatafiler kan laddas ner från följande länkar för att testa den här funktionen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öppnar TSV-filer (tabbavgränsade).**

Tabbavgränsade filer innehåller kalkylbladsdata men utan någon formatering. Data är ordnade i rader och kolumner som tabeller och kalkylblad. Kortfattat är en tabbavgränsad fil en speciell typ av vanlig textfil med en tabb mellan varje kolumn i texten.

För att öppna tabbavgränsade filer bör utvecklare använda**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** klass och välj**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** värde, fördefinierat i**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Öppna krypterade Excel-filer**

Vi vet att det är möjligt att skapa krypterade Excel-filer med Microsoft Excel. För att öppna sådana krypterade filer bör utvecklare anropa en speciell överbelastad LoadOptions-metod och välja DEFAULT-värdet, fördefinierat i FileFormatType-uppräkningen. Denna metod skulle också ta lösenordet för den krypterade filen som visas nedan i exemplet.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells stöder även öppning av lösenordsskyddade MS Excel 2013-filer.

{{% alert color="primary" %}}

Det finns rimliga chanser att Workbook-konstruktören kan kasta System.OutOfMemoryException när stora kalkylblad laddas. Detta undantag tyder på att det tillgängliga minnet är otillräckligt för att fullständigt ladda kalkylarket i minnet, därför måste kalkylarket laddas samtidigt som du aktiverar[Minnesinställningar](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Öppna SXC-filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkylbladen som skapas med denna programvara sparas med SXC-tillägget. SXC-filen används också för OpenOffice.org Calc-kalkylbladsfiler. Aspose.Cells kan läsa SXC-filer som visas av följande kodexempel.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Öppna FODS-filer**

FODS-filen är kalkylblad sparad i OpenDocument XML utan någon komprimering. Aspose.Cells kan läsa FODS-filer som visas av följande kodexempel.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Förhandsämnen**
- [Filtrera definierade namn när arbetsboken laddas](/cells/sv/java/filter-defined-names-while-loading-workbook/)
- [Filtrera objekt när du laddar arbetsbok eller arbetsblad](/cells/sv/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Få varningar när du laddar Excel-fil](/cells/sv/java/get-warnings-while-loading-excel-file/)
- [Behåll separatorer för tomma rader medan du exporterar kalkylark till CSV-format](/cells/sv/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Ladda arbetsbok med angiven skrivarpappersstorlek](/cells/sv/java/load-workbook-with-specified-printer-paper-size/)
- [Öppna olika Microsoft Excel-versionsfiler](/cells/sv/java/opening-different-microsoft-excel-versions-files/)
- [Optimera minnesanvändning när du arbetar med stora filer med stora datamängder](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Läs Numbers-kalkylblad Utvecklat av Apple Inc. med Aspose.Cells](/cells/sv/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Läser CSV-fil med flera kodningar](/cells/sv/java/reading-csv-file-with-multiple-encodings/)
- [Stoppa konvertering eller laddning med InterruptMonitor när det tar för lång tid](/cells/sv/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Använder LightCells API](/cells/sv/java/using-lightcells-api/)
