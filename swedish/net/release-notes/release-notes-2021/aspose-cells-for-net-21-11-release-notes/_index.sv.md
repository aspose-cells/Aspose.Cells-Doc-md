---
title: Aspose.Cells for .NET 21.11 Release Notes
type: docs
weight: 2
url: /sv/net/aspose-cells-for-net-21-11-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.11](https://www.nuget.org/packages/Aspose.Cells/21.11.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-48141|Stöd XLookup formel/funktion|Ny funktion|
|CELLSNET-49614|Stöd att spara bilder med workbook.Save()-metoden.|Ny funktion|
|CELLSNET-49651|Stöd för att spara som json-fil.|Ny funktion|
|CELLSNET-48499|Hämta formaterade cellvärden mot vissa celler|Förbättring|
|CELLSNET-49523|Rensa definierade namn när du rensar kalkylblad.|Förbättring|
|CELLSNET-48646|StackOverflow undantag medan Excel till PDF-konvertering|Prestanda|
|CELLSNET-49378|Problem med Excel till HTML-konverteringsprestanda och tomma celler|Prestanda|
|CELLSNET-49453|Förbättra prestanda samtidigt som du konverterar Excel till HTML|Prestanda|
|CELLSNET-48095|3D ändrades formen på molnet|Insekt|
|CELLSNET-49544|Bugg för att spara extern NamedRange som refererar till ett intervall med flera ark|Insekt|
|CELLSNET-49588|Enstaka data sparas annorlunda än det ursprungliga värdet|Insekt|
|CELLSNET-49667|Resultatet av ColorScale villkorlig formatering är felaktigt|Insekt|
|CELLSNET-49043|Positionen för den ritade linjen är inte korrekt i bilden|Insekt|
|CELLSNET-49068|Fel PDF genererad från Excel-fil|Insekt|
|CELLSNET-49179|Axeltitelreferens har oväntat tagits bort|Insekt|
|CELLSNET-49294|Axeln i vissa diagram skiljer sig från de i Excel-filer|Insekt|
|CELLSNET-49495|Formelrendering överlappar varandra|Insekt|
|CELLSNET-49542|Diagrammets horisontella axel försvinner|Insekt|
|CELLSNETCORE-148|Cirkeldiagrammet återges inte korrekt|Insekt|
|CELLSNET-49193|GridDesktop fungerar inte korrekt|Insekt|
|CELLSNET-49642|Aspose.Cells.GridWeb har odeklarerat beroende av Newtonsoft.Json|Insekt|
|CELLSNET-49452|Flerradstext renderas inte bra|Insekt|
|CELLSNET-49498|HTML-ström till Excel ger undantag med de senaste versionerna|Insekt|
|CELLSNET-49610|XML Importera förlorad mallformatering|Insekt|
|CELLSNET-49671|Text med Windings-teckensnitt renderas inte korrekt till bilder/HTML|Insekt|
|CELLSNETCORE-278|XLSX till PDF-konverteringsresultat är inte öppningsbara när kultur är inställd på norska|Insekt|
|CELLSNET-49560|Skillnader i XML|Insekt|
|CELLSNET-49598|Regression: Skillnader i XML efter lagring|Insekt|
|CELLSNET-49630|Felaktiga kryss vid konvertering till EMF|Insekt|
|CELLSNET-49673|Vissa delar av prickade linjer blev heldragna linjer vid konvertering av diagram till bilder|Insekt|
|CELLSNET-49545|Typerna HtmlCrossType.Default och HtmlCrossType.FitToCell är trasiga|Insekt|
|CELLSNET-49654|Makron fungerar inte efter konvertering av XLS till XLSM|Insekt|
|CELLSNET-49727|Bilder av Mht-filer är inte synliga i IE.|Insekt|
|CELLSNET-49609|"Shape to image error" vid konvertering av Excel-fil till PDF|Undantag|
|CELLSNET-49608|Aspose.Cells ger fel när man försöker lägga till vissa intervallnamn|Undantag|
|CELLSNET-49697|XLSX till PDF: Inmatningssträngen var inte i korrekt format.|Undantag|
|CELLSNETCORE-287|NullPointerException vid beräkning av formel|Undantag|
|CELLSNET-49497|ExportXml med XML Map kastar "NullReferenceException"|Undantag|
|CELLSNET-49595|ExportXml med XML Map kastar "NullReferenceException" för komplexa Excel-filer|Undantag|
|CELLSNET-49471|Regression: GetRanges() returnerar Null|Regression|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till enum CellValueFormatStrategy.DisplayString.**

Med denna strategi kommer Cell.GetStringValue(CellValueFormatStrategy) att ta hänsyn till gränsen för kolumnbredden vid formatering av cellvärden med visningsstilen. Om det formaterade resultatet överskrider den tillgängliga bredden, kan en eller flera "#" returneras, precis som vad ms excel visar för sådana typer av celler.

### **Lägger till egenskapen WorksheetCollection.ActiveSheetName.**

Hämtar och ställer in det aktiva arknamnet för arbetsboken.

### **Lägger till klasserna JsonLoadOptions och JsonSaveOptions.**

Representerar alternativen för att ladda eller spara filerna.

### **Lägger till egenskapen ImageSaveOptions.StreamProvider.**

Ange strömmarna om det finns två eller fler sidor.

### **Lägger till LoadFormat.Image och LoadFormat.Json enum.**

Representerar bilden och json-typen.

### **Lägger till SaveFormat.Bmp, SaveFormat.Emf,SaveFormat.Gif,SaveFormat.Jpg,SaveFormat.Json och SaveFormat.Png enum**

Nya sparade format som stöds.

### **Lägger till FileFormatType.Emf,FileFormatType.Gif,FileFormatType.Jpg,FileFormatType.Json,FileFormatType.Png,FileFormatType.Wmf enum**

Nya filformatstyper som stöds.

