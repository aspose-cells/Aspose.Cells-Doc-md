---
title: Stampa fogli di calcolo
type: docs
weight: 20
url: /it/net/print-spreadsheets/
---

Le impostazioni della configurazione pagina forniscono anche diverse Opzioni di stampa (anche indicate come Opzioni foglio) che consentono agli utenti di controllare le pagine stampate dei fogli di lavoro. Queste opzioni di stampa permettono agli utenti di:

- Selezionare un'area di stampa specifica del foglio di lavoro
- Stampare titoli
- Stampare griglie
- Stampare intestazioni di riga/colonna
- Ottenere la qualità a draft
- Stampare commenti
- Stampare gli errori delle celle
- Definire l'ordinamento delle pagine
  **Impostazione delle opzioni di stampa/foglio**

Aspose.Cells supporta tutte queste opzioni di stampa e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro desiderati utilizzando le varie proprietà offerte dalla classe PageSetup. L'utilizzo di queste proprietà della classe PageSetup è discusso di seguito in modo più dettagliato.
## **Impostare l'area di stampa**
Per impostazione predefinita, viene selezionata solo l'area di stampa che comprende l'intera area del foglio di lavoro che contiene dati, ma gli sviluppatori possono anche stabilire un'area di stampa specifica del foglio di lavoro secondo il loro desiderio.

Per selezionare un'area di stampa specifica, gli sviluppatori possono utilizzare il metodo **PrintArea** della classe **PageSetup**. È possibile fornire il range di celle dell'area di stampa a questo metodo come argomento.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Impostare i titoli di stampa**
Aspose.Cells consente di designare intestazioni di riga e colonna che si desidera ripetere su tutte le pagine del foglio di lavoro stampato. Per farlo, gli sviluppatori possono utilizzare i metodi **PrintTitleColumns** e **PrintTitleRows** della classe **PageSetup**.

Le righe o colonne (da ripetersi su tutte le pagine del foglio di lavoro stampato) sono definite passando i numeri delle rispettive righe o colonne. Ad esempio, le righe sono definite come \ $1: \ $2 e le colonne sono definite come \ $A: \ $B.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Impostare altre opzioni di stampa**
La classe **PageSetup** fornisce anche diversi altri metodi per impostare le opzioni di stampa generali come segue:

- metodo **setPrintGridlines**, a questo metodo viene passato un parametro booleano che definisce se stampare o meno le linee della griglia
- metodo **setPrintHeadings**, a questo metodo viene passato un parametro booleano che definisce se stampare o meno le intestazioni di riga e colonna
- metodo **setBlackAndWhite**, a questo metodo viene passato un parametro booleano che definisce se stampare il foglio di lavoro in modalità bianco e nero o meno
- metodo **setPrintComments**, definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro
- metodo **setPrintDraft**, a questo metodo viene passato un parametro booleano che definisce se stampare o meno il foglio di lavoro in modalità bozza
- metodo **setPrintErrors**, definisce se stampare gli errori delle celle come visualizzati, vuoti, trattini o N/D

Per utilizzare i metodi **PrintComments** e **PrintErrors**, Aspose.Cells fornisce anche due enumerazioni, PrintCommentsType & PrintErrorsType che contengono valori predefiniti da passare come parametri ai metodi **setPrintComments** e **setPrintErrors** rispettivamente.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **Imposta l'Ordine delle Pagine**
La classe **PageSetup** fornisce il metodo **setOrder** che viene utilizzato per ordinare le pagine multiple del tuo foglio di lavoro da stampare. Ci sono due possibilità per ordinare le pagine come segue:

Prima giù quindi stamperà tutte le pagine in basso prima di stampare le pagine a destra
Prima a sinistra quindi stamperà le pagine da sinistra a destra prima di stampare le pagine sotto
Aspose.Cells fornisce un'enumerazione, PrintOrderType, che contiene tutti i tipi di ordine predefiniti da assegnare al metodo **setPageOrder**.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
