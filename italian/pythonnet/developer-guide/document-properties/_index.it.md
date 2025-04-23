---
title: Gestire le proprietà del documento
linktitle: Proprietà del documento
type: docs
weight: 80
url: /it/python-net/managing-document-properties/
description: Impara come Gestire le Proprietà del Documento tramite le API Aspose.Cells for Python via .NET.
keywords: Come Gestire le Proprietà del Documento in C#, Ottenere o Impostare Proprietà del Documento usando C#, Aggiungere o Eliminare Proprietà del Documento tramite C#, Inserire o Rimuovere Proprietà del Documento con C#, Come Accedere alle Proprietà del Documento usando ASPose.Cells for Python via .NET API.
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

Gli sviluppatori possono gestire dinamicamente le proprietà del documento usando le API Aspose.Cells for Python via .NET. Questa funzione aiuta gli sviluppatori a memorizzare informazioni utili insieme al file, come quando il file è stato ricevuto, elaborato, marcato con timestamp, e così via.

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET scrive direttamente le informazioni su API e Numero di Versione nei documenti di output. Ad esempio, durante la conversione di un Documento in PDF, Aspose.Cells for Python via .NET popola il campo **Application** con 'Aspose.Cells' e il campo **PDF Producer** con il valore, ad esempio 'Aspose.Cells per Python via .NET v17.9'.

Si prega di notare che non è possibile istruire Aspose.Cells for Python via .NET a modificare o rimuovere queste informazioni dai Documenti di output.

{{% /alert %}}


### **Come Aggiungere o Rimuovere Proprietà del Documento Personalizzate**

Come abbiamo descritto in precedenza all'inizio di questo argomento, i programmatori non possono aggiungere o rimuovere proprietà integrate perché queste proprietà sono definite dal sistema, ma è possibile aggiungere o rimuovere proprietà personalizzate poiché queste sono definite dall'utente.

### **Come Aggiungere Proprietà Personalizzate**

Le API di Aspose.Cells for Python via .NET hanno esposto il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) per la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) per aggiungere proprietà personalizzate alla collezione. Il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) aggiunge la proprietà al file Excel e restituisce un riferimento alla nuova proprietà del documento come oggetto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Argomenti avanzati**
- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato](/cells/it/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato](/cells/it/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specificare la lingua del file Excel utilizzando le proprietà di documento incorporate](/cells/it/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

