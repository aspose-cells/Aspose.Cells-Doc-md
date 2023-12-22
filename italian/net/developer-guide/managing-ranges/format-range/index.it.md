---
title: Intervalli di formato
type: docs
weight: 105
url: /it/net/how-to-format-a-range/
---
##  **Possibili scenari di utilizzo**
Quando devi applicare uno stile a un intervallo, puoi utilizzare la formattazione dell'intervallo.

##  **Come formattare un intervallo in Excel**

Per formattare un intervallo di celle in Excel, puoi utilizzare le opzioni di formattazione integrate fornite da Excel. Ecco come puoi formattare un intervallo di celle direttamente in Excel:

1. Apri Excel e apri la cartella di lavoro che contiene l'intervallo che desideri formattare.

2. Seleziona l'intervallo di celle che desideri formattare. Puoi fare clic e trascinare per selezionare l'intervallo oppure utilizzare scorciatoie da tastiera come Maiusc + tasti freccia per estendere la selezione.

3. Una volta selezionato l'intervallo, fare clic con il pulsante destro del mouse sull'intervallo selezionato e scegliere "Formato Cells" dal menu contestuale. In alternativa, puoi andare alla scheda Home nella barra multifunzione di Excel, fare clic sul menu a discesa "Formato" nel gruppo "Cells" e selezionare "Formato Cells".

4. Apparirà la finestra di dialogo "Formato Cells". Qui puoi scegliere varie opzioni di formattazione da applicare all'intervallo selezionato. Ad esempio, puoi modificare lo stile del carattere, la dimensione del carattere, il colore del carattere, il formato dei numeri, i bordi, il colore dello sfondo, ecc. Esplora le diverse schede nella finestra di dialogo per accedere a varie opzioni di formattazione.

5. Dopo aver apportato le modifiche di formattazione desiderate, fare clic sul pulsante "OK" per applicare la formattazione all'intervallo selezionato.


##  **Come formattare un intervallo utilizzando C#**

Per formattare un intervallo utilizzando Aspose.Cells, puoi utilizzare È possibile utilizzare i seguenti metodi:
1. [Range.ApplyStyle(Stile stile, flag StyleFlag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Stile stile)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Stile stile)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


##  **Codice d'esempio**
In questo esempio creiamo una cartella di lavoro Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e definiamo due intervalli ("A1:C3" e "A4:C5"). Quindi creiamo nuovi stili, impostiamo varie opzioni di formattazione (ad esempio, colore del carattere, grassetto) e applichiamo lo stile all'intervallo. Infine, salviamo la cartella di lavoro in un nuovo file.
![cose da fare:immagine_alt_testo](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
