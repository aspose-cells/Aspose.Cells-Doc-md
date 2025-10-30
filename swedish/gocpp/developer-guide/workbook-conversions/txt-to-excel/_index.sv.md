---
title: Konvertera CSV, TSV och TXT till Excel med Golang via C++
linktitle: Konvertera CSV, TSV och TXT till Excel
type: docs
weight: 30
url: /sv/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: Lär dig att konvertera CSV , TSV och TXT filer till Excel med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Med Aspose.Cells for C++ kan du konvertera CSV-filer till Excel, OpenOffice, PDF, JSON och många andra format.

{{% /alert %}}

## **Öppning av CSV-filer**

Komma-separerade värden (CSV) filer innehåller poster där värdena separeras med kommatecken. Data lagras som en tabell där varje kolumn är separerad av kommatecknet och citerad med dubbla citattecken. Om ett fält innehåller ett dubbelt citattecken, är det undkommet med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera kalkylbladdata till CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **Öppna CSV-filer och ersätt ogiltiga tecken**

När du öppnar en CSV-fil med specialtecken i Excel, ersätts tecknen automatiskt. Samma funktion gör Aspose.Cells API, som demonstreras i kodexemplet nedan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **Använder föredragen parser**

Det är inte alltid nödvändigt att använda standardinställningar för parser när du öppnar CSV-filer. Ibland skapar import av en CSV-fil inte den förväntade utmatningen, till exempel när datumformatet inte är som förväntat eller tomma fält hanteras annorlunda. För detta ändamål finns **TxtLoadOptions.PreferredParsers** för att tillhandahålla din egen föredragna parser för att analysera olika datatyper enligt dina krav. Följande kodexempel visar användningen av en föredragen parser.

Exempelfilen och utdatafiler kan laddas ner från följande länkar för att testa denna funktion.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **Öppning av Textfiler med Anpassad Separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en typ av vanlig textfil som kan ha några anpassade separatorer.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **Öppna flik-begränsade filer**

Tab-begränsade (Text) filer innehåller kalkylbladsdata men utan formatering. Data är ordnade i rader och kolumner som i tabeller och kalkylblad. I princip är en tab-begränsad fil en särskild form av ren textfil med tab mellan varje kolumn.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **Öppning av tabseparatorvärdefiler (TSV-filer)**

Tab-separerade värden (TSV) filer innehåller kalkylbladsdata men utan någon formatering. Det är samma som en tab-begränsad fil där data är ordnad i rader och kolumner som i tabeller och kalkylblad.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **Avancerade ämnen**
- [Ladda eller importera CSV-fil med formler](/cells/sv/cpp/load-or-import-csv-file-with-formulas/)
- [Läsning av CSV-fil med flera teckentabeller](/cells/sv/cpp/reading-csv-file-with-multiple-encodings/)
