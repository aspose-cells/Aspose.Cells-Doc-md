---
title: Gestione delle proprietà del documento
type: docs
weight: 10
url: /it/java/managing-document-properties/
---
## **introduzione**

Microsoft Excel offre la possibilità di aggiungere proprietà ai file del foglio di calcolo. Queste proprietà del documento forniscono informazioni utili e sono suddivise in 2 categorie come descritto di seguito.

- Proprietà (integrate) definite dal sistema: le proprietà integrate contengono informazioni generali sul documento come titolo del documento, nome dell'autore, statistiche del documento e così via.
- Proprietà (personalizzate) definite dall'utente: proprietà personalizzate definite dall'utente finale sotto forma di coppia nome-valore.

{{% alert color="primary" %}}

Il punto più importante da sapere sulle proprietà integrate e personalizzate è che è possibile accedere e modificare le proprietà integrate, ma non è possibile crearle o rimuoverle, tuttavia è possibile creare e gestire proprietà del documento personalizzate.

{{% /alert %}}

## **Gestione delle proprietà del documento utilizzando Microsoft Excel**

 Microsoft Excel consente di gestire le proprietà dei documenti dei file Excel in modalità WYSIWYG. Si prega di seguire i passaggi seguenti per aprire il file**Proprietà** finestra di dialogo in Excel 2016.

1.  Dal**File** menù, selezionare**Informazioni**.

|**Selezionando Menu Informazioni**|
|:- |
|![cose da fare:immagine_alt_testo](managing-document-properties_1.png)|
1.  Clicca su**Proprietà**voce e selezionare "Proprietà avanzate".

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

 Aspose.Cells for Java scrive direttamente le informazioni su API e il numero di versione nei documenti di output. Ad esempio, dopo aver reso Document to PDF, Aspose.Cells for Java popola**Applicazione** campo con valore 'Aspose.Cells' e**PDF Produttore** campo con il valore, ad esempio 'Aspose.Cells for Java v17.9'.

Si prega di notare che non è possibile incaricare Aspose.Cells for Java di modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

### **Accesso alle proprietà del documento**

Aspose.Cells Le API supportano entrambi i tipi di proprietà del documento, integrate e personalizzate. Aspose.Cells'[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class rappresenta un file Excel e, come un file Excel, il file[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe può contenere più fogli di lavoro, ciascuno rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class mentre la raccolta di fogli di lavoro è rappresentata dal file[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)classe.

 Usa il[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)per accedere alle proprietà del documento del file come descritto di seguito.

-  Per accedere alle proprietà predefinite del documento, utilizzare[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  Per accedere alle proprietà del documento personalizzate, utilizzare il file[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 Sia il[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) e[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) restituire un'istanza di[**DocumentoPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . Questa raccolta contiene[**Proprietà documento**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)oggetti, ciascuno dei quali rappresenta una singola proprietà del documento incorporata o personalizzata.

 Spetta al requisito dell'applicazione come accedere a una proprietà, ovvero; utilizzando l'indice o il nome della proprietà da[**DocumentoPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)come dimostrato nell'esempio sottostante.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

 Il[**Proprietà documento**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)class consente di recuperare il nome, il valore e il tipo della proprietà del documento:

-  Per ottenere il nome della proprietà, utilizzare[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  Per ottenere il valore della proprietà, utilizzare[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)restituisce il valore come oggetto.
-  Per ottenere il tipo di proprietà, utilizzare[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . Questo restituisce uno dei[**Tipo di proprietà**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)valori di enumerazione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Aggiunta o rimozione di proprietà del documento personalizzate**

Come descritto in precedenza all'inizio di questo argomento, gli sviluppatori non possono aggiungere o rimuovere proprietà predefinite perché queste proprietà sono definite dal sistema, ma è possibile aggiungere o rimuovere proprietà personalizzate perché sono definite dall'utente.

### **Aggiunta di proprietà personalizzate**

 Aspose.Cells API hanno esposto il file[**Inserisci**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) metodo per il[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) class per aggiungere proprietà personalizzate alla raccolta. Il[**Inserisci**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) aggiunge la proprietà al file Excel e restituisce un riferimento per la nuova proprietà del documento come a[**Proprietà documento**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)oggetto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Configurazione della proprietà personalizzata "Link al contenuto".**

 Per creare una proprietà personalizzata collegata al contenuto di un determinato intervallo, chiama il metodo[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) ) metodo e passare il nome della proprietà e l'origine. Puoi verificare se una proprietà è configurata come collegata al contenuto utilizzando il file[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) proprietà. Inoltre, è anche possibile ottenere l'intervallo di origine utilizzando il file[**Fonte**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) proprietà del[**Proprietà documento**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)classe.

 Usiamo un semplice modello di file Excel Microsoft nell'esempio. La cartella di lavoro ha un intervallo denominato definito etichettato**MyRange** che fa riferimento a un valore di cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Rimozione delle proprietà personalizzate**

 Per rimuovere le proprietà personalizzate utilizzando Aspose.Cells, chiama il[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) e passare il nome della proprietà del documento da rimuovere.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
