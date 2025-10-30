---
title: Deaktivieren Sie Downlevel Revealed Comments beim Speichern als HTML mit Golang über C++
linktitle: Downlevel Revealed Comments deaktivieren
type: docs
weight: 20
url: /de/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Eliminieren Sie Downlevel Revealed Comments , wenn Sie Excel Dateien mit Aspose.Cells mit Golang über C++ in HTML speichern.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als HTML speichern, zeigt Aspose.Cells Downlevel Conditional Comments. Diese bedingten Kommentare sind hauptsächlich für ältere Versionen des Internet Explorers relevant und für moderne Webbrowser irrelevant. Sie können sie im Detail unter dem folgenden Link lesen.

- [Bedingter Kommentar - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells ermöglicht es Ihnen, diese Downlevel Revealed Comments zu eliminieren, indem Sie die [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-Eigenschaft auf **true** setzen.

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**

Das folgende Beispiel zeigt die Verwendung der [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-Eigenschaft. Das Bild zeigt die Wirkung dieser Eigenschaft, wenn sie nicht auf true gesetzt ist. Bitte laden Sie die in diesem Code verwendete Beispiel-Excel-Datei ([50528257.xlsx](50528257.xlsx)) und den generierten [Ausgabe-HTML-Code](50528258.zip) herunter.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
