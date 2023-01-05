---
title: Ändra Cells Justering och behåll befintlig formatering
type: docs
weight: 260
url: /sv/java/change-cells-alignment-and-keep-existing-formatting/
---
## **Möjliga användningsscenarier**

Ibland vill du ändra justeringen av flera celler men vill också behålla befintlig formatering. Aspose.Cells låter dig göra det med hjälp av[**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) fast egendom. Om du vill ställa in det**Sann** , kommer ändringar i anpassningen att ske annars inte. Vänligen notera,[**StilFlagga**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) objekt skickas som en parameter till[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) metod som faktiskt tillämpar formateringen på cellintervallet.

## **Ändra Cells Justering och behåll befintlig formatering**

Följande exempelkod laddar[exempel på Excel-fil](67338592.xlsx), skapar intervallet och mittjusterar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exemplet på Excel-filen och[utdata Excel-fil](67338591.xlsx)och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centrerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
