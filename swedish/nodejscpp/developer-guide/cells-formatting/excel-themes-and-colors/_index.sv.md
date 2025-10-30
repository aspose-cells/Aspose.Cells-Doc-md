---  
title: Excel teman och färger
linktitle: Excel teman och färger  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/excel-themes-and-colors/  
description: Lär dig hur man använder anpassade färgscheman med Aspose.Cells for Node.js via C++.  
keywords: Node.js Skapa och tillämpa färgscheman, Skapa ett anpassat färgschema i Node.js programmässigt, hur man tillämpar ett anpassat färgschema Node.js, Hur man använder färgschema i Excel med Node.js  
---  

## **Hur man tillämpar och skapar färgschema i Excel**  
Dokumentteman gör det enkelt att koordinera färger, teckensnitt och grafisk formateringseffekter för Excel-dokument och uppdatera dem snabbt.  
Teman ger ett enhetligt utseende med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel ser Accent1-stilen olika ut i Office- och Apex-teman. Ofta tillämpar du ett dokumenttema och ändrar det sedan som du vill ha det.  

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
Om temafärger används i filen behöver vi inte ändra varje cell individuellt; vi behöver bara ändra färgerna i temat.  

Nedan följer ett exempel på hur man tillämpar anpassade teman med önskade färger. Vi använder en provmall manuellt skapad i Microsoft Excel 2007.  

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, tillämpar de anpassade färgerna och sparar Excel-filen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **Hur man tillämpar temafärger i Aspose.Cells**  
Följande exempel tillämpar en cells förgrunds- och teckensfärger baserat på standardtema (arbetsbokens) färgtyper. Det sparar också Excel-filen till disk.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **Hur man får och ställer in temafärger i Aspose.Cells**  
Nedan följer några metoder och egenskaper som implementerar temafärger.  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-): Används för att sätta förgrundsfärgen.  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-): Används för att sätta bakgrundsfärgen.  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-): Används för att sätta teckenfärgen.  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-): Används för att få en temafärg.  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-): Används för att sätta en temafärg.  

Följande exempel visar hur man hämtar och ställer in tema färger.  

Följande exempel använder en mall XLSX-fil, hämtar färger för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **Fortsatta ämnen**  
- [Extrahera temadata från Excel-fil](/cells/sv/nodejs-cpp/extract-theme-data-from-excel-file/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
