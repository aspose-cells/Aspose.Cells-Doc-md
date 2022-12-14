---
title: Aggiorna Aspose.Grid.Web a Aspose.Cells.GridWeb
type: docs
weight: 30
url: /it/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

Per semplificare l'aggiornamento, manteniamo un documento che descrive le informazioni critiche per gli utenti esistenti, in particolare quelli che hanno utilizzato il vecchio Aspose.Grid.Web e devono eseguire l'aggiornamento al Aspose.Cells.GridWeb unito.

 Queste sono intese come brevi note e dovresti essere in grado di trovare maggiori informazioni guardando le sezioni del[Guida per sviluppatori](/cells/it/net/developer-guide/).

{{% /alert %}}

## **Aggiornamento a Aspose.Cells.GridWeb**

 Gli utenti Aspose.Grid.Web potrebbero riscontrare problemi utilizzando il nuovo Aspose.Cells.GridWeb durante l'aggiornamento. Si noti che Aspose.Grid.Web è stato rinominato ed è diventato parte di Aspose.Cells, quindi non continueremo o apporteremo modifiche alle versioni precedenti del controllo.

Non è difficile eseguire l'aggiornamento all'ultimo componente Aspose.Cells.GridWeb.

{{% alert color="primary" %}}

Ci sono alcune modifiche nello API poiché le classi con i membri, le strutture, le enumerazioni ecc. Rimangono le stesse. La maggior parte delle modifiche è stata apportata agli spazi dei nomi del controllo e ad altri tag o attributi.

{{% /alert %}}

Di seguito è riportato l'elenco degli spazi dei nomi e altri attributi/tag che sono stati modificati ora:

1. Lo spazio dei nomi Aspose.Grid.Web è stato rinominato in Aspose.Cells.GridWeb.
1. Lo spazio dei nomi Aspose.Grid.Web.Data è stato rinominato Aspose.Cells.GridWeb.Data.
1. Lo spazio dei nomi Aspose.Grid.Web.Design è stato rinominato Aspose.Cells.GridWeb.Design.
1. Lo spazio dei nomi Aspose.Grid.Formula è stato rinominato in Aspose.Cells.GridFormula e, con i recenti rilasci del componente, tale spazio dei nomi è stato completamente rimosso dal pubblico API.
1. Il tag agw:GridWeb è stato modificato in acw:GridWeb nel formato aspx.
1. Il vecchio percorso del client Aspose.Grid.Web, agw_client, è stato modificato in acw_client per Aspose.Cells.GridWeb .
1.  L'impostazione del percorso del client nel file web.config, ad esempio:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 è cambiato in

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
