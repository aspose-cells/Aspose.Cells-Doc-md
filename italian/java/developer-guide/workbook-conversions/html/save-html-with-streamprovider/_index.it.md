---
title: Salva Html con StreamProvider
type: docs
weight: 120
url: /it/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

Quando si convertono file Excel che contengono immagini e forme in file HTML, ci troviamo spesso di fronte ai seguenti due problemi:
1. Dove dovremmo salvare le immagini e le forme durante il salvataggio del file excel in formato html.
1. Sostituire il percorso predefinito con il percorso accettato.

Questo articolo spiega come implementare l'interfaccia [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) per impostare la proprietà [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider). Implementando questa interfaccia, sarà possibile salvare le risorse create durante la generazione di HTML nelle posizioni specifiche o nei flussi di memoria.

{{% /alert %}}

## Codice di esempio

Questo è il codice principale che mostra l'uso della proprietà [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Ecco il codice per la classe *ExportStreamProvider* che implementa l'interfaccia [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) utilizzata nel codice precedente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

{{< app/cells/assistant language="java" >}}
