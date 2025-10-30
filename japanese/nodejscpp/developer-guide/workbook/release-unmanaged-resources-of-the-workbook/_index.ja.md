---
title: Node.js経由のC++を使ってワークブックの未使用リソースを解放
linktitle: ブックのアンマネージリソースを解放する
type: docs
weight: 310
url: /ja/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Aspose.Cells for Node.js via C++を使用してWorkBookオブジェクトの未管理リソースを解放する方法を学習 
---

{{% alert color="primary" %}}

Aspose.Cellsは[**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--)メソッドを提供し、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)オブジェクトの未管理リソースを解放します。このdisposeパターンは、ファイルやパイプハンドル、レジストリハンドル、待機ハンドル、または未管理メモリブロックへのポインタなどの未管理リソースにアクセスするオブジェクトにのみ使われます。これは、ガベージコレクターは未管理オブジェクトの再回収に非常に効率的ですが、未管理オブジェクトの回収はできないためです。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)オブジェクトは現在、*System.IDisposable*インターフェースを実装しており、単一のメソッド[**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--)を持ちます。直接[**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--)メソッドを呼び出すか、*Using*ステートメントを使って自動的にこのメソッドを呼び出すことも可能です。

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
{{< app/cells/assistant language="nodejs-cpp" >}}
