---
title: Node.js kullanarak ve C++ üzerinden VBA Sertifikasını Dosyaya veya Akışa Aktarın
linktitle: VBA Sertifikasını Dosyaya veya Akışa Aktar
type: docs
weight: 90
url: /tr/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: VBA Dijital Sertifikasını bir dosya veya akışa dışa aktarmayı Aspose.Cells for Node.js via C++ kullanarak nasıl yapacağınızı öğrenin. VBA dijital sertifikalarının ham verilerine erişin.
---

{{% alert color="primary" %}}

Aspose.Cells, VBA Dijital Sertifikasını dosya veya bellek akışı gibi akışa aktarmanıza olanak tanır. [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--) özelliğini kullanarak VBA dijital sertifikasının ham verilerine erişebilirsiniz.

{{% /alert %}}

## **Node.js kullanarak VBA Sertifikasını Dosyaya veya Akışa Aktarın**

Lütfen, VBA Sertifikasının ham verilerini bir dosyaya kaydeden aşağıdaki örnek kodu inceleyin. Bu kodu içeren [örnek excel dosyasını buradaki bağlantıdan](5115031.xlsm) indirebilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file into workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleVBAProjectSigned.xlsm"));

// Retrieve bytes data of Digital Certificate of VBA Project
const certBytes = workbook.getVbaProject().getCertRawData();

// Save Certificate Data into FileStream
require("fs").writeFileSync(path.join(dataDir, "Cert_out_"), Uint8Array.from(certBytes));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
