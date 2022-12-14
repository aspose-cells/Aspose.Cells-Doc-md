---
title: Aspose.Cells för .NET 18.2 Release Notes
type: docs
weight: 110
url: /sv/net/aspose-cells-for-net-18-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 18.2](https://www.nuget.org/packages/Aspose.Cells/18.2.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-45889|Konvertera cellinnehåll till hyperlänk - alternativet ImportTableOptions.IsFormulas|Ny funktion|
|CELLSNET-45886|Ställ in kommentarens marginaler|Ny funktion|
|CELLSNET-45855|Tillhandahåll WorkbookSetting.StreamProvider för att kontrollera externa resurser|Ny funktion|
|CELLSNET-45845|Extern stilmall som inte stöds under konvertering tur och retur|Förbättring|
|CELLSNET-45888|DDE-länk finns inte i Worksheets.ExternalLinks|Förbättring|
|CELLSNET-45893|Aspose.Cells.GridWeb skriver inte in text som Microsoft Excel när radbrytning är aktiverat|Förbättring|
|CELLSNET-45833|Bildegenskaper (Titel och Ämne) går förlorade i form till bildkonvertering|Insekt|
|CELLSNET-45822|Inverterade tecken i etiketter vid konvertering av Excel till PDF|Insekt|
|CELLSNET-45776|Vissa kolumndata expanderas/visas inte helt när en MHtml-fil sparas i Excel-filformat|Insekt|
|CELLSNET-44829|Utdata HTML matchar inte med Microsoft Excel|Insekt|
|CELLSNET-44319|Pivottabellens filtervärde behålls inte vid uppdatering|Insekt|
|CELLSNET-45887|#VÄRDE!' fel för ArrayFormulas beräkning|Insekt|
|CELLSNET-45883|3D-cirkeldiagram - återges inte bra i utdata-PDF|Insekt|
|CELLSNET-45881|Att öppna och spara indatafilen i Excel orsakar varning för Red Protected View i MS Excel|Insekt|
|CELLSNET-45880|En del av x-axeletiketter återges på den andra raden i diagrammet|Insekt|
|CELLSNET-45864|EMF konverterad från Aspose.Cells är inte exakt korrekt|Insekt|
|CELLSNET-45885|Typen (attributet) för extern länk ändras efter öppna/spara|Insekt|
|CELLSNET-45872|Det går inte att läsa Excel-dataanslutning när dess typ är CSV|Insekt|
|CELLSNET-45868|PrintTitleRows egenskapsvärde försvinner efter att ha öppnats och sparats med Aspose.Cells|Insekt|
|CELLSNET-45865|Specialtecken som används i ett kolumnnamn fungerar inte - Problem med smarta markörer|Insekt|
|CELLSNET-45858|Ändring av länkkälla påverkar innehållet i rullgardinsmenyn|Insekt|
|CELLSNET-45857|Skadad fil när du kopierar ark från en arbetsbok till en annan|Insekt|
|CELLSNET-45901|Textrutejustering förloras när den renderades till PDF|Insekt|
|CELLSNET-45875|Cell-värdet försvinner och en del av x-axeletiketterna återges på den andra raden|Insekt|
|CELLSNET-45873|Implementering av interaktiv kontroll för grupper av radioknappar i GridWeb|Insekt|
|CELLSNET-45902|Arbetsbladet blir för stort och svarar inte när du navigerar till eller klickar på det i Aspose.Cells.GridWeb|Insekt|
|CELLSNET-45849|Bilden blir utanför kalkylbladets storlek|Insekt|
|CELLSNET-45824|Bilder i Excel-fil visas inte i normal storlek vid import av filen till Aspose.Cells.GridDesktop|Insekt|
|CELLSNET-45874|Undantag "Inmatningssträngen var inte i korrekt format" vid import av Excel-filen till Aspose.Cells.GridWeb|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till LoadDataFilterOptions.DefinedNames enum**
Anger om definierade namnobjekt laddas när mallfilen laddas.
#### **Ändrar beteendet för LoadDataFilterOptions.Formula enum**
äldre versioner laddar vi alltid definierade namnobjekt när vi laddar formler. Nu tillhandahåller vi separat enum för definierade Name-objekt explicit, så Formel Enum kommer bara att beteckna att formler ska laddas nu, oavsett vilka definierade Name-objekt kommer att laddas eller inte. En sak bör dock noteras, vanligen definierade namnobjekt används av formler, om användaren bara laddar formler och inte laddar de definierade namnobjekten, kommer cellformeln som refererar till dessa namn att bli skadad och kan orsaka undantag. Så, i allmänhet, om användaren vill ladda formler, bör de definierade namnobjekten också laddas. Men användaren kan bara ladda definierade namnobjekt utan att ladda formler.
#### **Lägg till SheetType.Dialog enum**
Representerar dialogblad.
#### **Lägger till egenskapen WorkbookSettings.MaxRowsOfSharedFormula**
Hämtar och ställer in det maximala radnumret för delad formel. Den delade formeln delas upp i flera delade formler om det totala antalet rader av delade formeln är större än det.
#### **Lägger till WorkbookSettings.StreamProvider-egenskapen**
Hämtar och ställer in strömleverantören för extern resurs.
#### **Lägger till egenskapen ShapeTextAlignment.IsAutoMargin**
Indikerar om marginalen på textramen är atuomatisk.
#### **Lägger till egenskapen ImportTableOptions.IsFormulas**
Representerar vilken kolumn i datatabellen som ska importeras som formler.
