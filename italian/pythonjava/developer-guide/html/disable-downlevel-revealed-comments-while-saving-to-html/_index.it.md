---
title: Disabilitare i commenti rivelati di livello inferiore durante il salvataggio in formato HTML
type: docs
weight: 20
url: /it/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML**
Quando il file Excel viene convertito in HTML, Aspose.Cells aggiunge commenti condizionali rivelati in discesa nel file HTML di output. Questi commenti condizionali sono principalmente rilevanti per le vecchie versioni di Internet Explorer e sono irrilevanti nei browser moderni. Per ulteriori informazioni sui commenti condizionali rivelati in discesa, si prega di visitare il seguente link

[Commento condizionale - Commento condizionale rivelato in discesa](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Per rimuovere i commenti condizionali rivelati in discesa, Aspose.Cells fornisce la proprietà [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments). Impostando la proprietà [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) su **True** verranno rimossi i commenti condizionali rivelati in discesa nel file HTML di output.

L'immagine seguente mostra i commenti condizionali rivelati in discesa che verranno rimossi nel file HTML di output

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
