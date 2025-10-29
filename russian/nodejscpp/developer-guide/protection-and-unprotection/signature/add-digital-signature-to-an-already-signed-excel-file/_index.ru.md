---
title: Добавьте цифровую подпись в уже подписанный файл Excel с помощью Node.js через C++
linktitle: Добавить цифровую подпись к уже подписанному файлу Excel
type: docs
weight: 20
url: /ru/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: В этой статье описывается, как добавить цифровую подпись в уже подписанный файл Excel с помощью Node.js и Aspose.Cells for Node.js via C++.
keywords: Добавьте цифровую подпись в уже подписанный файл Excel. Как добавить цифровую подпись в уже подписанный документ Excel с помощью Node.js через C++.
---

## **Возможные сценарии использования**

Aspose.Cells for Node.js via C++ предоставляет метод [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-), который можно использовать для добавления цифровой подписи в уже подписанный файл Excel.

{{% alert color="primary" %}}

Обратите внимание, при добавлении цифровой подписи в уже подписанный документ Excel, если исходный документ создан с помощью Aspose.Cells, он работает хорошо. Но если оригинальный документ создан другими движками (например, Microsoft Excel и др.), Aspose.Cells не сможет сохранить файл без изменений после загрузки и повторного сохранения, что сделает исходную подпись недействительной.

{{% /alert %}}

## **Как добавить цифровую подпись к уже подписанному файлу Excel**

Следующий пример кода демонстрирует, как использовать метод [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) для добавления цифровой подписи в уже подписанный файл Excel. Пожалуйста, посмотрите [пример файла Excel](50528280.xlsx), использованный в этом коде. Этот файл уже содержит цифровую подпись. Также ознакомьтесь с [выходным файлом Excel](50528281.xlsx), сгенерированным кодом. В этом примере используется демонстрационный сертификат [AsposeDemo.pfx](50528279.pfx), пароль которого **aspose**. На снимке экрана показан эффект от работы кода на примере файла Excel после выполнения.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
