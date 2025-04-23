---
title: Documenti PDF sicuri
type: docs
weight: 260
url: /it/java/secure-pdf-documents/
description: Proteggi i file PDF durante la conversione da file Excel. Questo articolo mostra come generare file PDF sicuri da Excel con l API Aspose.Cells for Java.
keywords: documenti pdf sicuri java, documenti pdf sicuri, excel in pdf sicuro, excel in pdf sicuro java, converti excel in pdf sicuro, converti excel in pdf sicuro java, converti excel in pdf protetto da password, converti excel in pdf protetto da password java, excel in pdf protetto da password java, excel in pdf protetto da password
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF criptati. Ad esempio:

- Proteggere i documenti con password per proprietario e utente in modo che non possa aprirlo chiunque.
- Impostare restrizioni o autorizzazioni al documento dopo l'apertura del documento, ad esempio limitare se È possibile stampare o estrarre il contenuto del documento.

Questo articolo spiega come passare le opzioni di sicurezza PDF durante il salvataggio dei fogli di calcolo in PDF.

{{% /alert %}}

Aspose.Cells fornisce [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) per lavorare con la sicurezza. È possibile impostare password per proprietario e utente durante il salvataggio in PDF. Sarà necessaria la password del proprietario o dell'utente per aprire il documento PDF criptato per la visualizzazione.

- La password dell'utente può essere nulla o una stringa vuota, in questo caso non sarà richiesta alcuna password all'utente durante l'apertura del documento PDF.
- L'apertura del documento PDF con la corretta password del proprietario consente l'accesso completo (senza alcuna restrizione di accesso specificata) al documento.
- L'apertura del documento PDF con la corretta password dell'utente (o l'apertura di un documento che non ha una password utente) consente l'accesso limitato come le autorizzazioni specificate.

Il codice di esempio di seguito descrive come creare file PDF protetti con l'API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) appena prima di renderlo in PDF. Ciò assicura che i valori dipendenti dalla formula vengano ricalcolati e i valori corretti vengano resi in PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
