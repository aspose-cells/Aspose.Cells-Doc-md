---  
title: Dosya Formatını Nasıl Tespit Eder ve Node.js ile C++ Kullanarak Dosyanın Şifreli olup olmadığını Kontrol Edersiniz  
linktitle: Bir Dosya Biçimini Algılamak ve Dosyanın Şifreli Olup Olmadığını Kontrol Etme  
type: docs  
weight: 2700  
url: /tr/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Aspose.Cells for Node.js via C++ kullanarak bir dosya formatını nasıl tespit edeceğinizi ve bir dosyanın şifreli olup olmadığını nasıl kontrol edeceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  
Bazen bir dosyanın formatını açmadan önce tespit etmeniz gerekir çünkü dosya uzantısı dosya içeriğinin uygun olduğunu garanti etmez. Dosya şifreli olabilir (parola korumalı dosya) doğrudan okunamaz ya da okunmasına gerek olmayabilir. Aspose.Cells for Node.js via C++, [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) statik metodunu ve belgeleri işlemek için kullanabileceğiniz bazı ilgili API'leri sağlar.  
{{% /alert %}}  

Aşağıdaki örnek kod, dosya biçimini (dosya yolu kullanarak) algılamanın ve uzantısını kontrol etmenin nasıl yapıldığını göstermektedir. Ayrıca dosyanın şifreli olup olmadığını belirleyebilirsiniz.  

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
