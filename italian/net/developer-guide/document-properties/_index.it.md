---
title: Gestisci le proprietà del documento
linktitle: Proprietà del documento
type: docs
weight: 80
url: /it/net/managing-document-properties/
description: Scopri come gestire le proprietà del documento tramite le API Aspose.Cells per NET.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **introduzione**

Microsoft Excel offre la possibilità di aggiungere proprietà ai file del foglio di calcolo. Queste proprietà del documento forniscono informazioni utili e sono divise in 2 categorie come descritto di seguito.

- Proprietà definite dal sistema (incorporate): le proprietà integrate contengono informazioni generali sul documento come titolo del documento, nome dell'autore, statistiche del documento e così via.
- Proprietà (personalizzate) definite dall'utente: proprietà personalizzate definite dall'utente finale sotto forma di coppia nome-valore.

{{% alert color="primary" %}}

Il punto più importante da sapere sulle proprietà integrate e personalizzate è che è possibile accedere e modificare le proprietà integrate, ma non crearle o rimuoverle. Tuttavia, è possibile creare e gestire proprietà personalizzate.

{{% /alert %}}

##  **Come gestire le proprietà del documento utilizzando Microsoft Excel**

 Microsoft Excel permette di gestire le proprietà del documento dei file Excel in modalità WYSIWYG. Si prega di seguire i passaggi seguenti per aprire il file**Proprietà** finestra di dialogo in Excel 2016.

1.  Dal**File** selezionare *Informazioni**.

|**Selezione del menu Informazioni**|
| :- |
|![cose da fare:immagine_alt_testo](managing-document-properties_1.png)|
1.  Clicca su**Proprietà** titolo e selezionare "Proprietà avanzate".

|**Facendo clic su Selezione proprietà avanzate**|
| :- |
|![cose da fare:immagine_alt_testo](managing-document-properties_2.png)|
1. Gestisci le proprietà del documento del file.

|**Finestra di dialogo Proprietà**|
| :- |
|![cose da fare:immagine_alt_testo](managing-document-properties_3.png)|
Nella finestra di dialogo Proprietà sono presenti diverse schede, come Generale, Riepilogo, Statistiche, Contenuti e Personalizzate. Ciascuna scheda aiuta a configurare diversi tipi di informazioni relative al file. La scheda Personalizzata viene utilizzata per gestire le proprietà personalizzate.

##  **Come lavorare con le proprietà del documento utilizzando Aspose.Cells**

Gli sviluppatori possono gestire dinamicamente le proprietà del documento utilizzando le API Aspose.Cells. Questa funzionalità aiuta gli sviluppatori a memorizzare informazioni utili insieme al file, ad esempio quando il file è stato ricevuto, elaborato, timestamp e così via.

{{% alert color="primary" %}}

 Aspose.Cells for .NET scrive direttamente le informazioni su API e il numero di versione nei documenti di output. Ad esempio, dopo aver eseguito il rendering del documento su PDF, Aspose.Cells for .NET viene popolato**Applicazione** campo con valore 'Aspose.Cells' e**PDF Produttore** campo con il valore, ad esempio 'Aspose.Cells v17.9'.

Tieni presente che non puoi chiedere a Aspose.Cells for .NET di modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

###  **Come accedere alle proprietà del documento**

 Aspose.Cells Le API supportano entrambi i tipi di proprietà del documento, integrate e personalizzate. Aspose.Cells'[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class rappresenta un file Excel e, come un file Excel, il file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe può contenere più fogli di lavoro, ciascuno rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe mentre la raccolta di fogli di lavoro è rappresentata da[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)classe.

 Usa il[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)per accedere alle proprietà del documento del file come descritto di seguito.

- Per accedere alle proprietà del documento integrate, utilizzare[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Per accedere alle proprietà personalizzate del documento, utilizzare[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Entrambi i[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) E[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) restituire l'istanza di[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Questa raccolta contiene[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)oggetti, ognuno dei quali rappresenta una singola proprietà del documento incorporata o personalizzata.

 Spetta ai requisiti della domanda come accedere a una proprietà, cioè; utilizzando l'indice o il nome della proprietà dal file[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)come dimostrato nell'esempio seguente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 IL[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)La classe consente di recuperare il nome, il valore e il tipo della proprietà del documento:

-  Per ottenere il nome della proprietà, utilizzare[**DocumentProperty.Nome**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Per ottenere il valore della proprietà, utilizzare[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)restituisce il valore come oggetto.
-  Per ottenere il tipo di proprietà, utilizzare[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Ciò restituisce uno dei[**Tipo di proprietà**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)valori di enumerazione. Dopo aver ottenuto il tipo di proprietà, utilizza uno dei file**DocumentProperty.ToXXX** metodi per ottenere il valore del tipo appropriato invece di utilizzare[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . IL**DocumentProperty.ToXXX**i metodi sono descritti nella tabella seguente.

{{% alert color="primary" %}}

 IL[**Proprietàdocumento**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)La classe fornisce anche un insieme di metodi che restituiscono i valori di altri tipi di dati.

{{% /alert %}}

|**Nome del membro**|**Descrizione**|**Metodo ToXXX**|
| :- | :- | :- |
|Booleano|Il tipo di dati della proprietà è booleano|ToBool|
|Data| Il tipo di dati della proprietà è DateTime. Tieni presente che Microsoft Excel memorizza solo<br>la parte della data, non è possibile archiviare l'ora in una proprietà personalizzata di questo tipo|ToDateTime|
|Galleggiante|Il tipo di dati della proprietà è Double|Raddoppiare|
|Numero|Il tipo di dati della proprietà è Int32|ToInt|
|String|Il tipo di dati della proprietà è String|Accordare|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **Come aggiungere o rimuovere proprietà personalizzate del documento**

Come descritto in precedenza all'inizio di questo argomento, gli sviluppatori non possono aggiungere o rimuovere proprietà integrate perché queste proprietà sono definite dal sistema ma è possibile aggiungere o rimuovere proprietà personalizzate perché sono definite dall'utente.

###  **Come aggiungere proprietà personalizzate**

 Aspose.Cells Le API hanno esposto il file[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) metodo per il[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) classe per aggiungere proprietà personalizzate alla raccolta. IL[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) Il metodo aggiunge la proprietà al file Excel e restituisce un riferimento per la nuova proprietà del documento come file[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)oggetto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **Come configurare la proprietà personalizzata "Link al contenuto".**

 Per creare una proprietà personalizzata collegata al contenuto di un determinato intervallo, chiama il file[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) metodo e passare il nome e l'origine della proprietà. Puoi verificare se una proprietà è configurata come collegata al contenuto utilizzando il file[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) proprietà. Inoltre, è anche possibile ottenere l'intervallo di origine utilizzando il file[**Fonte**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) proprietà del[**Proprietàdocumento**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)classe.

Nell'esempio utilizziamo un semplice file Excel modello Microsoft. La cartella di lavoro ha un intervallo denominato definito etichettato**MyRange** che si riferisce al valore di una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **Come rimuovere le proprietà personalizzate**

 Per rimuovere le proprietà personalizzate utilizzando Aspose.Cells, chiama il[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)metodo e passare il nome della proprietà del documento da rimuovere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **Argomenti avanzati**
- [Aggiunta di proprietà personalizzate visibili nel pannello informazioni del documento](/cells/it/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrate](/cells/it/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specificare la versione del documento del file Excel utilizzando le proprietà del documento integrate](/cells/it/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specificare la lingua del file Excel utilizzando le proprietà del documento integrate](/cells/it/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
