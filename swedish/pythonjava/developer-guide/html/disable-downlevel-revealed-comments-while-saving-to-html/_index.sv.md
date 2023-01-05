---
title: Inaktivera Downlevel Revealed Comments medan du sparar till HTML
type: docs
weight: 20
url: /sv/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **Inaktivera Downlevel Revealed Comments medan du sparar till HTML**
När Excel-filen konverteras till HTML, lägger Aspose.Cells till nednivåavslöjade villkorliga kommentarer i utdatafilen HTML. Dessa villkorliga kommentarer är mestadels relevanta för gamla versioner av Internet Explorer och är irrelevanta i moderna webbläsare. För ytterligare information om villkorliga kommentarer som avslöjas på nednivå, besök följande länk

[Villkorlig kommentar - Nedåtnivå-avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

För att ta bort Downlevel-avslöjade villkorliga kommentarer tillhandahåller Aspose.Cells[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)fast egendom. Ställa in[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) egendom till**Sann**kommer att ta bort de villkorliga kommentarerna som har avslöjats på Downlevel i utdatafilen HTML.

Följande bild visar nednivåavslöjade villkorliga kommentarer som kommer att tas bort i utdatafilen HTML

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
