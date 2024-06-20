---
title: Konvertera CSV, TSV och TXT till Excel
type: docs
weight: 30
url: /sv/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

Med Aspose.Cells kan du konvertera CSV-filer till Excel, OpenOffice, Pdf, Json och många olika format.

{{% /alert %}}


## **Öppning av CSV-filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecknet och citeras med dubbelcitat-tecknet. Om en fältvärde innehåller ett dubbelcitat-tecken escapas det med ett par av dubbelcitat-tecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Öppna CSV-filer och ersätt ogiltiga tecken**

I Excel när en CSV-fil med specialtecken öppnas, ersätts tecknen automatiskt. Samma sak görs av Aspose.Cells API som visas i följande kodexempel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Användning av föredragen parser**

Det är inte alltid nödvändigt att använda standardinställningar för parser för att öppna CSV-filerna. Ibland skapar importera CSV-filen inte det förväntade resultatet som t.ex. datumformatet är inte som förväntat eller tomma fält hanteras på ett annat sätt. För detta ändamål finns**TxtLoadOptions.PreferredParsers**tillgänglig för att tillhandahålla en egen föredragen parser för att parsa olika datatyper enligt behovet. Följande kodexempel visar användningen av föredragen parser.  

Exempelfilen och utdatafiler kan laddas ner från följande länkar för att testa denna funktion.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Öppning av Textfiler med Anpassad Separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en typ av vanlig textfil som kan ha några anpassade separatorer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Öppning av tabbehållna filer**

Tabbehållna (text) filer innehåller kalkyldata men utan någon formatering. Data är ordnad i rader och kolumner som i tabeller och kalkylblad. En tabbehållen fil är i grund och botten en särskild typ av ren textfil med ett tabstopp mellan varje kolumn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Öppning av tabseparatorvärdefiler (TSV-filer)**

Tabseparatorvärdefiler (TSV-filer) innehåller kalkyldata men utan någon formatering. De är samma som tabbehållna filer där data är ordnad i rader och kolumner som i tabeller och kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Fortsatta ämnen**
- [Läs in eller importera CSV-fil med formler](/cells/sv/net/load-or-import-csv-file-with-formulas/)
- [Läsning av CSV-fil med flera teckentabeller](/cells/sv/net/reading-csv-file-with-multiple-encodings/)

