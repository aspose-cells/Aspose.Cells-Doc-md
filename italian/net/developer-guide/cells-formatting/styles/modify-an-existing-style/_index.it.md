---
title: Modifica uno stile esistente
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo che consente agli utenti di modificare gli stili di cella esistenti. Questo articolo introdurrà come modificare uno stile di cella esistente con la libreria Aspose.Cells in modo che gli utenti possano modificare l'aspetto delle celle di cui hanno bisogno.
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /it/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Per applicare le stesse opzioni di formattazione alle celle, crea un nuovo oggetto stile di formattazione. Un oggetto stile di formattazione è una combinazione di caratteristiche di formattazione, come carattere, dimensione del carattere, rientro, numero, bordo, motivi ecc., denominati e archiviati come set. Una volta applicata, viene applicata tutta la formattazione in quello stile.

Puoi anche utilizzare uno stile esistente, salvarlo con la cartella di lavoro e utilizzarlo per formattare le informazioni con gli stessi attributi.

 Quando le celle non sono formattate esplicitamente, il file**Normale** viene applicato lo stile (lo stile predefinito della cartella di lavoro). Microsoft Excel predefinisce diversi stili oltre allo stile Normale, inclusi Virgola, Valuta e Percentuale.

Aspose.Cells consente di modificare uno qualsiasi di questi stili o qualsiasi altro stile definito con gli attributi desiderati.

{{% /alert %}}

##  **Utilizzando Microsoft Excel**

Per aggiornare uno stile in Microsoft Excel 97-2003:

1.  Sul**Formato** menu, fare clic su *Stile**.
1.  Seleziona lo stile che desideri modificare dal file**Nome dello stile** elenco.
1. Fare clic su *Modifica**.
1. Seleziona le opzioni di stile che desideri utilizzando le schede nella finestra di dialogo Formato Cells.
1. Fare clic su *OK**.
1. In *Lo stile include**, specifica le caratteristiche di stile che desideri.
1.  Clic**OK** per salvare lo stile e applicarlo all'intervallo selezionato.

##  **Utilizzando Aspose.Cells**

 Gli esempi seguenti dimostrano come utilizzare[**Stile.Aggiornamento**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)metodo.

###  **Creazione e modifica di uno stile**

 Questo esempio crea a[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto, lo applica a un intervallo di celle e modifica il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto. Le modifiche vengono applicate automaticamente alla cella e all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

###  **Modifica di uno stile esistente**

In questo esempio viene utilizzato un semplice file modello Excel in cui uno stile denominato Percentuale è già stato applicato a un intervallo. L'esempio:

1. ottiene lo stile,
1. crea un oggetto di stile e
1. modifica la formattazione dello stile.

Le modifiche vengono applicate automaticamente all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
