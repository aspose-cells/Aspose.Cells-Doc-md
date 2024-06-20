---
title: Ottieni avvisi per la sostituzione dei font durante il rendering del file Excel
type: docs
weight: 120
url: /it/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

A volte, quando si rendono file di Microsoft Excel in PDF, Aspose.Cells sostituisce i caratteri. Aspose.Cells fornisce una funzionalità che consente ai programmatori di sapere che un determinato carattere è stato sostituito generando un avviso. Questa è una funzionalità utile che può aiutarti a capire perché il PDF reso da Aspose.Cells è diverso rispetto al file di Excel effettivo e quindi puoi prendere azioni appropriate. Ad esempio, puoi installare i caratteri mancanti in modo che i risultati della resa possano apparire uguali.

Se desideri ottenere gli avvisi per la sostituzione dei caratteri durante la resa di un file Excel in PDF, implementa l'interfaccia IWarningCallback e imposta il metodo PdfSaveOptions.setWarningCallback() con la tua interfaccia implementata.

{{% /alert %}}

La schermata qui sotto mostra il file Excel di origine utilizzato nel codice seguente. Contiene del testo nelle celle A6 e A7 in caratteri che non sono ben resi da Microsoft Excel.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells sostituirà i font nelle celle A6 e A7 con font appropriati come mostrato di seguito.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Scarica file di origine e PDF di output**

È possibile scaricare il file Excel di origine e il PDF di output dai seguenti collegamenti

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

Il codice seguente implementa il [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) e imposta il metodo [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) con l'interfaccia implementata. Ora, ogni volta che viene sostituito un carattere in una qualsiasi cella, Aspose.Cells genererà un avviso all'interno del metodo WarningCallback.warning().

{{< highlight java >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **Avvisi di output**

Dopo la conversione del file di origine, i seguenti avvisi vengono visualizzati sulla console di debug:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

Se il foglio di lavoro contiene formule, è meglio chiamare il metodo Workbook.calculateFormula appena prima di rendere il foglio di lavoro nel formato PDF. Farlo garantirà che i valori dipendenti dalle formule vengano ricalcolati e i valori corretti vengano resi nel PDF. 

{{% /alert %}}
