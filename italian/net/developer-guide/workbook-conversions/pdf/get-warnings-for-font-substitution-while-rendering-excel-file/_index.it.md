---
title: Ricevi avvisi per la sostituzione dei caratteri durante il rendering del file Excel
type: docs
weight: 230
url: /it/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

volte, durante il rendering di un file Excel Microsoft in PDF, Aspose.Cells sostituisce i caratteri. Aspose.Cells fornisce una funzionalità che consente agli sviluppatori di sapere quale particolare carattere è stato sostituito attivando un avviso. Questa è una funzione utile che può aiutarti a identificare perché un Aspose.Cells reso PDF ha un aspetto diverso dal file Excel Microsoft originale in modo da poter intraprendere le azioni appropriate. Ad esempio, installando i caratteri mancanti in modo che i risultati del rendering abbiano lo stesso aspetto.

{{% /alert %}} 

Per ricevere avvisi per la sostituzione dei caratteri durante il rendering dei file Excel su PDF, implementa l'interfaccia IWarningCallback e imposta la proprietà PdfSaveOptions.WarningCallback con l'interfaccia implementata.

Lo screenshot qui sotto mostra un file Excel di origine che useremo nel codice seguente. Ha del testo nelle celle A6 e A7 in caratteri che non sono resi bene da Microsoft Excel.

|**Non tutti i caratteri vengono visualizzati correttamente**|
|:- |
|![cose da fare:immagine_alt_testo](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells sostituirà i caratteri nelle celle A6 e A7 con caratteri idonei come mostrato di seguito.

|**Font sostituiti**|
|:- |
|![cose da fare:immagine_alt_testo](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Scarica il file sorgente e l'output PDF**
È possibile scaricare il file Excel sorgente e l'output PDF dai seguenti collegamenti

- [fonte.xlsx](5112611.xlsx)
- [uscita.pdf](5112616.pdf)
## **Codice**
Il codice seguente implementa IWarningCallback e imposta la proprietà PdfSaveOptions.WarningCallback con l'interfaccia implementata. Ora, ogni volta che qualsiasi carattere verrà sostituito in qualsiasi cella, Aspose.Cells genererà un avviso all'interno del metodo WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Produzione**
Dopo aver convertito il file Excel di origine in PDF, gli avvisi vengono inviati alla console di debug in questo modo:

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Se il tuo foglio di calcolo contiene formule, è meglio chiamare il metodo Workbook.CalculateFormula appena prima di eseguire il rendering del foglio di calcolo nel formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
