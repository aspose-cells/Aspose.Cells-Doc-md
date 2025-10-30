---
title: Come ottenere la posizione dell oggetto nel grafico
description: Impara come ottenere le posizioni degli oggetti nei grafici Excel usando Aspose.Cells for .NET. 
keywords: Aspose.Cells for .NET, Grafico Excel, Ottieni le posizioni degli oggetti.
type: docs
weight: 74
url: /it/net/how-to-get-object-position-in-chart/
---

## Possibili scenari di utilizzo
In alcuni scenari, quando si utilizza un grafico Excel, potrebbe essere necessario ottenere la posizione degli oggetti nel grafico. Puoi facilmente raggiungere questo obiettivo con Aspose.Cells.

## Esempio: ottieni la posizione dell'oggetto nel grafico

Il seguente esempio di codice carica il [file Excel di esempio](TestFile.xlsx) e genera il [file Excel di output](Output.xlsx).
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

Con il codice sopra, puoi ottenere la posizione del titolo del grafico e dell'area di trama del grafico. 
Con le informazioni di posizione, le forme possono essere posizionate nella posizione corrispondente nel grafico. 
Il risultato è mostrato nell'immagine seguente, dove una forma è posizionata nell'angolo in alto a sinistra dell'area di trama e l'altra forma è posizionata sotto il titolo del grafico.
![todo:image_alt_text](OutputResult.png)

## Spiegazione dell'unità e conversione

Ci sono tre unità per la posizione dell'oggetto nel grafico:

1. Unità di rapporto dell'area di grafico.

2. Unità di 1/4000 dell'area di grafico. Questa è un'unità usata nelle versioni precedenti di Excel e non è consigliata.

3. Unità di pixel.

Il codice di conversione di essi viene mostrato nel seguente codice: 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
