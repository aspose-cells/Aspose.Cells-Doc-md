---
title: Deaktivieren von Downlevel Revealed Kommentaren beim Speichern als HTML
type: docs
weight: 20
url: /de/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als HTML speichern, zeigt Aspose.Cells Downlevel-Bedingte Kommentare an. Diese bedingten Kommentare sind größtenteils relevant für alte Versionen von Internet Explorer und sind für moderne Webbrowser irrelevant. Sie können sie im Detail unter dem folgenden Link nachlesen.

- [Bedingter Kommentar - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells ermöglicht es Ihnen, diese Downlevel Revealed Comments zu eliminieren, indem Sie die [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) Eigenschaft auf true setzen.

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**

Der folgende Beispielcode zeigt die Verwendung der [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) Eigenschaft. Der Screenshot zeigt den Effekt dieser Eigenschaft, wenn sie nicht auf true gesetzt ist. Bitte laden Sie die im Code verwendete [Beispiel-Excel-Datei](50528267.xlsx) und die generierte [Ausgabe-HTML-Datei](50528266.zip) herunter, um eine Referenz zu erhalten.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
