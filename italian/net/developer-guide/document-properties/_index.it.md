---
title: Gestire le proprietà del documento
linktitle: Proprietà del documento
type: docs
weight: 80
url: /it/net/managing-document-properties/
description: Scopri come gestire le proprietà del documento tramite l API Aspose.Cells for NET.
keywords: Come gestire le proprietà del documento in C#, Ottenere o impostare le proprietà del documento usando C#, Aggiungere o eliminare le proprietà del documento tramite C#, Inserire o rimuovere le proprietà del documento con C#, Come accedere alle proprietà del documento tramite l API Aspose.Cells for NET.
---


## **Introduzione**

Microsoft Excel fornisce la possibilità di aggiungere proprietà ai file di fogli elettronici. Queste proprietà del documento forniscono informazioni utili e sono divise in 2 categorie come dettagliato di seguito.

- Proprietà predefinite di sistema (builtin): Le proprietà incorporano informazioni generali sul documento come il titolo del documento, il nome dell'autore, le statistiche del documento e così via.
- Proprietà definite dall'utente (personalizzate): Proprietà personalizzate definite dall'utente sotto forma di coppia nome-valore.

{{% alert color="primary" %}}

Il punto più importante da conoscere sulle proprietà integrate e personalizzate è che le proprietà integrate possono essere accessibili e modificate, ma non create o rimosse. Tuttavia, le proprietà personalizzate possono essere create e gestite.

{{% /alert %}}

## **Come gestire le proprietà del documento con Microsoft Excel**

Microsoft Excel ti permette di gestire le proprietà dei file Excel in modo WYSIWYG. Segui i seguenti passaggi per aprire il **Dialogo Proprietà** in Excel 2016.

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

## **Come lavorare con le proprietà del documento utilizzando Aspose.Cells**

Gli sviluppatori possono gestire dinamicamente le proprietà del documento utilizzando le API di Aspose.Cells. Questa funzionalità aiuta gli sviluppatori a memorizzare informazioni utili insieme al file, come quando il file è stato ricevuto, elaborato, con timestamp e così via.

{{% alert color="primary" %}}

Aspose.Cells for .NET scrive direttamente le informazioni su API e Numero di Versione nei documenti di output. Ad esempio, al momento del rendering del Documento in PDF, Aspose.Cells for .NET popola il campo **Applicazione** con il valore 'Aspose.Cells' e il campo **Produttore PDF** con il valore, ad es. 'Aspose.Cells v17.9'.

Si noti che non è possibile istruire Aspose.Cells for .NET a modificare o rimuovere queste informazioni dai Documenti di output.

{{% /alert %}}

### **Come accedere alle proprietà del documento**

Le API di Aspose.Cells supportano entrambi i tipi di proprietà del documento, integrate e personalizzate. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) di Aspose.Cells rappresenta un file Excel e, come un file Excel, la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) può contenere più fogli di lavoro, ognuno rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) mentre la collezione di fogli di lavoro è rappresentata dalla classe [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)

Utilizzare [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) per accedere alle proprietà del documento del file come descritto di seguito.

- Per accedere alle proprietà integrate del documento, utilizzare [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- Per accedere alle proprietà personalizzate del documento, utilizzare [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

Sia il [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) che il [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) restituiscono l'istanza di [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Questa raccolta contiene [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) oggetti, ognuno dei quali rappresenta una singola proprietà del documento integrata o personalizzata.

È a discrezione delle esigenze dell'applicazione come accedere a una proprietà, cioè; utilizzando l'indice o il nome della proprietà da [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) come dimostrato nell'esempio sotto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

La classe [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) consente di recuperare il nome, il valore e il tipo della proprietà del documento:

- Per ottenere il nome della proprietà, utilizzare [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- Per ottenere il valore della proprietà, utilizzare [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) restituisce il valore come un Oggetto.
- Per ottenere il tipo di proprietà, utilizzare [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type). Questo restituisce uno dei valori di enumerazione [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype). Dopo aver ottenuto il tipo di proprietà, utilizzare uno dei metodi **DocumentProperty.ToXXX** per ottenere il valore del tipo appropriato anziché utilizzare [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). I metodi **DocumentProperty.ToXXX** sono descritti nella tabella sotto.

{{% alert color="primary" %}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) fornisce anche un insieme di metodi che restituiscono i valori di altri tipi di dati.

{{% /alert %}}

|**Nome membro**|**Descrizione**|**Metodo ToXXX**|
| :- | :- | :- |
|Boolean|Il tipo di dati della proprietà è Booleano|ToBool|
|Date|Il tipo di dati della proprietà è DataOra. Nota che Microsoft Excel memorizza solo <br>la parte della data, nessuna ora può essere memorizzata in una proprietà personalizzata di questo tipo|ToDateTime|
|Float|Il tipo di dati della proprietà è Double|ToDouble|
|Number|Il tipo di dati della proprietà è Int32|ToInt|
|String|Il tipo di dati della proprietà è Stringa|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Come Aggiungere o Rimuovere Proprietà del Documento Personalizzate**

Come abbiamo descritto in precedenza all'inizio di questo argomento, i programmatori non possono aggiungere o rimuovere proprietà integrate perché queste proprietà sono definite dal sistema, ma è possibile aggiungere o rimuovere proprietà personalizzate poiché queste sono definite dall'utente.

### **Come Aggiungere Proprietà Personalizzate**

Le API di Aspose.Cells hanno esposto il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) per la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) al fine di aggiungere proprietà personalizzate alla raccolta. Il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) aggiunge la proprietà al file di Excel e restituisce un riferimento per la nuova proprietà del documento come un oggetto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Come Configurare Proprietà Personalizzata “Collegamento al contenuto”**

Per creare una proprietà personalizzata collegata al contenuto di un determinato intervallo, chiamare il metodo [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) e passare il nome della proprietà e la sorgente. È possibile verificare se una proprietà è configurata come collegata al contenuto utilizzando la proprietà [**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent). Inoltre, è anche possibile ottenere l'intervallo di origine utilizzando la proprietà [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) della classe [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

Utilizziamo un file modello semplice di Microsoft Excel nell'esempio. Il workbook ha un intervallo denominato definito **MyRange**, che si riferisce a un valore della cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Come rimuovere proprietà personalizzate**

Per rimuovere le proprietà personalizzate utilizzando Aspose.Cells, chiamare il metodo [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove) e passare il nome della proprietà del documento da rimuovere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Argomenti avanzati**
- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato](/cells/it/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato](/cells/it/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specificare la lingua del file Excel utilizzando le proprietà di documento incorporate](/cells/it/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="csharp" >}}
