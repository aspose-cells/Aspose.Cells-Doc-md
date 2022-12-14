---
title: Aspose.Cells för .NET 18.7 Release Notes
type: docs
weight: 60
url: /sv/net/aspose-cells-for-net-18-7-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 18.7](https://www.nuget.org/packages/Aspose.Cells/18.7.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46046|Runda bilder blir kvadratiska bilder i den utgående PDF-filen|Ny funktion|
|CELLSNET-43538|Stöd Pivot Table Slicers|Ny funktion|
|CELLSNET-41946|Handtagsskärare och pivotbord|Ny funktion|
|CELLSNET-46163|Stöd för kryptering och dekryptering av ODS-fil|Ny funktion|
|CELLSNET-46186|Använder List<dynamic> eller Lista<ExpandoObject> som DataSource för att importera data till kalkylblad|Ny funktion|
|CELLSNET-46185|Lägg till egenskaperna WorkbookSettings.MaxRow och WorkbookSettings.MaxColumn|Ny funktion|
|CELLSNET-46205|Lägg till egenskapen WriteProtection.Author för att uppdatera författaren|Förbättring|
|CELLSNET-41946|Pivottabellsfilter fungerar inte efter laddning och spara|Insekt|
|CELLSNET-45921|Cirkel blir kvadratisk i Excel till PDF-rendering|Insekt|
|CELLSNET-46217|#NUM!' inuti "FV(NPER())"-formeln orsakar utvärderingsfel|Insekt|
|CELLSNET-46214|Undantag "Ogiltig BIFF8-fil" när en XLS-fil laddas|Insekt|
|CELLSNET-46212|Undantag vid laddning av en XLSX-fil|Insekt|
|CELLSNET-46193|Validering fungerar inte i XLS-format men det fungerar bra i XLSX-format|Insekt|
|CELLSNET-46189|Utdata-PDF-dokumentet är inte detsamma som MS Excel-utdata|Insekt|
|CELLSNET-46187|Dubbel understruken längd är inte korrekt - Excel till PDF-konvertering|Insekt|
|CELLSNET-46213|OLE-objekt trasiga under lagring till XLSB|Insekt|
|CELLSNET-46210|Det fungerar inte att skapa kommentarer med HtmlNote-egenskapen|Insekt|
|CELLSNET-46198|Tom PDF skapad vid konvertering av XLSX till PDF|Insekt|
|CELLSNET-46196|Diagramhöjden ändras i utdatafilen när arbetsböcker kombineras|Insekt|
|CELLSNET-46195|Konvertering av bifogad XLSX till PDF ger undantag|Insekt|
|CELLSNET-46192|Konvertering av en XLSX-fil med dde till XLS kommer att uppmanas med skyddad vy|Insekt|
|CELLSNET-46180|Formateringsproblem när storleken på ListObject/Table ändras|Insekt|
|CELLSNET-46216|Undantag vid laddning av XLS-fil|Undantag|
|CELLSNET-46207|Undantag för index utanför intervallet i metoden SheetRender.ToImage|Undantag|
|CELLSNET-46206|Undantag "Ogiltiga parametrar för funktion om fel..." när en Excel-fil laddas|Undantag|
|CELLSNET-46199|Ogiltigt undantag för PatternType-strängvärde när en fil laddas|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till enum StyleFlag.Alignments**
Representerar alla inställningar för justering.
#### **Lägger till egenskaperna WorkbookSettings.MaxRow och WorkbookSettings.MaxColumn**
Hämtar det maximala rad- och kolumnindexet för arbetsboken.
#### **Lägger till egenskapen WriteProtection.Author**
Får och ställer in författaren till skrivskyddet.
