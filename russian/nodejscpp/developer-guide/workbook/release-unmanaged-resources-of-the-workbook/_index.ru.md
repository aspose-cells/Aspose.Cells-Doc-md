---
title: Освободите необработанные ресурсы книги с помощью Node.js через C++
linktitle: Освобождение неуправляемых ресурсов книги
type: docs
weight: 310
url: /ru/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Узнайте, как освобождать необработанные ресурсы объекта Workbook с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) метод для освобождения неуправляемых ресурсов объекта [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Шаблон dispose используется только для объектов, получающих доступ к неуправляемым ресурсам, таким как дескрипторы файлов и каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это потому, что сборщик мусора очень эффективен в освобождении неиспользуемых управляемых объектов, но не способен освобождать неуправляемые объекты.

{{% /alert %}}

Объект [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) теперь реализует интерфейс *System.IDisposable*, который имеет один метод [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--). Вы можете вызвать метод [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) напрямую или воспользоваться оператором *Using* для автоматического вызова этого метода.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create workbook object
const wb1 = new AsposeCells.Workbook();

// Call Dispose method
wb1.dispose();

// Call Dispose method via a scoped approach
(async () => {
const wb2 = new AsposeCells.Workbook();
// Any other code goes here
wb2.dispose();
})();
```
