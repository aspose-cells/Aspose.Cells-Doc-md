---
title: Salva Html con StreamProvider
type: docs
weight: 80
url: /it/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

Quando si convertono file excel che contengono immagini e forme in file HTML, ci troviamo spesso di fronte ai seguenti due problemi:
1. Dove dovremmo salvare le immagini e le forme durante il salvataggio del file excel in formato html.
1. Sostituire il percorso predefinito con il percorso accettato.

Questo articolo spiega come implementare l'interfaccia [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) per impostare la proprietà [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider). Implementando questa interfaccia, sarai in grado di salvare le risorse create durante la generazione di HTML in posizioni specifiche o flussi di memoria.

{{% /alert %}} 

Questo è il codice principale che mostra l'uso della proprietà [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Ecco il codice per la classe *ExportStreamProvider* che implementa l'interfaccia [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) utilizzata nel codice sopra.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

{{< app/cells/assistant language="csharp" >}}
