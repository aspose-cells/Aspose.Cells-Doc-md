---
title: Gestione delle proprietà del documento
type: docs
weight: 10
url: /it/java/managing-document-properties/
---

## **Introduzione**

Microsoft Excel fornisce la possibilità di aggiungere proprietà ai file di fogli elettronici. Queste proprietà del documento forniscono informazioni utili e sono divise in 2 categorie come dettagliato di seguito.

- Proprietà predefinite di sistema (builtin): Le proprietà incorporano informazioni generali sul documento come il titolo del documento, il nome dell'autore, le statistiche del documento e così via.
- Proprietà definite dall'utente (personalizzate): Proprietà personalizzate definite dall'utente sotto forma di coppia nome-valore.

{{% alert color="primary" %}}

Il punto più importante da conoscere riguardo alle proprietà predefinite e personalizzate è che le proprietà predefinite possono essere accessate e modificate, ma non possono essere create o rimosse, mentre le proprietà personalizzate del documento possono essere create e gestite.

{{% /alert %}}

## **Gestione delle proprietà del documento utilizzando Microsoft Excel**

Microsoft Excel consente di gestire le proprietà del documento dei file Excel in modo WYSIWYG. Seguire i passaggi seguenti per aprire il dialogo **Proprietà** in Excel 2016.

1. Dal menu **File**, seleziona **Informazioni**.

|**Selezionare il menu Informazioni**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Clicca sulla voce **Proprietà** e seleziona "Proprietà avanzate".

|**Selezione Proprietà Avanzate**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Gestire le proprietà del documento del file.

|**Dialogo Proprietà**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Nel dialogo Proprietà, ci sono diverse schede, come Generale, Riepilogo, Statistiche, Contenuti e Personalizzati. Ogni scheda aiuta a configurare diversi tipi di informazioni relative al file. La scheda Personalizzati è utilizzata per gestire le proprietà personalizzate.

## **Lavorare con le proprietà del documento utilizzando Aspose.Cells**

Gli sviluppatori possono gestire dinamicamente le proprietà del documento utilizzando le API di Aspose.Cells. Questa funzionalità aiuta gli sviluppatori a memorizzare informazioni utili insieme al file, come quando il file è stato ricevuto, elaborato, con timestamp e così via.

{{% alert color="primary" %}}

Aspose.Cells for Java scrive direttamente le informazioni su API e Numero di versione nei documenti di output. Ad esempio, durante la resa del documento in PDF, Aspose.Cells for Java popola il campo **Applicazione** con il valore 'Aspose.Cells' e il campo **Produttore PDF** con il valore, ad esempio 'Aspose.Cells for Java v17.9'.

Si noti che non è possibile istruire Aspose.Cells for Java a modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

### **Accesso alle proprietà del documento**

Le API di Aspose.Cells supportano entrambi i tipi di proprietà del documento, integrate e personalizzate. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) di Aspose.Cells rappresenta un file Excel e, come un file Excel, la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) può contenere più fogli di lavoro, ognuno rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) mentre la collezione di fogli di lavoro è rappresentata dalla classe [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)

Utilizzare [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) per accedere alle proprietà del documento del file come descritto di seguito.

- Per accedere alle proprietà integrate del documento, utilizzare [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- Per accedere alle proprietà del documento personalizzate, utilizzare il [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

Sia il [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) che il [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) restituiscono un'istanza di [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection). Questa raccolta contiene [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) oggetti, ciascuno dei quali rappresenta una singola proprietà del documento incorporata o personalizzata.

È a discrezione delle esigenze dell'applicazione come accedere a una proprietà, cioè; utilizzando l'indice o il nome della proprietà da [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) come dimostrato nell'esempio sotto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) consente di recuperare il nome, il valore e il tipo della proprietà del documento:

- Per ottenere il nome della proprietà, utilizzare [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- Per ottenere il valore della proprietà, utilizzare [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) restituisce il valore come un Oggetto.
- Per ottenere il tipo di proprietà, utilizzare [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). Questo restituisce uno dei valori di enumerazione di [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Aggiunta o rimozione delle proprietà personalizzate del documento**

Come abbiamo descritto in precedenza all'inizio di questo argomento, i programmatori non possono aggiungere o rimuovere proprietà integrate perché queste proprietà sono definite dal sistema, ma è possibile aggiungere o rimuovere proprietà personalizzate poiché queste sono definite dall'utente.

### **Aggiunta di proprietà personalizzate**

Le API di Aspose.Cells hanno esposto il [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) metodo per la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) al fine di aggiungere proprietà personalizzate alla raccolta. Il metodo [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-) aggiunge la proprietà al file Excel e restituisce un riferimento per la nuova proprietà del documento come un oggetto [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Configurazione della proprietà personalizzata "Collegamento al contenuto"**

Per creare una proprietà personalizzata collegata al contenuto di un determinato intervallo, chiamare il metodo [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent-java.lang.String-java.lang.String-) e passare il nome della proprietà e la sorgente. È possibile verificare se una proprietà è configurata come collegata al contenuto utilizzando la proprietà [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent). Inoltre, è anche possibile ottenere l'intervallo di origine utilizzando la proprietà [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) della classe [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

Utilizziamo un file modello semplice di Microsoft Excel nell'esempio. Il workbook ha un intervallo denominato definito **MyRange**, che si riferisce a un valore della cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Rimozione delle proprietà personalizzate**

Per rimuovere le proprietà personalizzate utilizzando Aspose.Cells, chiamare il metodo [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove-java.lang.String-) e passare il nome della proprietà del documento da rimuovere.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
{{< app/cells/assistant language="java" >}}
