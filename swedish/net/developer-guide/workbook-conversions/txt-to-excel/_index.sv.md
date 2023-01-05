---
title: Konvertera CSV, TSV och TXT till Excel
type: docs
weight: 30
url: /sv/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

Med hjälp av Aspose.Cells kan du konvertera filen CSV till Excel , OpenOffice, Pdf, Json och många olika format.

{{% /alert %}}


## **Öppnar CSV Filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecken och citattecken med dubbla citattecken. Om ett fältvärde innehåller ett dubbelt citattecken escapes det med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Öppnar CSV-filer och ersätter ogiltiga tecken**

I Excel, när CSV-filen med specialtecken öppnas, ersätts tecknen automatiskt. Detsamma görs av Aspose.Cells API vilket visas i kodexemplet nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Använder föredragen parser**

Detta är inte alltid nödvändigt för att använda standardparserinställningar för att öppna CSV-filerna. Ibland skapar import av CSV-fil inte förväntad utdata som att datumformatet inte är som förväntat eller tomma fält hanteras annorlunda. För detta ändamål**TxtLoadOptions.PreferredParsers**är tillgänglig för att tillhandahålla en egen föredragen parser för att analysera olika datatyper enligt kravet. Följande exempelkod visar användningen av föredragen parser.

Exempel på källfiler och utdatafiler kan laddas ner från följande länkar för att testa den här funktionen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Öppna textfiler med anpassad separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en sorts vanlig textfil som kan ha några anpassade avgränsare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Öppnar flikavgränsade filer**

Tabbavgränsad (text) fil innehåller kalkylbladsdata men utan någon formatering. Data är ordnade i rader och kolumner som i tabeller och kalkylblad. I grund och botten är en tabbavgränsad fil en speciell typ av vanlig textfil med en tabb mellan varje kolumn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Öppna flikseparerade värden (TSV) filer**

Filen med tabbavgränsade värden (TSV) innehåller kalkylbladsdata men utan någon formatering. Det är samma sak med Tab Delimited fil där data är ordnade i rader och kolumner som i tabeller och kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Förhandsämnen**
- [Ladda eller importera CSV-fil med formler](/cells/sv/net/load-or-import-csv-file-with-formulas/)
- [Läser CSV Fil med flera kodningar](/cells/sv/net/reading-csv-file-with-multiple-encodings/)

