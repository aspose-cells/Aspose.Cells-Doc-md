---
title: Aspose.Cells for .NET 21.9 Release Notes
type: docs
weight: 4
url: /sv/net/aspose-cells-for-net-21-9-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.9](https://www.nuget.org/packages/Aspose.Cells/21.9.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-48134|Stöd för rendering av Box & Whisker Excel 2016 Diagram till bild|Ny funktion|
|CELLSNET-48683|Ta bort pivottabell medan data bevaras|Förbättring|
|CELLSNET-48624|Stöd namngivna rader/kolumner för .ods-filer|Förbättring|
|CELLSNET-49052|Stödinställning Transparens i bilden för xlsx-filer.|Förbättring|
|CELLSNETCORE-233|Förbättring för att ändra författare av trådad kommentar|Förbättring|
|CELLSNET-49011|Snabba upp celliteratoråtkomst för rendering för GridDesktop|Prestanda|
|CELLSNET-48915|Minneslöst undantag vid återgivning av kalkylblad till bild|Prestanda|
|CELLSNET-47663|Excel-dokument konverteras inte till html|Prestanda|
|CELLSNET-48506|Förbättra prestanda för att skriva .ods-fil.|Prestanda|
|CELLSNET-48645| Text inuti en pilform fick fel position|Insekt|
|CELLSNET-48475|Pivottabellens uppdatering fungerar inte korrekt|Insekt|
|CELLSNET-48711|Exportera den zoomade xlsx till html.|Insekt|
|CELLSNET-48998|Ändringar av egenskaper går förlorade eller gör att de försvinner för Slicer-objektet|Insekt|
|CELLSNET-48614|Excel-filterfunktionen verkar inte fungera korrekt|Insekt|
|CELLSNETCORE-136|Arrowhead visas inte i Linux-miljö|Insekt|
|CELLSNETCORE-137|Pilspets saknas vid konvertering av Excel till SVG|Insekt|
|CELLSNET-49045|Felaktig cellhöjd observerades i GridWeb när den bifogade filen laddades|Insekt|
|CELLSNET-49069|Aspose.Cells.GridWeb SessionMode fungerar inte|Insekt|
|CELLSNET-40974| Excel till Xps-konvertering: länken är inte klickbar efter konvertering gjord .NET|Insekt|
|CELLSNET-48540| Linjer blev prickade på datafält i Emf/OfficeCompatibleEmf|Insekt|
|CELLSNET-48609|Problem med teckensnittsskillnad när man jämför det med ExcelInterop-bilden|Insekt|
|CELLSNET-48983| Ark till Emf lämnar kantkanterna felaktigt ritade|Insekt|
|CELLSNET-49049|Teckensnittet förvrängs när arket konverteras till Emf-bild med alternativet EmfOnly|Insekt|
|CELLSNET-48049|Olika axelavstånd vid konvertering från xlsx-arbetsbok till emf|Insekt|
|CELLSNET-48509|Diagram visas ibland inte baserat på förklaringsposition|Insekt|
|CELLSNET-48580| Miss Legend-post i utgången SVG i Excel-diagrammet|Insekt|
|CELLSNET-48696|Fel vid ändring av dataetikettens färg|Insekt|
|CELLSNET-48698|Problem med diagramfärg vid export i PDF|Insekt|
|CELLSNET-48797|Medelmarkörvärdet är fel vid läsning från xlsx|Insekt|
|CELLSNET-48455|Problem med autofit radhöjd|Insekt|
|CELLSNET-48473|AutoFit Column fungerar inte korrekt|Insekt|
|CELLSNET-48605|Lägg till VBA-kod i arbetsboken producerade skadade resultat|Insekt|
|CELLSNET-48644|Missa rader och vattenstämpel när du konverterar XLSX till HTML genom sidbrytningar|Insekt|
|CELLSNET-48669|Namngivna intervall av .ods-filen läses som tabell.|Insekt|
|CELLSNET-48718|Få fel namn på inbäddat objekt|Insekt|
|CELLSNET-48966| Efter kopiering av cellintervall går formler förlorade|Insekt|
|CELLSNET-49055| Autoanpassa kolumner för sammanfogad cell fungerar inte|Insekt|
|CELLSNET-49100|Vissa celler saknar rutnätslinjer vid export till HTML|Insekt|
|CELLSNETCORE-149|Genom att kopiera stilar efter att ha kopierat värden raderas cellvärden i Excel 97-format|Insekt|
|CELLSNETCORE-152|EMF bilddata kan inte läsas från filen XLS|Insekt|
|CELLSNET-48444|Ogiltigt parameterfel vid konvertering av xlsb till xls-fil|Undantag|
|CELLSNET-48607|Form till bild Fel|Undantag|
|CELLSNET-48866|Det går inte att öppna specifik XLSX Excel-fil i GridDesktop-kontrollen|Undantag|
|CELLSNET-48956| Undantag efter inställning av cellstil med Cell.SetStyle|Undantag|
|CELLSNET-48712|Array out of bound vid rendering av Box&Whisker-diagram|Undantag|
|CELLSNET-48910|Undantag vid rendering av box&Whisker Chart till bild|Undantag|
|CELLSNET-48648| Ogiltigt kolumnindex vid kopiering av ett intervall|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till egenskapen AutoFitterOptions.FormatStrategy.**

Hämtar och ställer in den formaterade strategin för automatisk anpassning.

### **Lägger till egenskapen MsoFormatPicture.Transparency.**

 Returnerar eller ställer in graden av transparens för området som ett värde från 0,0 (opak) till 1,0 (ren).

### **Lägger till överbelastade PivotTableCollection.Remove()-metoder.**

Tar bort den angivna pivottabellen och kontrollerar om celldata behålls .

### **Lägger till egenskapen ImageOrPrintOptions.IsOptimized.**

 Indikerar om utgångselementen optimeras. Standardvärdet är falskt. För närvarande är bara gränslinjerna optimerade när den här egenskapen är inställd på sant.

