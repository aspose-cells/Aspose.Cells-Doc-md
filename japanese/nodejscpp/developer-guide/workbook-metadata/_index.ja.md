---  
title: Node.js経由のC++を使用したWorkbookMetadataの利用例  
linktitle: ワークブックメタデータ  
type: docs  
weight: 320  
url: /ja/nodejs-cpp/using-workbookmetadata/  
description: Workbookメタデータの編集方法について、Aspose.Cells for Node.js via C++を使用した学習。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは、メモリに軽量なワークブックのバージョンをロードして、そのメタデータ情報を編集することを可能にします。ワークブックをロードするには、[**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata)クラスを使用してください。  
{{% /alert %}}  

以下のサンプルコードは、[**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata)クラスを使用してワークブックのカスタムドキュメントプロパティを編集する例です。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを使ってワークブックを開くと、ドキュメントのプロパティを読むことができます。こちらは、[**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata)クラスを使ったサンプルコードです。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open Workbook metadata
const options = new AsposeCells.MetadataOptions(AsposeCells.MetadataType.Document_Properties);
const meta = new AsposeCells.WorkbookMetadata(path.join(dataDir, "Sample1.xlsx"), options);

// Set some properties
meta.getCustomDocumentProperties().add("test", "test");

// Save the metadata info
meta.save(path.join(dataDir, "Sample2.out.xlsx"));

// Open the workbook
const w = new AsposeCells.Workbook(path.join(dataDir, "Sample2.out.xlsx"));

// Read document property
console.log(w.getCustomDocumentProperties().get("test"));

console.log("Press any key to continue...");
```  

