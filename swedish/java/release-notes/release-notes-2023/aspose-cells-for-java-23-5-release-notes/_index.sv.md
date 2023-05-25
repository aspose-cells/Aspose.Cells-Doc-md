---
title: Aspose.Cells for Java 23.5 Release Notes
type: docs
weight: 8
url: /sv/java/aspose-cells-for-java-23-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 23.5](https://releases.aspose.com/cells/java/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSJAVA-45230|Stöd för att lägga till vattenstämpel under rendering till pdf|
|CELLSJAVA-45334|Data i textrutan är utanför gränserna|
|CELLSJAVA-45336|Text flyttas när grupperade autoformer konverteras till pdf|
|CELLSJAVA-45364|Vertikal text i figur i Excel är lutande när den konverteras till PDF|
|CELLSJAVA-45366|Oval form visningsfel vid export av fil till html|
|CELLSJAVA-45369| Problem med ersatt teckensnitt i textrutor|
|CELLSJAVA-45290|Referensregler för villkorlig formatering uppdateras inte bra när man kopierar intervall från en arbetsbok till en annan arbetsbok|
|CELLSJAVA-45362|Felplot visas inte|
|CELLSJAVA-45363|Endless loop vid konvertering av diagram till bild|
|CELLSJAVA-45239|Cell vertikal Justering av motivering träder inte i kraft när du sparar till html|
|CELLSJAVA-45335|Text är felplacerad när cellen är formaterad som nummer i utdata-html|
|CELLSJAVA-45323| Om du tar bort inställningarna för automatisk anpassning på kolumner i pivottabellen tar du bort pivottabellens stil/formatering|
|CELLSJAVA-45341|Diagramstil går förlorad när du laddar gamla arbetsbokströmmar och sparar|
|CELLSJAVA-45351|Formatets pivotområde inkluderar endast delsummor för pivotfält|
|CELLSJAVA-45374|Programmet fastnar vid öppning av XML-fil|
|CELLSJAVA-45319|Snitvinkeln på cirkeldiagrammet 3D är felaktig vid konvertering av fil till ODS|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Ändrar beteendet för ExternalLinkCollection.Clear(bool)/RemoveAt(int,bool) metoder**

I gamla versioner, när "updateReferencesAsLocal" är sant, uppdaterar vi endast dessa referenser av externa namn till lokala namn på aktuell arbetsbok. För referenser till externa bladdata uppdaterade vi dem som "#REF!" alltid. Från 23.5, om det finns ett kalkylblad i den aktuella arbetsboken med samma arknamn som den externa referensen, kommer referensen att uppdateras till det lokala bladet också.

###  **Lägger till metoden Row.iterator (bool omvänd, bool sync).**

Ge användaren möjlighet att passera Cell i omvänd ordning.

###  **Föråldrad Cells.getRowEnumerator()**

Använd RowCollection.iterator() istället.

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
