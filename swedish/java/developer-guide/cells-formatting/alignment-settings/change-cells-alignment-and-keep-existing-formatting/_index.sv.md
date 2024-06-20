---
title: Ändra cells justering och behåll befintlig formatering
type: docs
weight: 260
url: /sv/java/change-cells-alignment-and-keep-existing-formatting/
---

## **Möjliga användningsscenario**

Ibland vill du ändra justeringen av flera celler men behålla den befintliga formateringen. Aspose.Cells låter dig göra det genom egenskapen [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments). Om du ställer in den som **true** kommer ändringar i justering att ske annars inte. Observera att [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)-objektet skickas som parameter till [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag))-metoden som faktiskt tillämpar formateringen på cellområdet.

## **Ändra cellers justering och behåll befintlig formatering**

Följande provkod laddar den [provdatabladet Excel-fil](67338592.xlsx), skapar området och centrering fastnar den horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmbild jämför provdatabladet Excel-fil och [utdata Excel-filent](67338591.xlsx) och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centrerad horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
