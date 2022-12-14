---
title: Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML
type: docs
weight: 20
url: /it/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **Possibili scenari di utilizzo**

Quando salvi il tuo file Excel in HTML, Aspose.Cells rivela i commenti condizionali di livello inferiore. Questi commenti condizionali sono per lo più rilevanti per le vecchie versioni di Internet Explorer e sono irrilevanti per i browser Web moderni. Puoi leggerli in dettaglio al seguente link.

- [Commento condizionale: commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells consente di eliminare questi commenti rivelati di livello inferiore impostando l'estensione[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)proprietà a**VERO**.

## **Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML**

Il codice di esempio seguente mostra l'utilizzo di[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) proprietà. Lo screenshot mostra l'effetto di questa proprietà quando non è impostata su**VERO**Si prega di scaricare il[esempio di file Excel](50528267.xlsx)utilizzato in questo codice e il[output HTML](50528266.zip)file generato da esso per un riferimento.

![cose da fare:immagine_alt_testo](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
