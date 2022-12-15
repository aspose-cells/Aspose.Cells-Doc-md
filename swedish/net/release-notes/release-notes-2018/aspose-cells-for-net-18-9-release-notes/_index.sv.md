---
title: Aspose.Cells for .NET 18.9 Release Notes
type: docs
weight: 40
url: /sv/net/aspose-cells-for-net-18-9-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 18.9](https://www.nuget.org/packages/Aspose.Cells/18.9.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42992|Tillämpa textjustering på deltext i textrutan|Ny funktion|
|CELLSNET-46308|Exportera anpassade dokumentegenskaper till PDF|Ny funktion|
|CELLSNET-46301|Hämta XML-sökväg från listobjekt/tabell|Ny funktion|
|CELLSNET-46315|Stöd aktiediagram i ODS-fil|Ny funktion|
|CELLSNET-46304|Lägg till egenskapen Row.FirstDataCell för att hämta den första datacellen i raden|Förbättring|
|CELLSNET-46298|Skapa säkerhetsbladsnamn som liknar Apache POI|Förbättring|
|CELLSNET-46319|FilterOperatorType.Innehåller saknas från API|Förbättring|
|CELLSNET-46297|Hämta utbud av frågetabell|Förbättring|
|CELLSNET-46294|Namn arbetsblad samma som källfilens namn vid konvertering av CSV/TSV till kalkylblad|Förbättring|
|CELLSNET-46289|Inkludera osignerade Dll-filer med Aspose.Cells|Förbättring|
|CELLSNET-46290|Fel färger återgivna för former i Excel till PDF-konvertering|Insekt|
|CELLSNET-46282|Ganska små bilder renderade i PDF|Insekt|
|CELLSNET-46328|Trasig hyperlänk i HTML|Insekt|
|CELLSNET-46322|Problem med antal och datumvärden när AutoFitColumns() anropas|Insekt|
|CELLSNET-46312|Pivottabeller fungerar inte efter laddning och spara|Insekt|
|CELLSNET-46291|Problem i pivottabeller medan du uppdaterar och döljer pivotobjekt|Insekt|
|CELLSNET-46279|PivotTable.RefreshData ger undantaget "Index utanför intervallet".|Insekt|
|CELLSNET-46303|Formeln är inte korrekt beräknad|Insekt|
|CELLSNET-46327|Namngivna intervall när de konverteras till SVG, som inte fångar de exakta teckensnitten och avstånden|Insekt|
|CELLSNET-46313|Problem i utdata-PDF när du använder tyska nyckelord i skripthuvuden och sidfötter|Insekt|
|CELLSNET-46300|Tabell/Listobjekt överlappade data under tabellen vid import av xml-data till kalkylarket|Insekt|
|CELLSNET-46318|Vertikala rutnät visades i diagrammet efter att ha anropat metoden Chart.Calculate().|Insekt|
|CELLSNET-46287|Horisontell axel saknas i renderade bilder från Excel-diagram|Insekt|
|CELLSNET-46286|Problem vid inställning av rotationsvinkel för kategoriaxel|Insekt|
|CELLSNET-46333|Applikations-GUID har ändrats|Insekt|
|CELLSNET-46332|Lagringar och strömmar saknas i OLE-paketet efter att en krypterad XLSX-fil har sparats på nytt|Insekt|
|CELLSNET-46325|Grafer som går förlorade vid kopiering av kalkylblad från en arbetsbok till en annan|Insekt|
|CELLSNET-46316|Villkorlig formatering tillämpas utan teckensnitt och skuggfärger när arbetsböcker slås samman|Insekt|
|CELLSNET-46305|Text ur utskriftsområdet renderas i PDF|Insekt|
|CELLSNET-46296|Autopassa kolumner eller rader som stör de grupperade formerna|Insekt|
|CELLSNET-46292|Skillnad i XML-filer|Insekt|
|CELLSNET-46283|Kant saknas i ODS Excel-utdata|Insekt|
|CELLSNET-46331|Undantag vid konvertering av en XLSX-fil till PDF-filformat|Undantag|
|CELLSNET-46270|ArgumentOutOfRangeException höjdes när Slicer.Refresh() anropades|Undantag|
|CELLSNET-46323|Datavalideringsproblem när man försöker ändra cellvärde med något av rullgardinsmenyn|Undantag|
|CELLSNET-46307|Undantag vid hämtning av webbadressen till listobjektets xml-databindningskarta|Undantag|
|CELLSNET-46336|System.OverflowException höjdes när Chart.Calculate anropades|Undantag|
|CELLSNET-46293|Undantag när dokumentet sparas|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till metoderna CellsHelper.CreateSafeSheetName(strängnamnProposal)/CreateSafeSheetName(strängnamnProposal, char replaceChar)**
Metoder för användarens bekvämlighet för att skapa ett giltigt arknamn.
#### **Lägger till Row.FirstDataCell**
Får den första icke-tomma cellen i raden.
#### **Lägger till MapChartLabelLayout enum**
Representerar etikettlayouttypen för kartdiagrammet.
#### **Lägger till MapChartProjectionType enum**
Representerar projektionstypen för kartdiagrammet.
#### **Lägger till MapChartRegionType enum**
Representerar regiontypen för kartdiagrammet.
#### **Lägger till QuartileCalculationType enum**
Representerar diagrammets kvartilberäkningstyp.
#### **Lägger till egenskapen Series.LayoutProperties och klassen SeriesLayoutProperties**
Representerar layoutegenskaperna för serien.
#### **Lägger till egenskapen TickLabels.IsAutomaticRotation**
Indikerar om rotationen av bocketiketterna är automatisk.
#### **Lägger till FilterOperatorType.BeginsWith, Contains, EndsWith och NotContains enum**
Representerar textfilteroperatortypen.
#### **Lägger till metoden Cell.GetDisplayStyle(bool).**
Hämtar visningsstilen för cellen.
#### **Lägger till metoden GlobalizationSettings.GetStandardHeaderFooterFontStyleName(string localFontStyleName)**
Får standardnamn på engelska typsnittsstilen (vanlig, fet, kursiv) för sidhuvud/sidfot enligt det givna språkets teckensnittsnamn.
#### **Lägger till PdfCustomPropertiesExport enum**
Anger hur CustomDocumentPropertyCollection exporteras till PDF-fil.
#### **Lägger till egenskapen PdfSaveOptions.CustomPropertiesExport**
Hämtar eller ställer in ett värde som bestämmer hur CustomDocumentPropertyCollection exporteras till PDF-fil. Standardvärdet är None.
#### **Lägger till klass XmlDataBinding**
Representerar Xml-databindningsinformation.
#### **Lägger till egenskapen ListObject.XmlMap**
Får en XmlMap som används för den här listan.
#### **Lägger till egenskapen XmlDataBinding.Url**
Hämtar käll-url för denna databindning.
#### **Lägger till egenskapen XmlMap.DataBinding**
Får en XmlDataBinding av denna karta.
