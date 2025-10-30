---
title: Crea un grafico azioni Open High Low Close (OHLC) con Golang via C++
description: Impara come creare un grafico azioni open high low close usando Aspose.Cells for C++. La nostra guida dimostrerà come tracciare i dati del mercato azionario, inclusi i prezzi di apertura, massimo, minimo e chiusura, per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for C++, Grafico azioni Open High Low Close, Dati di Mercato, Analisi, Visualizzazione.
type: docs
weight: 182
url: /it/go-cpp/create-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il grafico Open-High-Low-Close (OHLC) utilizza cinque colonne di dati, in ordine: categoria, apertura, alta, bassa e chiusura. L'intervallo di prezzi in ogni categoria è nuovamente indicato da una linea verticale, mentre l'intervallo tra apertura e chiusura è dato da una barra galleggiante più ampia; se il prezzo aumenta nella categoria (chiusura è superiore all'apertura), la barra è riempita con un colore, mentre se il prezzo diminuisce, la barra è riempita con un altro. Questo tipo di grafico è spesso chiamato grafico a candela.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Miglioramenti della visibilità nel grafico**
Spesso usiamo colori anziché bianco e nero per indicare prezzi in aumento e diminuzione. Nel primo set di candlestick sottostante, il rosso mostra prezzi in aumento e il verde in diminuzione.

![todo:image_alt_text](sample2.png)

## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateOpenHighLowCloseChart.go" >}}
