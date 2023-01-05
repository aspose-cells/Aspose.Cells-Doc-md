---
title: Caricamento dei dati GridWeb in modalità asincrona
type: docs
weight: 40
url: /it/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

Quando si crea una cartella di lavoro con set di dati di grandi dimensioni o si legge un file Excel di grandi dimensioni Microsoft, ci vorranno sicuramente più tempo e risorse per farlo. La memoria totale che il processo occuperà è sempre una preoccupazione. Ci sono misure che possono essere adottate per far fronte alla sfida. Aspose.Cells.GridWeb fornisce alcune opzioni e API rilevanti per abbassare, ridurre e ottimizzare l'utilizzo della memoria. Inoltre, può aiutare il processo a funzionare in modo più efficiente e a funzionare più velocemente. Per un foglio di lavoro che contiene dati di celle di grandi dimensioni, è possibile caricare il set di dati in modo asincrono per migliorare le prestazioni complessive per l'esperienza dell'utente.

{{% /alert %}} 

Usare l'opzione GridWeb.EnableAsync per ottimizzare la memoria e le prestazioni per i dati delle celle. Quando si crea un set di dati di grandi dimensioni per le celle. Quando si imposta l'opzione su true, il caricamento dei dati si baserà solo sull'area Windows attualmente visibile. In breve, quando si scorrono i dati delle celle del foglio di lavoro in GridWeb, verranno caricati i nuovi dati Windows basati solo sulla posizione di scorrimento corrente.

L'esempio seguente mostra come abilitare la modalità asincrona di GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
