---
title: Come utilizzare Aspose.Cells.GridWeb con .NET Core
type: docs
weight: 40
url: /it/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: Questo articolo introduce come utilizzare GridWeb in un applicazione web .net core
---

{{% alert color="primary" %}} 

Questo argomento spiega come utilizzare Aspose.Cells.GridWeb con le applicazioni .NET Core usando Visual Studio.NET 2019. Questo argomento è utile per i programmatori principianti che lavorano con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Usa Aspose.Cells.GridWeb con .NET Core**
Questo argomento mostra come utilizzare Aspose.Cells.GridWeb creando un sito web di esempio in Visual Studio 2019. Il processo è stato diviso in passaggi.
### **Passo 1: Creazione di un nuovo progetto**
1. Aprire Visual Studio 2019.
1. Dal menu **File**, seleziona **Nuovo**, poi **Progetto**.
   Viene aperta la finestra di creazione di un nuovo progetto.
1. Seleziona **Applicazione Web ASP.NET Core** dai modelli di progetto installati di Visual Studio e fai clic su **Avanti**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Specifica una posizione dove si trova la posizione e il nome del progetto e clicca su **Crea**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. Seleziona il template **Applicazione web (Modello-Vista-Controller)** e assicurati che sia selezionato **ASP .NET Core 2.1**. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. Fai clic su **Crea**.
### **Passaggio 2: Verifica della visualizzazione iniziale**
L'esecuzione del progetto appena creato mostra il modello predefinito nel browser come mostrato nell'immagine sottostante.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Passaggio 3: Aggiunta di Aspose.Cells.GridWeb**
1. Aggiungi i seguenti pacchetti Nuget al progetto

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Aggiungi il pacchetto Aspose.Cells.GridWeb

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Aggiungi quanto segue al file **_ViewImports.cshtml** nella cartella Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Il file avrà questo aspetto dopo le modifiche

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Inserisci il seguente codice nel metodo Index dell'HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Ricorda di aggiornare il percorso SessionStorePath e il percorso ImportExcelFile.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. Aggiungi il seguente codice nel file **Index.cshtml** nella directory View > Home.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Il file avrà questo aspetto dopo la modifica.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Aggiungi il supporto alla sessione e GridScheduedService nel file Startup.cs
   1. Aggiungi il seguente snippet di codice nel metodo ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Aggiungi il seguente snippet di codice nel metodo Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Sposta il più recente acw_client nella directory: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. Aggiungi **AcwController** nei controller per gestire la mappatura della route acw che può fornire tutte le operazioni predefinite per l'azione di modifica generale.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Passaggio 4: Test dell'app**
L'esecuzione dell'app mostrerà l'output simile a quello mostrato nell'immagine sottostante.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
