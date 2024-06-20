---
title: Formato intervalli
type: docs
weight: 105
url: /it/python-net/how-to-format-a-range/
description: Questo articolo descrive come formattare gli intervalli con Aspose.Cells per la libreria Python via .NET.
keywords: Libreria Python Excel, Python Come formattare un intervallo, Python Come formattare intervalli.
---

## **Possibili Scenari di Utilizzo**
Quando hai bisogno di applicare uno stile a un intervallo, puoi utilizzare la formattazione dell'intervallo.

## **Come formattare un intervallo in Excel**

Per formattare un intervallo di celle in Excel, puoi utilizzare le opzioni di formattazione integrate fornite da Excel. Ecco come puoi formattare direttamente un intervallo di celle in Excel:

1. Apri Excel e apri il foglio di lavoro che contiene l'intervallo che desideri formattare.

2. Seleziona l'intervallo di celle che desideri formattare. Puoi fare clic e trascinare per selezionare l'intervallo, oppure puoi utilizzare scorciatoie da tastiera come Maiusc + frecce per estendere la selezione.

3. Una volta selezionato l'intervallo, fai clic con il pulsante destro del mouse sull'intervallo selezionato e scegli "Formatta celle" dal menu contestuale. In alternativa, puoi andare alla scheda Home nella barra dei menu di Excel, fare clic sulla voce "Formato" nel gruppo "Celle" e selezionare "Formatta celle".

4. La finestra di dialogo "Formatta celle" apparirà. Qui puoi scegliere varie opzioni di formattazione da applicare all'intervallo selezionato. Ad esempio, puoi cambiare lo stile del carattere, la dimensione del carattere, il colore del carattere, il formato numero, i bordi, il colore di sfondo, ecc. Esplora le diverse schede nella finestra di dialogo per accedere a varie opzioni di formattazione.

5. Dopo aver apportato le modifiche di formattazione desiderate, fai clic sul pulsante "OK" per applicare la formattazione all'intervallo selezionato.


## **Come formattare un intervallo usando C#**

Per formattare un intervallo utilizzando Aspose.Cells, puoi utilizzare i seguenti metodi:
1. [Range.apply_style(style, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag)
2. [Range.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style)
3. [Range.set_style(style, explicit_flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style-bool)


## **Codice di Esempio**
In questo esempio, creiamo un foglio di lavoro Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e definiamo due intervalli("A1:C3" e "A4:C5"). Poi, creiamo nuovi stili, impostiamo varie opzioni di formattazione (ad esempio, colore del carattere, grassetto) e applichiamo lo stile all'intervallo. Infine, salviamo il foglio di lavoro in un nuovo file.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-FormatRanges.py" >}}
