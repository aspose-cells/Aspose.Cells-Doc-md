---
title: Come creare un grafico dinamico a scorrimento
description: Scopri come creare un grafico dinamico a scorrimento utilizzando Aspose.Cells for .NET. La nostra guida dimostrerà come implementare transizioni dati regolari e medie mobili nel tuo grafico per una visualizzazione continuativa e aggiornata.
keywords: Aspose.Cells for .NET, Grafico Dinamico a Scorrimento, Transizioni Dati, Medie Regolari, Visualizzazione Continua, Aggiornamento della Visualizzazione.
type: docs
weight: 74
url: /it/net/create-dynamic-rolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento si riferisce a una rappresentazione grafica che visualizza costantemente punti dati in continuo spostamento e aggiornamento nel tempo. È un tipo di grafico che si aggiorna continuamente, mostrando una finestra mobile dei punti dati più recenti mentre scarta i punti dati più vecchi man mano che ne arrivano di nuovi.

I grafici dinamici a scorrimento sono comunemente utilizzati per visualizzare tendenze e pattern in dati in tempo reale o in streaming. Sono particolarmente utili in scenari in cui gli aspetti temporali e i cambiamenti nel tempo sono fondamentali, come l'analisi di mercato azionario, il monitoraggio meteorologico o il tracciamento delle performance in tempo reale.

Questi grafici di solito impiegano meccanismi di animazione o autoscrolling per assicurare che le informazioni più aggiornate siano sempre presentate. La lunghezza della finestra mobile può essere personalizzata per mostrare un periodo temporale specifico, come l'ultima ora, giorno o settimana.

In sintesi, un grafico dinamico a scorrimento è una rappresentazione grafica continuamente aggiornata che visualizza gli ultimi punti dati mentre scarta quelli più vecchi, consentendo agli utenti di osservare tendenze e pattern in tempo reale.

## **Usa Aspose Cells per creare un grafico dinamico a scorrimento**
Nei paragrafi successivi, ti mostreremo come creare un grafico dinamico a scorrimento utilizzando Aspose.Cells. Ti mostreremo il codice dell'esempio, nonché il file Excel creato con questo codice.

## **Codice di Esempio**
Il seguente codice di esempio genererà il [File del Grafico Dinamico a Scorrimento](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

## **Note**
Nel file generato, puoi continuare ad aggiungere dati nelle colonne A e B, mentre il grafico conta dinamicamente gli ultimi 5 set di dati. Ciò viene fatto utilizzando la formula "SCARTO" nel codice di esempio:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puoi provare a cambiare il numero "-5" in "-10" nella formula, e il grafico dinamico conterà gli ultimi 10 set di dati. Ora abbiamo creato con successo un grafico dinamico a scorrimento utilizzando Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
