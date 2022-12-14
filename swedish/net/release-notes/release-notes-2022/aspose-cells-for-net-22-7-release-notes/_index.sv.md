---
title: Aspose.Cells för .NET 22.7 Release Notes
type: docs
weight: 6
url: /sv/net/aspose-cells-for-net-22-7-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 22.7](https://www.nuget.org/packages/Aspose.Cells/22.7.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-51296| Gridweb hoppar hela tiden tillbaka till toppen när du försöker kopiera och klistra in|
|CELLSNET-51355|Och Range.Top, Left, Width, Höjd i poängenhet|
|CELLSNET-51367|Konvertera alla ark till en sida när du sparar som html.|
|CELLSNET-51486|Texten återgiven som små rutor|
|CELLSNET-51492|Standardteckensnitt används inte vid konvertering av XLSX till HTML|
|CELLSNET-51306|Pivottabellstilar har inte kopierats korrekt med den senaste versionen av Aspose.Cells för .NET|
|CELLSNET-51268|Problem med att COUNTIFS-formeln behandlar 0 felaktigt|
|CELLSNET-51297|Cell.GetPrecedents() tillhandahåller inte alla prejudikat när formeln refererar till definierat namn|
|CELLSNET-51399|Print_Titles med namnet intervall och MATCH-funktionen returnerar #NAME-fel|
|CELLSNET-51456|celler hoppar när gör ctrl+c ctrl+v när GridWeb-höjden är inställd på 100 %|
|CELLSNET-51457|snabbmenyn visas inte när höjden är inställd på 100 % efter vissa rader|
|CELLSNET-51471|valideringslistan visas inte i tom cell|
|CELLSNET-51469|Text i bilden saknas efter konvertering till pdf|
|CELLSNET-51476|Pilelementet blir förvrängt i bilden|
|CELLSNET-51001|Formobjektet på diagrammet är inte väl placerat|
|CELLSNET-51156|Konvertering av diagram till bild - Olika visning av diagram i utdatabilden|
|CELLSNET-51213|3D-cirkeldiagram inte korrekt renderat - Konvertering av diagram till bild|
|CELLSNET-51472|Sjökortsetiketter saknas i SVG när de är inställda på utsidan|
|CELLSNET-51491|Fel värden används i diagramserier vid rendering till bild eller HTML|
|CELLSNET-51525|Vattenfallsdiagram är annorlunda när det exporteras till HTML/PNG eller PDF|
|CELLSNET-51353|Att konvertera en XLSB-fil med DDE-länk till XLSM-fil ändrar DDE-applikationens position i länken|
|CELLSNET-51376|Sidstorlek ändras automatiskt från A4 ? Brev för ett ark|
|CELLSNET-51379| Extern länk av typen OLE i XLS-fil läses som av typen DDE|
|CELLSNET-51402|Innehållet flyttas innehållet från cellen när html-filen sparas|
|CELLSNET-51417|Länkar från form till ark i fil tas bort efter uppgradering från 22.5 till 22.6.1|
|CELLSNET-51418|En extern länk av typen xlPathMissing ändras till normal externLinkPath-typ i XLSB till XLSM-konvertering|
|CELLSNET-51420|Skillnader i dokumentegenskaperna i filen app.xml|
|CELLSNET-51427|Extern länk som innehåller specialtecknet "#" som inte är escaped av Aspose.Cells|
|CELLSNET-51482|Att kombinera ark från olika arbetsböcker resulterar i korrupta filer som kan krascha MS Excel|
|CELLSNET-51507|Talvärden från XLSX-fil läses som 0|
|CELLSNET-51280|Undantag vid lagring av ODS-fil (RB-60121)|
|CELLSNET-51483|Filinläsning misslyckas med undantaget "Källmatrisen var inte tillräckligt lång..."|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till metoden Cells.GetDependentsInCalculation(int,int,bool)**

Hämtar alla celler vars beräknade resultat beror på cellen som anges av rad och kolumn enligt aktuell beräkningskedja. För cellen som är tom och inte har instansierats i nuvarande cellmodell, kan användaren använda denna metod istället för Cell.GetDependentsInCalculation(bool) eftersom den senare måste instansiera cellobjektet till den aktuella cellmodellen först.

### **Ändrar cellens vänster/höger kant för Cell.GetStyle() när den intilliggande kolumnen är dold**

gamla versioner, om den intilliggande kolumnen är dold för en cell, kommer denna cells Vänster/Höger-kant inte att kontrolleras med den intilliggande cellen, så den returnerade gränsen kan skilja sig från vad som visas i ms excels dialogruta när den här cellens kant ställs in. Från 22.7 gör vi att den returnerade gränsen alltid är det faktiska värdet (vilket bör överensstämma med gränsen för dess intilliggande cell) för cellen för Cell.GetStyle(). Om användaren behöver det som visas för cellen i ms excel (när den intilliggande kolumnen är dold, kan den visade gränsen vara den av nästa synliga kolumn), kan användaren prova Cell.GetDisplayStyle().

### **Lägg till egenskaperna Range.Top, Range.Left, Range.Height och Range.Width.**

Hämtar intervallets position och storlek i poängenhet.

### **Ta bort klassen PowerQueryFormulaCollction och lägg till klassen PowerQueryFormulaCollection.**

Det är ett stavfel i den gamla klassen.

### **Lägg till egenskaperna HtmlSaveOptions.ExportPageFooters och HtmlSaveOptions.ExportPageHeaders.**

Anger om sidhuvuden och sidfötter exporteras när du sparar som en enda html-fil.

### **Lägger till egenskapen HtmlSaveOptions.ShowAllSheets.**

Anger om alla ark visas när du sparar som en enda html-fil.

### **Föråldrar egenskapen HtmlSaveOptions.ExportHeadings och lägger till egenskapen HtmlSaveOptions.ExportRowColumnHeadings.**

Använd HtmlSaveOptions.ExportRowColumnHeadings istället.

### **Föråldrade Chart.ToImage(string, ImageFormat) och lägg till Chart.ToImage(string, ImageType)**

Använd Chart.ToImage(string, ImageType) istället.

### **Föråldrade Chart.ToImage(Stream, ImageFormat) och lägg till Chart.ToImage(Stream, ImageType)**

Använd Chart.ToImage(Stream, ImageType) istället.

### **Föråldrar Shape.ToImage(Stream, ImageFormat) och lägg till Shape.ToImage(Stream, ImageType)**

Använd Shape.ToImage(Stream, ImageType) istället.
