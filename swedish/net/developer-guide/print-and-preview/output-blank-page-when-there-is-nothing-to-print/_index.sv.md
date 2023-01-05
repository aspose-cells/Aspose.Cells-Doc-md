---
title: Skriv ut tom sida när det inte finns något att skriva ut
type: docs
weight: 90
url: /sv/net/output-blank-page-when-there-is-nothing-to-print/
---
## **Möjliga användningsscenarier**

 Om arket är tomt kommer Aspose.Cells inte att skriva ut något när du exporterar kalkylblad till bild. Du kan ändra detta beteende genom att använda[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) fast egendom. När du ska ställa in den**Sann**, kommer den att skriva ut den tomma sidan.

## **Skriv ut tom sida när det inte finns något att skriva ut**

Följande exempelkod skapar den tomma arbetsboken som har ett tomt kalkylblad och renderar det tomma kalkylbladet till en bild efter att ha ställt in[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) egendom som**Sann**. Följaktligen genererar den den tomma sidan eftersom det inte finns något att skriva ut som du kan se på bilden nedan.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
