---  
title: Node.jsとC++を使用して、ワークブックの自動回復プロパティを設定する方法。  
linktitle: ワークブックのAutoRecoverプロパティを設定する方法  
type: docs  
weight: 220  
url: /ja/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Aspose.Cells for Node.js via C++を使って、ワークブックの自動回復プロパティを設定する方法を学びます。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsを使用して、ワークブックの自動回復プロパティを設定できます。このプロパティのデフォルト値は**true**です。これを**false**に設定すると、Microsoft ExcelはそのExcelファイルの自動回復（自動保存）を無効にします。  

Aspose.Cellsは、このオプションを有効または無効にするための[**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--)プロパティを提供しています。  
{{% /alert %}}  

以下のコードは、ワークブックの[**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--)プロパティの使用方法を説明します。最初にこのプロパティのデフォルト値（**true**）を読み取り、その後**false**に設定してワークブックを保存します。次に再度ワークブックを読み取り、その時点でのこのプロパティの値（**false**）を確認します。  

## Node.jsコードによるワークブックの自動回復プロパティ設定  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **出力**  

上記のサンプルコードのコンソール出力は次の通りです。  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
