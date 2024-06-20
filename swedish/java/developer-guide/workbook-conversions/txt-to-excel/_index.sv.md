---
title: Konvertera CSV, TSV och TXT till Excel
type: docs
weight: 50
url: /sv/java/convert-csv-tsv-and-txt-to-excel/
---

## **Öppning av CSV-filer**

Comma Separated Values (CSV)-filer innehåller poster vars värden är avgränsade eller separerade med kommatecken. I CSV-filer lagras data i en tabellformat som har fält separerade av kommatecknet och citerade av dubbelfnuttarkarakteren. Om ett fälts värde innehåller en dubbelfnuttarkaraktär escaperas den med ett par av dubblefnuttarkaraktärer. Du kan också använda Microsoft Excel för att exportera dina kalkylbladsdata till en CSV-fil.

För att öppna CSV-filer, använd [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)-klassen och välj värdet [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), fördefinierat i [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)-uppräkning.

## **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Öppna CSV-filer och ersätt ogiltiga tecken**

I Excel, när en CSV-fil med specialtecken öppnas, ersätts tecknen automatiskt. Samma sak görs av Aspose.Cells API som visas i det givna kodexemplet nedan.

#### **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Öppning av CSV-filer med föredragen parser**

Det är inte alltid nödvändigt att använda standard-inställningar för öppning av CSV-filer. Ibland skapas inte förväntad utdata vid import av CSV-filen, exempelvis är inte datumformatet som förväntat eller tomma fält hanteras på ett annat sätt. För detta ändamål används [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) för att tillhandahålla en egen föredragen parser för att tolka olika datatyper enligt behov. Följande exempelkod visar användningen av föredragen parser.  

Exempelfilen och utdatafiler kan laddas ner från följande länkar för att testa denna funktion.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Öppning av TSV (Tab Separated Values) filer**

Tab-separerade filer innehåller kalkylbladsdata utan någon formatering. Data ordnas i rader och kolumner som tabeller och kalkylblad. Kort sagt, en tab-separerad fil är en speciell typ av ren textfil med en tabulator mellan varje kolumn i texten.

För att öppna tab-separerade filer ska utvecklare använda klassen [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) och välja värdet [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), som är fördefinierat i [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)-uppräkningen.

## **Exempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Fortsatta ämnen**
- [Läs in eller importera CSV-fil med formler](/cells/sv/java/load-or-import-csv-file-with-formulas/)
- [Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format](/cells/sv/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

