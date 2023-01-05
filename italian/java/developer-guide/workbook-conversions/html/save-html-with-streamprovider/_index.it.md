---
title: Salva Html con StreamProvider
type: docs
weight: 120
url: /it/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

Quando convertiamo i campi excel che contengono immagini e forme in file html, spesso affrontiamo i seguenti due problemi:
1. Dove dovremmo salvare le immagini e le forme quando salviamo il file excel nel flusso html.
1. Sostituisci il percorso predefinito con il percorso escluso.

 Questo articolo spiega come implementare[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interfaccia per l'impostazione del[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) proprietà. Implementando questa interfaccia, sarai in grado di salvare le risorse create durante la generazione di HTML nelle tue posizioni o flussi di memoria specifici.

{{% /alert %}}

## Codice d'esempio

 Questo è il codice principale che mostra l'utilizzo di[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)proprietà

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 Ecco il codice per*ExportStreamProvider* classe che implementa[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interfaccia utilizzata all'interno del codice precedente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

