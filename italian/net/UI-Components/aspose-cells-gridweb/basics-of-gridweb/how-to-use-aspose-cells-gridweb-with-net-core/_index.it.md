---
title: Come usare Aspose.Cells.GridWeb con .NET Core
type: docs
weight: 40
url: /it/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

Questo argomento spiega come usare Aspose.Cells.GridWeb con le applicazioni .NET Core usando Visual Studio.NET 2019. Questo argomento è utile per gli sviluppatori di livello principiante che lavorano con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Usa Aspose.Cells.GridWeb con .NET Core**
Questo argomento illustra come usare Aspose.Cells.GridWeb creando un sito Web di esempio in Visual Studio 2019. Il processo è stato suddiviso in passaggi.
### **Passaggio 1: creazione di un nuovo progetto**
1. Apri Visual Studio 2019.
1.  Dal**File** menù, selezionare**Nuovo** , poi**Progetto**.
 Viene aperta la finestra di dialogo Crea un nuovo progetto.
1.  Selezionare**ASP.NET Applicazione Web principale** dai modelli di progetto installati di Visual Studio e fare clic su**Prossimo**.

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  Specificare una posizione in cui la posizione e il nome del progetto e fare clic**Creare**.

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  Seleziona il**Applicazione Web (Model-View-Controller)** modello e assicurati che**ASP .NET Nucleo 2.1** è selezionato.

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  Clic**Creare**.
### **Passaggio 2: controllo della vista iniziale**
L'esecuzione del progetto appena creato mostra il modello predefinito nel browser, come mostrato nell'immagine sottostante.



![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Passaggio 3: aggiunta di Aspose.Cells.GridWeb**
1. Aggiungere i seguenti pacchetti Nuget al progetto

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Aggiungere il pacchetto Aspose.Cells.GridWeb

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Aggiungi quanto segue al file **_ViewImports.cshtml** nella cartella Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Il file avrà questo aspetto dopo le modifiche

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Inserisci il seguente codice nel metodo Index di HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Ricordarsi di aggiornare SessionStorePath e il percorso ImportExcelFile.

{{% /alert %}} 

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  Aggiungere il seguente codice nel file**Index.cshtml** file nella directory Visualizza > Home.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Il file avrà questo aspetto dopo la modifica.

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Aggiungere il supporto della sessione e GridScheduedService nel file Startup.cs
 1. Aggiungere il seguente frammento di codice nel metodo ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Aggiungere il frammento di codice seguente nel metodo Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Metti l'ultimo acw_client nella directory: **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1.  Aggiungere**AcwController**nei controller per gestire la mappa del percorso acw che può fornire tutte le operazioni predefinite per l'azione di modifica generale.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Passaggio 4: prova l'app**
L'esecuzione dell'app produrrà un output simile a quello mostrato nell'immagine sottostante.

![cose da fare:immagine_alt_testo](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
