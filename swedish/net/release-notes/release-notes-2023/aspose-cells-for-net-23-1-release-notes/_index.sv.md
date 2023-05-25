---
title: Aspose.Cells for .NET 23.1 Release Notes
type: docs
weight: 12
url: /sv/net/aspose-cells-for-net-23-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 23.1](https://www.nuget.org/packages/Aspose.Cells/23.1.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSNET-50111|Stöd avbrott vid beräkning av formler|
|CELLSNET-52496|Stöd för att ändra standardstilen för rad/kolumn utan att ändra stilinställningarna för befintliga celler|
|CELLSNET-52505|Stöd för nya funktioner HSTACK/VSTACK|
|CELLSNET-52429|Stöd för att få författare och datum tid för revisioner|
|CELLSNET-52337|Stöd CHOOSECOLS och CHOOSEROWS Excel 365-formler|
|CELLSNET-52498| Förbättra SaveOptions.HasHeaderRow när du konverterar xlsx till json|
|CELLSNET-52499|JSON-värde saknas när ett ark är tomt|
|CELLSNET-52500|JsonSaveOptions.SkipEmptyRows fungerar inte korrekt|
|CELLSNET-52502|Exportera alltid excel som JObject när du konverterar excel till json|
|CELLSNET-52418|Formfyllningen är inte rätt vid konvertering till pdf|
|CELLSNET-52420| Former och bilder deformeras i Excel till PDF-rendering efter kopiering av ark|
|CELLSNET-52437|Felaktig skugga vid konvertering av bild till pdf|
|CELLSNET-52494|Pilteckenskiftningsfel vid konvertering av Excel-fil till PDF|
|CELLSNET-52442|SUMIF returnerar 4 istället för 0 med Aspose.Cells formelberäkningsmotor|
|CELLSNET-52441|Bild konverterad av diagram är inte samma sak som MS Excel|
|CELLSNET-52486|Säkerhetssårbarhet – CVE-2021-24112|
|CELLSNET-52410|Bild till SVG - Texten överlappas för den horisontella stapeln för datumetiketter i diagrambilden|
|CELLSNET-52366| Tjockare linjer och saknad kant när du sparar XLSB till en bild|
|CELLSNET-52395|Excel-fil (XLS) är skadad vid omspara via Aspose.Cells|
|CELLSNET-52435|Stöd filterkriterier när du öppnar och sparar html|
|CELLSNET-52440|Omfattningen av pivotable är inte samma som MS Excel när du konverterar pivittable till pdf|
|CELLSNET-52458|Innehållet och formateringen av arken ändras under kopiering|
|CELLSNET-52493|Undantag "Artikel har redan lagts till." om att spara XLS till XLSX|
|CELLSNET-48991|Objektreferens är inte inställd på en instans av ett objekt. undantag när filen ODS är öppen|
|CELLSNET-52419|Undantag för index utanför intervallet inträffar efter kopiering av ark och konvertering till pdf|
|CELLSNET-52433|Undantag "Filen är skadad" när en XLSX-fil med en hyperlänk laddas|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Lägger till klassen PivotGlobalizationSettings.**

Klassen hanterar alla globaliseringsinställningar om pivottabeller.

###  **Tar bort metoden GlobalizationSettings.GetOtherName().**

Denna metod har inte hänvisats längre, den har ingen effekt även om användaren implementerar den i GlobalizationSettings. Så vi tar bort det nu. Användaren bör använda metoden ChartGlobalizationSettings.GetOtherName() istället.

###  **Tar bort metoderna GlobalizationSettings.GetColumnLablesName()/GetRowLablesName().**

Använd PivotGlobalizationSettings.GetTextOfColumnLabels()/GetTextOfRowLabels().

###  **Föråldrar alla metoder om pivottabeller i GlobalizationSettings.**

Använd motsvarande metoder i PivotGlobalizationSettings.

###  **Lägger till GetStyle()/SetStyle()-metoder för klassen Row och Column.**

Stöder för att få/ställa in anpassad stil för hela raden/kolumnen. För att ställa in anpassad stil är skillnaden mellan SetStyle() och ApplyStyle() att SetStyle() inte ändrar stilinställningarna för befintliga celler.

###  **Lägger till HasCustomStyle-egenskapen för Cell, rad- och kolumnklasser.**

Indikerar om cellen, raden eller kolumnen har ställts in med anpassade stilinställningar (till skillnad från den standard som den ärver).

###  **Föråldrade egenskaperna Row.Style och Column.Style**

Använd Row.GetStyle() och Column.GetStyle() istället.

###  **Lägger till egenskapen JsonSaveOptions.AlwaysExportAsJsonObject.**

Anger om Excel-filer alltid exporteras som Json-objekt även om det bara finns ett kalkylblad.

###  **Lägger till klassen RevisionHeader och egenskapen RevisionLog.MetadataTable.**

Stöder att hämta och ställa in egenskaper för revisionslogg.

###  **Lägger till metoden Style.GetTwoColorGradientSetting() och föråldrar metoden Style.GetTwoColorGradient().**

Använd metoden Style.GetTwoColorGradientSetting() istället.

###  **Föråldrat JsonUtility.ExportRangeToJson(Range,ExportRangeToJsonOptions) och lägger till JsonUtility.ExportRangeToJson(Range, JsonSaveOptions)**

Använd metoden ExportRangeToJson(Range, JsonSaveOptions) istället.

###  **Lägger till egenskapen Charts.Axis.CustomUnit.**

Anger ett anpassat värde för visningsenheten.

###  **Föråldrade egenskapen Charts.Axis.CustUnit.**

Använd Charts.Axis.CustomUnit istället.

###  **Lägger till egenskapen Charts.Chart.PlotVisibleCellsOnly.**

Anger om endast synliga celler plottas.

###  **Föråldrade egenskapen Charts.Chart.PlotVisibleCells.**

Använd Charts.Chart.PlotVisibleCellsOnly istället.

###  **Tar bort egenskapen ShapeFormat.FillFormat.**

Använd egenskapen ShapeFormat.Fill istället.

###  **Tar bort egenskapen ShapeFormat.Outline.**

Använd egenskapen ShapeFormat.Line istället.
