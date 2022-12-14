---
title: Come rilevare un formato di file e verificare se il file è crittografato
type: docs
weight: 2700
url: /it/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 A volte è necessario rilevare il formato di un file prima di aprirlo perché l'estensione del file non garantisce che il contenuto del file sia appropriato. Il file potrebbe essere crittografato (un file protetto da password) quindi non può essere letto direttamente o non dovremmo leggerlo. Aspose.Cells fornisce il[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) metodo statico e alcune API pertinenti che è possibile utilizzare per elaborare i documenti.

{{% /alert %}}

Il seguente codice di esempio illustra come rilevare un formato di file (utilizzando il percorso del file) e controllarne l'estensione. È inoltre possibile determinare se il file è crittografato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
