---
title: Proteggi i documenti PDF
type: docs
weight: 260
url: /it/java/secure-pdf-documents/
description: Proteggi i file PDF durante la conversione da file Excel. Questo articolo illustra la generazione del file PDF sicuro da Excel con Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF crittografati. Per esempio:

- Proteggi i documenti con le password del proprietario e dell'utente in modo che non chiunque possa aprirli.
- Imposta restrizioni o autorizzazioni per il documento dopo l'apertura del documento. ad esempio, limitare se il contenuto del documento può essere stampato o estratto.

Questo articolo spiega come trasferire le opzioni di sicurezza PDF quando si salvano i fogli di calcolo su PDF.

{{% /alert %}}

 Aspose.Cells fornisce[**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)per lavorare in sicurezza. È possibile impostare la password del proprietario e dell'utente durante il salvataggio su PDF. La password del proprietario o dell'utente sarà richiesta per aprire il documento crittografato PDF per la visualizzazione.

- La password dell'utente può essere nulla o una stringa vuota, in questo caso non verrà richiesta alcuna password all'utente all'apertura del documento PDF.
- L'apertura del documento PDF con la password del proprietario corretta consente l'accesso completo (senza alcuna restrizione di accesso specificata) al documento.
- L'apertura del documento PDF con la password utente corretta (o l'apertura di un documento che non dispone di una password utente) consente un accesso limitato secondo le autorizzazioni specificate.

Il codice di esempio seguente descrive come creare file PDF protetti con Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()subito prima di renderizzarlo in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
