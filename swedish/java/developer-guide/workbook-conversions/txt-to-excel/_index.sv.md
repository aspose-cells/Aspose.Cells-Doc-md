---
title: Konvertera CSV, TSV och TXT till Excel
type: docs
weight: 50
url: /sv/java/convert-csv-tsv-and-txt-to-excel/
---
## **Öppna CSV-filer**

CSV-filer (Comma Separated Values) innehåller poster vars värden är avgränsade eller separerade med kommatecken. I CSV-filer lagras data i ett tabellformat som har fält separerade med kommatecken och citerade med dubbla citattecken. Om ett fälts värde innehåller ett dubbelcitattecken escapes det med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera dina kalkylbladsdata till en CSV-fil.

För att öppna CSV-filer, använd**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** klass och välj**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** värde, fördefinierat i**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

## **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Öppnar CSV-filer och ersätter ogiltiga tecken**

I Excel, när CSV-fil med specialtecken öppnas, ersätts tecknen automatiskt. Detsamma görs av Aspose.Cells API vilket visas i kodexemplet nedan.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Öppna CSV-filer med föredragen parser**

Detta är inte alltid nödvändigt för att använda standardparserinställningar för att öppna CSV-filerna. Ibland skapar import av CSV-fil inte förväntad utdata som att datumformatet inte är som förväntat eller tomma fält hanteras annorlunda. För det här syftet**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**är tillgänglig för att tillhandahålla en egen föredragen parser för att analysera olika datatyper enligt kravet. Följande exempelkod visar användningen av den föredragna parsern.

Exempel på källfiler och utdatafiler kan laddas ner från följande länkar för att testa den här funktionen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öppnar TSV-filer (tabbavgränsade).**

Tabbavgränsade filer innehåller kalkylbladsdata men utan någon formatering. Data är ordnade i rader och kolumner som tabeller och kalkylblad. Kortfattat är en tabbavgränsad fil en speciell typ av vanlig textfil med en tabb mellan varje kolumn i texten.

För att öppna tabbavgränsade filer bör utvecklare använda**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** klass och välj**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** värde, fördefinierat i**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**uppräkning.

## **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Förhandsämnen**
- [Ladda eller importera CSV-fil med formler](/cells/sv/java/load-or-import-csv-file-with-formulas/)
- [Trimma ledande tomma rader och kolumner samtidigt som du exporterar kalkylblad till CSV-format](/cells/sv/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

