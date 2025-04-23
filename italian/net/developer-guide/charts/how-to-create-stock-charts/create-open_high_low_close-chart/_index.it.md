---
title: Crea un grafico di scorta Open High Low Close (OHLC)
description: Scopri come creare un grafico di stock open high low close utilizzando Aspose.Cells for .NET. La nostra guida ti mostrerà come tracciare i dati di mercato azionario, inclusi i prezzi di apertura, alti, bassi e di chiusura, su un grafico per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for .NET, Grafico di stock Open High Low Close, Dati di mercato azionario, Analisi, Visualizzazione.
type: docs
weight: 182
url: /it/net/create-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il grafico Open-High-Low-Close (OHLC) utilizza cinque colonne di dati, in ordine: categoria, apertura, alta, bassa e chiusura. L'intervallo di prezzi in ogni categoria è nuovamente indicato da una linea verticale, mentre l'intervallo tra apertura e chiusura è dato da una barra galleggiante più ampia; se il prezzo aumenta nella categoria (chiusura è superiore all'apertura), la barra è riempita con un colore, mentre se il prezzo diminuisce, la barra è riempita con un altro. Questo tipo di grafico è spesso chiamato grafico a candela.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Miglioramenti della visibilità nel grafico**
Spesso usiamo i colori invece che il bianco e nero per indicare i prezzi in aumento e in diminuzione. Nel primo set di candele di seguito, il rosso mostra i prezzi in aumento e il verde i prezzi in diminuzione.

![todo:image_alt_text](sample2.png)
## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
