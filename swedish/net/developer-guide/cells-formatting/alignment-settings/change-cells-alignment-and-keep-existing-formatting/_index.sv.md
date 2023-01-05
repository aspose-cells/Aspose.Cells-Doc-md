---
title: Ändra Cells Justering och behåll befintlig formatering
type: docs
weight: 340
url: /sv/net/change-cells-alignment-and-keep-existing-formatting/
---
## **Möjliga användningsscenarier**

Ibland vill du ändra justeringen av flera celler men vill också behålla befintlig formatering. Aspose.Cells låter dig göra det med hjälp av[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) fast egendom. Om du vill ställa in det**Sann** , kommer ändringar i anpassningen att ske annars inte. Vänligen notera,[**StilFlagga**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) objekt skickas som en parameter till[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)metod som faktiskt tillämpar formateringen på ett cellintervall.

## **Ändra Cells Justering och behåll befintlig formatering**

 Följande exempelkod laddar[exempel på Excel-fil](67338585.xlsx) , skapar intervallet och mittjusterar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exemplet på Excel-filen och[utdata Excel-fil](67338586.xlsx)och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centrerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
