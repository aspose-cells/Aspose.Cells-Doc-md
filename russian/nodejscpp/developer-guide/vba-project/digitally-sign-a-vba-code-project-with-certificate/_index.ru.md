---
title: Цифровая подпись VBA проекта с помощью сертификата с помощью Node.js через C++
linktitle: Цифровая подпись проекта VBA с помощью сертификата
type: docs
weight: 110
url: /ru/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Узнайте, как цифрово подписать VBA проект с помощью сертификата, используя Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Вы можете цифрово подписать ваш проект VBA с помощью Aspose.Cells и его метода [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Пожалуйста, следуйте этим шагам, чтобы проверить, подписан ли ваш файл Excel с помощью сертификата.

- Нажмите **Visual Basic** на вкладке **Разработчиков**, чтобы открыть **Интегрированную среду разработки Visual Basic for Applications**
- Нажмите **Сервис** > **Цифровые подписи...** в **Среде VBA**

и отобразится **Форма цифровой подписи**, показывающая, подписан ли документ цифровым сертификатом или нет.

{{% /alert %}} 

## **Цифровая подпись VBA-проекта с помощью сертификата в Node.js**

Следующий пример кода демонстрирует использование метода [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Здесь приведены входные и выходные файлы примера. Вы можете использовать любой файл Excel и любой сертификат для тестирования этого кода.

- [Исходный файл Excel](5115028.xlsm), используемый в образцовом коде.
- [Образец файла pfx](5115039.pfx) для создания цифровой подписи. Пожалуйста, установите его на ваш компьютер, чтобы запустить этот код. Пароль - 1234.
- [Файл Excel вывода](5115029.xlsm), сгенерированный образцовым кодом.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Set up paths
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const pfxPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.pfx");
const workbookPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.xlsm");

// Set Digital Signature
const password = "1234";
const comment = "Signing Digital Signature using Aspose.Cells";
const digitalSignature = new AsposeCells.DigitalSignature(fs.readFileSync(pfxPath), password, comment, new Date());

// Create workbook object from excel file
const workbook = new AsposeCells.Workbook(workbookPath);

// Sign VBA Code Project with Digital Signature
workbook.getVbaProject().sign(digitalSignature);

// Save the workbook
workbook.save(path.join(outputDir, "outputDigitallySignVbaProjectWithCertificate.xlsm"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
