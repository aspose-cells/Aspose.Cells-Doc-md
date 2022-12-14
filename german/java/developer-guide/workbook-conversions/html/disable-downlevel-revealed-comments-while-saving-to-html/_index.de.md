---
title: Deaktivieren Sie aufgedeckte Kommentare auf niedrigerer Ebene beim Speichern in HTML
type: docs
weight: 20
url: /de/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie Ihre Excel-Datei im HTML-Format speichern, zeigt Aspose.Cells Downlevel Conditional Comments an. Diese bedingten Kommentare sind hauptsächlich für alte Versionen von Internet Explorer relevant und für moderne Webbrowser irrelevant. Sie können sie im Detail unter folgendem Link nachlesen.

- [Bedingter Kommentar – Bedingter Kommentar, der auf einer niedrigeren Ebene offenbart wurde](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells ermöglicht es Ihnen, diese aufgedeckten Kommentare auf niedrigerem Niveau zu eliminieren, indem Sie das einstellen[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)Eigentum zu**Stimmt**.

## **Deaktivieren Sie aufgedeckte Kommentare auf niedrigerer Ebene beim Speichern in HTML**

Der folgende Beispielcode zeigt die Verwendung von[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) Eigentum. Der Screenshot zeigt die Auswirkung dieser Eigenschaft, wenn sie nicht auf eingestellt ist**Stimmt**Bitte laden Sie die herunter[Beispiel-Excel-Datei](50528267.xlsx)in diesem Code verwendet und die[HTML ausgeben](50528266.zip)von ihm generierte Datei als Referenz.

![todo: Bild_alt_Text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
