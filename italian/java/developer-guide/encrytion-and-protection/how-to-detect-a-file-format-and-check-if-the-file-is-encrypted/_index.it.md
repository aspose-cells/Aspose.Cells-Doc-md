---
title: Come individuare un formato di file e verificare se il file è criptato
type: docs
weight: 2000
url: /it/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

A volte è necessario individuare il formato di un file prima di aprirlo perché l'estensione del file non garantisce che il contenuto del file sia appropriato. Il file potrebbe essere criptato (un file protetto da password), quindi non può essere letto direttamente, oppure non dovremmo leggerlo. Aspose.Cells fornisce il metodo statico [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)) e alcune API correlate che è possibile utilizzare per elaborare i documenti.

{{% /alert %}}

## **Codice Java per individuare il formato del file e verificare se il file è criptato**

Il seguente codice di esempio illustra come individuare un formato di file (utilizzando il percorso del file) e verificare la sua estensione. È anche possibile determinare se il file è criptato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
