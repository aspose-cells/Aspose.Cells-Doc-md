---
title: Salva Html con StreamProvider
type: docs
weight: 80
url: /it/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

Durante la conversione di campi excel che contengono iamges e forme in file html, spesso affrontiamo i seguenti due problemi:
1. Dove dovremmo salvare le immagini e le forme quando salviamo il file excel nel flusso html.
1. Sostituisci il percorso predefinito con il percorso escluso.

 Questo articolo spiega come implementare[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interfaccia per l'impostazione del[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) proprietà. Implementando questa interfaccia, sarai in grado di salvare le risorse create durante la generazione di HTML nelle tue posizioni o flussi di memoria specifici.

{{% /alert %}} 

 Questo è il codice principale che mostra l'utilizzo di[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)proprietà



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 Ecco il codice per*ExportStreamProvider* classe che implementa[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)interfaccia utilizzata all'interno del codice precedente.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

