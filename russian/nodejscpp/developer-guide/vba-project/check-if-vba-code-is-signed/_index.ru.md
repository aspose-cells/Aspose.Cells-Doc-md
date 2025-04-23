---
title: Проверьте, подписан ли VBA код с помощью Node.js через C++
linktitle: Проверить, подписан ли код VBA
type: docs
weight: 100
url: /ru/nodejs-cpp/check-if-vba-code-is-signed/
description: Узнайте, как проверить, подписан ли проект VBA с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells позволяет пользователю проверить, подписан ли проект кода VBA или нет. Используйте свойство [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) для проверки, подписан ли проект кода VBA или нет.

{{% /alert %}}

Следующий код показывает, как проверить, подписан ли VBA-код с помощью свойства [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--). Вы можете использовать любой из ваших файлов Excel для тестирования этого кода. Для тестирования можно использовать [этот Excel-файл, использованный в коде](5115032.xlsm).

## **Проверьте, подписан ли VBA-код в Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## Вывод в консоль

Ниже представлен вывод в консоль вышеупомянутого кода с использованием [образцового файла Excel](5115032.xlsm), предоставленного по ссылке.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
