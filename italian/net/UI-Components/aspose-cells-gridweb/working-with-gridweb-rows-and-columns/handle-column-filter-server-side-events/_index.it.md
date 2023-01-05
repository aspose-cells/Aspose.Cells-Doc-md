---
title: Gestisci gli eventi lato server del filtro colonna
type: docs
weight: 90
url: /it/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

Il filtro dei dati è probabilmente la funzionalità di Excel più utilizzata che consente di filtrare i dati in base a criteri specifici. I dati filtrati visualizzano solo le righe che soddisfano la condizione nascondendo le righe che non soddisfano i criteri.
Il componente Aspose.Cells.GridWeb fornisce la possibilità di eseguire il filtraggio dei dati utilizzando la sua interfaccia. Per estendere le sue capacità, il componente Aspose.Cells.GridWeb fornisce anche due eventi che possono fungere da callback al meccanismo di filtraggio eseguito tramite l'interfaccia utente di GridWeb.

{{% /alert %}} 
## **Gestione dell'evento lato server all'applicazione del filtro di colonna**
Ci sono due eventi principali come descritto di seguito.

1. OnBeforeColumnFilter: si attiva prima che il filtro venga applicato a una colonna.
1. OnAfterColumnFilter: si attiva dopo che il filtro è stato applicato a una colonna.

Ecco lo script ASPX del componente Aspose.Cells.GridWeb per aggiungere e assegnare i suddetti eventi.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Questi eventi possono essere utilizzati per ottenere informazioni utili sul processo di filtraggio come l'indice di colonna e il valore su cui applicare il filtro. Di seguito è riportato il frammento di codice che illustra l'utilizzo dell'evento OnBeforeColumnFilter per recuperare l'indice e il valore della colonna che l'utente ha selezionato nell'interfaccia utente di GridWeb per il filtro.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


D'altra parte, se il requisito è ottenere il numero di righe filtrate dopo l'applicazione del filtro, è possibile utilizzare l'evento OnAfterColumnFilter come illustrato di seguito.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

 Controlla l'introduzione a tutti[Utilizzo degli eventi GridWeb](/cells/it/net/working-with-gridweb-events/) insieme ad alcuni dettagli su come gestire questi eventi.

{{% /alert %}}
