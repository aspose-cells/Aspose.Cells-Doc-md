---
title: Documenti PDF sicuri
type: docs
weight: 120
url: /it/net/secure-pdf-documents/
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF criptati. Ad esempio:

- Proteggere i documenti con password per proprietario e utente in modo che non possa aprirlo chiunque.
- Impostare restrizioni o autorizzazioni al documento dopo l'apertura del documento, ad esempio limitare se È possibile stampare o estrarre il contenuto del documento.

Questo articolo spiega come passare le opzioni di sicurezza PDF durante il salvataggio dei fogli di calcolo in PDF.

{{% /alert %}}

Aspose.Cells fornisce [**PdfSecurityOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) per lavorare con la sicurezza. È possibile impostare password per proprietario e utente durante il salvataggio in PDF. Sarà necessaria la password del proprietario o dell'utente per aprire il documento PDF criptato per la visualizzazione.

- La password dell'utente può essere nulla o una stringa vuota, in questo caso non sarà richiesta alcuna password all'utente durante l'apertura del documento PDF.
- L'apertura del documento PDF con la corretta password del proprietario consente l'accesso completo (senza alcuna restrizione di accesso specificata) al documento.
- L'apertura del documento PDF con la corretta password dell'utente (o l'apertura di un documento che non ha una password utente) consente l'accesso limitato come le autorizzazioni specificate.

Il codice di esempio qui sotto descrive come proteggere i PDF con Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) proprio prima di renderlo in PDF. Ciò garantisce che i valori dipendenti dalle formule vengano ricalcolati e i valori corretti siano resi nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
