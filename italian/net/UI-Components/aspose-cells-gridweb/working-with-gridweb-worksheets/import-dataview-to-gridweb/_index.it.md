---
title: Importa DataView in GridWeb
type: docs
weight: 60
url: /it/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

Con il rilascio di Microsoft .NET Framework, è stato introdotto un nuovo modo di archiviare i dati. Ora oggetti DataSet, DataTable e DataView che memorizzano i dati in modalità offline. Questi oggetti sono molto utili come repository di dati. Usando Aspose.Cells.GridWeb, è possibile importare dati da oggetti DataTable o DataView in fogli di lavoro. Aspose.Cells.GridWeb supporta solo l'importazione di dati da un DataView. oggetto ma un oggetto DataTable può essere utilizzato anche indirettamente. Discutiamo questa caratteristica in dettaglio.

{{% /alert %}} 
## **Importazione di dati da DataView**
Importare i dati da un oggetto DataView utilizzando il metodo ImportDataView di GridWorsheetCollection nel controllo GridWeb. Passare l'oggetto DataView da cui importare i dati al metodo ImportDataView. È possibile specificare l'intestazione della colonna e gli stili dei dati durante l'importazione.

{{% alert color="primary" %}} 

Quando i dati vengono importati da un oggetto DataView, viene creato un nuovo foglio di lavoro per contenere i dati importati. Il foglio di lavoro ha lo stesso nome del DataTable.

{{% /alert %}} 

**Output: dati importati da un DataView in un nuovo foglio di lavoro** 

![cose da fare:immagine_alt_testo](import-dataview-to-gridweb_1.png)

 Le larghezze delle colonne vengono regolate per mostrare tutti i dati che contengono. Quando i dati vengono importati da DataView, le larghezze delle colonne non vengono regolate automaticamente. Gli utenti devono regolarli da soli. Per regolare le larghezze delle colonne a livello di codice, fare riferimento a[Ridimensiona righe e colonne](/cells/it/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Una versione di overload del metodo ImportDataView consente agli sviluppatori di specificare il nome del foglio che contiene i dati importati e un numero specifico di righe e colonne da importare dall'oggetto DataView.

{{% /alert %}}
