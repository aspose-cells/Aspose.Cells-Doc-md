---
title: Öppning av filer med olika format
linktitle: Öppna filer
type: docs
weight: 10
url: /sv/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Utvecklare använder Aspose.Cells för att öppna olika filer för olika ändamål. Till exempel öppna en fil för att hämta data från den, eller använd en fördefinierad designer kalkylbladsfil för att påskynda din utvecklingsprocess. Aspose.Cells tillåter utvecklare att öppna olika typer av källfiler. Dessa källfiler kan vara Microsoft Excel-rapporter, SpreadsheetML, Komma-separerade värden (CSV), Tabulator Begränsad eller Tab-separerade värden (TSV) filer. Denna artikel diskuterar öppning av dessa olika källfiler med hjälp av Aspose.Cells.

Om du behöver veta alla stödda filformat, se följande sidor:
[Supportfilformat](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Enkla sätt att öppna Excel-filer**

### **Öppning genom sökväg**

För att öppna en Microsoft Excel-fil med hjälp av filen sökvägen ska du passera sökvägen till filen som en parameter vid skapande av instansen av [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klassen. Följande exempelkod demonstrerar öppnandet av en Excel-fil med hjälp av filen sökvägen.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Öppning genom Ström**

Ibland är Excel-filen som du vill öppna lagrad som en ström. I så fall, liknande vid öppning av en fil med hjälp av filen sökvägen, ska passera strömmen som en parameter vid instantieringen av [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klassen. Följande exempelkod demonstrerar öppnandet av en Excel-fil med hjälp av strömmen.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Öppning av filer av olika Microsoft Excel-versioner**

Användaren kan använda [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) klassen för att specificera formatet av Excel-filen med hjälp av [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) uppräkningen.

[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)uppräkningen innehåller många fördefinierade filformat varav några ges nedan.

|**Formattyper**|**Beskrivning**|
| :- | :- |
|Csv|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX fil|
|Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX fil|
|Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM fil|
|Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB fil|
|SpreadsheetML|Representerar en SpreadsheetML fil|
|Tsv|Representerar en tabb-separerad värden fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|Ods|Representerar en ODS fil|
|Html|Representerar en HTML fil|
|Mhtml|Representerar en MHTML fil|

### **Öppna Microsoft Excel 95/5.0 Fil**

För att öppna Microsoft Excel 95 filer, instansiera [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) med sökvägen eller strömmen av mallfilen. Exempelfil för att testa koden kan laddas ner från följande länk:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Öppnar Microsoft Excel 97 eller senare versioner XLS-filer**

För att öppna XLS-filer av Microsoft Excel XLS 97 eller senare versioner, instansiera [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) med sökvägen eller strömmen av mallfilen. Eller använd [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) metoden och välj värdet [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003) i [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) uppräkningen.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Öppna Microsoft Excel 2007 eller senare versioners XLSX-filer**

För att öppna XLSX-filer av Microsoft Excel 2007 eller senare versioner, instansiera [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) med sökvägen eller strömmen av mallfilen. Eller använd [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) klassen och välj värdet [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) i [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) uppräkningen.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Öppna filer med olika format**

Aspose.Cells tillåter utvecklare att öppna kalkylblad med olika format som SpreadsheetML, CSV, Tabbavgränsade filer. För att öppna sådana filer, kan utvecklare använda samma metodik som de använder för att öppna filer av olika Microsoft Excel-versioner.

### **Öppning av SpreadsheetML Filer**

SpreadsheetML-filer är XML-representationer av dina kalkylblad inklusive all information om kalkylarket som formatering, formler, etc. Sedan Microsoft Excel XP, har en XML-exportalternativ lagts till i Microsoft Excel som exporterar dina kalkylblad till SpreadsheetML-filer.

För att öppna SpreadsheetML-filer, använd [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) klassen och välj värdet [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML) i [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) uppräkningen.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Öppning av CSV-filer**

Comma Separated Values (CSV)-filer innehåller poster vars värden är avgränsade eller separerade med kommatecken. I CSV-filer lagras data i en tabellformat som har fält separerade av kommatecknet och citerade av dubbelfnuttarkarakteren. Om ett fälts värde innehåller en dubbelfnuttarkaraktär escaperas den med ett par av dubblefnuttarkaraktärer. Du kan också använda Microsoft Excel för att exportera dina kalkylbladsdata till en CSV-fil.

För att öppna CSV-filer, använd [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)-klassen och välj värdet [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), fördefinierat i [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)-uppräkning.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Öppna CSV-filer och ersätt ogiltiga tecken**

I Excel, när en CSV-fil med specialtecken öppnas, ersätts tecknen automatiskt. Samma sak görs av Aspose.Cells API som visas i det givna kodexemplet nedan.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Öppning av CSV-filer med föredragen parser**

Det är inte alltid nödvändigt att använda standard-inställningar för öppning av CSV-filer. Ibland skapas inte förväntad utdata vid import av CSV-filen, exempelvis är inte datumformatet som förväntat eller tomma fält hanteras på ett annat sätt. För detta ändamål används [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) för att tillhandahålla en egen föredragen parser för att tolka olika datatyper enligt behov. Följande exempelkod visar användningen av föredragen parser.  

Exempelfilen och utdatafiler kan laddas ner från följande länkar för att testa denna funktion.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öppning av TSV (Tab Separated Values) filer**

Tab-separerade filer innehåller kalkylbladsdata utan någon formatering. Data ordnas i rader och kolumner som tabeller och kalkylblad. Kort sagt, en tab-separerad fil är en speciell typ av ren textfil med en tabulator mellan varje kolumn i texten.

För att öppna tab-separerade filer ska utvecklare använda klassen [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) och välja värdet [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), som är fördefinierat i [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)-uppräkningen.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Öppna krypterade Excelfiler**

Vi vet att det är möjligt att skapa krypterade Excelfiler med Microsoft Excel. För att öppna sådana krypterade filer, bör utvecklare använda en särskild överbelastad LoadOptions metod och välja värdet DEFAULT, fördefinierat i FileFormatType uppräkningen. Denna metod skulle också ta lösenordet för den krypterade filen som visas nedan i exemplet.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells stöder också öppnande av lösenordsskyddade MS Excel 2013-filer.

{{% alert color="primary" %}}

Det finns goda chanser att Workbook-konstruktören kan kasta System.OutOfMemoryException vid laddning av stora kalkylblad. Detta undantag antyder att tillgängligt minne är otillräckligt för att helt ladda in kalkylarket i minnet, därför måste kalkylarket laddas med hjälp av [Minnesinställningar](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Öppning av SXC-filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkylblad som skapats med den här programvaran sparas med SXC-tillägget. SXC-filen används också för OpenOffice.org Calc kalkylbladsfiler. Aspose.Cells kan läsa SXC-filer som visas i följande kodexempel.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Öppning av FODS-filer**

FODS-fil är ett kalkylblad sparat i OpenDocument XML utan komprimering. Aspose.Cells kan läsa FODS-filer enligt den följande kodexempel.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Fortsatta ämnen**
- [Filtrera Definierade namn vid inläsning av arbetsbok](/cells/sv/java/filter-defined-names-while-loading-workbook/)
- [Filtrera objekt vid inläsning av arbetsbok eller arbetsblad](/cells/sv/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Få varningar vid inläsning av Excel-fil](/cells/sv/java/get-warnings-while-loading-excel-file/)
- [Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format](/cells/sv/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Ladda arbetsbok med specificerad pappersstorlek](/cells/sv/java/load-workbook-with-specified-printer-paper-size/)
- [Öppna filer från olika Microsoft Excel-versioner](/cells/sv/java/opening-different-microsoft-excel-versions-files/)
- [Optimera minnesanvändningen vid arbete med stora filer med stora dataset](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Läsa Numbers-kalkylblad utvecklat av Apple Inc. med Aspose.Cells](/cells/sv/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Läsning av CSV-fil med flera teckentabeller](/cells/sv/java/reading-csv-file-with-multiple-encodings/)
- [Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid](/cells/sv/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Använda LightCells API](/cells/sv/java/using-lightcells-api/)
