---
title: Node.js ve C++ kullanarak Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırakma
linktitle: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak
type: docs
weight: 310
url: /tr/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabı nesnesinin yönetilmeyen kaynaklarını nasıl serbest bırakacağınızı öğrenin. 
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) metodunu sağlayarak [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) nesnesinin yönetilmeyen kaynaklarını serbest bırakmanızı sağlar. Dispose deseni, yalnızca dosya ve boru tutamağı, kayıt defteri tutamağı, bekleme tutamağı veya yönetilmeyen bellek bloklarına işaret eden iş nesneleriyle erişen nesneler için kullanılır. Bu, çöp toplayıcının kullanılmayan yönetilen nesneleri geri kazanmakta çok verimli olması, ancak yönetilmeyen nesneleri geri kazanamaması nedeniyle yapılır.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) nesnesi artık *System.IDisposable* arayüzünü uygular ve tek bir yöntem olan [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) içerir. Ya doğrudan [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) metodunu çağırabilir veya *Using* ifadesiyle bu yöntemi otomatik olarak çağırabilirsiniz.

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
