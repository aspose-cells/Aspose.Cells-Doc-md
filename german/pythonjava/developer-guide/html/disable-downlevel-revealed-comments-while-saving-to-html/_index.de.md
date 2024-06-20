---
title: Deaktivieren von Downlevel Revealed Kommentaren beim Speichern als HTML
type: docs
weight: 20
url: /de/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**
Wenn eine Excel-Datei in HTML konvertiert wird, fügt Aspose.Cells Downlevel-revealed bedingte Kommentare in die Ausgabedatei ein. Diese bedingten Kommentare sind hauptsächlich für alte Versionen des Internet Explorers relevant und in modernen Browsern irrelevant. Für weitere Informationen zu Downlevel-revealed bedingten Kommentaren besuchen Sie bitte den folgenden Link

[Bedingter Kommentar - Downlevel-revealed bedingter Kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Um Downlevel-revealed bedingte Kommentare zu entfernen, bietet Aspose.Cells die Eigenschaft [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) an. Durch Setzen der Eigenschaft [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) auf **True** werden die Downlevel-revealed bedingten Kommentare in der Ausgabedatei entfernt.

Das folgende Bild zeigt die Downlevel-revealed bedingten Kommentare, die aus der Ausgabedatei entfernt werden

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
