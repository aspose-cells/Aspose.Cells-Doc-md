---  
title: Come rilevare il formato di un file e verificare se il file è criptato con Node.js tramite C++  
linktitle: Come individuare un formato di file e verificare se il file è criptato  
type: docs  
weight: 2700  
url: /it/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Impara come rilevare il formato di un file e controllare se un file è criptato usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A volte è necessario rilevare il formato di un file prima di aprirlo perché l'estensione del file non garantisce che il contenuto del file sia appropriato. Il file potrebbe essere criptato (protetto da password) e quindi non leggibile direttamente, o non dovremmo leggerlo. Aspose.Cells for Node.js via C++ fornisce il metodo statico [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) e alcune API pertinenti che puoi usare per processare i documenti.  
{{% /alert %}}  

Il seguente codice di esempio illustra come individuare un formato di file (utilizzando il percorso del file) e verificare la sua estensione. È anche possibile determinare se il file è criptato.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Detect file format
const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(require("fs").readFileSync(filePath)));

// Gets the detected load format
console.log("The spreadsheet format is: " + AsposeCells.FileFormatUtil.loadFormatToExtension(info.getLoadFormat()));

// Check if the file is encrypted.
console.log("The file is encrypted: " + info.isEncrypted());
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
