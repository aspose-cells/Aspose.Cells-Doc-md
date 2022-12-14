---
title: Proteggi i documenti PDF
type: docs
weight: 260
url: /it/java/secure-pdf-documents/
description: Proteggi i file PDF durante la conversione da file Excel. Questo articolo illustra la generazione di file PDF protetti da Excel con Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF crittografati. Ad esempio, devono proteggere i documenti con password dell'utente e del proprietario in modo che non tutti possano aprirli o vogliono limitare la stampa o l'estrazione del contenuto del documento.

Questo articolo spiega come trasferire le opzioni di sicurezza PDF durante il salvataggio di fogli di calcolo in PDF.

{{% /alert %}} 

 Aspose.Cells Le API forniscono il[**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)classe per lavorare con la sicurezza del formato di file PDF. Il codice di esempio seguente descrive come creare file PDF protetti con Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Se il foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) appena prima di renderla in PDF. Ciò garantisce che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
