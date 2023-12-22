---
title: Excel-teman och färger
type: docs
weight: 100
url: /sv/net/excel-themes-and-colors/
description: C# kod för att använda Excel Color Scheme med Aspose.Cells for .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **Hur man applicerar och skapar färgschema i Excel**
Dokumentteman gör det enkelt att koordinera färger, teckensnitt och grafiska formateringseffekter av Excel-dokument och uppdatera dem snabbt.
Teman ger ett enhetligt utseende med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel, stilen Accent1, till exempel, ser annorlunda ut i Office- och Apex-teman. Ofta tillämpar du ett dokumenttema och ändrar det sedan till hur du vill ha det.

###  **Hur man använder ett färgschema i Excel**
1. Öppna Excel och gå till fliken "Sidlayout" i Excel-bandet.
1. Klicka på knappen "Färger" i avsnittet "Teman".
<br>
<img src="color.png" width=70% />
1. Välj en färgpalett som matchar dina krav eller håll muspekaren över ett schema för att se en liveförhandsvisning.

###  **Hur man skapar ett anpassat färgschema i Excel**
Du kan skapa din egen färguppsättning för att ge ditt dokument ett fräscht, unikt utseende eller följa din organisations varumärkesstandarder.

1. Öppna Excel och gå till fliken "Sidlayout" i Excel-bandet.
1. Klicka på knappen "Färger" i avsnittet "Teman".
1. Klicka på knappen "Anpassa färger...".
<br>
<img src="color2.png" width=70% />

1. dialogrutan "Skapa nya temafärger" kan du välja färger för varje element genom att klicka på färgrullgardinerna bredvid dem. Du kan välja färger från paletten eller definiera anpassade färger med alternativet "Fler färger".
<br>
<img src="color3.png" width=70% />
1. När du har valt alla önskade färger, ange ett namn för ditt anpassade färgschema i fältet "Namn".

1. Klicka på "Spara"-knappen för att spara ditt anpassade färgschema. Ditt anpassade färgschema kommer nu att vara tillgängligt i rullgardinsmenyn "Färger" för framtida användning.

##  **Hur man skapar och tillämpar färgschema på Aspose.Cells**
Aspose.Cells tillhandahåller funktioner för att anpassa teman och färger.

###  **Hur man skapar anpassat färgtema i Aspose.Cells**
Om temafärger används i filen behöver vi inte modifiera varje cell individuellt, vi behöver bara modifiera färgerna i temat.

Följande exempel visar hur du använder anpassade teman med dina önskade färger. Vi använder en exempelmallfil som skapats manuellt i Microsoft Excel 2007.

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, tillämpar de anpassade färgerna och sparar excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **Hur man applicerar temafärger i Aspose.Cells**

Följande exempel tillämpar en cells förgrunds- och teckensnittsfärger baserat på färgtyperna för standardtema (i arbetsboken). Det sparar även excel-filen på disk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **Hur man får och ställer in temafärger i Aspose.Cells**
 Nedan finns några metoder och egenskaper som implementerar temafärger.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Används för att ställa in förgrundsfärgen.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Används för att ställa in bakgrundsfärgen.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Används för att ställa in teckensnittsfärgen.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Används för att få en temafärg.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Används för att ställa in en temafärg.

Följande exempel visar hur du får och ställer in temafärger.

Följande exempel använder en mall XLSX-fil, hämtar färgerna för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **Förhandsämnen**
- [Extrahera temadata från Excel-fil](/cells/sv/net/extract-theme-data-from-excel-file/)
