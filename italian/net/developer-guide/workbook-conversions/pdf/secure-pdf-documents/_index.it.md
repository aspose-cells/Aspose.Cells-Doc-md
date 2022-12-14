---
title: Proteggi i documenti PDF
type: docs
weight: 120
url: /it/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF crittografati. Ad esempio, devono proteggere i documenti con password dell'utente e del proprietario in modo che non tutti possano aprirli o vogliono limitare la stampa o l'estrazione del contenuto del documento.

Questo articolo spiega come trasferire le opzioni di sicurezza PDF durante il salvataggio di fogli di calcolo in PDF.

{{% /alert %}}

 Aspose.Cells fornisce il[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) spazio dei nomi per lavorare con la sicurezza. Il codice di esempio riportato di seguito descrive come proteggere i PDF con Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)appena prima di renderla in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
