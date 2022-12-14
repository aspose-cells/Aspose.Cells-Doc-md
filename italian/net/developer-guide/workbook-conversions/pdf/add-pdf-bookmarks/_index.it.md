---
title: Aggiungi segnalibri PDF
type: docs
weight: 10
url: /it/net/add-pdf-bookmarks/
---
{{% alert color="primary" %}}

Questo articolo fornisce informazioni su come inserire segnalibri PDF durante la conversione di un foglio di calcolo in PDF.

Aspose.Cells consente di aggiungere segnalibri al volo. I segnalibri PDF possono migliorare drasticamente la navigabilità di documenti lunghi. Quando aggiungi collegamenti ai segnalibri al documento PDF, puoi avere un controllo preciso sulla visualizzazione esatta che desideri, non sei limitato al collegamento a una pagina. È possibile impostare la visualizzazione precisa posizionando la pagina di destinazione e quindi creare il segnalibro.

{{% /alert %}}

Si prega di consultare il seguente codice di esempio per scoprire come aggiungere segnalibri PDF. Il codice genera una semplice cartella di lavoro, specifica i segnalibri PDF con le posizioni di destinazione e genera il file PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

 Se il tuo foglio di calcolo ha formule, è meglio chiamare[**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) appena prima di eseguire il rendering del foglio di calcolo in formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano aggiornati e visualizzati correttamente nel PDF.

{{% /alert %}}
