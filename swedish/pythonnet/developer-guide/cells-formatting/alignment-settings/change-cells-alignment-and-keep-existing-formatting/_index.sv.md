---
title: Ändra cells justering och behåll befintlig formatering
description: Använd biblioteket Aspose.Cells för Python via .NET för att ändra celljustering och bevara befintlig formatering
keywords: Aspose.Cells för Python via .NET, celljustering i Python, bevara befintlig formatering
type: docs
weight: 340
url: /sv/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Möjliga användningsscenario**

Ibland vill du ändra justeringen för flera celler men vill också behålla befintlig formatering. Aspose.Cells för Python via .NET tillåter detta med hjälp av egenskapen [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments). Om du sätter den till **true** kommer justeringsändringarna att ske, annars inte. Observera att objektet [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) skickas som parameter till [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style)-metoden, som faktiskt tillämpar formateringen på ett cellområde.

## **Ändra cellers justering och behåll befintlig formatering**

Den följande exempelkoden läser in den [exempel Excel-filen](67338585.xlsx), skapar området och centrera justerar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exempel Excel-filen och [utdata Excel-filen](67338586.xlsx) och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centralt justerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
