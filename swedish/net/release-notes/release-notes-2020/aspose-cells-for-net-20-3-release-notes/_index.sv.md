---
title: Aspose.Cells for .NET 20.3 Release Notes
type: docs
weight: 50
url: /sv/net/aspose-cells-for-net-20-3-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.3](https://www.nuget.org/packages/Aspose.Cells/20.3.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47130|Stöd för FLOOR.MATH(-555,5,1)|Ny funktion|
|CELLSNET-47168|Stöd för FILTER-funktion|Ny funktion|
|CELLSNET-47204|Få ett unikt kalkylblads-id|Ny funktion|
|CELLSNET-47229|Stöd för att ställa chart.series.dataLables.TextDirection till vertikal|Ny funktion|
|CELLSNET-47092|Gör ikoner tillgängliga för IStreamProvider som vanliga bilder samtidigt som du sparar dokumentet i HTML|Förbättring|
|CELLSNET-47094|Minska flimmer i GridDesktop för smidig storleksändring|Förbättring|
|CELLSNET-47173|Särskilj dolda/mycket dolda ark i Aspose.Cells.GridDesktop|Förbättring|
|CELLSNET-47101|Förbättra prestandan för att spara villkorlig formatering och validering med hela rader.|Förbättring|
|CELLSNET-47178|Indrag förlorades när en tabell skapades och konverterades till HTML|Insekt|
|CELLSNET-47199|Skillnaden i beräkningen för namngivet intervall när CreateCalcChain ställs in på sant och falskt|Insekt|
|CELLSNET-47077|Kunde inte tillämpa gränser på cellerna (med data) vid import av en Excel-fil till GridDesktop|Insekt|
|CELLSNET-47172|Problem med att tillämpa villkorlig formatering|Insekt|
|CELLSNET-47177|ParetoLine-diagramseriens namn och linje renderade inte till bilden|Insekt|
|CELLSNET-47191|Skillnaden mellan diagram och bild|Insekt|
|CELLSNET-47202|Förklaringsposter överlappas i diagrammets utdatabild|Insekt|
|CELLSNET-47167|Fel antal synliga länkar|Insekt|
|CELLSNET-47184|BIFF5 med kyrilliskt innehåll har konverterats felaktigt till XLSX|Insekt|
|CELLSNET-47205|Range.ApplyStyle() på kolumnområdet ökade storleken på arbetsboksfilen kraftigt|Insekt|
|CELLSNET-47210|Det rika formaterade strängvärdet för en cell är tomt i Apple Numbers'09|Insekt|
|CELLSNET-47213|Kopiera ark till en annan arbetsbok - dolda celler (rader) försvinner|Insekt|
|CELLSNETCORE-53|Datapunkt på Excel-diagramlinje tas bort efter konvertering till PDF|Insekt|
|CELLSNET-47212|NullReferenceException när du sparar viss XLSM till XLS|Undantag|
|CELLSNET-47222|Aspose.Cells 20.2: Undantag vid konvertering av viss XLSB-fil till Excel97To2003|Undantag|
|CELLSNET-47226|Aspose.Cells 20.2: Undantag vid försök att ta bort tomma kolumner|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Ändra beteende för formateringsfunktioner för vissa användarspecificerade CultureInfos.(ENDAST .NET)**
 I gamla versioner kan vår formateringsmotor ändra vissa egenskaper hos vissa speciella kulturer för att få det generella formaterade resultatet. Till exempel, för de flesta situationer bör JapaneseCalendar användas för att formatera datum-tid-värden, så i gamla versioner får vi alltid CultureInfo av "ja-JP" att använda JapaneseCalendar för formatering. Det är dock inte alltid avsett för användare när de anger sin anpassade CultureInfo av API:er, som WorkbookSettings.CultureInfo eller CustomImplementationFactory.CreateCultureInfo(). Så från 20.3 använder vi egenskapen CultureInfo.UseUserOverride för att bestämma om egenskaperna ska ändras automatiskt för formatering. För den angivna CultureInfo, om den här egenskapen är**Sann** , då tar vi det som att användaren har åsidosatt alla nödvändiga egenskaper, så vi kommer inte att ändra det längre för formatering. Om denna egenskap är**falsk**, då kan vi ändra andra egenskaper för den automatiskt om det behövs.
#### **Lägg till egenskapen LoadFilter.SheetsInLoadingOrder.**
Användare kan åsidosätta den här egenskapen för att ange arken och ordningen som ska laddas när de importerar arbetsböcker från mallfilen.
#### **Tar bort föråldrad TickLabels.Background-egenskap**
Använd egenskapen TickLabels.BackgroundMode istället.
#### **Föråldrar egenskapen TickLabels.TextDirection och lägger till egenskapen TickLabels.ReadingOrder**
Använd egenskapen TickLabels.ReadingOrder istället.
#### **Föråldrade TickLabels.DirectionTypeproperty och lägger till enum ChartTextDirectionType**
Representerar textens riktning.
#### **Lägger till metoden Shape.RemoveActiveXControl().**
Tar bort ActiveX-data från formen.
#### **Lägger till egenskapen ThreadedComment.CreatedTime.**
Hämtar och ställer in skapad tid för trådade kommentarer.
#### **Lägger till egenskapen Worksheet.UniqueId.**
Hämtar och ställer in det unika ID:t för kalkylbladet.
#### **Lägger till enum IconSetType.ColorSmilies3 och IconSetType.Smilies3.**
Representerar 3smiles-ikonuppsättningens villkorliga formatering. Endast för .ods file.s
#### **Lägger till enum TimePeriodType.LastYear,TimePeriodType.NextYear och ThisYear.**
Representerar det senaste året, nästa år och i år villkorlig formatering. Endast för .ods-filer.
#### **Lägger till metoden WorksheetCollection.RefreshPivotTables().**
Uppdaterar alla pivottabeller i filen.
