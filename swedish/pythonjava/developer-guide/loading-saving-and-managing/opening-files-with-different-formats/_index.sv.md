---
title: Öppna filer med olika format
type: docs
weight: 30
url: /sv/python-java/opening-files-with-different-formats/
description: Aspose.Cells for .NET API låter dig öppna/läsa olika format som XLSX, HTML, CSV, ODS, TSV, 806173411, 8718, 8718, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Med Aspose.Cells kan du öppna filer med olika format.**Aspose.Cells** kan öppna en rad filformat som Microsoft Excel-kalkylblad (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (XLS, 076116361, Tab-avgränsade, etc.)

Om du behöver veta alla filformat som stöds, se följande sidor:
[Filformat som stöds](https://docs.aspose.com/cells/python-java/supported-file-formats/)

{{% /alert %}}

## **Öppna filer med olika format**

Aspose.Cells tillåter utvecklare att öppna kalkylbladsfiler med olika format som SpreadsheetML, kommaseparerade värden (CSV), tabbavgränsade eller tabbavgränsade värden (TSV), ODS filer. För att öppna sådana filer kan utvecklare använda samma metod som de använder för att öppna filer av olika Microsoft Excel-versioner.

### **Öppnar SpreadsheetML Filer**

SpreadsheetML-filer är XML-representationer av kalkylblad inklusive all information om det, såsom formatering, formler etc. Sedan Microsoft Excel XP har ett XML-exportalternativ lagts till i Microsoft Excel som exporterar dina kalkylblad till SpreadsheetML-filer.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenSpreadsheetMLFile.py" >}}

### **Öppnar HTML Filer**

Aspose.Cells låter dig öppna HTML-filen i ett arbetsboksobjekt. HTML-filen bör Microsoft Excel-orienterad, dvs MS-Excel ska kunna öppna den.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenHTMLFile.py" >}}

### **Öppnar CSV Filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecken och citattecken med dubbla citattecken. Om ett fältvärde innehåller ett dubbelt citattecken escapes det med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenCSVFile.py" >}}

#### **Öppnar CSV-filer och ersätter ogiltiga tecken**

I Excel, när CSV-filen med specialtecken öppnas, ersätts tecknen automatiskt. Detsamma görs av Aspose.Cells API vilket visas i kodexemplet nedan.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenCSVFileAndReplaceInvalidCharacters.py" >}}

Exempel på källfil kan laddas ner från följande länkar för att testa den här funktionen.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Öppna textfiler med anpassad separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en sorts vanlig textfil som kan ha några anpassade avgränsare.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTextFilewithCustomSeparator.py" >}}

Exempel på källfil kan laddas ner från följande länkar för att testa den här funktionen.

[CustomSeparator.txt](CustomSeparator.txt)

### **Öppnar flikavgränsade filer**

Tabbavgränsad (text) fil innehåller kalkylbladsdata men utan någon formatering. Data är ordnade i rader och kolumner som i tabeller och kalkylblad. I grund och botten är en tabbavgränsad fil en speciell typ av vanlig textfil med en tabb mellan varje kolumn.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTabDelimitedFile.py" >}}

Exempel på källfil kan laddas ner från följande länkar för att testa den här funktionen.

[TabDelimited.txt](TabDelimited.txt)

### **Öppna flikseparerade värden (TSV) filer**

Filen med tabbavgränsade värden (TSV) innehåller kalkylbladsdata men utan någon formatering. Det är samma sak med Tab Delimited fil där data är ordnade i rader och kolumner som i tabeller och kalkylblad.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenTSVFile.py" >}}

### **Öppnar SXC Filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkylbladen som skapas med denna programvara sparas med tillägget SXC. Filen SXC används också för OpenOffice.org Calc-kalkylbladsfiler. Aspose.Cells kan läsa SXC-filer som visas av följande kodexempel.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenSXCFile.py" >}}

### **Öppnar FODS Filer**

FODS-filen är ett kalkylblad som sparas i OpenDocument XML utan någon komprimering. Aspose.Cells kan läsa FODS-filer som visas av följande kodexempel.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFODSFile.py" >}}
