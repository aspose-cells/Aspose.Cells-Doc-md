---  
title: Node.js経由のC++を使ったファイル形式の検出と暗号化確認方法  
linktitle: ファイルフォーマットを検出してファイルが暗号化されているかどうかをチェックする方法  
type: docs  
weight: 2700  
url: /ja/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Aspose.Cells for Node.js via C++を使用してファイル形式を検出し、ファイルが暗号化されているかどうかを確認する方法を学びます。  
---  

{{% alert color="primary" %}}  
時には、ファイルの拡張子だけでは内容が適切かどうかわからないため、開く前にファイルの形式を検出する必要があります。ファイルが暗号化されている（パスワード保護されたファイル）場合、直接は読み込めませんし、読むべきではありません。Aspose.Cells for Node.js via C++は、ドキュメントを処理するための[**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-)静的メソッドといくつかの関連APIを提供します。  
{{% /alert %}}  

次のサンプルコードは、ファイルパスを使用してファイルの形式を検出し、その拡張子をチェックし、ファイルが暗号化されているかどうかを判断する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Detect file format
const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(require("fs").readFileSync(filePath)));

// Gets the detected load format
console.log("The spreadsheet format is: " + AsposeCells.FileFormatUtil.loadFormatToExtension(info.getLoadFormat()));

// Check if the file is encrypted.
console.log("The file is encrypted: " + info.isEncrypted());
```  
