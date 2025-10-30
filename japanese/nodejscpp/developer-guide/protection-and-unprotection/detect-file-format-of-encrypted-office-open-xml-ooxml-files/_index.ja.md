---  
title: 暗号化されたOffice Open XML  OOXMLファイルのファイルフォーマットをNode.jsとC++経由で検出  
linktitle: 暗号化されたOffice Open XMLファイルのファイル形式を検出する  
type: docs  
weight: 340  
url: /ja/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Aspose.Cells for Node.js via C++を使用して暗号化されたOOXMLファイルのファイル形式を検出する方法を学びます。  
---  

{{% alert color="primary" %}}  

**Office Open XML**（または**OOXML**、**Microsoft Open XML**（MOX）とも呼ばれる）は、Microsoftが開発したXMLベースのファイル形式であり、スプレッドシート、チャート、プレゼンテーション、ワードプロセッシングドキュメントの表現に使用されます。  

{{% /alert %}}  

Aspose.Cellsは、暗号化された**Microsoft Open XML**ファイルのファイル形式を検出する方法を提供しています。ファイルタイプを識別するには、[FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-)メソッドを以下のコード例のように使用します。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "encryptedBook1.out.tmp");

fs.writeFileSync(filePath, Buffer.from([0x50, 0x4B, 0x03, 0x04]));
const stream = fs.readFileSync(filePath);
AsposeCells.FileFormatUtil.verifyPassword(stream, "1234");
const fileFormatInfo = AsposeCells.FileFormatUtil.detectFileFormat(stream);

console.log("File Format: " + fileFormatInfo.getFileFormatType());
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
