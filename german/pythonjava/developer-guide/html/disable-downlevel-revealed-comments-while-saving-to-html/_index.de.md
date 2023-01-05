---
title: Deaktivieren Sie aufgedeckte Kommentare auf niedrigerem Niveau, während Sie unter HTML speichern
type: docs
weight: 20
url: /de/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **Deaktivieren Sie aufgedeckte Kommentare auf niedrigerem Niveau, während Sie unter HTML speichern**
Wenn die Excel-Datei in HTML konvertiert wird, fügt Aspose.Cells in der Ausgabedatei HTML aufgedeckte bedingte Kommentare der unteren Ebene hinzu. Diese bedingten Kommentare sind hauptsächlich für alte Versionen von Internet Explorer relevant und in den modernen Browsern irrelevant. Weitere Informationen zu auf niedriger Ebene aufgedeckten bedingten Kommentaren finden Sie unter folgendem Link

[Bedingter Kommentar – Bedingter Kommentar, der auf einer niedrigeren Ebene offenbart wurde](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Um von Downlevel aufgedeckte bedingte Kommentare zu entfernen, bietet Aspose.Cells die[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)Eigentum. Einstellung der[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) Eigentum zu**Wahr**entfernt die von Downlevel offenbarten bedingten Kommentare in der Ausgabedatei HTML.

Das folgende Bild zeigt die von Downlevel offenbarten bedingten Kommentare, die in der Ausgabedatei HTML entfernt werden

![todo: Bild_alt_Text](Disable-Downlevel-Revealed-Comments.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
