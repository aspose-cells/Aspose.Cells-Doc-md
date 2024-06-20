---
title: Accedere e aggiornare le porzioni di testo arricchito della cella
linktitle: Formattazione del testo arricchito
type: docs
weight: 440
url: /it/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells ti consente di accedere e aggiornare le porzioni di testo arricchito della cella. A questo scopo, è possibile utilizzare i metodi Cell.getCharacters() e Cell.setCharacters(). Questi metodi restituiranno e accetteranno l'array di oggetti FontSetting che è possibile utilizzare per accedere e aggiornare varie proprietà del font come il nome del font, il colore del font e il grassetto ecc.

{{% /alert %}} 
## **Accedere e aggiornare le porzioni di testo arricchito della cella**
Il seguente codice dimostra l'utilizzo dei metodi Cell.getCharacters() e Cell.setCharacters() utilizzando il [file excel di origine](5472937.xlsx) che puoi scaricare dal link fornito. Il file excel di origine ha un testo arricchito nella cella A1. Ha 3 porzioni e ciascuna porzione ha un font diverso. Accederemo a queste porzioni e aggiorneremo la prima porzione con il nuovo nome del font. Infine salva il foglio di lavoro come [file excel di output](5472930.xlsx). Quando lo aprirai, troverai che il font della prima porzione del testo è stato cambiato in **"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Output della console**
Ecco l'output della console del codice di esempio usando il [file excel di origine](5472937.xlsx).

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
