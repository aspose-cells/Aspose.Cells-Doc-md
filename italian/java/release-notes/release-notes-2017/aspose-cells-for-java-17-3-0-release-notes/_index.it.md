---
title: Aspose.Cells for Java 17.3.0 Note di rilascio
type: docs
weight: 100
url: /it/java/aspose-cells-for-java-17-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.3.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.3.0/).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42205|L'impostazione della formula con risultati letterali a stringa lunga in un file Excel corrotto|Aumento|
|CELLSJAVA-42204|I bordi punteggiati del foglio di calcolo non sono stati visualizzati in HTML|Insetto|
|CELLSJAVA-42198|Il calcolo della formula è errato con il file Excel generato da Aspose.Cells|Insetto|
|CELLSJAVA-42156|I bordi superiore e inferiore delle celle sono spariti durante la conversione in HTML|Insetto|
|CELLSJAVA-42208|I commenti (alla fine) vengono tagliati verticalmente quando generati PDF tramite Aspose.Cells|Insetto|
|CELLSJAVA-42206|Le linee tratteggiate della serie per i grafici non vengono visualizzate correttamente nell'output PDF|Insetto|
|CELLSJAVA-42167 |Etichette dell'asse delle categorie visualizzate su due righe dopo la conversione del grafico in immagine|Insetto|
|CELLSJAVA-42199|Grafico a cascata, la linea dalla barra totale e la barra subito prima che manca|Insetto|
|CELLSJAVA-42201|Attività secondaria: etichette dell'asse delle categorie visualizzate su due righe dopo la conversione del grafico in immagine|Insetto|
|CELLSJAVA-42155|Il grafico esportato ha etichette dell'asse x diverse da quelle in Excel|Insetto|
|CELLSJAVA-42128|Il grafico è errato all'apertura e al salvataggio del file Excel di origine|Insetto|
|CELLSJAVA-42203|Il carattere è stato modificato dopo aver semplicemente caricato e salvato nuovamente lo XLSM|Insetto|
|CELLSJAVA-42196|La formattazione del file risultante è incasinata nel file salvato di nuovo|Insetto|
|CELLSJAVA-42195|Grafico a cascata, la serie Total sembra sbagliata|Insetto|
|CELLSJAVA-42181|Vista protetta dopo aver salvato nuovamente un file XLS|Insetto|
|CELLSJAVA-42045|L'immagine del grafico radar non viene generata|Insetto|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Personalizza le impostazioni di globalizzazione di una tabella pivot**
Utilizzando la recente versione 17.3.0 o successiva, gli sviluppatori possono personalizzare le impostazioni di globalizzazione di una tabella pivot in un file Excel. Possono modificare il testo del totale pivot, del totale parziale, del totale complessivo, di tutti gli elementi, di più elementi, delle etichette di colonna, delle etichette di riga e dei valori vuoti secondo i requisiti. Gli sviluppatori possono incorporare questa funzionalità nelle loro applicazioni .NET, indipendentemente dalla lingua del testo di Excel. Può essere arabo, hindi, polacco, ecc. Tutti i nuovi metodi supportati sono elencati di seguito:

1. **Aggiunge il metodo GlobalizationSettings.getPivotTotalName()** - Ottiene il nome dell'etichetta "Totale" nella tabella pivot. Gli sviluppatori possono eseguire l'override di questo metodo quando la tabella pivot contiene due o più campi pivot nell'area dati.
1. **Aggiunge il metodo GlobalizationSettings.getPivotGrandTotalName()** - Ottiene il nome dell'etichetta "Totale complessivo" nella tabella pivot.
1. **Aggiunge il metodo GlobalizationSettings.getMultipleItemsName()** - Ottiene il nome dell'etichetta "(Multiple Items)" nella tabella pivot.
1. **Aggiunge il metodo GlobalizationSettings.getAllName()** - Ottiene il nome dell'etichetta "(Tutto)" nella tabella pivot.
1. **Aggiunge GlobalizationSettings.getColumnLablesName()** metodo - Ottiene il nome dell'etichetta "Etichette colonna" nella tabella pivot.
1. **Aggiunge il metodo GlobalizationSettings.getRowLablesName()** - Ottiene il nome dell'etichetta "Row Labels" nella tabella pivot.
1. **Aggiunge il metodo GlobalizationSettings.getEmptyDataName()** - Ottiene il nome dell'etichetta "(vuoto)" nella tabella pivot.
1. **Aggiunge il metodo GlobalizationSettings.getSubTotalName(PivotFieldSubtotalType subTotalType)** - Ottiene il nome del tipo "PivotFieldSubtotalType" nella tabella pivot.

Questo esempio di codice illustra come personalizzare le impostazioni di globalizzazione di una tabella pivot. Crea una classe CustomPivotTableGlobalizationSettings derivata da una classe base GlobalizationSettings ed esegue l'override di tutti i relativi metodi necessari. Questi metodi restituiscono il testo personalizzato per Totale pivot, Totale parziale, Totale complessivo, Tutti gli elementi, Elementi multipli, Etichette colonna, Etichette riga, Valori vuoti. Quindi assegna l'oggetto di questa classe alla proprietà Workbook.GlobalizationSettings. Il codice carica il file excel di origine che contiene la tabella pivot, aggiorna e calcola i suoi dati e lo salva come file di output PDF. Gli sviluppatori possono anche salvare la cartella di lavoro in qualsiasi formato supportato.

**Java**

{{< highlight "java" >}}

 //Load your excel file

Workbook wb = new Workbook(dirPath + "samplePivotTableGlobalizationSettings.xlsx");



//Setting Custom Pivot Table Globalization Settings

wb.getSettings().setGlobalizationSettings(new CustomPivotTableGlobalizationSettings());



//Hide first worksheet that contains the data of the pivot table

wb.getWorksheets().get(0).setVisible(false);



//Access second worksheet

Worksheet ws = wb.getWorksheets().get(1);



//Access the pivot table, refresh and calculate its data

PivotTable pt = ws.getPivotTables().get(0);

pt.setRefreshDataFlag(true);

pt.refreshData();

pt.calculateData();

pt.setRefreshDataFlag(false);



//Pdf save options - save entire worksheet on a single pdf page

PdfSaveOptions options = new PdfSaveOptions();

options.setOnePagePerSheet(true);



//Save the output pdf 

wb.save(dirPath + "outputPivotTableGlobalizationSettings.pdf", options);



// it derives a new class, called CustomPivotTableGlobalizationSettings, from the GlobalizationSettings class, as follows:

class CustomPivotTableGlobalizationSettings extends GlobalizationSettings

{   

    //Gets the name of "Total" label in the PivotTable.

    //You need to override this method when the PivotTable contains two or more PivotFields in the data area.

    public String getPivotTotalName()

    {

        System.out.println("---------GetPivotTotalName-------------");

        return "AsposeGetPivotTotalName";

    }



    //Gets the name of "Grand Total" label in the PivotTable.

    public String getPivotGrandTotalName()

    {

        System.out.println("---------GetPivotGrandTotalName-------------");

        return "AsposeGetPivotGrandTotalName";

    }



    //Gets the name of "(Multiple Items)" label in the PivotTable.

    public String getMultipleItemsName()

    {

        System.out.println("---------GetMultipleItemsName-------------");

        return "AsposeGetMultipleItemsName";

    }



    //Gets the name of "(All)" label in the PivotTable.

    public String getAllName()

    {

        System.out.println("---------GetAllName-------------");

        return "AsposeGetAllName";

    }



    //Gets the name of "Column Labels" label in the PivotTable.

    public String getColumnLablesName()

    {

        System.out.println("---------GetColumnLablesName-------------");

        return "AsposeGetColumnLablesName";

    }



    //Gets the name of "Row Labels" label in the PivotTable.

    public String getRowLablesName()

    {

        System.out.println("---------GetRowLablesName-------------");

        return "AsposeGetRowLablesName";

    }



    //Gets the name of "(blank)" label in the PivotTable.

    public String getEmptyDataName()

    {

        System.out.println("---------GetEmptyDataName-------------");

        return "(blank)AsposeGetEmptyDataName";

    }



    //Gets the name of PivotFieldSubtotalType type in the PivotTable.

    public String getSubTotalName(int subTotalType)

    {

        System.out.println("---------GetSubTotalName-------------");



        switch (subTotalType)

        {

            case PivotFieldSubtotalType.SUM:

                return "AsposeSum";//polish



            case PivotFieldSubtotalType.COUNT:

                return "AsposeCount";



            case PivotFieldSubtotalType.AVERAGE:

                return "AsposeAverage";



            case PivotFieldSubtotalType.MAX:

                return "AsposeMax";



            case PivotFieldSubtotalType.MIN:

                return "AsposeMin";



            case PivotFieldSubtotalType.PRODUCT:

                return "AsposeProduct";



            case PivotFieldSubtotalType.COUNT_NUMS:

                return "AsposeCount";



            case PivotFieldSubtotalType.STDEV:

                return "AsposeStdDev";



            case PivotFieldSubtotalType.STDEVP:

                return "AsposeStdDevp";



            case PivotFieldSubtotalType.VAR:

                return "AsposeVar";

            case PivotFieldSubtotalType.VARP:

                return "AsposeVarp";

        }

        return "AsposeSubTotalName";

    }

}//End CustomPivotTableGlobalizationSettings

{{< /highlight >}}
### **Eseguire lo script lato client all'evento di modifica della pagina del controllo GridWeb**
Utilizzando la proprietà OnPageChangeClientFunction del controllo GridWeb, gli sviluppatori possono eseguire uno script lato client sull'evento di modifica della pagina perché il controllo GridWeb può contenere dati in più pagine. Potrebbero aver bisogno di visualizzare l'indice della pagina corrente nelle loro applicazioni web.

1. **Aggiunge una proprietà OnPageChangeClientFunction in GridWeb Control** - ottiene o imposta la funzione di script lato client da chiamare quando l'indice della pagina cambia. Ha effetto solo quando EnablePaging è vero.

Questo esempio di codice mostra l'utilizzo della proprietà OnPageChangeClientFunction. Imposta la proprietà con la funzione lato client denominata MyOnPageChange. Ora, ogni volta che l'utente cambierà la pagina GridWeb, chiamerà la funzione lato client MyOnPageChange che stampa il**indice della pagina corrente**sul**consolare**:

**Java**

{{< highlight "java" >}}

 // It is the client side function MyOnPageChange that will be executed because of setting OnPageChangeClientFunction ="MyOnPageChange"property in GridWeb.

function MyOnPageChange(index) {

    console.log("current page is:" + (index+1));

}



// The following code explains how to enable paging and set the OnPageChangeClientFunction property.

GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
### **Convalida l'intero foglio di lavoro di Excel**
Per impostazione predefinita, GridWeb convalida solo le celle aggiornate e non convalida l'intero foglio di lavoro di Excel. Tuttavia, se gli sviluppatori richiedono di convalidare l'intero foglio di lavoro di Excel sul lato client prima che GridWeb invii la richiesta al server, è necessario impostare la variabile needValidateall all'interno di acwmain.js su true.
### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

1. [Personalizza le impostazioni di globalizzazione per la tabella pivot](/cells/it/java/customize-globalization-settings-for-pivot-table/)
1. [Esegui la funzione lato client al cambio di pagina GridWeb](/cells/it/java/execute-client-side-function-on-gridweb-page-change/)
1. [Convalida l'intero foglio di lavoro anziché solo le celle aggiornate](/cells/it/java/validate-entire-worksheet-instead-of-only-the-updated-cells/)
