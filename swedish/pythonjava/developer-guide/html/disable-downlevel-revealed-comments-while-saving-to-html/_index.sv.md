---
title: Inaktivera kommentarer med låg nivå som upptäcks medan du sparar till HTML
type: docs
weight: 20
url: /sv/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**
När Excel-filen konverteras till HTML lägger Aspose.Cells till conditionella kommentarer som avslöjas på nedre nivå i den resulterande HTML-filen. Dessa conditionella kommentarer är mest relevanta för äldre versioner av Internet Explorer och är irrelevanta i moderna webbläsare. För ytterligare information om conditionella kommentarer som avslöjas på nedre nivå, besök följande länk

[Conditionell kommentar - Conditionell kommentar avslöjad på nedre nivå](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

För att ta bort conditionella kommentarer som avslöjas på nedre nivå tillhandahåller Aspose.Cells egenskapen [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments). Genom att ange värdet av [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) till **Sant** kommer conditionella kommentarer som avslöjas på nedre nivå att tas bort i den resulterande HTML-filen.

Följande bild visar de conditionella kommentarer som avslöjas på nedre nivå som kommer att tas bort i den resulterande HTML-filen

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
