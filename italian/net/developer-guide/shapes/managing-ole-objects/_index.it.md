---
title: Gestione degli Oggetti OLE
type: docs
weight: 50
url: /it/net/managing-ole-objects/
---

## **Introduzione**

OLE (Object Linking and Embedding) è il framework Microsoft per una tecnologia di documento composto. In breve, un documento composto è qualcosa come una scrivania che può contenere oggetti visivi e informativi di ogni tipo: testo, calendari, animazioni, suoni, video in movimento, 3D, notizie continuamente aggiornate, controlli, e così via. Ogni oggetto della scrivania è un'entità di programma indipendente che può interagire con un utente e comunicare anche con altri oggetti sulla scrivania.

OLE (Object Linking and Embedding) è supportato da molti programmi diversi ed è utilizzato per rendere il contenuto creato in un programma disponibile in un altro. Ad esempio, puoi inserire un documento di Microsoft Word in Microsoft Excel. Per vedere che tipi di contenuto puoi inserire, fai clic su **Oggetto** nel menu **Inserisci**. Solo i programmi installati sul computer e che supportano gli oggetti OLE appaiono nella casella del **Tipo di oggetto**.

### **Inserimento di oggetti OLE nel foglio di lavoro**

Aspose.Cells supporta l'aggiunta, l'estrazione e la manipolazione degli oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells ha la classe [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection), utilizzata per aggiungere un nuovo oggetto OLE alla lista di collezioni. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), rappresenta un oggetto OLE. Ha alcuni membri importanti:

- La proprietà [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) specifica i dati dell'immagine (icona) di tipo array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.
- La proprietà [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) specifica i dati dell'oggetto sotto forma di un array di byte. Questi dati verranno mostrati nel relativo programma quando si fa doppio clic sull'icona dell'oggetto OLE.

L'esempio seguente mostra come aggiungere un/i oggetto(i) OLE in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Estrazione degli oggetti OLE nel Workbook**

Nell'esempio seguente viene mostrato come estrarre gli oggetti OLE in un Workbook. L'esempio ottiene diversi oggetti OLE da un file XLS esistente e salva file diversi (DOC, XLS, PPT, PDF, ecc.) in base al tipo di formato file dell'oggetto OLE.

Dopo aver eseguito il codice, possiamo salvare file diversi in base ai rispettivi tipi di formato degli oggetti OLE.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Estrazione del file MOL incorporato**

Aspose.Cells supporta l'estrazione di oggetti di tipi non comuni come MOL (file di dati molecolari contenenti informazioni su atomi e legami). Il seguente frammento di codice illustra l'estrazione di un file MOL incorporato e il salvataggio su disco utilizzando questo [file di esempio in Excel](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Argomenti avanzati**
- [Accesso e modifica dell'etichetta di visualizzazione dell'oggetto Ole collegato](/cells/it/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aggiornare automaticamente l'oggetto OLE tramite Microsoft Excel usando Aspose.Cells](/cells/it/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Estrarre gli oggetti OLE dal Workbook](/cells/it/net/extract-ole-objects-from-workbook/)
- [Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato](/cells/it/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Inserimento di un file WAV come oggetto Ole](/cells/it/net/inserting-a-wav-file-as-an-ole-object/)

{{< app/cells/assistant language="csharp" >}}
