---
title: Come impostare un punto come totale
description: In alcuni grafici Excel, ad esempio il grafico WaterFall, potrebbe essere necessario impostare il punto come totale. Questo articolo descrive come usare Aspose.Cells per farlo. 
keywords: Grafico WaterFall, Punto, Imposta come totale.
type: docs
weight: 72
url: /it/net/how-to-set-point-as-total/
---

## Cos'è "Impostare il punto come totale" in un grafico Excel

In alcuni grafici Excel, ad esempio il grafico WaterFall, alcuni dati dei punti sono la somma dei punti precedenti, potrebbe essere necessario "impostare il punto come totale". Mostreremo il codice esempio e l'illustrazione di seguito.

## Un grafico WaterFall necessita di "Impostare il punto come totale" 

![todo:image_alt_text](set-as-total1.png)

Questa immagine mostra un grafico WaterFall in Excel. Possiamo vedere che ci sono quattro punti dati che iniziano con "Totale", e sono usati per contare tutti i punti dati precedenti.
In questa immagine, le impostazioni non sono esattamente corrette, quando selezioniamo un punto "Totale 2024" e vediamo che l'opzione "Imposta come totale" non è selezionata in Excel.
Di seguito è allegato il [file Excel di esempio](SampleSheet.xlsx) che necessita di essere modificato, e useremo Aspose.Cells per configurarlo correttamente.

## Usa Aspose.Cells per "Impostare il punto come totale" 

Usiamo il seguente codice per configurare correttamente il file:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Set-point-as-total.cs" >}}

Puoi ottenere il [file di output corretto](output.xlsx)

Come mostrato nell'immagine seguente, i quattro punti dati "Total" sono impostati correttamente, e puoi vedere la differenza rispetto al grafico precedente.

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="csharp" >}}
