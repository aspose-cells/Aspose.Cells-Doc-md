---
title: Accedi e aggiorna le porzioni di Rich Text di Cell
linktitle: Ricco testo di formattazione
type: docs
weight: 440
url: /it/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells consente di accedere e aggiornare le porzioni del rich text della cella. A tale scopo, è possibile utilizzare i metodi Cell.getCharacters() e Cell.setCharacters(). Questi metodi restituiranno e accetteranno l'array di oggetti FontSetting che è possibile utilizzare per accedere e aggiornare varie proprietà del carattere come nome del carattere, colore del carattere, grassetto ecc.

{{% /alert %}} 
## **Accedi e aggiorna le porzioni di Rich Text di Cell**
 Il codice seguente mostra l'utilizzo del metodo Cell.getCharacters() e Cell.setCharacters() utilizzando il[file excel di origine](5472937.xlsx) che puoi scaricare dal link fornito. Il file excel di origine ha un rich text nella cella A1. Ha 3 porzioni e ogni porzione ha un carattere diverso. Accederemo a queste parti e aggiorneremo la prima parte con il nuovo nome del font. Infine salva la cartella di lavoro come[file excel di output](5472930.xlsx) . Quando lo aprirai, scoprirai che il carattere della prima parte del testo è cambiato in**"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Uscita console**
 Ecco l'output della console del codice di esempio precedente utilizzando il file[file excel di origine](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
