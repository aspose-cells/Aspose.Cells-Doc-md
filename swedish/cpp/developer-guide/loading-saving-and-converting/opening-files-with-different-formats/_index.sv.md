---
title: Öppning av filer med olika format
type: docs
weight: 30
url: /sv/cpp/opening-files-with-different-formats/

description: Aspose.Cells for .NET API en tillåter dig att öppna/läsa in olika format som XLSX, HTML, CSV, ODS, TSV, SXC, FODS, osv.
keywords: öppna xlsx filer, öppna html filer, läsa in fods filer, läsa in ods filer, läsa in sxc filer, öppna csv filer, tabulerad, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Med Aspose.Cells kan du öppna filer med olika format. **Aspose.Cells** kan öppna en rad filformat som Microsoft Excel-kalkylblad (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (CSV), Tab Delimited eller Tab-separerade värden (TSV) osv.

Om du behöver veta alla stödda filformat, se följande sidor:
[Stödda filformat](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **Öppna filer med olika format**

Aspose.Cells gör det möjligt för utvecklare att öppna kalkylbladsfiler med olika format som SpreadsheetML, kommaseparerade värden (CSV), Tab Delimited eller Tab-separerade värden (TSV), ODS-filer. För att öppna sådana filer kan utvecklare använda samma metod som de använder för att öppna filer för olika versioner av Microsoft Excel.

### **Öppning av SpreadsheetML Filer**

SpreadsheetML-filer är XML-representationer av kalkylblad som innehåller all information om det, som formatering, formler etc. Sedan Microsoft Excel XP har en XML export-alternativ lagts till i Microsoft Excel som exporterar dina kalkylblad till SpreadsheetML-filer.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

### **Öppning av HTML filer**

Aspose.Cells tillåter dig att öppna HTML-fil i en Workbook-objekt. HTML-filen bör vara Microsoft Excel-orienterad dvs MS-Excel bör kunna öppna det.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

### **Öppning av CSV-filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecknet och citeras med dubbelcitat-tecknet. Om en fältvärde innehåller ett dubbelcitat-tecken escapas det med ett par av dubbelcitat-tecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

#### **Öppna CSV-filer och ersätt ogiltiga tecken**

I Excel när en CSV-fil med specialtecken öppnas, ersätts tecknen automatiskt. Samma sak görs av Aspose.Cells API som visas i följande kodexempel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Provexempelfil kan laddas ner från följande länkar för att testa den här funktionen.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Öppning av Textfiler med Anpassad Separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en typ av vanlig textfil som kan ha några anpassade separatorer.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Provexempelfil kan laddas ner från följande länkar för att testa den här funktionen.

[CustomSeparator.txt](CustomSeparator.txt)

### **Öppning av tabbehållna filer**

Tabbehållna (text) filer innehåller kalkyldata men utan någon formatering. Data är ordnad i rader och kolumner som i tabeller och kalkylblad. En tabbehållen fil är i grund och botten en särskild typ av ren textfil med ett tabstopp mellan varje kolumn.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

### **Öppning av tabseparatorvärdefiler (TSV-filer)**

Tabseparatorvärdefiler (TSV-filer) innehåller kalkyldata men utan någon formatering. De är samma som tabbehållna filer där data är ordnad i rader och kolumner som i tabeller och kalkylblad.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

### **Öppning av SXC-filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkylblad som skapats med den här programvaran sparas med SXC-tillägget. SXC-filen används också för OpenOffice.org Calc kalkylbladsfiler. Aspose.Cells kan läsa SXC-filer som visas i följande kodexempel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

### **Öppning av FODS-filer**

FODS-filer är kalkylblad som sparas i OpenDocument XML utan någon komprimering. Aspose.Cells kan läsa FODS-filer som visas i följande kodexempel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
