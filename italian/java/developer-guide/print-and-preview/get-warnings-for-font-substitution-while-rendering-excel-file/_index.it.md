---
title: Ricevi avvisi per la sostituzione dei caratteri durante il rendering del file Excel
type: docs
weight: 120
url: /it/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

volte, durante il rendering di file Microsoft Excel in PDF, Aspose.Cells sostituisce i caratteri. Aspose.Cells fornisce una funzionalità che consente agli sviluppatori di sapere che un determinato carattere è stato sostituito attivando un avviso. Questa è una funzione utile che può aiutarti a identificare perché Aspose.Cells ha reso il PDF è diverso dal file Excel effettivo e puoi quindi intraprendere le azioni appropriate. Ad esempio, è possibile installare i caratteri mancanti in modo che i risultati del rendering abbiano lo stesso aspetto.

Se desideri ricevere gli avvisi per la sostituzione dei caratteri durante il rendering di un file Excel in PDF, implementa l'interfaccia IWarningCallback e imposta il metodo PdfSaveOptions.setWarningCallback() con l'interfaccia implementata.

{{% /alert %}}

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice seguente. Ha del testo nelle celle A6 e A7 in caratteri che non sono resi bene da Microsoft Excel.

![cose da fare:immagine_alt_testo](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells sostituirà i caratteri nelle celle A6 e A7 con caratteri idonei come mostrato di seguito.

![cose da fare:immagine_alt_testo](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Scarica il file sorgente e il PDF di output**

È possibile scaricare il file Excel di origine e il PDF di output dai seguenti collegamenti

- [fonte.xlsx](5472700.xlsx)
- [uscita.pdf](5472699.pdf)

 Il codice seguente implementa il[**AvvisoRichiamata**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) e impostare il[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) metodo con l'interfaccia implementata. Ora, ogni volta che qualsiasi carattere verrà sostituito in qualsiasi cella, Aspose.Cells genererà un avviso all'interno del metodo WarningCallback.warning().

{{< highlight "java" >}}

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

## **Uscita avvisi**

Dopo aver convertito il file di origine, nella console di debug vengono visualizzati i seguenti avvisi:

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare il metodo Workbook.calculateFormula appena prima di eseguire il rendering del foglio di calcolo in formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
