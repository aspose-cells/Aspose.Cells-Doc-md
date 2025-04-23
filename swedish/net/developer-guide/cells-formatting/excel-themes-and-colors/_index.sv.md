---
title: Excel teman och färger
type: docs
weight: 100
url: /sv/net/excel-themes-and-colors/
description: C# kod för att använda Excel färgschema med Aspose.Cells for .NET API
keywords: C# för att skapa och tillämpa färgscheman, c# programmatiskt skapa ett anpassat färgschema, programmatiskt hur man tillämpar ett anpassat färgschema, c# hur man använder färgschema i excel
---

## **Hur man tillämpar och skapar färgschema i Excel**
Dokumentteman gör det enkelt att koordinera färger, teckensnitt och grafisk formateringseffekter för Excel-dokument och uppdatera dem snabbt. 
Teman ger en enhetlig look med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel ser Accent1-stilen annorlunda ut i Office och Apex-temana. Ofta tillämpar du ett dokumenttema och ändrar det sedan efter hur du vill ha det.

### **Hur man tillämpar ett färgschema i Excel**
1. Öppna Excel och gå till fliken "Sidlayout" i Excel-ribbonen.
1. Klicka på knappen "Färger" i avsnittet "Teman".
<br>
<img src="color.png" width=70% />
1. Välj en färgpalett som matchar dina krav eller sväva över en schema för att se en förhandsgranskning i realtid.

### **Hur man skapar en anpassad färgpalett i Excel**
Du kan skapa din egen färguppsättning för att ge ditt dokument en fräsch, unik look eller följa din organisations varumärkesstandard.

1. Öppna Excel och gå till fliken "Sidlayout" i Excel-ribbonen.
1. Klicka på knappen "Färger" i avsnittet "Teman".
1. Klicka på knappen "Anpassa färger...".
<br>
<img src="color2.png" width=70% />

1. I dialogrutan "Skapa nya temafärger" kan du välja färger för varje element genom att klicka på färgnedtagningarna bredvid dem. Du kan välja färger från paletten eller definiera anpassade färger med hjälp av alternativet "Fler färger".
<br>
<img src="color3.png" width=70% />
1. Efter att ha valt alla önskade färger, ange ett namn för din anpassade färgpalett i fältet "Namn".

1. Klicka på knappen "Spara" för att spara din anpassade färgpalett. Din anpassade färgpalett kommer nu att finnas tillgänglig i rullgardinsmenyn "Färger" för framtida användning.

## **Hur man skapar och tillämpar färgpalett i Aspose.Cells**
Aspose.Cells ger funktioner för anpassning av teman och färger.

### **Hur man skapar anpassat färgtema i Aspose.Cells**
Om färgteman används i filen behöver vi inte modifiera varje cell individuellt, vi behöver bara ändra färgerna i temat.

Nedan följer ett exempel på hur man tillämpar anpassade teman med önskade färger. Vi använder en provmall manuellt skapad i Microsoft Excel 2007.

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, applicerar de anpassade färgerna och sparar excelfilen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

### **Hur man tillämpar temafärger i Aspose.Cells**

Det följande exemplet applicerar en cells förgrund och fontfärger baserat på standardtema (av arbetsbok) färgtyper. Det sparar också excelfilen på disken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

### **Hur man får och ställer in temafärger i Aspose.Cells**
 Nedan följer några metoder och egenskaper som implementerar temafärger.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Används för att ställa in förgrundsfärgen.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Används för att ställa in bakgrundsfärgen.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Används för att ställa in teckensnittsfärgen.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Används för att hämta ett tema i färg.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Används för att ställa in ett tema i färg.

Följande exempel visar hur man hämtar och ställer in tema färger.

Följande exempel använder en mall XLSX-fil, hämtar färgerna för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

## **Fortsatta ämnen**
- [Extrahera temadata från Excel-fil](/cells/sv/net/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="csharp" >}}
