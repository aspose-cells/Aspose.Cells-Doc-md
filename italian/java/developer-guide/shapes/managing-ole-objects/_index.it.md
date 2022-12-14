---
title: Gestione degli oggetti OLE
type: docs
weight: 30
url: /it/java/managing-ole-objects/
---
## **introduzione**

OLE (Object Linking and Embedding) è il framework di Microsoft per una tecnologia di documenti composti. In breve, un documento composto è qualcosa di simile a un display desktop che può contenere oggetti visivi e informativi di ogni tipo: testo, calendari, animazioni, suoni, video in movimento, 3D, notizie continuamente aggiornate, controlli e così via. Ogni oggetto desktop è un'entità programma indipendente che può interagire con un utente e comunicare anche con altri oggetti sul desktop.

 OLE (Object Linking and Embedding) è supportato da molti programmi diversi e viene utilizzato per rendere il contenuto creato in un programma disponibile in un altro. Ad esempio, è possibile inserire un documento Word Microsoft in Excel Microsoft. Per vedere quali tipi di contenuto è possibile inserire, fare clic su**Oggetto** sul**Inserire** menù. Nel file vengono visualizzati solo i programmi installati sul computer e che supportano gli oggetti OLE**Tipo di oggetto** scatola.

## **Inserimento di oggetti OLE in un foglio di lavoro**

Aspose.Cells supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo Aspose.Cells ha il[**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)class, utilizzata per aggiungere un nuovo oggetto OLE all'elenco di raccolte. Un'altra classe,[**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), rappresenta un oggetto OLE. Ha alcuni membri importanti:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)specifica i dati dell'immagine (icona) del tipo di array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)specifica i dati dell'oggetto sotto forma di un array di byte. Questi dati verranno visualizzati nel relativo programma quando si fa doppio clic sull'icona dell'oggetto OLE.

Nell'esempio seguente viene illustrato come aggiungere un oggetto OLE in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Estrazione di oggetti OLE nella cartella di lavoro**

L'esempio seguente mostra come estrarre oggetti OLE in una cartella di lavoro. L'esempio ottiene oggetti OLE diversi da un file XLS esistente e salva file diversi (DOC, XLS, PPT, PDF e così via) in base al tipo di formato file dell'oggetto OLE.

Ecco lo screenshot del file XLS modello, ha diversi oggetti OLE incorporati nel primo foglio di lavoro.

**Il file modello contiene quattro oggetti OLE** 

![cose da fare:immagine_alt_testo](managing-ole-objects_1.png)

Dopo aver eseguito il codice, possiamo salvare diversi file in base ai rispettivi tipi di formato degli oggetti OLE. Di seguito sono riportati gli screenshot per alcuni dei file creati.

**Il file XLS estratto** 

![cose da fare:immagine_alt_testo](managing-ole-objects_2.png)

**Il file PPT estratto** 

![cose da fare:immagine_alt_testo](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Estrazione del file MOL incorporato**

Aspose.Cells supporta l'estrazione di oggetti di tipi non comuni come MOL (file di dati molecolari contenente informazioni su atomi e legami). Il seguente frammento di codice illustra l'estrazione del file MOL incorporato e il suo salvataggio su disco utilizzando this[file excel di esempio](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Argomenti avanzati**
- [Accedi e modifica l'etichetta di visualizzazione dell'oggetto Ole collegato](/cells/it/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aggiorna automaticamente l'oggetto OLE tramite Microsoft Excel utilizzando Aspose.Cells](/cells/it/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Estrai oggetti OLE dalla cartella di lavoro](/cells/it/java/extract-ole-objects-from-workbook/)
- [Ottenere o impostare l'identificatore di classe dell'oggetto OLE incorporato](/cells/it/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
