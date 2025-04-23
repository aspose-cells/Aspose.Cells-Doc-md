---
title: Öppning av filer med olika format
type: docs
weight: 30
url: /sv/python-net/opening-files-with-different-formats/
description: Aspose.Cells för Python via .NET API tillåter dig att öppna/läsa olika format som XLSX, HTML, CSV, ODS, TSV, SXC, FODS osv.
keywords: öppna xlsx filer, öppna html filer, läsa in fods filer, läsa in ods filer, läsa in sxc filer, öppna csv filer, tabulerad, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Med Aspose.Cells för Python via .NET kan du öppna filer med olika format. Aspose.Cells för Python via .NET kan öppna ett brett utbud av filformat såsom Microsoft Excel-kalkylblad (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (CSV), tabbseparerade eller tab-separerade värden (TSV) filer etc.

Om du behöver veta alla stödda filformat, se följande sidor:
[Supported File Formats](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Öppna filer med olika format**

Aspose.Cells för Python via .NET tillåter utvecklare att öppna kalkylbladsfiler med olika format som SpreadsheetML, kommaseparerade värden (CSV), tabbseparaterade eller tab-separerade värden (TSV), ODS-filer. För att öppna sådana filer kan utvecklare använda samma metod som för att öppna filer av olika Microsoft Excel-versioner.

### **Öppning av SpreadsheetML Filer**

SpreadsheetML-filer är XML-representationer av kalkylblad som innehåller all information om det, som formatering, formler etc. Sedan Microsoft Excel XP har en XML export-alternativ lagts till i Microsoft Excel som exporterar dina kalkylblad till SpreadsheetML-filer.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **Öppning av HTML filer**

Aspose.Cells för Python via .NET tillåter dig att öppna HTML-filer i Workbook-objektet. HTML-filen ska vara Microsoft Excel-inriktad, dvs MS-Excel ska kunna öppna den.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **Öppning av CSV-filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecknet och citeras med dubbelcitat-tecknet. Om en fältvärde innehåller ett dubbelcitat-tecken escapas det med ett par av dubbelcitat-tecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **Öppna CSV-filer och ersätt ogiltiga tecken**

När du i Excel öppnar en CSV-fil med specialtecken ersätts tecknen automatiskt. Detsamma gör Aspose.Cells för Python via .NET API, vilket demonstreras i kodexemplet nedan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Öppning av tabbehållna filer**

Tabbehållna (text) filer innehåller kalkyldata men utan någon formatering. Data är ordnad i rader och kolumner som i tabeller och kalkylblad. En tabbehållen fil är i grund och botten en särskild typ av ren textfil med ett tabstopp mellan varje kolumn.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Öppning av tabseparatorvärdefiler (TSV-filer)**

Tabseparatorvärdefiler (TSV-filer) innehåller kalkyldata men utan någon formatering. De är samma som tabbehållna filer där data är ordnad i rader och kolumner som i tabeller och kalkylblad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **Öppning av SXC-filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkylblad skapade med denna programvara sparas med SXC-ändelsen. SXC-filen används även för OpenOffice.org Calc kalkylbladsfiler. Aspose.Cells för Python via .NET kan läsa SXC-filer som demonstreras i följande kodexempel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **Öppning av FODS-filer**

FODS-fil är ett kalkylblad sparat i OpenDocument XML utan komprimering. Aspose.Cells för Python via .NET kan läsa FODS-filer som demonstreras i följande kodexempel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
