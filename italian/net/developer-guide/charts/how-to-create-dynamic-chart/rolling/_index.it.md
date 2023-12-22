---
title: Come creare una tabella mobile dinamica
description: Scopri come creare un grafico mobile dinamico utilizzando Aspose.Cells for .NET. La nostra guida mostrerà come implementare transizioni fluide dei dati e medie mobili nel grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /it/net/create-dynamic-rolling-chart/
---
##  **Possibili scenari di utilizzo**
Un grafico mobile dinamico si riferisce a una rappresentazione grafica che mostra i punti dati che cambiano e si aggiornano costantemente nel tempo. È un tipo di grafico che si aggiorna continuamente, mostrando una finestra mobile dei punti dati più recenti mentre scarta i punti dati più vecchi man mano che ne arrivano di nuovi.

grafici dinamici vengono comunemente utilizzati per visualizzare tendenze e modelli in dati in tempo reale o in streaming. Sono particolarmente utili in scenari in cui gli aspetti temporali e i cambiamenti nel tempo sono critici, come l'analisi del mercato azionario, il monitoraggio meteorologico o il monitoraggio delle prestazioni in tempo reale.

Questi grafici in genere utilizzano meccanismi di animazione o di scorrimento automatico per garantire che siano sempre presentate le informazioni più aggiornate. La lunghezza della finestra scorrevole può essere personalizzata per mostrare un periodo di tempo specifico, come l'ultima ora, giorno o settimana.

In sintesi, un grafico dinamico è una rappresentazione grafica continuamente aggiornata che mostra i dati più recenti scartando quelli più vecchi, consentendo agli utenti di osservare tendenze e modelli in tempo reale.

##  **Utilizza Aspose Cells per creare un grafico a rotazione dinamico**
Nei prossimi paragrafi ti mostreremo come creare un Rolling Chart dinamico utilizzando Aspose.Cells. Ti mostreremo il codice dell'esempio, oltre al file Excel creato con questo codice.

##  **Codice d'esempio**
 Il seguente codice di esempio genererà il file[File grafico dinamico](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

##  **Appunti**
Nel file generato, puoi continuare ad aggiungere dati nelle colonne A e B, mentre il grafico conta dinamicamente gli ultimi 5 set di dati. Questo viene fatto utilizzando la formula "OFFSET" nel codice di esempio:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puoi provare a cambiare il numero "-5" in "-10" nella formula e il grafico dinamico conterà gli ultimi 10 set di dati. Ora abbiamo creato un grafico dinamico utilizzando con successo Aspose.Cells.
