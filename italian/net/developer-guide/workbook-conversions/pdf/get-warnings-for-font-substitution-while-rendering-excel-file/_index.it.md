---
title: Ottieni avvisi per la sostituzione dei font durante il rendering del file Excel
type: docs
weight: 230
url: /it/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

A volte, durante la conversione di un file Microsoft Excel in PDF, Aspose.Cells sostituisce i font. Aspose.Cells fornisce una funzione che permette agli sviluppatori di sapere quale particolare font è stato sostituito scatenando un avviso. Si tratta di una funzionalità utile che può aiutarti a capire perché un PDF generato da Aspose.Cells appare diverso dal file di origine di Microsoft Excel, in modo da poter adottare azioni appropriate. Ad esempio, installare i font mancanti in modo che i risultati della conversione siano uguali.

{{% /alert %}} 

Per ottenere avvisi per la sostituzione dei font durante la conversione dei file Excel in PDF, implementare l'interfaccia IWarningCallback e impostare la proprietà PdfSaveOptions.WarningCallback con la tua interfaccia implementata.

La schermata sottostante mostra un file Excel di origine che utilizzeremo nel codice seguente. Contiene del testo nelle celle A6 e A7 con caratteri che non vengono visualizzati correttamente in Microsoft Excel.

|**Non tutti i font vengono visualizzati correttamente**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells sostituirà i font nelle celle A6 e A7 con font appropriati come mostrato di seguito.

|**Font sostituiti**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Scarica file di origine e PDF di output**
È possibile scaricare il file Excel di origine e il PDF di output dai seguenti collegamenti

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **Codice**
Il codice seguente implementa l'interfaccia IWarningCallback e imposta la proprietà PdfSaveOptions.WarningCallback con l'interfaccia implementata. Ora, ogni volta che un font verrà sostituito in una cella, Aspose.Cells sconterà un avviso all'interno del metodo WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Output**
Dopo la conversione del file Excel di origine in PDF, gli avvisi vengono visualizzati sulla console di debug come segue:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo Workbook.CalculateFormula appena prima di rendere il foglio di calcolo nel formato PDF. In questo modo ci si assicurerà che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti vengano resi nel PDF.

{{% /alert %}}
