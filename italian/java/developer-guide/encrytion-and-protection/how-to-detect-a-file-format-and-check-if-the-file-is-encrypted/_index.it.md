---
title: Come rilevare un formato di file e verificare se il file è crittografato
type: docs
weight: 2000
url: /it/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 A volte è necessario rilevare il formato di un file prima di aprirlo perché l'estensione del file non garantisce che il contenuto del file sia appropriato. Il file potrebbe essere crittografato (un file protetto da password) quindi non può essere letto direttamente o non dovremmo leggerlo. Aspose.Cells fornisce il[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)metodo statico e alcune API pertinenti che è possibile utilizzare per elaborare i documenti.

{{% /alert %}}

## **Java codice per rilevare il formato del file e verificare se il file è crittografato**

Il seguente codice di esempio illustra come rilevare un formato di file (utilizzando il percorso del file) e controllarne l'estensione. È inoltre possibile determinare se il file è crittografato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
