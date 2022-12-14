---
title: Aspose.Cells för .NET 21.6 Release Notes
type: docs
weight: 7
url: /sv/net/aspose-cells-for-net-21-6-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 21.6](https://www.nuget.org/packages/Aspose.Cells/21.6.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-48104|Få värdet av SlicerCacheItem i samlingen Slicer.SlicerCache.SlicerCacheItems|Ny funktion|
|CELLSNET-48121|Stöd anpassad stil av Slicer i Xlsb|Ny funktion|
|CELLSNET-48053|Ange användardefinierade formler som matrisformler och ange samtidigt värden som beräknade resultat för dessa formler|Ny funktion|
|CELLSNET-43532|Möjlighet att bädda in typsnitten med ANSI-kodning|Ny funktion|
|CELLSNET-48042|Hämtade formaterade cellvärden är felaktiga i Excel-kalkylbladet|Förbättring|
|CELLSNET-48078|Djup kopia av arbetsbok efter beräkning med CreateCalcChain-inställning|Förbättring|
|CELLSNET-48079| Hur man kontrollerar om ett kalkylblad är tomt|Förbättring|
|CELLSNET-48135| Problem med skyddad arbetsbok (med lösenord) genererad av Aspose.Cells|Förbättring|
|CELLSNET-48050| cpu hänger på öppen arbetsbok|Prestanda|
|CELLSNET-48063|Tme kostnad när du ringer api Cells.GetRowRawHeightPoint|Prestanda|
|CELLSNET-48046|Formens textförskjutning är felaktig (pil:quad).|Insekt|
|CELLSNET-48064|Textarrangemanget för standardteckensnittet i textrutan är inte korrekt|Insekt|
|CELLSNET-48088|Den överlappande delen av kurvan är avskuren.|Insekt|
|CELLSNET-48089|Vänster och höger kurvor reduceras|Insekt|
|CELLSNET-48060|Fel när funktionen RemoveUnusedStyles användes med anpassade stilar|Insekt|
|CELLSNET-48080|Pivottabell kan inte använda "值" eller "Värden" som kolumnnamn när du skapar pivottabell|Insekt|
|CELLSNET-48085| Dold kolumnrubrik återges|Insekt|
|CELLSNET-48105|Textboxens placering ändras när Excel konverteras till HTML|Insekt|
|CELLSNET-48048| Undantag när du sparar XLSX med kommentarer till PDF-format|Insekt|
|CELLSNET-48082|Om du lägger till fler än 30 rader med ImportCustomObjects genereras en skadad fil|Insekt|
|CELLSNET-48086|Namngivna intervall skapades inte korrekt i 21.5 men fungerade 21.4|Insekt|
|CELLSNET-48118|Stöd för att uppdatera dynamiska arrayformler enligt det uppdaterade utspillda intervallet|Insekt|
|CELLSNET-48081|Bilden visas inte i GridWeb|Insekt|
|CELLSNET-48117|Lägg till GridCell.GetValidation() för GridDesktop|Insekt|
|CELLSNET-47627|Problem vid åtkomst/ändring av X-axeln i ett Excel-diagram med Aspose.Cells|Insekt|
|CELLSNET-48041|Det extraherade diagrammet är förvrängt i diagram till bild/PDF-rendering|Insekt|
|CELLSNET-48049|Olika axelavstånd vid konvertering från xlsx-arbetsbok till emf|Insekt|
|CELLSNET-48101|Chinse-tecken visas som Rectangle Linux Docker|Insekt|
|CELLSNET-48061|PowerQueries försvinner efter frågebyte|Insekt|
|CELLSNET-48065|Återsparad fil med ett specifikt namngivet intervallvärde gör att Excel skadas|Insekt|
|CELLSNET-48067|SetChartDataRange kände inte igen sammanslagna celler|Insekt|
|CELLSNET-48072|Läs tomt diagram kommer att få en felaktig diagramtyp|Insekt|
|CELLSNET-48133|Fel uppstod av MS Excel när du öppnade XLSX-filen|Insekt|
|CELLSNET-48045|Ett undantag görs när svg konverteras till bild|Undantag|
|CELLSNET-48062|Undantag höjdes vid konvertering av XLS till XLSX|Undantag|
|CELLSNET-48074|Värdet kan inte vara null när Apple-nummerfilen öppnas|Undantag|
|


## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Ändrar beteendet för egenskapen Cell.IsErrorValue.**

I gamla versioner gäller den här egenskapen endast formelceller. För att det ska överensstämma med andra egenskaper kontrollerar vi från 21.6 även icke-formelceller och om dess värde är felvärde returnerar vi också sant. Användaren kan kontrollera Cell.IsFormula-egenskapen först om han bara behöver kontrollera felvärdet för formelceller.

### **Ändrar beteendet för Cell.Value-egenskapen.**

I gamla versioner returnerar den här egenskapen alltid DateTime-objekt om cellen är formaterad som datumtid och dess värde är numeriskt. Från 21.6 returnerar den här egenskapen själva det numeriska värdet om det överskrider det maximala giltiga DateTime-värdet. Med denna ändring överensstämmer det returnerade objektet med det som visas i formelfältet i ms excel.

### **Lägger till egenskapen Cell.IsNumericValue.**

Ger ett bekvämt och effektivt sätt för användaren att kontrollera om en cells värde är numeriskt värde (int, double, datetime).

### **Lägger till överbelastade metoder för Cell.SetSharedFormula()/SetArrayFormula()/SetDynamicArrayFormula().**

Stöd för att ställa in matrisformler och delade formler med fördefinierade värden.

### **Lägger till enum PdfFontEncoding.**

Representerar pdf-inbäddad teckensnittskodning.

### **Lägger till egenskapen PdfSaveOptions.FontEncoding.**

Hämtar eller ställer in inbäddad teckensnittskodning i pdf.

### **Lägger till egenskapen SlicerCacheItem.Value.**

Returnerar etiketttexten för utsnittsobjektet. Skrivskyddad.

### **Lägger till metoden GlobalizationSettings.GetProtectionNameOfPivotTable().**

Hämtar skyddsnamnet i pivottabellen.

### **Lägger till metoden FileFormatUtil.FileFormatToSaveFormat.**

Konverterar filformat till sparformat.

