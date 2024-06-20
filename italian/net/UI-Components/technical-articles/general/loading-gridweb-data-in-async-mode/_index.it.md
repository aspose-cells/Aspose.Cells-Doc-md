---
title: Caricamento dei dati di GridWeb in modalità asincrona
type: docs
weight: 40
url: /it/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: Questo articolo descrive come utilizzare la modalità asincrona per ottenere una migliore performance in GridWeb.
keywords: GridWeb, performance, asincrono, modalità asincrona
---

{{% alert color="primary" %}} 

Quando si crea un Workbook con grandi set di dati, o si legge un grande file Microsoft Excel, ci vorrà sicuramente più tempo e risorse per farlo. La memoria totale che il processo richiederà è sempre una preoccupazione. Ci sono misure che possono essere adottate per far fronte alla sfida. Aspose.Cells.GridWeb fornisce alcune opzioni e API pertinenti per ridurre, ridurre e ottimizzare l'uso della memoria. Inoltre, può aiutare il processo a funzionare in modo più efficiente e veloce. Per un foglio di calcolo che contiene dati di celle numerose, è possibile caricare il dataset in modo asincrono che può migliorare le prestazioni complessive per l'esperienza dell'utente.

{{% /alert %}} 

Usa l'opzione GridWeb.EnableAsync per ottimizzare memoria e prestazioni per i dati delle celle. Quando si costruisce un grande set di dati per le celle. Quando si imposta l'opzione su true, il caricamento dati sarà basato solo sull'area visibile corrente di Windows. In breve, quando si scorre nei dati delle celle del foglio di calcolo in GridWeb, verranno caricati nuovi dati di Windows in base alla posizione di scroll corrente.

L'esempio seguente mostra come abilitare la modalità asincrona di GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
