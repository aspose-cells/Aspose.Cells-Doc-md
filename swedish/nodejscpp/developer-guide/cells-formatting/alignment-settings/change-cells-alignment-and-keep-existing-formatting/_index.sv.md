---
title: Ändra cells justering och behåll befintlig formatering
linktitle: Ändra cells justering och behåll befintlig formatering
description: Använd Aspose.Cells biblioteket för att ändra celljustering och behåll befintlig formatering i Node.js via C++
keywords: Aspose.Cells, Node.js via C++, Celljustering, behåll befintlig formatering
type: docs
weight: 340
url: /sv/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Möjliga användningsscenario**

Ibland vill du ändra justeringen för flera celler men vill också behålla den befintliga formateringen. Aspose.Cells for Node.js via C++ låter dig göra detta med hjälp av [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-)-metoden. Om du sätter den till **true**, kommer justeringsändringar att ske, annars inte. Observera att [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-objektet skickas som parameter till [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)-metoden som faktiskt tillämpar formateringen på ett cellområde.

## **Ändra cellers justering och behåll befintlig formatering**

Den följande exempelkoden läser in den [exempel Excel-filen](67338585.xlsx), skapar området och centrera justerar det horisontellt och vertikalt och behåller den befintliga formateringen intakt. Följande skärmdump jämför exempel Excel-filen och [utdata Excel-filen](67338586.xlsx) och visar att all befintlig formatering av cellerna är densamma förutom att cellerna nu är centralt justerade horisontellt och vertikalt.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
