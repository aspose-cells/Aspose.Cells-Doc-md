---
title: Aspose.Cells for .NET 23.5 Release Notes
type: docs
weight: 8
url: /sv/net/aspose-cells-for-net-23-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 23.5](https://www.nuget.org/packages/Aspose.Cells/23.5.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSNET-53234|Stöd för att uppdatera referenser av externa bladdata till lokala blad när externa länkar tas bort|
|CELLSNET-46133|Render Checkbox-kontroll som kontroll och inte som statisk bild|
|CELLSNET-53252|Ställ in önskad bilddimension och behåll bildförhållandet medan du konverterar arbetsboken till bilder|
|CELLSNET-53267|Autopassa rader för rendering|
|CELLSNET-53109|Stöd för att få PivotArea och PivotFormat|
|CELLSNET-53216| Filstorleken för genererad pdf är för stor vid konvertering till pdf|
|CELLSNET-53181|Ogiltigt kolumnindex.' om att spara pdf|
|CELLSNET-53192|Tick-symbolen visas inte korrekt när du konverterar Excel till pdf|
|CELLSNET-53292|Onormal textrotation vid konvertering av fil till pdf|
|CELLSNET-53293|Anslutningslinjepositionsfel vid konvertering av fil till Pdf|
|CELLSNET-46629|Excel till PDF konvertering med tidslinjeobjekt|
|CELLSNET-53124| Att ställa in värden och beräkna förstör arbetsboken i den senaste versionen av Aspose.Cells|
|CELLSNET-53186| Det går inte att analysera formeln som innehåller en hel kolumn i Apples nummerfil|
|CELLSNET-53208|Filen går sönder efter att formeln tagits bort|
|CELLSNET-53228|Layouten av Legend överensstämmer inte med Excel när diagram till bild|
|CELLSNET-53229|Axelfärgen överensstämmer inte med Excel när diagram till bild|
|CELLSNET-53235| Felplot visas inte|
|CELLSNET-53153|Det går inte att mata ut PDF vid konvertering av en fil med många bilder|
|CELLSNET-53209| En skadad fil genereras när en stor fil konverteras till PDF|
|CELLSNET-53286|Header image konverteringsfel vid konvertering av fil till PDF|
|CELLSNET-49624|Problem med textbrytning under konverteringen XLSX till HTML|
|CELLSNET-51101|Excel till HTML konvertering - formatering/innehåll är förvrängt och oordning|
|CELLSNET-53206| Exportera intervall som HTML med länkar ändrar stilar/formatering|
|CELLSNET-53133|Excel kraschar med dokument som sparats tillbaka från Aspose.Cells|
|CELLSNET-53180|Tillåt text att svämma över forminställningarna rensas när filen sparas till xls|
|CELLSNET-53185|Hålstorleken på munkdiagrammet förlorades när du sparade som ODS|
|CELLSNET-53191|TextBox textmarginalfel när filen sparas till xls|
|CELLSNET-53207| Excel-kalkylblad återges inte korrekt till PDF (med all data/innehåll) förrän det sparas via MS Excel|
|CELLSNET-53218|Pivottabelldiagrammet visas annorlunda i den konverterade PDF-filen efter att ha uppdaterat pivottabellen|
|CELLSNET-53258|Diagramtiteljustering ändrades från vänster till mitten när filen sparades om|
|CELLSNET-53260|TextBox kan redigeras efter inställning av skydd|
|CELLSNET-53268|Inledande nollor tas bort|
|CELLSNET-53271|Teckenstorleken ändras när filen sparas som xls|
|CELLSNET-53279|Det returnerade teckensnittet i formrik formaterad text är inte samma som Excel.|
|CELLSNET-53283|Teckensnittet för diagrammet Längd är inte samma som Excel|
|CELLSNET-53285|Tabellen ska inte expanderas om den innehåller total rad.|
|CELLSNET-53287| Bilden i rubriken ska visas i gråskala och i två färger (svart och vitt)|
|CELLSNET-53251|Ogiltig tabellreferens CellsException under tur och retur|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Ändrar beteendet för ExternalLinkCollection.Clear(bool)/RemoveAt(int,bool) metoder**

I gamla versioner, när "updateReferencesAsLocal" är sant, uppdaterar vi endast dessa referenser av externa namn till lokala namn på aktuell arbetsbok. För referenser till externa bladdata uppdaterade vi dem som "#REF!" alltid. Från 23.5, om det finns ett kalkylblad i den aktuella arbetsboken med samma arknamn som den externa referensen, kommer referensen att uppdateras till det lokala bladet också.

###  **Lägger till metoden Row.GetEnumerator (bool omvänd, bool sync).**

Ge användaren möjlighet att passera Cell i omvänd ordning.

###  **Föråldrad Cells.GetRowEnumerator()**

Använd RowCollection.GetEnumerator() istället.

###  **Föråldrar metoden Chart.IsReferedByChart() och lägger till metoden Chart.IsCellReferedByChart()**

Använd Chart.IsCellReferedByChart() istället.

###  **Lägger till egenskapen SeriesLayoutProperties.IsIntervalLeftClosed**

Indikerar om intervallet är stängt på vänster sida.

###  **Lägger till egenskapen ShapeTextAlignment.IsLockedText**

Anger om formens text är låst.

###  **Tar bort föråldrade ShapeFormat-klass och Shape.ShapeFormat**

Använd egenskapen Shape.Line och Shape.Fill istället.

###  **Lägger till egenskapen ListColumn.TotalsRowLabel**

Hämtar och ställer in etiketten för totalraden i tabellen.

###  **Lägger till metoden ListObject.PutCellValue(Int32,Int32,Object,Boolean)**

Ställer in värdet på cellen i tabellen.

###  **Lägger till PivotAreaType enum och PivotArea.RuleType-egenskapen**

Hämtar och ställer in typen av pivotområde i pivottabellen.

###  **Lägger till klassen PivotTableFormat**

Representerar formatet för pivottabellen.

###  **Lägger till klassen PivotTableFormatCollection**

Representerar alla format för pivottabellen.

###  **Lägger till egenskapen PivotTable.PivotFormats**

Hämtar och lägger till alla format för pivottabellen.

###  **Lägger till egenskapen PivotTable.AutofitColumnWidthOnUpdate**

Indikerar om kolumnbredden automatiskt passar vid uppdatering av pivottabell.

###  **Lägger till klasserna PivotAreaFilter och PivotAreaFilterCollection**

Representerar filtren för att välja pivotområde i pivottabellen.

###  **Lägger till egenskapen PivotArea.Filters**

Representerar filtren för att välja pivotområde i pivottabellen.

###  **Lägger till egenskaperna PivotArea.IsRowGrandIncluded och PivotArea.IsColumnGrandIncluded**

Indikerar om inklusive rad eller kolumns totalsumma i området.

###  **Lägger till egenskapen PivotArea.AxisType**

Hämtar och ställer in den region i pivottabellen som denna regel gäller.

###  **Lägger till egenskapen PivotArea.IsOutline**

Anger om regeln hänvisar till pivotområdet som är i konturläge.

###  **Lägger till metoden ImageOrPrintOptions.SetDesiredSize(int wantedWidth, int wantedHeight, bool keepAspectRatio)**

Ställer in önskad bredd och höjd på bilden och anger om bildförhållandet för ursprungsbilden ska behållas.

###  **Föråldrade metoden ImageOrPrintOptions.SetDesiredSize(int önskadBredd, int önskadHöjd)**

Använd ImageOrPrintOptions.SetDesiredSize(desiredWidth, wantedHeight, false) istället.

###  **Lägger till egenskapen PdfSaveOptions.Watermark**

Hämtar eller ställer in vattenstämpel till utmatning.

###  **Lägger till klasser RenderingFont och RenderingWatermark**

För att lägga till vattenstämpel till utdata av rendering.

###  **Lägger till egenskapen AutoFitterOptions.ForRendering**

Anger om lämplig för återgivningsändamål.
 
###  **Ändrar definitionen av EquationNodeParagraph.EquationHorizontalJustificationType**

Ändra från instansvariabel till egenskaps-/metodåtkomst.

