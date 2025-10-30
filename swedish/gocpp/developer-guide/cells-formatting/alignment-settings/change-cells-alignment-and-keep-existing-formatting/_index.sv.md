---
title: Ändra cellinriktning och behåll befintlig formatering med Golang via C++
description: Använd Aspose.Cells biblioteket för att ändra cells justering och behålla befintlig formatering
keywords: Aspose.Cells, C++, celljustering, bevara befintlig formatering
type: docs
weight: 340
url: /sv/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Möjliga användningsscenario**

 Ibland vill du ändra inriktningen för flera celler men också behålla befintlig formatering. Aspose.Cells gör det möjligt med [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/)-egenskapen. Om du ställer in den till **true**, kommer justeringen att ändras, annars inte. Observera att [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag)-objektet skickas som parameter till [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)-metoden som faktiskt tillämpar formateringen på en cellområde.

## **Ändra cellers justering och behåll befintlig formatering**

Den följande exempelkoden läser in den [exempel Excel-filen](67338585.xlsx), skapar området och centrera justerar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exempel Excel-filen och [utdata Excel-filen](67338586.xlsx) och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centralt justerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
