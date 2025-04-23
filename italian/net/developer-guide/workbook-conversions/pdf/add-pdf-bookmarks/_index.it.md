---
title: Aggiungi segnalibri PDF
type: docs
weight: 10
url: /it/net/add-pdf-bookmarks/
---

{{% alert color="primary" %}}

Questo articolo fornisce informazioni su come inserire segnalibri PDF durante la conversione di un foglio di calcolo in PDF.

Aspose.Cells ti consente di aggiungere segnalibri al volo. I segnalibri PDF possono migliorare notevolmente la navigabilità dei documenti lunghi. Quando si aggiungono collegamenti ai segnalibri del documento PDF, è possibile avere un controllo preciso sulla visualizzazione esatta desiderata, senza limitarsi a collegare a una pagina. È possibile impostare la visualizzazione precisa posizionando la pagina di destinazione e quindi creare il segnalibro.

{{% /alert %}}

Si prega di consultare il codice di esempio seguente per scoprire come aggiungere i segnalibri PDF. Il codice genera un foglio di lavoro semplice, specifica i segnalibri PDF con posizioni di destinazione e genera il file PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) poco prima di renderizzare il foglio di calcolo nel formato PDF. Così facendo, si garantisce che i valori dipendenti dalle formule vengano aggiornati e renderizzati correttamente nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
