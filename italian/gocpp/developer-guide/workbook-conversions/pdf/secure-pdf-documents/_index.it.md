---
title: Proteggi i documenti PDF con Golang tramite C++
linktitle: Documenti PDF sicuri
type: docs
weight: 120
url: /it/go-cpp/secure-pdf-documents/
description: Impara come proteggere i documenti PDF con password proprietario e utente usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF criptati. Ad esempio:

- Proteggere i documenti con password per proprietario e utente in modo che non possa aprirlo chiunque.
- Impostare restrizioni o autorizzazioni al documento dopo l'apertura del documento, ad esempio limitare se È possibile stampare o estrarre il contenuto del documento.

Questo articolo spiega come passare le opzioni di sicurezza PDF durante il salvataggio dei fogli di calcolo in PDF.

{{% /alert %}}

Aspose.Cells fornisce [**PdfSecurityOptions**](https://reference.aspose.com/cells/go-cpp/pdfsecurityoptions/) per lavorare sulla sicurezza. Puoi impostare password proprietarie e utente durante il salvataggio in PDF. La password proprietaria o la password utente sarà richiesta per aprire il documento PDF criptato per la visualizzazione.

- La password dell'utente può essere nulla o una stringa vuota, in questo caso non sarà richiesta alcuna password all'utente durante l'apertura del documento PDF.
- Aprire il documento PDF con la corretta password proprietaria consente l'accesso completo (senza restrizioni di accesso specificate) al documento.
- L'apertura del documento PDF con la corretta password dell'utente (o l'apertura di un documento che non ha una password utente) consente l'accesso limitato come le autorizzazioni specificate.

Il codice di esempio qui sotto descrive come proteggere i PDF con Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SecurePdfDocuments.go" >}}
{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è consigliabile chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) appena prima di convertirlo in PDF. Ciò garantisce che i valori dipendenti dalle formule siano ricalcolati e vengano visualizzati i valori corretti nel PDF.

{{% /alert %}}
