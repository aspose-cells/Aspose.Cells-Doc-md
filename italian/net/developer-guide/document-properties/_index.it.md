---
title: Gestisci le proprietà del documento
linktitle: Proprietà del documento
type: docs
weight: 80
url: /it/net/managing-document-properties/
description: Gestisci le proprietà del documento dei file del foglio di calcolo.
---
## **introduzione**

Microsoft Excel offre la possibilità di aggiungere proprietà ai file del foglio di calcolo. Queste proprietà del documento forniscono informazioni utili e sono suddivise in 2 categorie come descritto di seguito.

- Proprietà (integrate) definite dal sistema: le proprietà integrate contengono informazioni generali sul documento come titolo del documento, nome dell'autore, statistiche del documento e così via.
- Proprietà (personalizzate) definite dall'utente: proprietà personalizzate definite dall'utente finale sotto forma di coppia nome-valore.

{{% alert color="primary" %}}

Il punto più importante da sapere sulle proprietà predefinite e personalizzate è che è possibile accedere e modificare le proprietà predefinite, ma non crearle o rimuoverle. Tuttavia, è possibile creare e gestire proprietà personalizzate.

{{% /alert %}}

## **Gestione delle proprietà del documento utilizzando Microsoft Excel**

 Microsoft Excel permette di gestire le proprietà dei documenti dei file Excel in maniera WYSIWYG. Si prega di seguire i passaggi seguenti per aprire il file**Proprietà** finestra di dialogo in Excel 2016.

1.  Dal**File** menù, selezionare**Informazioni**.

|**Selezionando Menu Informazioni**|
|:- |
|![cose da fare:immagine_alt_testo](managing-document-properties_1.png)|
1.  Clicca su**Proprietà** voce e selezionare "Proprietà avanzate".

|**Facendo clic su Selezione proprietà avanzate**|
|:- |
|![cose da fare:immagine_alt_testo](managing-document-properties_2.png)|
1. Gestisci le proprietà del documento del file.

|**Finestra di dialogo Proprietà**|
|:- |
|![cose da fare:immagine_alt_testo](managing-document-properties_3.png)|
Nella finestra di dialogo Proprietà, ci sono diverse schede, come Generale, Riepilogo, Statistiche, Contenuti e Personalizzazioni. Ogni scheda consente di configurare diversi tipi di informazioni relative al file. La scheda Personalizzato viene utilizzata per gestire le proprietà personalizzate.

## **Lavorare con le proprietà del documento usando Aspose.Cells**

Gli sviluppatori possono gestire dinamicamente le proprietà del documento utilizzando le API Aspose.Cells. Questa funzione aiuta gli sviluppatori a memorizzare informazioni utili insieme al file, ad esempio quando il file è stato ricevuto, elaborato, timestamp e così via.

{{% alert color="primary" %}}

 Aspose.Cells for .NET scrive direttamente le informazioni su API e il numero di versione nei documenti di output. Ad esempio, al momento del rendering del documento in PDF, Aspose.Cells for .NET viene popolato**Applicazione** campo con valore 'Aspose.Cells' e**Produttore PDF** campo con il valore, ad esempio 'Aspose.Cells v17.9'.

Si prega di notare che non è possibile incaricare Aspose.Cells for .NET di modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

### **Accesso alle proprietà del documento**

Aspose.Cells Le API supportano entrambi i tipi di proprietà del documento, integrate e personalizzate. Aspose.Cells'[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class rappresenta un file Excel e, come un file Excel, il file[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe può contenere più fogli di lavoro, ciascuno rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class mentre la raccolta di fogli di lavoro è rappresentata dal file[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)classe.

 Utilizzare il[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)per accedere alle proprietà del documento del file come descritto di seguito.

-  Per accedere alle proprietà predefinite del documento, utilizzare[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Per accedere alle proprietà del documento personalizzate, utilizzare[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Sia il[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) e[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) restituire l'istanza di[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Questa raccolta contiene[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)oggetti, ciascuno dei quali rappresenta una singola proprietà del documento incorporata o personalizzata.

 Spetta al requisito dell'applicazione come accedere a una proprietà, ovvero; utilizzando l'indice o il nome della proprietà da[**DocumentoPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)come dimostrato nell'esempio sottostante.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 Il[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class consente di recuperare il nome, il valore e il tipo della proprietà del documento:

-  Per ottenere il nome della proprietà, utilizzare[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Per ottenere il valore della proprietà, utilizzare[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)restituisce il valore come oggetto.
-  Per ottenere il tipo di proprietà, utilizzare[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Questo restituisce uno dei[**Tipo di proprietà**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) valori di enumerazione. Dopo aver ottenuto il tipo di proprietà, utilizzare uno dei**DocumentProperty.ToXXX** metodi per ottenere il valore del tipo appropriato invece di utilizzare[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . Il**DocumentProperty.ToXXX**metodi sono descritti nella tabella sottostante.

{{% alert color="primary" %}}

 Il[**Proprietà documento**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class fornisce anche un insieme di metodi che restituiscono i valori di altri tipi di dati.

{{% /alert %}}

|**Nome del membro**|**Descrizione**|**Metodo ToXXX**|
|:- |:- |:- |
|Booleano|Il tipo di dati della proprietà è booleano|ToBool|
|Data|Il tipo di dati della proprietà è DateTime. Si noti che Microsoft Excel memorizza solo<br>la parte relativa alla data, nessuna ora può essere memorizzata in una proprietà personalizzata di questo tipo|ToDateTime|
|Galleggiante|Il tipo di dati della proprietà è Double|Raddoppiare|
|Numero|Il tipo di dati della proprietà è Int32|ToInt|
|Corda|Il tipo di dati della proprietà è String|Accordare|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Aggiunta o rimozione di proprietà del documento personalizzate**

Come descritto in precedenza all'inizio di questo argomento, gli sviluppatori non possono aggiungere o rimuovere proprietà predefinite perché queste proprietà sono definite dal sistema, ma è possibile aggiungere o rimuovere proprietà personalizzate perché sono definite dall'utente.

### **Aggiunta di proprietà personalizzate**

 Aspose.Cells API hanno esposto il file[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) metodo per il[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) class per aggiungere proprietà personalizzate alla raccolta. Il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) Il metodo aggiunge la proprietà al file Excel e restituisce un riferimento per la nuova proprietà del documento come un[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)oggetto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Configurazione della proprietà personalizzata "Link al contenuto".**

 Per creare una proprietà personalizzata collegata al contenuto di un determinato intervallo, chiama il metodo[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) metodo e passare il nome della proprietà e l'origine. Puoi verificare se una proprietà è configurata come collegata al contenuto utilizzando il file[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) proprietà. Inoltre, è anche possibile ottenere l'intervallo di origine utilizzando il file[**Fonte**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) proprietà del[**Proprietà documento**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)classe.

 Usiamo un semplice modello di file Excel Microsoft nell'esempio. La cartella di lavoro ha un intervallo denominato definito etichettato**MyRange** che fa riferimento a un valore di cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Rimozione delle proprietà personalizzate**

 Per rimuovere le proprietà personalizzate utilizzando Aspose.Cells, chiama il[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)metodo e passare il nome della proprietà del documento da rimuovere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Argomenti avanzati**
- [Aggiunta di proprietà personalizzate visibili all'interno del pannello Informazioni documento](/cells/it/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento incorporate](/cells/it/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specificare la versione del documento del file Excel utilizzando le proprietà del documento integrate](/cells/it/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specificare la lingua del file Excel utilizzando le proprietà del documento incorporate](/cells/it/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
