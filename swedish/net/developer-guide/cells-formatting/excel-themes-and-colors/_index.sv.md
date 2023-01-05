---
title: Excel-teman och färger
type: docs
weight: 100
url: /sv/net/excel-themes-and-colors/
---
## **Excel-teman och färger**

Teman ger ett enhetligt utseende med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel, stilen Accent1, till exempel, ser annorlunda ut i Office- och Apex-teman. Ofta tillämpar du ett dokumenttema och ändrar det sedan till hur du vill ha det.

Aspose.Cells tillhandahåller funktioner för att anpassa teman och färger.

### **Skaffa och ställ in temafärger**

Nedan finns några metoder och egenskaper som implementerar temafärger.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Används för att ställa in förgrundsfärgen.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Används för att ställa in bakgrundsfärgen.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Används för att ställa in teckensnittsfärgen.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Används för att få en temafärg.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Används för att ställa in en temafärg.

Följande exempel visar hur du får och ställer in temafärger.

Följande exempel använder en mall XLSX-fil, hämtar färgerna för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **Anpassa teman**

Följande exempel visar hur du använder anpassade teman med dina önskade färger. Vi använder en exempelmallfil som skapats manuellt i Microsoft Excel 2007.

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, tillämpar de anpassade färgerna och sparar excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **Använd temafärger**

Följande exempel tillämpar en cells förgrunds- och teckensnittsfärger baserat på färgtyperna för standardtema (i arbetsboken). Det sparar även excel-filen på disk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

## **Förhandsämnen**
- [Extrahera temadata från Excel-fil](/cells/sv/net/extract-theme-data-from-excel-file/)
