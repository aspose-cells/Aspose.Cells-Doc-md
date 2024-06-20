---
title: Documenti PDF sicuri
type: docs
weight: 120
url: /it/python-net/secure-pdf-documents/
description: Scopri come passare opzioni di sicurezza PDF durante il salvataggio di fogli di calcolo in PDF con Aspose.Cells per Python via .NET API.
keywords: Python scrive opzioni di sicurezza in pdf, crittografa documento PDF 
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF criptati. Ad esempio:

- Proteggere i documenti con password per proprietario e utente in modo che non possa aprirlo chiunque.
- Impostare restrizioni o autorizzazioni al documento dopo l'apertura del documento, ad esempio limitare se È possibile stampare o estrarre il contenuto del documento.

Questo articolo spiega come passare le opzioni di sicurezza PDF durante il salvataggio dei fogli di calcolo in PDF.

{{% /alert %}}

Aspose.Cells for Python via .NET fornisce [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) per lavorare con la sicurezza. È possibile impostare le password proprietario e utente durante il salvataggio in PDF. Sarà necessaria la password proprietario o la password utente per aprire il documento PDF crittografato per la visualizzazione.

- La password dell'utente può essere nulla o una stringa vuota, in questo caso non sarà richiesta alcuna password all'utente durante l'apertura del documento PDF.
- L'apertura del documento PDF con la corretta password del proprietario consente l'accesso completo (senza alcuna restrizione di accesso specificata) al documento.
- L'apertura del documento PDF con la corretta password dell'utente (o l'apertura di un documento che non ha una password utente) consente l'accesso limitato come le autorizzazioni specificate.

Il codice di esempio qui sotto descrive come proteggere i PDF con Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) proprio prima di renderlo in PDF. Ciò garantisce che i valori dipendenti dalle formule vengano ricalcolati e i valori corretti siano resi nel PDF.

{{% /alert %}}
