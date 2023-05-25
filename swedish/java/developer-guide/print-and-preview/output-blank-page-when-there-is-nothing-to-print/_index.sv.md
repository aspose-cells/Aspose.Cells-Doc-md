---
title: Skriv ut tom sida när det inte finns något att skriva ut
type: docs
weight: 80
url: /sv/java/output-blank-page-when-there-is-nothing-to-print/
---
##  **Möjliga användningsscenarier**

Om arket är tomt kommer Aspose.Cells inte att skriva ut något när du exporterar kalkylblad till bild. Du kan ändra detta beteende genom att använda[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)fast egendom. När du ställer in den på *true** kommer den att skriva ut den tomma sidan.

##  **Skriv ut tom sida när det inte finns något att skriva ut**

Följande exempelkod skapar den tomma arbetsboken som har ett tomt kalkylblad och renderar det tomma kalkylbladet till en bild efter att ha ställt in[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)egendom som *sann**. Följaktligen genererar den den tomma sidan eftersom det inte finns något att skriva ut som du kan se nedan.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
