---
title: Aggiorna Aspose.Grid.Web a Aspose.Cells.GridWeb
type: docs
weight: 30
url: /it/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: Questo articolo illustra come eseguire l aggiornamento a GridWeb.
---

{{% alert color="primary" %}}

Per rendere più semplice l'aggiornamento, manteniamo un documento che descrive le informazioni critiche per gli utenti esistenti, specialmente quelli che hanno utilizzato il vecchio Aspose.Grid.Web e hanno bisogno di aggiornare a Aspose.Cells.GridWeb.

Queste sono note brevi e dovresti essere in grado di trovare ulteriori informazioni guardando le sezioni della [Guida dello Sviluppatore](/cells/it/net/aspose-cells-gridweb/developer-guide/).

{{% /alert %}}

## **Aggiornamento a Aspose.Cells.GridWeb**

Gli utenti di Aspose.Grid.Web potrebbero incontrare problemi nell'utilizzare il nuovo Aspose.Cells.GridWeb quando effettuano l'aggiornamento. È da notare che Aspose.Grid.Web è stato rinominato ed è diventato parte di Aspose.Cells, quindi non continueremo a modificare le versioni precedenti del controllo. 

Non è difficile fare l'aggiornamento al componente Aspose.Cells.GridWeb più recente.

{{% alert color="primary" %}}

Ci sono pochi cambiamenti nell'API poiché le classi con i membri, le strutture, le enumerazioni, ecc., rimangono uguali. La maggior parte dei cambiamenti sono stati apportati ai namespace del controllo e ad altri tag o attributi.

{{% /alert %}}

Di seguito è riportato l'elenco dei namespace e degli altri attributi/tag che sono stati cambiati ora:

1. Il namespace Aspose.Grid.Web è stato rinominato in Aspose.Cells.GridWeb.
1. Il namespace Aspose.Grid.Web.Data è stato rinominato Aspose.Cells.GridWeb.Data.
1. Il namespace Aspose.Grid.Web.Design è stato rinominato in Aspose.Cells.GridWeb.Design.
1. Il namespace Aspose.Grid.Formula è stato rinominato Aspose.Cells.GridFormula e con le versioni più recenti del componente, il suddetto namespace è stato completamente rimosso dall'API pubblica.
1. Il tag agw:GridWeb è stato cambiato in acw:GridWeb nel form aspx.
1. Il percorso client dell'Aspose.Grid.Web precedente, agw_client, è stato cambiato in acw_client per Aspose.Cells.GridWeb.
1. L'impostazione del percorso client nel file web.config, ad esempio: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

è stato cambiato in 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
