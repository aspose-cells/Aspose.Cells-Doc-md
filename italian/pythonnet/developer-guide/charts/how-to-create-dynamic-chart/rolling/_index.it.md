---
title: Come creare un grafico dinamico a scorrimento
description: Impara come creare un grafico mobile dinamico utilizzando Aspose.Cells per Python via .NET. La nostra guida dimostrerà come implementare transizioni di dati fluide e medie mobili nel tuo grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells per Python via .NET, grafico mobile dinamico, transizioni di dati, medie mobili fluide, visualizzazione continua, aggiornamento della visualizzazione.
type: docs
weight: 74
url: /it/python-net/create-dynamic-rolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento si riferisce a una rappresentazione grafica che visualizza costantemente punti dati in continuo spostamento e aggiornamento nel tempo. È un tipo di grafico che si aggiorna continuamente, mostrando una finestra mobile dei punti dati più recenti mentre scarta i punti dati più vecchi man mano che ne arrivano di nuovi.

I grafici dinamici a scorrimento sono comunemente utilizzati per visualizzare tendenze e pattern in dati in tempo reale o in streaming. Sono particolarmente utili in scenari in cui gli aspetti temporali e i cambiamenti nel tempo sono fondamentali, come l'analisi di mercato azionario, il monitoraggio meteorologico o il tracciamento delle performance in tempo reale.

Questi grafici di solito impiegano meccanismi di animazione o autoscrolling per assicurare che le informazioni più aggiornate siano sempre presentate. La lunghezza della finestra mobile può essere personalizzata per mostrare un periodo temporale specifico, come l'ultima ora, giorno o settimana.

In sintesi, un grafico dinamico a scorrimento è una rappresentazione grafica continuamente aggiornata che visualizza gli ultimi punti dati mentre scarta quelli più vecchi, consentendo agli utenti di osservare tendenze e pattern in tempo reale.

## **Usa Aspose.Cells per Python via .NET per creare grafico mobile dinamico**
Nei paragrafi successivi, ti mostreremo come creare un grafico mobile dinamico usando Aspose.Cells per Python via .NET. Mostreremo il codice di esempio, così come il file Excel creato con questo codice.

## **Codice di Esempio**
Il seguente codice di esempio genererà il [File del Grafico Dinamico a Scorrimento](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-rolling-chart.py" >}}

## **Note**
Nel file generato, puoi continuare ad aggiungere dati nelle colonne A e B, mentre il grafico conta dinamicamente gli ultimi 5 set di dati. Ciò viene fatto utilizzando la formula "SCARTO" nel codice di esempio:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puoi provare a cambiare il numero "-5" in "-10" nella formula, e il grafico dinamico conterà gli ultimi 10 set di dati. Ora abbiamo creato con successo un grafico mobile dinamico usando Aspose.Cells per Python via .NET.
