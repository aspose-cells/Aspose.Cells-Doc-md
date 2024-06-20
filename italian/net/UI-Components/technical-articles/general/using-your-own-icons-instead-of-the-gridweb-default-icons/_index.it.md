---
title: Utilizzare le proprie icone invece delle icone predefinite della GridWeb
type: docs
weight: 10
url: /it/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb, icona, icone
description: Questo articolo descrive come utilizzare le icone in GridWeb.
---

{{% alert color="primary" %}} 

A volte potresti voler utilizzare le proprie icone (immagini) invece delle icone predefinite del controllo Aspose.Cells.GridWeb. Questo articolo spiega come farlo.

{{% /alert %}} 

Le icone predefinite del controllo si trovano nel percorso URL "/acw_client/". Il percorso del file può essere: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" di default. Trovi file come submit.gif, save.gif ecc. in quella cartella. Se vuoi sostituire queste immagini con le tue, aggiungi una sezione di configurazione al file web.config della tua applicazione web.

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Potresti aver notato che questa configurazione influisce solo sul percorso delle immagini di controllo e non influisce sul percorso degli script client del controllo. Ad esempio, se esegui la tua pagina con il controllo GridWeb e controlli il file di origine nel browser, potresti scoprire che la proprietà del percorso acw_client del DIV del grid dice ancora: "/yourApp/webform1.aspx/". In alcuni casi, potresti dover ridefinire il percorso degli script client. Per obbligare il controllo a utilizzare il percorso dell'immagine ridefinito come percorso degli script client, aggiungi un'altra impostazione di configurazione nella sezione appSettings
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Questa configurazione avrà effetto solo con il controllo con licenza.

{{% /alert %}}
