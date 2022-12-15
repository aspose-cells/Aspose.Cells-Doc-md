---
title: Aspose.Cells for .NET 18.3 Release Notes
type: docs
weight: 100
url: /sv/net/aspose-cells-for-net-18-3-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 18.3](https://www.nuget.org/packages/Aspose.Cells/18.3.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42655|Gruppera pivotfält i pivottabellen|Ny funktion|
|CELLSNET-45960|Ändra punkten från NumPad till decimalavgränsare (',') - Aspose.Cells.GridWeb|Ny funktion|
|CELLSNET-45966|Orsak till undantag under bakåtriktad HTML-till-Cells-konvertering|Förbättring|
|CELLSNET-45976|Fel vid öppning av ODS-fil på grund av att möjligen olika ramverk håller olika precision för flytvärden|Förbättring|
|CELLSNET-45981|Lägg till egenskapen i StyleFlag för att ställas in på false för att inte åsidosätta QuotePrefix-värdet|Förbättring|
|CELLSNET-45957|Stöd att behålla kartdiagrammet i mallfilen|Förbättring|
|CELLSNET-45941|ActiveX-kontrollen blir bild när du kopierar ark från en arbetsbok till en annan arbetsbok|Förbättring|
|CELLSNET-45928|Datavalidering - GridWeb bör visa en dialogruta med ett felmeddelande|Förbättring|
|CELLSNET-45935|Workbook.CalculateFormula hänger oändligt när du ställer in ett specifikt värde för cellen|Prestanda|
|CELLSNET-45920|Understrykning av texten "KEY DRIVERS:" är bruten i utdatabilden|Insekt|
|CELLSNET-45939|Förutom bruten understrykning är texten också feljusterad som visas på den medföljande skärmdumpen|Insekt|
|CELLSNET-45890|Vissa former återges inte helt eftersom några delar saknas|Insekt|
|CELLSNET-45878|Utdata Excel-fil av ny version kraschar Microsoft Excel 2016|Insekt|
|CELLSNET-43360|Stilproblem med HTML till Excel-rendering|Insekt|
|CELLSNET-45979|VLOOKUPS formelberäkning fungerar inte korrekt|Insekt|
|CELLSNET-45949|Cell textjustering (med blandade teckensnitt) ändras i den konverterade bilden|Insekt|
|CELLSNET-45940|Villkorlig formatering tillämpas inte vid konvertering av Excel-fil till PDF-filformat|Insekt|
|CELLSNET-45896|Oönskade kanter visas runt bilden när Excel-filen sparas till PDF|Insekt|
|CELLSNET-45942|Cellreferensen för dataetiketten försvinner efter öppning/spara|Insekt|
|CELLSNET-45923|Sista axeletikett, dvs. 17 juni, saknas i diagrambilden|Insekt|
|CELLSNET-45911|Dålig position och linje i återgivningen av marknadsriskdiagram|Insekt|
|CELLSNET-45908|Dålig position i diagramrenderingen|Insekt|
|CELLSNET-45906|Saknar etikett i diagramrendering|Insekt|
|CELLSNET-45884|Smart Art-diagram på flik - konernas kanter är ojämna i PDF-filformatet|Insekt|
|CELLSNET-45989|Dialogrutor sparas inte korrekt i XLSM-filer|Insekt|
|CELLSNET-45977|Worksheet.Protect(ProtectionType.Objects) fungerar inte för XLS-filer|Insekt|
|CELLSNET-45946|Hyperlänk med bindestreck i schemaavbrott under spara|Insekt|
|CELLSNET-45944|Metoden ConvertToRange() bryter namnen i Namnhanteraren|Insekt|
|CELLSNET-45905|Excel hänger sig när man försöker öppna utdataarbetsboken, dvs "_function plot 2D.xlsx" två gånger|Insekt|
|CELLSNET-45904|Excel hänger sig när du försöker öppna utdataarbetsboken två gånger|Insekt|
|CELLSNET-45959|Aspose.Cells.GridWeb kultur datum problem|Insekt|
|CELLSNET-45929|Kolumngruppen fungerar inte i GridWeb|Insekt|
|CELLSNET-45926|Flikar är inte synliga eller delvis synliga på GridWeb i IE 11|Insekt|
|CELLSNET-45925|Offsetproblem i GridWeb-arbetsbladet på IE 11|Insekt|
|CELLSNET-45918|"<br>" är inbäddad i cellen vid cellbyte i Aspose.Cells.GridWeb|Insekt|
|CELLSNET-45914|Formel försvinner efter validering/uppdatering av värdet i cellen|Insekt|
|CELLSNET-45912|Fel efter validering av en cell enligt valideringsmetoden|Insekt|
|CELLSNET-45894|Kontroller fungerar inte korrekt förmodligen på grund av att två GridWebs laddas|Insekt|
|CELLSNET-45987|Undantag för att öppna en XLSX-fil via Aspose.Cells API:er|Undantag|
|CELLSNET-45951|Ogiltig formel ger undantag vid start|Undantag|
|CELLSNET-45950|Undantag vid laddning av en ODS-fil|Undantag|
|CELLSNET-45947|Undantag: Ogiltig formel:"=ark3!#ref!" när du öppnar en XLSX-fil|Undantag|
|CELLSNET-45938|System.IndexOutOfRangeException vid öppning av XLSB-filer|Undantag|
|CELLSNET-45937|System.FormatException inträffar när XLSX-fil öppnas|Undantag|
|CELLSNET-45903|Att ladda XLSX orsakar StackOverflowException|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen HtmlSaveOptions.ExportSimilarBorderStyle**
Anger om liknande kantstil exporteras när kantstilen inte stöds av webbläsare. Om du vill importera HTML- eller MHT-filen till Excel, behåll standardvärdet. Standardvärdet är falskt.
#### **Lägger till egenskapen Axis.AxisLabels**
Hämtar beteckningarna för axeln efter anrop av metoden Chart.Calculate().
#### **Lägger till ny enumtyp: GridValidationType.CustomServerFunction**
Representerar anpassad funktionsvalidering på serversidan.
#### **Lägger till ChartType.Map enum**
Representerar kartdiagrammet.
#### **Lägger till egenskapen OleObject.Label**
Hämtar och ställer in visningsetiketten för det länkade Ole-objektet.
#### **Lägger till egenskapen BuiltInDocumentPropertyCollection.DocumentVersion**
Representerar versionen av filen.
#### **Lägger till StyleFlag.QuotePrefix enum**
Anger om stilens QuotePrefix-egenskap tillämpas.
#### **Lägger till DialogBox-klass**
Representerar dialogrutan.
#### **Lägger till egenskapen PdfSaveOptions.DrawObjectEventHandler**
Hämtar och ställer in DrawObjectEventHandler för att hämta DrawObject och Bound under rendering.
#### **Lägger till egenskapen DrawObject.Shape**
Får den relaterade formen under rendering.
