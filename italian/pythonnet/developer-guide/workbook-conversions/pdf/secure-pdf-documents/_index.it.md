---
title: Proteggi i documenti PDF
type: docs
weight: 120
url: /it/python-net/secure-pdf-documents/
description: Scopri come trasferire le opzioni di sicurezza PDF quando salvi i fogli di calcolo su PDF con Aspose.Cells for Python via .NET API.
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF crittografati. Per esempio:

- Proteggi i documenti con le password del proprietario e dell'utente in modo che non chiunque possa aprirli.
- Imposta restrizioni o autorizzazioni per il documento dopo l'apertura del documento. ad esempio, limitare se il contenuto del documento può essere stampato o estratto.

Questo articolo spiega come trasferire le opzioni di sicurezza PDF quando si salvano i fogli di calcolo su PDF.

{{% /alert %}}

 Aspose.Cells for Python via .NET fornisce[**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)per lavorare in sicurezza. È possibile impostare la password del proprietario e dell'utente durante il salvataggio su PDF. La password del proprietario o dell'utente sarà richiesta per aprire il documento crittografato PDF per la visualizzazione.

- La password dell'utente può essere nulla o una stringa vuota, in questo caso non verrà richiesta alcuna password all'utente all'apertura del documento PDF.
- L'apertura del documento PDF con la password del proprietario corretta consente l'accesso completo (senza alcuna restrizione di accesso specificata) al documento.
- L'apertura del documento PDF con la password utente corretta (o l'apertura di un documento che non dispone di una password utente) consente un accesso limitato secondo le autorizzazioni specificate.

Il codice di esempio riportato di seguito descrive come proteggere i PDF con Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) appena prima di renderizzarlo in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
