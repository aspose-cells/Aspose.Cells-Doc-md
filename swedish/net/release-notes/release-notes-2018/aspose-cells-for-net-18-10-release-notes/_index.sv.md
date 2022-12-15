---
title: Aspose.Cells for .NET 18.10 Release Notes
type: docs
weight: 30
url: /sv/net/aspose-cells-for-net-18-10-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 18.10](https://www.nuget.org/packages/Aspose.Cells/18.10.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46311|Få anslutningspunkter från former|Ny funktion|
|CELLSNET-46194|Ändra kolumnernas fasta storleksbredd (dvs. pt/px) till skalbar enhet som "em" eller "procent"|Förbättring|
|CELLSNET-46383|Problem med bildkällan när du renderar Excel till HTML-filformat|Insekt|
|CELLSNET-46367|Teckenstorleken ändrades från 6,5 till 6 när XLSX konverterades till HTML|Insekt|
|CELLSNET-46353| Känn igen tomma taggar som<td /> medan du konverterar HTML till MS Excel-filformat|Insekt|
|CELLSNET-46341|Delsumma saknas när rader kollapsade efter uppdatering|Insekt|
|CELLSNET-46330|Utfärda i nummerfält när du anropar Worksheet.AutoFitColumns()|Insekt|
|CELLSNET-42681|XLSB-filen blir korrupt när den öppnas och sparas|Insekt|
|CELLSNET-46382|CSV-import skapar felaktig formatering med PreferredParsers|Insekt|
|CELLSNET-46338|"_xll" bifogas framför formelnamnet|Insekt|
|CELLSNET-46334|Namngiven intervallformel ("=GET.CELL") skapad inte korrekt i tysk språk|Insekt|
|CELLSNET-46321|Escape-tecken visas som det är i PDF|Insekt|
|CELLSNET-46376|PDF-utdatasidstorlek (och marginaler) matchar inte MS Excel-utdata|Insekt|
|CELLSNET-46373|Bildens höjd i rubriken trunkeras tillsammans med trasig layout under XLSM->PDF-konvertering|Insekt|
|CELLSNET-46349|Bilden upprepas inte korrekt när utskriftstitlar är inställda för rader och kolumner|Insekt|
|CELLSNET-46358|Att rendera bild från ett enkelt diagram tar alla resurser och väcker sedan undantag|Insekt|
|CELLSNET-46343|Att komma åt synlighetsegenskaper ändrade synligheten för diagrammet i den återsparade utdata|Insekt|
|CELLSNET-46390|Egenskapen SourceFullName för OLE Object är tom vid åtkomst i XLSB|Insekt|
|CELLSNET-46385|Huvudbilden/formen återges inte korrekt när en XLSX-fil sparas på nytt|Insekt|
|CELLSNET-46384|Skillnad i OLE-objekt före och efter att XLSB-filen har sparats|Insekt|
|CELLSNET-46378|Fonetisk guide saknas efter kopiering och spara|Insekt|
|CELLSNET-46375|Ändra storlek på tabeller ändrar format på celler|Insekt|
|CELLSNET-46374|Fel upptäckt av cellförgrund och bakgrundsfärg|Insekt|
|CELLSNET-46369|Autopassning sker automatiskt för de dolda raderna när rader automatiskt filtreras|Insekt|
|CELLSNET-46368|Anpassat schema 'm-files://...' konverteras i dokumentspara-operationen|Insekt|
|CELLSNET-46357|XLSB-filer kan inte öppnas med andra LoadDataFilterOption än LoadDataFilterOption.All|Insekt|
|CELLSNET-46356|Formel saknar enstaka citat|Insekt|
|CELLSNET-46351|LoadDataFilterOptions.SheetSettings fungerar inte för XLSB-filer|Insekt|
|CELLSNET-46350|Vyn ändras till skyddad vid konvertering av XLS -> XLSM -> XLS|Insekt|
|CELLSNET-46347|XLSX-filen är korrupt efter konvertering från en XML-fil (SpreadsheetML).|Insekt|
|CELLSNET-46344|Smart Marker utvärderar inte ISBLANK korrekt|Insekt|
|CELLSNET-46319|FilterOperatorType.Innehåller saknas från API|Insekt|
|CELLSNET-46354|Undantag inträffade när en Excel-fil laddades|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen HtmlSaveOptions.WidthScalable**
Anger om skalbar enhet används för att beskriva kolumnbredden vid export av fil till HTML. Standardvärdet är falskt.
#### **Lägger till egenskapen WorkbookDesigner.UpdateEmptyStringAsNull**
Anger om det tomma strängvärdet bearbetas som null.
#### **Uppdaterar det returnerade värdet för metoden DocumentProperty.ToDateTime(), egenskaperna BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted och BuiltInDocumentPropertyCollection.LastSavedTime.**
Returnerar tiden i lokal tidszon.
#### **Kräver starkare begränsningar för användarens input för FormatCondition.Formula1/Formula2**
Den vanliga inmatningssträngen kan inte bestämmas om den ska referera till en namnreferens eller om det bara är ett konstant strängvärde. Så nu kräver vi att formeln måste börja med '='-tecken. För vanligt strängvärde "sss", använd format som "=\"sss\"".
