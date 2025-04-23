---
title: Come individuare un formato di file e verificare se il file è criptato
type: docs
weight: 2700
url: /it/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

A volte è necessario rilevare il formato di un file prima di aprirlo perché l'estensione del file non garantisce che il contenuto del file sia appropriato. Il file potrebbe essere crittografato (protetto da password) quindi non può essere letto direttamente, o non dovrebbe essere letto. Aspose.Cells per Python via .NET fornisce il metodo statico [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) e alcune API pertinenti che puoi usare per elaborare i documenti.

{{% /alert %}}

Il seguente codice di esempio illustra come individuare un formato di file (utilizzando il percorso del file) e verificare la sua estensione. È anche possibile determinare se il file è criptato.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

