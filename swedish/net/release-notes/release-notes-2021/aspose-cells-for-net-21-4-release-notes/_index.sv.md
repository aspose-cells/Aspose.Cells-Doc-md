---
title: Aspose.Cells for .NET 21.4 Release Notes
type: docs
weight: 9
url: /sv/net/aspose-cells-for-net-21-4-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.4](https://www.nuget.org/packages/Aspose.Cells/21.4.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47891|Stöd för att få visningsstil med cacheaktivering|Ny funktion|
|CELLSNET-47922|Återge data med cellkoordinater i Excel till HTML konvertering|Förbättring|
|CELLSNET-47924|Implementera Crypto med BouncyCastles API|Förbättring|
|CELLSNET-47951|Stöd XML-kartor av XSD|Förbättring|
|CELLSNET-47206|Gruppera data med horisontella smarta markörer och kapslad datakälla|Förbättring|
|CELLSNET-47888|Lämpliga SmartMarkers krävs för att uppnå önskad effekt|Förbättring|
|CELLSNET-47918|Hopfällbara rader tillsammans med smarta markörer|Förbättring|
|CELLSNET-47953|Stöd för att lägga till .webp-bild till .xlsx-filer.|Förbättring|
|CELLSNET-47916|HTML stiltagg förbrukar 4 Gb minne och kraschar när den laddas in i arbetsboken|Prestanda|
|CELLSNET-46869|WordArts och former renderas inte korrekt i PDF|Insekt|
|CELLSNET-47890|Linjer kommer att glida under Pdf-konvertering|Insekt|
|CELLSNET-47858|Former återges inte korrekt i HTML och PDF|Insekt|
|CELLSNET-47907|Diagrammets placering ändras när Excel konverteras till HTML|Insekt|
|CELLSNET-47856|XLSX till PDF konverteringsproblem med pivottabeller|Insekt|
|CELLSNET-47846|GridWeb-implementering inkompatibel med de senaste DevExpress-komponenterna|Insekt|
|CELLSNET-47923|Felaktig sidlayoutvy för arbetsbok med ett annat standardteckensnitt än Calibri|Insekt|
|CELLSNET-47965| Excel till PDF Konvertering - Dokumentsidor blandas ihop|Insekt|
|CELLSNET-46161|Sned text visas inte korrekt i utgången PDF|Insekt|
|CELLSNET-47917|Cirkeldiagram-etiketter trasslat i PDF Genererade från Excel-kalkylblad|Insekt|
|CELLSNET-47919|Fel maxvärde extraherat från diagram|Insekt|
|CELLSNET-46363|Kapslad struktur importeras inte korrekt till XLSX|Insekt|
|CELLSNET-47838|Inbyggd diagramfärgpalett bevaras inte|Insekt|
|CELLSNET-47910|Range.Copy uppdaterar felaktigt villkorlig formatering|Insekt|
|CELLSNET-47931|Style.SetBorder() kraschar när flera alternativ ställs in samtidigt|Insekt|
|CELLSNET-47937|Metadataegenskapen Author är inte uppdaterad|Insekt|
|CELLSNET-47958|Missat ark i den laddade arbetsboken|Insekt|
|CELLSNET-47976|Formatet är inte implementerat när du använder FontSettings|Insekt|
|CELLSNET-47935|Undantag skapas när PivotTable.CalculateData() anropas|Undantag|
|CELLSNET-47940|Ett undantag görs när en speciell mht-fil öppnas.|Undantag|
|CELLSNET-47944|Null Undantag vid konvertering av skivform till bild|Undantag|
|CELLSNET-47932|Null Undantag vid laddning av en speciell xlsx-fil med konstig formel.|Undantag|
|CELLSNET-47963|Parametern är inte ett giltigt undantag när intervallet renderas till PNG|Undantag|
|CELLSNET-47967|Overflow-fel när en XLS-fil sparades|Undantag|
|CELLSNET-47921|Null Undantag när en speciell xlsx-fil laddas|Undantag|
|CELLSNET-47945|Null Undantag när en speciell html-fil laddas|Undantag|
|CELLSNET-47949|Ogiltigt mindre enhetsundantag kastas när ny arbetsbok|Undantag|
|CELLSNET-47950|NullReferenceException när du sparar en kopierad arbetsbok|Undantag|
|CELLSNET-47961|Null undantag när pivotCacheRecords1.xml inte existerar.|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till StartAccessCache()/CloseAccessCache()-metoder för arbetsbok och arbetsblad.**

Ge användarna möjlighet att komma åt data i batch-läge med bättre prestanda.

### **Lägger till egenskaperna TxtSaveOptions.ExportQuotePrefix och TxtLoadOptions.TreatQuotePrefixAsValue.**

Ge användarna möjligheten att bestämma hur de ska göra med det ledande citatet av cellens värde vid export/import av CSV/TSV-filer.

### **Lägger till metoderna GlobalizationSettings.GetCollationKey(string,bool) och Compare(string,string,bool).**

Ge användarna möjlighet att åsidosätta standardreglerna för strängjämförelse. För vissa lokaler eller strängvärden kan standardregeln för strängjämförelse inte vara den förväntade (resultatet av vissa funktioner, såsom formelberäkning, sortering, etc., skiljer sig från vad som borde finnas i ms excel). Om så är fallet kan användaren åsidosätta dessa metoder med den förväntade regeln (till exempel kan användaren använda implementeringen av icu-biblioteket).

### **Lägger till enum ImageType.WebP.**

Representerar Weppy-bilden.

### **Lägger till metoden OleObject.SetEmbeddedObject().**

För att kontrollera om ikonen uppdateras automatiskt.

### **Lägger till egenskapen WorkbookDesigner.LineByLine.**

Indikerar om bearbetning av smarta markörer rad för rad.

### **Lägger till egenskapen HtmlSaveOptions.ExportCellCoordinate?.**

Anger om excel-koordinater för icke-tomma celler exporteras när filen sparas till html. Standardvärdet är false.Om du vill importera utdata-html till Excel, behåll standardvärdet.

### **Lägger till egenskapen AutoFitterOptions.DefaultEditLanguage.**

 Hämtar eller ställer in standardspråk för redigering.

