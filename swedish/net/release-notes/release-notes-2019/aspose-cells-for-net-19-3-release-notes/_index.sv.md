---
title: Aspose.Cells for .NET 19.3 Release Notes
type: docs
weight: 100
url: /sv/net/aspose-cells-for-net-19-3-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.3](https://www.nuget.org/packages/Aspose.Cells/19.3.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46598|Lägg till Name.GetReferredAreas-metoden (Boolean recalculate) för att ge rikare data (inklusive externa referenser och länkade data)|Ny funktion|
|CELLSNET-46580|Felaktig återgivning av roterade former i form till bildkonvertering|Insekt|
|CELLSNET-46587|Pivottabell bryts när rader och kolumner tas bort|Insekt|
|CELLSNET-46608|Pivottabellsfilter rensas efter laddning och spara|Insekt|
|CELLSNET-46623|Problem med inbäddade delade fil-URL:er vid konvertering av Excel-fil till HTML|Insekt|
|CELLSNET-46590|Fel i en cell som anropar ett makro efter att filen har bearbetats av Aspose.Cells|Insekt|
|CELLSNET-46597|Fel värde i PDF i Excel till PDF rendering|Insekt|
|CELLSNET-46613|Problem när du hämtar och skapar namngivna intervall|Insekt|
|CELLSNET-46625|Fel tabellbakgrund i utdata PDF och HTML|Insekt|
|CELLSNET-46628|Skillnad i utgången PDF|Insekt|
|CELLSNET-46589|Oväntade rutnätslinjer dök upp i SVG konverterade från MS Excel-kalkylblad|Insekt|
|CELLSNET-46600|Dubbel understrykning försvinner när Excel-fil konverteras till PDF|Insekt|
|CELLSNET-46626|Utrymmesformateringsproblem vid konvertering av XLSX-filen till PDF|Insekt|
|CELLSNET-46585|Problem med DataLabel-teckensnitt|Insekt|
|CELLSNET-46602|OutOfMemoryException medan du renderar ett vertikalt eller horisontellt stapeldiagram|Insekt|
|CELLSNET-46605|Raden ökar i höjd efter automatisk anpassning av rader (tillval).|Insekt|
|CELLSNET-46609|Infoga alternativ CopyFormatType.Clear fungerar inte korrekt|Insekt|
|CELLSNET-46611|Problem med externa länkar och dess visning|Insekt|
|CELLSNET-46616|Hantera ListObject.ConvertToRange på gigantiska tabeller|Insekt|
|CELLSNET-46620|Line.SolidFill.Color fungerar felaktigt på former när färg skickas från Argb eller från känt namn|Insekt|
|CELLSNET-46622|Cells.ImportData importerar fel antal kolumner från datatabellen|Insekt|
|CELLSNET-46624|XLSX problem med filladdning|Insekt|
|CELLSNET-46635|För många sidbrytningar i ODS-filen (XLSX till ODS rendering)|Insekt|
|CELLSNET-46618|Undantag "Instans är skrivskyddad"|Undantag|
|CELLSNET-46617|Undantag vid inläsning av en arbetsbok|Undantag|
|CELLSNET-46636|Undantag vid laddning av en XLSX-fil|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Ändringar för standardteckensnitt för inläst XLS mallfil**
äldre versioner stödde vi inte att använda teckensnittet som definierats i temat (avancerad funktion i MS Excel 2007 och senare versioner) enligt regionen när XLS-mallfilerna laddas. På vissa användares krav har vi stött det från v19.3. Om regionen har specificerats i mallfilen XLS, kommer vi att tillämpa teckensnittet som definieras i temat enligt det sparade specificerade regionvärdet. Annars kommer vi att tillämpa typsnittet som definieras i temat enligt applikationsmiljöns regionala inställningar. Detta kommer att göra att standardteckensnittet för arbetsboken (laddat från XLS mallfil som har specificerat temadata) ändras och sedan påverka andra funktioner, såsom kolumnbredd, formstorlek, renderingseffekt, ...etc.
#### **Lägger till metoden Name.GetReferredAreas(bool recalculate).**
Tillhandahåller referenserna som hänvisas till av det definierade namnet som GetRanges(bool recalculate)-metoden. Men de returnerade referenserna representeras av ReferredArea-objekt som ger rikare funktioner inklusive externa länkar.
#### **Lägger till egenskapen TxtSaveOptions.KeepSeparatorsForBlankRow**
Anger om separatorer ska matas ut för tom rad. Standardvärdet är falskt vilket betyder att innehållet för den tomma raden kommer att vara tomt.
#### **Lägger till enum AutoFitMergedCellsType**
Representerar typen av automatiskt anpassade sammanslagna celler.
#### **Föråldrar egenskapen AutoFitterOptions.AutoFitMergedCells och lägger till egenskapen AutoFitterOptions.AutoFitMergedCellsType**
Hämtar och ställer in typen av automatisk passande radhöjd.
#### **Lägger till klasser JSONUtility och JsonLayoutOptions**
Den används för att importera json-filer.
#### **Lägger till klassen TableToRangeOptions och metoden ListObject.ConvertToRange(TableToRangeOptions options)**
Konverterar tabellen till intervall med alternativ.
