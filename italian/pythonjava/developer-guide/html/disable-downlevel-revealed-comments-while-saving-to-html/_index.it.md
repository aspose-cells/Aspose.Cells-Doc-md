---
title: Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML
type: docs
weight: 20
url: /it/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML**
Quando il file Excel viene convertito in HTML, Aspose.Cells aggiunge commenti condizionali rivelati di livello inferiore nel file HTML di output. Questi commenti condizionali sono per lo più rilevanti per le vecchie versioni di Internet Explorer e sono irrilevanti nei browser moderni. Per ulteriori informazioni sui commenti condizionali rivelati di livello inferiore, visitare il seguente collegamento

[Commento condizionale: commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Per rimuovere i commenti condizionali rivelati di livello inferiore, Aspose.Cells fornisce il file[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)proprietà. Impostazione del[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) proprietà a**Vero**rimuoverà i commenti condizionali rivelati di livello inferiore nel file HTML di output.

L'immagine seguente mostra i commenti condizionali rivelati di livello inferiore che verranno rimossi nel file HTML di output

![cose da fare:immagine_alt_testo](Disable-Downlevel-Revealed-Comments.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
