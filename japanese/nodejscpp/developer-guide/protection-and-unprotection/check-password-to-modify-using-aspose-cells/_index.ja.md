---  
title: Aspose.Cells for Node.js via C++を使用した修正パスワードの確認  
linktitle: 修正パスワードの確認  
type: docs  
weight: 2400  
url: /ja/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Aspose.Cells for Node.js via C++を使用して修正パスワードが一致するかどうかを確認する方法を学びます。  
---  

{{% alert color="primary" %}}  
プログラムmatically、与えられたパスワードが**修正用パスワード**と一致するかどうかを確認する必要がある場合があります。Aspose.Cellsは`WorkbookSettings.writeProtection.validatePassword()`メソッドを提供しており、これを使用してパスワードの正確性を確認できます。  
{{% /alert %}}  

## **Microsoft Excelで変更するためのパスワードをチェックする**  

Microsoft Excelで作成するワークブックに**開くためのパスワード**および**変更するためのパスワード**を割り当てることができます。これらのパスワードを指定するためのMicrosoft Excelが提供するインターフェースを示すスクリーンショットをご覧ください。  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Aspose.Cells for Node.js via C++を使用した修正パスワードの確認例**  

以下のサンプルコードは、[ソースExcel](5112232.xlsx)ファイルを読み込みます。このファイルには、開くためのパスワードが1234、修正用パスワードが5678と設定されています。最初に、567が正しい修正パスワードかどうかを確認し、間違っていればfalseを返します。次に、5678が正しい修正パスワードかどうかをチェックし、正しければtrueを返します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **コンソール出力**  

上記のサンプルコードで[元のExcel](5112232.xlsx)ファイルをロードした後のコンソール出力はこちらです。  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
