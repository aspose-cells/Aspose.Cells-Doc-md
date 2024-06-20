---
title: Gestire gli eventi del filtro della colonna
type: docs
weight: 90
url: /it/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: Questo articolo introduce come gestire l evento di filtro della colonna in GridWeb.
---

{{% alert color="primary" %}} 

La filtrazione dei dati è probabilmente la funzione di Excel più utilizzata che ti consente di filtrare i dati in base a criteri specifici. I dati filtrati mostrano solo le righe che soddisfano la condizione nascondendo le righe che non soddisfano il criterio.
Il componente Aspose.Cells.GridWeb fornisce la possibilità di effettuare la filtrazione dei dati utilizzando la sua interfaccia. Per estendere le sue funzionalità, il componente Aspose.Cells.GridWeb fornisce anche due eventi che possono servire come richiamo al meccanismo di filtraggio effettuato attraverso l'interfaccia utente di GridWeb.

{{% /alert %}} 
## **Gestione dell'evento lato server sull'applicazione del filtro della colonna**
Ci sono due eventi principali come dettagliato di seguito.

1. OnBeforeColumnFilter: Si attiva prima che il filtro venga applicato a una colonna.
2. OnAfterColumnFilter: Si attiva dopo che il filtro è stato applicato a una colonna.

Ecco lo script ASPX del componente Aspose.Cells.GridWeb per aggiungere e assegnare i suddetti eventi.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Questi eventi possono essere utilizzati per ottenere informazioni utili sul processo di filtraggio, come l'indice della colonna e il valore su cui deve essere applicato il filtro. Di seguito è riportato lo snippet che dimostra l'uso dell'evento OnBeforeColumnFilter per recuperare l'indice della colonna e il valore che l'utente ha selezionato sull'interfaccia utente di GridWeb per il filtraggio.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


D'altro canto, se il requisito è quello di ottenere il numero di righe filtrate dopo che il filtro è stato applicato, puoi utilizzare l'evento OnAfterColumnFilter come dimostrato di seguito.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Controlla l'introduzione a tutti [Lavorare con gli eventi di GridWeb](/cells/it/net/aspose-cells-gridweb/working-with-gridweb-events/) insieme ad alcuni dettagli su come gestire questi eventi.

{{% /alert %}}
