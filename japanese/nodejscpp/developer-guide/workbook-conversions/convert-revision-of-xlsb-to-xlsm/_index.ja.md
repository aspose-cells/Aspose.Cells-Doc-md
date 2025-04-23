---  
title: XLSBのリビジョンをC++経由のNode.jsでXLSMに変換  
linktitle: XLSBのリビジョンをXLSMに変換する  
type: docs  
weight: 290  
url: /ja/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Aspose.Cells for Node.js via C++を使い、XLSBファイルのリビジョンを完全にXLSMフォーマットに変換する方法を学習。  
---  

{{% alert color="primary" %}}  

Aspose.Cellsは現在、XLSBファイルのリビジョンを完全にXLSMファイルに変換することをサポートしています。リビジョンは\xl\revisionsパス内にあります。拡張子をZIPに変更することで閲覧できます。\xl\revisions パスには .bin 拡張子のファイルが含まれています。  

Aspose.Cellsを使用してXLSBファイルをXLSMに変換した際、これらの .bin ファイルは正常に .xml ファイルに変換されることが、これら2つのスクリーンショットで示されています。  

{{% /alert %}}  

以下のコード例は、Aspose.Cells for Node.js via C++を使用してXLSBファイルをXLSM形式に変換する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

