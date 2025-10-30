---
title: Utdata tom sida när det inte finns något att skriva ut
type: docs
weight: 90
url: /sv/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **Möjliga användningsscenario**

Om bladet är tomt kommer Aspose.Cells för Python via .NET inte att skriva ut något när du exporterar arbetsblad till bild. Du kan ändra detta beteende med hjälp av [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) egenskapen. När du ställer in den på **true** kommer den att skriva ut en tom sida.

## **Utdata tom sida när det inte finns något att skriva ut**

Följande exempelkod skapar den tomma arbetsboken som har ett tomt kalkylblad och renderar det tomma kalkylbladet till en bild efter att ha ställt in [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print)-egenskapen som **true**. Följaktligen genererar den den tomma sidan eftersom det inte finns något att skriva ut, vilket du kan se i bilden nedan.

![todo:image_alt_text](1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
