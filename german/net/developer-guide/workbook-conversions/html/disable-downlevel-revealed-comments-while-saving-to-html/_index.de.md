---
title: Deaktivieren von Downlevel Revealed Kommentaren beim Speichern als HTML
type: docs
weight: 20
url: /de/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, zeigt Aspose.Cells Downlevel Conditional Comments an. Diese bedingten Kommentare sind meist relevant für ältere Versionen von Internet Explorer und sind für moderne Webbrowser irrelevant. Sie können Details dazu unter folgendem Link nachlesen.

- [Bedingter Kommentar - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Mit Aspose.Cells können Sie diese Downlevel Revealed Comments beseitigen, indem Sie die [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)-Eigenschaft auf **true** setzen.

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**

Das folgende Beispiel zeigt die Verwendung der [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)-Eigenschaft. Der Screenshot zeigt die Wirkung dieser Eigenschaft, wenn sie nicht auf **true** gesetzt ist. Bitte laden Sie die [Beispiel-Excel-Datei](50528257.xlsx) herunter, die in diesem Code verwendet wurde, sowie die [generierte Ausgabe-HTML](50528258.zip) zur Referenz.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
