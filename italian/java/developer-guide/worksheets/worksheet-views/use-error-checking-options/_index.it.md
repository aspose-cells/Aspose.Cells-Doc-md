---
title: Usa le opzioni di controllo degli errori
type: docs
weight: 60
url: /it/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire opzioni di controllo degli errori e regole. Gli utenti vedono spesso controlli degli errori quando creano formule, un triangolo piccolo nell'angolo in alto a destra di una cella evidenzia un problema con la cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.

{{% /alert %}} 
## **Tipi di errori**
Gli errori che significano che la formula non può restituire un risultato - come dividere un numero per zero - richiedono attenzione immediata e viene visualizzato un valore di errore nella cella. Fare clic sul triangolo verde mostra un punto esclamativo, facendo clic su questo si aprono una lista di opzioni. 

L'errore può essere risolto utilizzando le opzioni, o essere ignorato. Ignorare un errore significa che quell'errore non apparirà nei successivi controlli degli errori.

Aspose.Cells fornisce funzionalità di opzioni di controllo degli errori. La classe ErrorCheckOptions gestisce diversi tipi di controlli degli errori, ad esempio numeri memorizzati come testo, errori di calcolo della formula e errori di convalida. Utilizzare l'enumerazione ErrorCheckType per impostare il controllo degli errori desiderato.
## **Numeri memorizzati come testo**
Occasionalmente, i numeri potrebbero essere formattati e memorizzati nelle celle come testo. Questo può causare problemi con i calcoli o produrre ordini di ordinamento confusi. I numeri formattati come testo sono allineati a sinistra invece che a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controllare l'allineamento delle celle a cui si riferisce la formula: alcune o tutte quelle celle potrebbero essere numeri formattati come testo.

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:

1. Nel menu **Strumenti**, fare clic su **Opzioni**.
1. Seleziona la scheda Controllo errori.
   L'opzione **Numero memorizzato come testo** è selezionata per impostazione predefinita. 
1. Disabilitala.
   Guarda l'immagine sottostante su come il triangolo verde viene visualizzato per i dati in MS Excel.

![todo:image_alt_text](use-error-checking-options_1.png)

Il seguente codice di esempio mostra come disabilitare l'opzione di controllo degli errori del numero memorizzato come testo per un foglio di lavoro nel file XLS di modello utilizzando le API di Aspose.Cells. 

**Java**

{{< highlight csharp >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
