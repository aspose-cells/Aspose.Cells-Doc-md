---
title: Formato intervalli con Golang tramite C++
linktitle: Formato intervalli
type: docs
weight: 105
url: /it/go-cpp/how-to-format-a-range/
description: Impara come formattare intervalli in Excel usando Aspose.Cells con Golang tramite C++. Applica stili, caratteri e colori agli intervalli di celle programmaticamente.
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

## **Come formattare un intervallo usando C++**

Per formattare un intervallo usando Aspose.Cells, puoi usare i seguenti metodi:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/go-cpp/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/go-cpp/range/setstyle_style_bool/)

## **Codice di Esempio**
In questo esempio, creiamo un workbook Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e definiamo due intervalli ("A1:C3" e "A4:C5"). Poi, creiamo nuovi stili, impostiamo varie opzioni di formattazione (ad esempio colore del carattere, grassetto) e applichiamo lo stile all'intervallo. Infine, salviamo il workbook in un nuovo file.
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatRange.go" >}}
