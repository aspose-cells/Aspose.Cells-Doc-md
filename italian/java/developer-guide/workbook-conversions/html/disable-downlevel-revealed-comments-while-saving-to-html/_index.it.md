---
title: Disabilitare i commenti rivelati di livello inferiore durante il salvataggio in formato HTML
type: docs
weight: 20
url: /it/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **Possibili Scenari di Utilizzo**

Quando si salva il file Excel in formato HTML, Aspose.Cells rivela i commenti condizionali di livello inferiore. Questi commenti condizionali sono per lo più pertinenti alle vecchie versioni di Internet Explorer e non sono rilevanti per i moderni browser web. È possibile leggere maggiori dettagli al seguente link.

- [Commento condizionale - Commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells consente di eliminare questi commenti condizionali rivelati di livello inferiore impostando la proprietà [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) su **true**.

## **Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments). La schermata mostra l'effetto di questa proprietà quando non è impostata su **true**. Si prega di scaricare il [file Excel di esempio](50528267.xlsx) utilizzato in questo codice e il file HTML di output (50528266.zip) generato da esso per un riferimento.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
