---
title: Excel teman och färger
type: docs
weight: 130
url: /sv/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

Teman ger en enhetlig utformning med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel ser Accent1-stilen annorlunda ut i Office och Apex-temana. Ofta tillämpar du ett dokumenttema och ändrar det sedan efter dina behov.

**Tillämpa teman i Microsoft Excel**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Få och ställ in temafärger**

Aspose.Cells API:er erbjuder funktioner för anpassning av teman och färger. Nedan finns några metoder och egenskaper som implementerar tema färger.

- Egenskapen Style.ForegroundThemeColor kan användas för att ställa in förgrundsfärgen.
- Egenskapen Style.BackgroundThemeColor kan användas för att ställa in bakgrundsfärgen.
- Egenskapen Font.ThemeColor kan användas för att ställa in fontfärgen.
- Metoden Workbook.getThemeColor kan användas för att hämta en tema färg.
- Metoden Workbook.setThemeColor kan användas för att ställa in en tema färg.

Följande exempel visar hur man hämtar och ställer in tema färger.

Följande exempel använder en mall XLSX-fil, hämtar färgerna för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Anpassning av teman**

Följande exempel visar hur man applicerar anpassade teman med önskade färger. Exemplet använder en provmallfil som skapats manuellt i Microsoft Excel 2007.

**Mallen CustomThemeColor.xlsx-fil**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, applicerar de anpassade färgerna och sparar excelfilen.

**Den genererade filen med anpassade tema färger**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Användning av tema färger**

Det följande exemplet applicerar en cells förgrund och fontfärger baserat på standardtema (av arbetsbok) färgtyper. Det sparar också excelfilen på disken.

Följande utdata genereras vid körning av koden.

**Tema färger applicerade på cellen D3 i arbetsbladet** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Fortsatta ämnen**
- [Extrahera temadata från Excel-fil](/cells/sv/java/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="java" >}}
