---
title: Usa le opzioni di controllo degli errori
type: docs
weight: 60
url: /it/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire opzioni e regole di controllo degli errori. Gli utenti vedono spesso i controlli degli errori durante la creazione di formule, un piccolo triangolo nell'angolo in alto a destra di una cella evidenzia quando c'è un problema con una cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.

{{% /alert %}} 
## **Tipi di errori**
Gli errori che indicano che la formula non può restituire un risultato, come la divisione di un numero per zero, richiedono un'attenzione immediata e nella cella viene visualizzato un valore di errore. Facendo clic sul triangolo verde viene visualizzato un punto esclamativo, facendo clic su questo si apre un elenco di opzioni.

L'errore può essere risolto utilizzando le opzioni o essere ignorato. Ignorare un errore significa che quell'errore non verrà visualizzato in ulteriori controlli degli errori.

Aspose.Cells fornisce funzionalità di opzione di controllo degli errori. La classe ErrorCheckOptions gestisce diversi tipi di controllo degli errori, ad esempio numeri memorizzati come testo, errori di calcolo delle formule ed errori di convalida. Utilizzare l'enumerazione ErrorCheckType per impostare il controllo degli errori desiderato.
## **Numbers Memorizzato come testo**
Occasionalmente, i numeri potrebbero essere formattati e archiviati nelle celle come testo. Ciò può causare problemi con i calcoli o produrre ordinamenti confusi. Numbers formattati come testo sono allineati a sinistra anziché a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controlla l'allineamento nelle celle a cui fa riferimento la formula: alcune o tutte le celle potrebbero essere numeri formattati come testo.

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:

1.  Sul**Utensili** menu, fare clic**Opzioni**.
1. Selezionare la scheda Controllo errori.
   **Numero memorizzato come testo** l'opzione è selezionata per impostazione predefinita.
1. Disattivalo.
 Guarda l'immagine qui sotto su come viene visualizzato il triangolo verde per i dati in MS Excel.

![cose da fare:immagine_alt_testo](use-error-checking-options_1.png)

 Il codice di esempio seguente mostra come disabilitare i numeri archiviati come opzione di controllo degli errori di testo per un foglio di lavoro nel file modello XLS usando le API Aspose.Cells.

**Java**

{{< highlight "csharp" >}}

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
