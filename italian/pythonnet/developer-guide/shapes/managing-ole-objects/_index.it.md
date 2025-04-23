---
title: Gestione degli Oggetti OLE
type: docs
weight: 50
url: /it/python-net/managing-ole-objects/
---

## **Introduzione**

OLE (Object Linking and Embedding) è il framework Microsoft per una tecnologia di documento composto. In breve, un documento composto è qualcosa come una scrivania che può contenere oggetti visivi e informativi di ogni tipo: testo, calendari, animazioni, suoni, video in movimento, 3D, notizie continuamente aggiornate, controlli, e così via. Ogni oggetto della scrivania è un'entità di programma indipendente che può interagire con un utente e comunicare anche con altri oggetti sulla scrivania.

OLE (Object Linking and Embedding) è supportato da molti programmi diversi ed è utilizzato per rendere il contenuto creato in un programma disponibile in un altro. Ad esempio, puoi inserire un documento di Microsoft Word in Microsoft Excel. Per vedere che tipi di contenuto puoi inserire, fai clic su **Oggetto** nel menu **Inserisci**. Solo i programmi installati sul computer e che supportano gli oggetti OLE appaiono nella casella del **Tipo di oggetto**.

### **Inserimento di oggetti OLE nel foglio di lavoro**

Aspose.Cells per Python via .NET supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells per Python via .NET dispone della classe [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection), utilizzata per aggiungere un nuovo oggetto OLE alla lista della raccolta. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), rappresenta un oggetto OLE. Ha alcuni membri importanti:

- La proprietà [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) specifica i dati dell'immagine (icona) di tipo array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.
- La proprietà [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) specifica i dati dell'oggetto sotto forma di un array di byte. Questi dati verranno mostrati nel relativo programma quando si fa doppio clic sull'icona dell'oggetto OLE.

L'esempio seguente mostra come aggiungere un/i oggetto(i) OLE in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **Estrazione degli oggetti OLE nel Workbook**

Nell'esempio seguente viene mostrato come estrarre gli oggetti OLE in un Workbook. L'esempio ottiene diversi oggetti OLE da un file XLS esistente e salva file diversi (DOC, XLS, PPT, PDF, ecc.) in base al tipo di formato file dell'oggetto OLE.

Dopo aver eseguito il codice, possiamo salvare file diversi in base ai rispettivi tipi di formato degli oggetti OLE.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **Estrazione del file MOL incorporato**

Aspose.Cells per Python via .NET supporta l'estrazione di oggetti di tipi insoliti come MOL (file dati molecolari contenenti informazioni su atomi e legami). Il seguente snippet di codice dimostra come estrarre un file MOL incorporato e salvarlo su disco usando questo [file Excel di esempio](94896196.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **Argomenti avanzati**
- [Accesso e modifica dell'etichetta di visualizzazione dell'oggetto Ole collegato](/cells/it/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aggiornamento automatico dell'oggetto OLE](/cells/it/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Estrarre gli oggetti OLE dal Workbook](/cells/it/python-net/extract-ole-objects-from-workbook/)
- [Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato](/cells/it/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Inserimento di un file WAV come oggetto Ole](/cells/it/python-net/inserting-a-wav-file-as-an-ole-object/)

