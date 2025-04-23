---
title: Generera bilder för betingad formatering DataBars
linktitle: Generera bilder för betingad formatering DataBars
description: Aspose.Cells är ett Node.js bibliotek för att arbeta med kalkylbladsfiler. Det stödjer generering av villkorsstyrda datastaplar och bilder, vilket gör att användare kan anpassa visningen av kalkylbladet baserat på cellernas värde. Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att generera villkorsstyrda datastaplar och bilder.
keywords: Aspose.Cells, Villkorsstyrd formatering, Datastaplar, Bilder, Kalkylblad, Node.js via C++
type: docs
weight: 40
url: /sv/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilder på DataBars för betingad formatering. Du kan använda Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-)-metod för att generera dessa bilder. Denna artikel visar hur man genererar en DataBar-bild med hjälp av Aspose.Cells.

{{% /alert %}}

Följande exempel genererar Datastapeln för cell C1. Först accessar den formateringsvillkoret för cellen, och därefter från detta objekt accessar den [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar)-objektet och använder dess [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-)-metod för att generera bilden av cellen. Slutligen sparas bilden på disken.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

