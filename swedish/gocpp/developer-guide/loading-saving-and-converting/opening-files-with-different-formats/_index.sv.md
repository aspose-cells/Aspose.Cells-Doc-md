---
title: Öppning av filer med olika format
type: docs
weight: 30
url: /sv/go-cpp/opening-files-with-different-formats/

description: Aspose.Cells for Go via C++ API tillåter dig att öppna/läsa olika format som XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: öppna xlsx filer, öppna html filer, läsa in fods filer, läsa in ods filer, läsa in sxc filer, öppna csv filer, tabulerad, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Med Aspose.Cells kan du öppna filer i olika format. **Aspose.Cells** kan öppna en rad filerformat som Microsoft Excel-kalkylblad (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (CSV), tab-separerade eller Tab-separerade värden (TSV)-filer etc.

Om du behöver veta alla stödda filformat, se följande sidor:
[Supported File Formats](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **Öppna filer med olika format**

Aspose.Cells tillåter utvecklare att öppna kalkylbladsfiler i olika format som SpreadsheetML, kommaseparerade värden (CSV), tab-separerade eller Tab-separerade värden (TSV) och ODS-filer. För att öppna sådana filer kan utvecklare använda samma metodik som för att öppna filer av olika Microsoft Excel-versioner.

### **Öppning av SpreadsheetML Filer**

SpreadsheetML-filer är XML-representationer av kalkylblad som inkluderar all information om det, såsom formatering, formeln osv. Sedan Microsoft Excel XP har ett XML-exportalternativ lagts till i Microsoft Excel som exporterar dina kalkylblad till SpreadsheetML-filer.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **Öppning av HTML filer**

Aspose.Cells tillåter dig att öppna HTML-fil i en Workbook-objekt. HTML-filen bör vara Microsoft Excel-orienterad dvs MS-Excel bör kunna öppna det.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **Öppning av CSV-filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecknet och citeras med dubbelcitat-tecknet. Om en fältvärde innehåller ett dubbelcitat-tecken escapas det med ett par av dubbelcitat-tecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

### **Öppning av Textfiler med Anpassad Separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en typ av vanlig textfil som kan ha några anpassade separatorer.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

Exempelfiler kan laddas ner från följande länkar för att testa denna funktion.

[CustomSeparator.txt](CustomSeparator.txt)

### **Öppning av tabbehållna filer**

Tabb-separerad (Text) fil innehåller kalkylbladsdata men utan någon formatering. Data är ordnad i rader och kolumner som i tabeller och kalkylblad. I grund och botten är en tabb-separerad fil en speciell sorts vanlig textfil med en tabb mellan varje kolumn.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **Öppning av tabseparatorvärdefiler (TSV-filer)**

En tabb-separerad värdefil (TSV) innehåller kalkylbladsdata men utan någon formatering. Det är samma som en tabb-separerad fil där data är ordnad i rader och kolumner som i tabeller och kalkylblad.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **Öppning av SXC-filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkylblad skapade med denna programvara sparas med SXC-ändelsen. SXC-filen används även för OpenOffice.org Calc kalkylbladsfiler. Aspose.Cells kan läsa SXC-filer, vilket demonstreras av följande kodexempel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **Öppning av FODS-filer**

FODS-filen är ett kalkylblad sparat i OpenDocument XML utan någon komprimering. Aspose.Cells kan läsa FODS-filer, vilket demonstreras av följande kodexempel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
