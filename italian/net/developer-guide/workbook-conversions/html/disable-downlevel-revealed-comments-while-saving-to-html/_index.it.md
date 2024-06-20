---
title: Disabilitare i commenti rivelati di livello inferiore durante il salvataggio in formato HTML
type: docs
weight: 20
url: /it/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Possibili Scenari di Utilizzo**

Quando si salva il file Excel in HTML, Aspose.Cells mostra commenti condizionali di livello inferiore. Questi commenti condizionali sono principalmente rilevanti per le versioni precedenti di Internet Explorer e non sono rilevanti per i moderni browser web. È possibile leggere informazioni dettagliate al seguente link.

- [Commento condizionale - Commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells consente di eliminare questi Commenti Rivelati di Livello Inferiore impostando la proprietà [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) su **true**.

## **Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML**

Il seguente codice di esempio mostra l'uso della proprietà [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments). La schermata mostra l'effetto di questa proprietà quando non è impostata su **true**. Si prega di scaricare il [file Excel di esempio](50528257.xlsx) utilizzato in questo codice e l'[HTML di output](50528258.zip) generato da esso per un riferimento.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
