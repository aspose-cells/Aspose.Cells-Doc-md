---
title: Deaktivieren von Downlevel Revealed Kommentaren beim Speichern als HTML
type: docs
weight: 20
url: /de/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, zeigt Aspose.Cells for Python via .NET die Downlevel Conditional Comments an. Diese bedingten Kommentare sind hauptsächlich für ältere Versionen des Internet Explorers relevant und für moderne Webbrowser unwichtig. Mehr Details finden Sie unter dem folgenden Link.

- [Bedingter Kommentar - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Python via .NET ermöglicht es, diese Downlevel Revealed Comments zu entfernen, indem Sie die [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments)-Eigenschaft auf **true** setzen.

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**

Das folgende Beispiel zeigt die Verwendung der [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments)-Eigenschaft. Der Screenshot zeigt die Wirkung dieser Eigenschaft, wenn sie nicht auf **true** gesetzt ist. Bitte laden Sie die [Beispiel-Excel-Datei](50528257.xlsx) herunter, die in diesem Code verwendet wurde, sowie die [generierte Ausgabe-HTML](50528258.zip) zur Referenz.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
