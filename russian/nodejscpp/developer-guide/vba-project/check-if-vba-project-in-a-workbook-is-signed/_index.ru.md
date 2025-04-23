---
title: Проверьте, подписан ли VBA проект в рабочей книге с помощью Node.js через C++
linktitle: Проверка подписан ли проект VBA в книге Excel
type: docs
weight: 70
url: /ru/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Узнайте, как проверить, подписан ли VBA проект в рабочей книге, с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Вы можете проверить подписан ли ваш проект VBA или нет, используя Microsoft Excel через меню **Инструменты > Цифровые подписи...**. Аналогичным образом, вы можете проверить это программным способом с помощью свойства [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) библиотеки Aspose.Cells.

{{% /alert %}}

## **Проверьте, подписан ли VBA-проект в рабочей книге с помощью Node.js**

Следующий код загружает рабочую книгу и проверяет, подписан ли VBA-проект с помощью свойства [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--). Свойство вернет **true**, если проект подписан, иначе — **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
