---
title: Excel-teman och färger
type: docs
weight: 130
url: /sv/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

Teman ger ett enhetligt utseende med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel ser Accent1-stilen annorlunda ut i Office- och Apex-teman. Ofta tillämpar du ett dokumenttema och ändrar det sedan enligt dina behov.

**Tillämpa teman i Microsoft Excel**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Skaffa och ställ in temafärger**

Aspose.Cells API:er tillhandahåller funktioner för att anpassa teman och färger. Nedan finns några metoder och egenskaper som implementerar temafärger.

- Style.ForegroundThemeColor-egenskapen kan användas för att ställa in förgrundsfärgen.
- Style.BackgroundThemeColor-egenskapen kan användas för att ställa in bakgrundsfärgen.
- Font.ThemeColor-egenskapen kan användas för att ställa in teckensnittsfärgen.
- Workbook.getThemeColor-metoden kan användas för att få en temafärg.
- Workbook.setThemeColor-metoden kan användas för att ställa in en temafärg.

Följande exempel visar hur du får och ställer in temafärger.

Följande exempel använder en mall XLSX-fil, hämtar färgerna för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Anpassa teman**

Följande exempel visar hur du använder anpassade teman med dina önskade färger. Exemplet använder en exempelmallfil som skapats manuellt i Microsoft Excel 2007.

**Mallen CustomThemeColor.xlsx-filen**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, tillämpar de anpassade färgerna och sparar excel-filen.

**Den genererade filen med anpassade temafärger**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Använda temafärger**

Följande exempel tillämpar en cells förgrunds- och teckensnittsfärger baserat på färgtyperna för standardtema (i arbetsboken). Det sparar även excel-filen på disk.

Följande utdata genereras när koden exekveras.

**Temafärgerna tillämpas på D3-cellen i kalkylbladet** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Förhandsämnen**
- [Extrahera temadata från Excel-fil](/cells/sv/java/extract-theme-data-from-excel-file/)
