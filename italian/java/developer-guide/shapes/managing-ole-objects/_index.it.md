---
title: Gestione degli Oggetti OLE
type: docs
weight: 30
url: /it/java/managing-ole-objects/
---

## **Introduzione**

OLE (Object Linking and Embedding) è il framework Microsoft per una tecnologia di documento composto. In breve, un documento composto è qualcosa come una scrivania che può contenere oggetti visivi e informativi di ogni tipo: testo, calendari, animazioni, suoni, video in movimento, 3D, notizie continuamente aggiornate, controlli, e così via. Ogni oggetto della scrivania è un'entità di programma indipendente che può interagire con un utente e comunicare anche con altri oggetti sulla scrivania.

OLE (Object Linking and Embedding) è supportato da molti programmi diversi ed è utilizzato per rendere il contenuto creato in un programma disponibile in un altro. Ad esempio, puoi inserire un documento di Microsoft Word in Microsoft Excel. Per vedere che tipi di contenuto puoi inserire, fai clic su **Oggetto** nel menu **Inserisci**. Solo i programmi installati sul computer e che supportano gli oggetti OLE appaiono nella casella del **Tipo di oggetto**.

## **Inserimento di Oggetti OLE in un Foglio di Lavoro**

Aspose.Cells supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells ha la classe [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection) usata per aggiungere un nuovo oggetto OLE alla lista di raccolta. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), rappresenta un oggetto OLE. Ha alcuni membri importanti:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) specifica i dati dell'immagine (icona) di tipo matrice di byte. L'immagine verrà visualizzata per mostrare l'Oggetto OLE nel foglio di lavoro.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) specifica i dati dell'oggetto sotto forma di un array di byte. Questi dati verranno visualizzati nel relativo programma quando si fa doppio clic sull'icona dell'oggetto OLE.

L'esempio seguente mostra come aggiungere un oggetto OLE in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Estrazione degli oggetti OLE nel Workbook**

Nell'esempio seguente viene mostrato come estrarre gli oggetti OLE in un Workbook. L'esempio ottiene diversi oggetti OLE da un file XLS esistente e salva file diversi (DOC, XLS, PPT, PDF, ecc.) in base al tipo di formato file dell'oggetto OLE.

Ecco lo screenshot del file XLS di esempio, che contiene diversi oggetti OLE incorporati nel primo foglio di lavoro.

**Il file di modello contiene quattro oggetti OLE** 

![todo:image_alt_text](managing-ole-objects_1.png)

Dopo aver eseguito il codice, possiamo salvare file diversi in base ai rispettivi tipi di formato degli oggetti OLE. Di seguito sono riportati gli screenshot di alcuni dei file creati.

**Il file XLS estratto** 

![todo:image_alt_text](managing-ole-objects_2.png)

**Il file PPT estratto** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Estrazione del file MOL incorporato**

Aspose.Cells supporta l'estrazione di oggetti di tipi non comuni come MOL (file di dati molecolari contenente informazioni su atomi e legami). Il seguente frammento di codice dimostra l'estrazione di un file MOL incorporato e il salvataggio su disco utilizzando questo [file di esempio di Excel](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Argomenti avanzati**
- [Accesso e modifica dell'etichetta di visualizzazione dell'oggetto Ole collegato](/cells/it/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aggiornare automaticamente l'oggetto OLE tramite Microsoft Excel usando Aspose.Cells](/cells/it/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Estrarre gli oggetti OLE dal Workbook](/cells/it/java/extract-ole-objects-from-workbook/)
- [Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato](/cells/it/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
{{< app/cells/assistant language="java" >}}
