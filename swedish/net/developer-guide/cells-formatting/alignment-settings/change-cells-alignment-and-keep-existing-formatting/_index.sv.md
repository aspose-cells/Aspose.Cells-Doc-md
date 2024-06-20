---
title: Ändra cells justering och behåll befintlig formatering
description: Använd Aspose.Cells biblioteket för att ändra cells justering och behålla befintlig formatering
keywords: Aspose.Cells, C#, Celljustering, behålla befintlig formatering
type: docs
weight: 340
url: /sv/net/change-cells-alignment-and-keep-existing-formatting/
---

## **Möjliga användningsscenario**

Ibland vill du ändra justeringen av flera celler men också behålla befintlig formatering. Aspose.Cells tillåter dig att göra det med hjälp av egenskapen [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments). Om du ställer det till 'true' kommer ändringar i justering att ske, annars inte. Observera att objektet [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) skickas som parameter till [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)-metoden som faktiskt tillämpar formatering på en rad celler.

## **Ändra cellers justering och behåll befintlig formatering**

Den följande exempelkoden läser in den [exempel Excel-filen](67338585.xlsx), skapar området och centrera justerar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exempel Excel-filen och [utdata Excel-filen](67338586.xlsx) och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centralt justerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
