---
title: Öppna filer med olika format
type: docs
weight: 30
url: /sv/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API låter dig öppna/läsa olika format som XLSX, HTML, CSV, ODS, TSV, 806173411, 8718, 8718, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Med Aspose.Cells kan du öppna filer med olika format.**Aspose.Cells** kan öppna en rad filformat som Microsoft Excel-kalkylblad (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (XLS, 076116361, Tab-avgränsade, etc.)

Om du behöver veta alla filformat som stöds, se följande sidor:
[Filformat som stöds](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Öppna filer med olika format**

Aspose.Cells tillåter utvecklare att öppna kalkylbladsfiler med olika format som SpreadsheetML, kommaseparerade värden (CSV), tabbavgränsade eller tabbavgränsade värden (TSV), ODS filer. För att öppna sådana filer kan utvecklare använda samma metod som de använder för att öppna filer av olika Microsoft Excel-versioner.

### **Öppnar SpreadsheetML Filer**

SpreadsheetML-filer är XML-representationer av kalkylblad inklusive all information om det, såsom formatering, formler etc. Sedan Microsoft Excel XP har ett XML-exportalternativ lagts till i Microsoft Excel som exporterar dina kalkylblad till SpreadsheetML-filer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **Öppnar HTML Filer**

Aspose.Cells låter dig öppna HTML-filen i ett arbetsboksobjekt. HTML-filen bör Microsoft Excel-orienterad, dvs MS-Excel ska kunna öppna den.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **Öppnar CSV Filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecken och citattecken med dubbla citattecken. Om ett fältvärde innehåller ett dubbelt citattecken escapes det med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **Öppnar CSV-filer och ersätter ogiltiga tecken**

I Excel, när CSV-filen med specialtecken öppnas, ersätts tecknen automatiskt. Detsamma görs av Aspose.Cells API vilket visas i kodexemplet nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Använder föredragen parser**

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

### **Öppnar SXC Filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkylbladen som skapas med denna programvara sparas med tillägget SXC. Filen SXC används också för OpenOffice.org Calc-kalkylbladsfiler. Aspose.Cells kan läsa SXC-filer som visas av följande kodexempel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **Öppnar FODS Filer**

FODS-filen är ett kalkylblad som sparas i OpenDocument XML utan någon komprimering. Aspose.Cells kan läsa FODS-filer som visas av följande kodexempel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

