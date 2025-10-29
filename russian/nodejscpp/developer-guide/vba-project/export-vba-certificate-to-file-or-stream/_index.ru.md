---
title: Экспортируйте сертификат VBA в файл или поток с помощью Node.js через C++
linktitle: Экспорт сертификата VBA в файл или поток
type: docs
weight: 90
url: /ru/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Узнайте, как экспортировать цифровой сертификат VBA в файл или поток с помощью Aspose.Cells for Node.js via C++. Получайте необработанные данные цифровых сертификатов VBA.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать цифровой сертификат VBA в поток, такой как файл или поток памяти. Вы можете получить доступ к сырым данным цифрового сертификата VBA, используя свойство [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--).

{{% /alert %}}

## **Экспортируйте сертификат VBA в файл или поток в Node.js**

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, который сохраняет сырые данные сертификата VBA в файл. Вы можете загрузить [образец excel файла, используемого в этом коде](5115031.xlsm) по предоставленной ссылке.

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
