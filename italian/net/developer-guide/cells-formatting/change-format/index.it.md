---
title: Cambia il formato di una cella
description: Come utilizzare la libreria Aspose.Cells in C# per modificare la formattazione delle celle, inclusi carattere, colore, bordo, ecc. Regolando queste proprietà, hai un maggiore controllo sull'aspetto e sulla visualizzazione delle celle.
keywords: Aspose.Cells, cell formatting, C#, font, color, border
type: docs
weight: 105
url: /it/net/how-to-change-format-of-cell/
---
##  **Possibili scenari di utilizzo**
Quando desideri evidenziare determinati dati, puoi modificare lo stile delle celle.

##  **Come modificare il formato di una cella in Excel**

Per modificare il formato di una singola cella in Excel, attenersi alla seguente procedura:

1. Apri Excel e apri la cartella di lavoro che contiene la cella che desideri formattare.

2. Individua la cella che desideri formattare.

3. Fare clic con il tasto destro sulla cella e selezionare "Formato Cells" dal menu contestuale. In alternativa, puoi selezionare la cella e andare alla scheda Home nella barra multifunzione di Excel, fare clic sul menu a discesa "Formato" nel gruppo "Cells" e selezionare "Formato Cells".

4. Apparirà la finestra di dialogo "Formato Cells". Qui puoi scegliere varie opzioni di formattazione da applicare alla cella selezionata. Ad esempio, puoi modificare lo stile del carattere, la dimensione del carattere, il colore del carattere, il formato dei numeri, i bordi, il colore dello sfondo, ecc. Esplora le diverse schede nella finestra di dialogo per accedere a varie opzioni di formattazione.

5. Dopo aver apportato le modifiche di formattazione desiderate, fare clic sul pulsante "OK" per applicare la formattazione alla cella selezionata.


##  **Come cambiare il formato di una cella utilizzando C#**

Per modificare il formato di una cella utilizzando Aspose.Cells, puoi utilizzare Puoi utilizzare i seguenti metodi:
1. [Cell.SetStyle(Stile stile)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Stile stile, bool esplicitamenteFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Stile stile, flag StyleFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


##  **Codice d'esempio**
In questo esempio creiamo una cartella di lavoro Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e otteniamo due celle ("A2" e "B3"). Successivamente, otteniamo lo stile della cella, impostiamo varie opzioni di formattazione (ad esempio, colore del carattere, grassetto) e modifichiamo il formato della cella. Infine, salviamo la cartella di lavoro in un nuovo file.
![cose da fare:immagine_alt_testo](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
