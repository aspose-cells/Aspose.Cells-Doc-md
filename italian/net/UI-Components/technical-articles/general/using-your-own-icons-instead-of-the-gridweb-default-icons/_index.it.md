---
title: Utilizzo delle tue icone invece delle icone predefinite di GridWeb
type: docs
weight: 10
url: /it/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

A volte potresti voler usare le tue icone (immagini) invece delle icone predefinite del controllo Aspose.Cells.GridWeb. Questo articolo spiega come farlo.

{{% /alert %}} 

Le icone predefinite del controllo si trovano nel percorso URL "/acw_client/". Il percorso del file può essere: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" per impostazione predefinita. Troverai file come submit.gif, save.gif ecc. in quella cartella. Se vuoi sostituire queste immagini con le tue, aggiungi una sezione di configurazione al file web.config della tua applicazione web.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Potresti aver notato che questa configurazione influisce solo sul percorso delle immagini del controllo e non sul percorso degli script client del controllo. Ad esempio, se esegui la tua pagina con il controllo GridWeb e controlli il file di origine nel browser, potresti scoprire che acw_ cliente_path dell'elemento DIV della griglia dice ancora: "/yourApp/webform1.aspx/". In alcuni casi, potrebbe essere necessario ridefinire il percorso dello script client. Per forzare il controllo a utilizzare il percorso dell'immagine ridefinito come percorso dello script client, aggiungi un'altra impostazione di configurazione nella sezione appSettings
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Questa configurazione avrà effetto solo con il controllo concesso in licenza.

{{% /alert %}}
