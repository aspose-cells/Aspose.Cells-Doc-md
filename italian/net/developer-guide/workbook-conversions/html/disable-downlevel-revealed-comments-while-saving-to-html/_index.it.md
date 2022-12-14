---
title: Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML
type: docs
weight: 20
url: /it/net/disable-downlevel-revealed-comments-while-saving-to/
---
## **Possibili scenari di utilizzo**

Quando salvi il tuo file Excel in HTML, Aspose.Cells rivela commenti condizionali di livello inferiore. Questi commenti condizionali sono per lo più rilevanti per le versioni precedenti di Internet Explorer e sono irrilevanti per i browser Web moderni. Puoi leggerli in dettaglio al seguente link.

- [Commento condizionale: commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells consente di eliminare questi commenti rivelati di livello inferiore impostando l'estensione[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) proprietà a**VERO**.

## **Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML**

Il codice di esempio seguente mostra l'utilizzo di[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) proprietà. Lo screenshot mostra l'effetto di questa proprietà quando non è impostata su true. Si prega di scaricare il[esempio di file Excel](50528257.xlsx) utilizzato in questo codice e il[output HTML](50528258.zip) generato da esso per un riferimento.

![cose da fare:immagine_alt_testo](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
