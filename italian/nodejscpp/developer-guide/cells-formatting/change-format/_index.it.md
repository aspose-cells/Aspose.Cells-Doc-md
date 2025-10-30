---
title: Cambia il formato di una cella
linktitle: Cambia il formato di una cella
description: Come usare la libreria Aspose.Cells in Node.js tramite C++ per modificare la formattazione delle celle, inclusi font, colore, bordo, ecc. Modificando queste proprietà, hai più controllo sull aspetto delle celle.
keywords: Aspose.Cells, formattazione delle celle, Node.js tramite C++, font, colore, bordo
type: docs
weight: 20
url: /it/nodejs-cpp/how-to-change-format-of-cell/
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


## **Come modificare il formato di una cella utilizzando Node.js**

Per modificare il formato di una cella usando Aspose.Cells, puoi usare i seguenti metodi:
1. [Cell.setStyle(Style)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)
2. [Cell.setStyle(Style, explicitFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-boolean-)
3. [Cell.setStyle(Style, StyleFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-styleflag-)


## **Codice di Esempio**
In questo esempio, creiamo una cartella di lavoro Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e otteniamo due celle ("A2" e "B3"). Quindi, otteniamo lo stile della cella, impostiamo varie opzioni di formattazione (ad esempio, colore del font, grassetto) e cambiamo il formato della cella. Infine, salviamo la cartella di lavoro in un nuovo file.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ChangeFormat.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
