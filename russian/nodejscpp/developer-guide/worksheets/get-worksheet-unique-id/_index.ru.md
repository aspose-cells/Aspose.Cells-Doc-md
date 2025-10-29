---
title: Получить уникальный идентификатор листа с помощью Node.js через C++
linktitle: Получить уникальный идентификатор листа
type: docs
weight: 190
url: /ru/nodejs-cpp/get-worksheet-unique-id/
description: В этой статье показано, как программным способом получить уникальный идентификатор листа Excel, используя библиотеку Node.js и API C++.
keywords: уникальный id листа Excel Node.js через C++, уникальный id листа Node.js через C++
---

## **Получить уникальный идентификатор листа**

Aspose.Cells for Node.js via C++ предоставляет возможность получить уникальный идентификатор листа с помощью свойства [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--). Следующий фрагмент кода демонстрирует использование свойства [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) для отображения уникального id листа. Этот пример использует [пример файла Excel](105480213.xlsx).

### Исходный код

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
