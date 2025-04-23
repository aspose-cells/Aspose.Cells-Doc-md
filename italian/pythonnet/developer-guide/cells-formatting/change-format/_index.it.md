---
title: Cambia il formato di una cella
description: Come usare la libreria Aspose.Cells per Python via .NET per modificare la formattazione delle celle, incluso font, colore, bordo, ecc. Modificando queste proprietà, hai un controllo maggiore sull aspetto e sulla visualizzazione delle celle.
keywords: Libreria Aspose.Cells per Python via .NET, formattazione delle celle, Python, font, colore, bordo
type: docs
weight: 20
url: /it/python-net/how-to-change-format-of-cell/
---

## **Possibili Scenari di Utilizzo**
Quando si desidera evidenziare determinati dati, è possibile modificare lo stile delle celle.

## **Come cambiare il formato di una cella in Excel**

Per cambiare il formato di una singola cella in Excel, seguire questi passaggi:

1. Apri Excel e apri il foglio di lavoro che contiene la cella da formattare.

2. Trova la cella che si desidera formattare.

3. Fai clic con il pulsante destro del mouse sulla cella e seleziona "Formato celle" dal menu contestuale. In alternativa, è possibile selezionare la cella e andare alla scheda Home nel nastro di Excel, fare clic sul menu a discesa "Formato" nel gruppo "Celle" e selezionare "Formato celle".

4. Comparirà la finestra di dialogo "Formato celle". Qui è possibile scegliere varie opzioni di formattazione da applicare alla cella selezionata. Ad esempio, è possibile cambiare lo stile del carattere, la dimensione del carattere, il colore del carattere, il formato numerico, i bordi, il colore di sfondo, ecc. Esplora le diverse schede nella finestra di dialogo per accedere alle varie opzioni di formattazione.

5. Dopo aver apportato le modifiche di formattazione desiderate, fare clic sul pulsante "OK" per applicare la formattazione alla cella selezionata.


## **Come cambiare il formato di una cella utilizzando C#**

Per cambiare il formato di una cella usando Aspose.Cells per Python via .NET, puoi usare i seguenti metodi:
1. [Cell.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style)
2. [Cell.set_style(stile, flag_esplicito)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-bool)
3. [Cell.set_style(stile, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-aspose.cells.StyleFlag)


## **Codice di Esempio**
In questo esempio, creiamo un workbook di Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e otteniamo due celle ("A2" e "B3"). Quindi, otteniamo lo stile della cella, impostiamo varie opzioni di formattazione (ad esempio, colore del font, grassetto) e cambiamo il formato della cella. Infine, salviamo il workbook in un nuovo file.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-change-format.py" >}}

