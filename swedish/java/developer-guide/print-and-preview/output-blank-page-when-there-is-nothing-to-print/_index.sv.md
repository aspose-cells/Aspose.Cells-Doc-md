---
title: Utdata tom sida när det inte finns något att skriva ut
type: docs
weight: 80
url: /sv/java/output-blank-page-when-there-is-nothing-to-print/
---

## **Möjliga användningsscenario**

Om bladet är tomt kommer Aspose.Cells inte att skriva ut något när du exporterar arbetsblad till bild. Du kan ändra detta beteende genom att använda [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) egenskapen. När du ställer in den till **true**, kommer den att skriva ut den tomma sidan.

## **Utdata tom sida när det inte finns något att skriva ut**

Följande exempelkod skapar den tomma arbetsboken som har en tom kalkylblad och renderar det tomma kalkylbladet till en bild efter att [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)-egenskapen har ställts in som **true**. Följaktligen genererar den en tom sida eftersom det inte finns något att skriva ut vilket du kan se nedan.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
{{< app/cells/assistant language="java" >}}
