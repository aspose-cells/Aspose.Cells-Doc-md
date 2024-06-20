---
title: Importare DataView in GridWeb
type: docs
weight: 60
url: /it/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb, importazione
description: Questo articolo presenta come importare dati in GridWeb.
---

{{% alert color="primary" %}} 

Con il rilascio del Microsoft .NET Framework è stata introdotta una nuova modalità di archiviazione dei dati. Ora sono presenti oggetti DataSet, DataTable e DataView che memorizzano i dati in modalità offline. Questi oggetti sono molto utili come archivi dati. Utilizzando Aspose.Cells.GridWeb, è possibile importare dati da oggetti DataTable o DataView nei fogli di lavoro. Aspose.Cells.GridWeb supporta solo l'importazione dei dati da un oggetto DataView, ma un oggetto DataTable può essere utilizzato anche in modo indiretto. Discutiamo dettagliatamente questa funzionalità.

{{% /alert %}} 
## **Importazione dati da DataView**
Importa dati da un oggetto DataView utilizzando il metodo ImportDataView della collezione GridWorsheet nell'elemento di controllo GridWeb. Passa l'oggetto DataView da cui desideri importare dati al metodo ImportDataView. È possibile specificare l'intestazione delle colonne e gli stili dei dati durante l'importazione.

{{% alert color="primary" %}} 

Quando i dati vengono importati da un oggetto DataView, viene creato un nuovo foglio di lavoro per contenere i dati importati. Il foglio di lavoro ha lo stesso nome del DataTable.

{{% /alert %}} 

**Output: Dati importati da un DataView in un nuovo foglio di lavoro** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

Le larghezze delle colonne vengono regolate per mostrare tutti i dati contenuti. Quando i dati vengono importati da DataView, le larghezze delle colonne non vengono regolate automaticamente. Gli utenti devono regolarle manualmente. Per regolare le larghezze delle colonne in modo programmatico, fare riferimento a [Ridimensionare righe e colonne](/cells/it/net/aspose-cells-gridweb/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Una versione sovraccaricata del metodo ImportDataView consente agli sviluppatori di specificare il nome del foglio che contiene i dati importati e un numero specifico di righe e colonne da importare dall'oggetto DataView.

{{% /alert %}}
