---
title: Stampa fogli di calcolo
type: docs
weight: 20
url: /it/net/print-spreadsheets/
---
Le impostazioni di impostazione della pagina forniscono anche diverse opzioni di stampa (denominate anche Opzioni foglio ) che consentono agli utenti di controllare le pagine stampate dei fogli di lavoro. Queste opzioni di stampa consentono agli utenti di:

- Selezionare un'area di stampa specifica del foglio di lavoro
- Stampa titoli
- Stampa griglia
- Stampa intestazioni riga/colonna
- Ottieni la qualità bozza
- Stampa commenti
- Stampa Cell Errori
- Definisci l'ordine delle pagine
  **Impostazione delle opzioni di stampa/foglio**

Aspose.Cells supporta tutte queste opzioni di stampa e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro desiderati utilizzando le diverse proprietà offerte dalla classe PageSetup. L'utilizzo di queste proprietà della classe PageSetup è discusso più dettagliatamente di seguito.
## **Imposta area di stampa**
Per impostazione predefinita, viene selezionata solo l'area di stampa che incorpora l'intera area del foglio di lavoro, che contiene i dati, ma gli sviluppatori possono anche stabilire un'area di stampa specifica del foglio di lavoro in base alle proprie esigenze.

 Per selezionare un'area di stampa specifica, gli sviluppatori possono utilizzare set**Area di stampa** metodo del**Impostazione della pagina** classe. È possibile fornire l'intervallo di celle dell'area di stampa a questo metodo come argomento.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Imposta i titoli di stampa**
 Aspose.Cells consente di designare le intestazioni di riga e colonna che si desidera ripetere su tutte le pagine del foglio di lavoro stampato. Per fare ciò, gli sviluppatori possono utilizzare set**PrintTitleColonne** e**setPrintTitleRows** metodi del**Impostazione della pagina** classe.

Le righe o colonne (da ripetere su tutte le pagine del foglio di lavoro stampato) sono definite passando i loro numeri di riga o colonna. Ad esempio, le righe sono definite come \ $1: \ $2 e le colonne sono definite come \ $A: \ $B.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Imposta altre opzioni di stampa**
**Impostazione della pagina** class fornisce anche diversi altri metodi per impostare le opzioni di stampa generali come segue:

- **metodo di setPrintGridline** , a questo metodo viene passato un parametro booleano che definisce se stampare o meno la griglia
- **metodo setPrintHeadings** a questo metodo viene passato un parametro booleano che definisce se stampare o meno le intestazioni di righe e colonne
- **metodo setBlackAndWhite** , a questo metodo viene passato un parametro booleano che definisce se stampare il foglio di lavoro in modalità bianco e nero o meno
- **metodo setPrintComments** , definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro
- **metodo setPrintDraft** , a questo metodo viene passato un parametro booleano che definisce se stampare il foglio di lavoro in qualità bozza o meno
- **metodo setPrintErrors** , definisce se stampare gli errori della cella come visualizzato, vuoto, trattino o N/D

 Per usare set**StampaCommenti** e impostare**Errori di stampa** metodi, Aspose.Cells fornisce anche due enumerazioni, PrintCommentsType e PrintErrorsType che contengono valori predefiniti da passare a parametri per impostare rispettivamente i metodi PrintComments e PrintErrors.

{{< highlight "csharp" >}}

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
## **Imposta l'ordine delle pagine**
**Impostazione della pagina**class fornisce il metodo set Order che viene utilizzato per ordinare la stampa di più pagine del foglio di lavoro. Ci sono due possibilità per ordinare le pagine come segue:

Down then over quindi stamperà tutte le pagine in basso prima di stampare le pagine a destra
Sopra e poi verso il basso quindi stamperà le pagine da sinistra a destra prima di stampare le pagine sottostanti
Aspose.Cells fornisce un'enumerazione, PrintOrderType, che contiene tutti i tipi di ordine predefiniti da assegnare al metodo setPage Order.

{{< highlight "csharp" >}}

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
