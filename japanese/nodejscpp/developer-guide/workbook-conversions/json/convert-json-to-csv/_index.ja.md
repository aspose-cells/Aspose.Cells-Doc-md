---  
title: Node.js経由でC++を使用してJSONをCSVに変換  
linktitle: JSONをCSVに変換する  
type: docs  
weight: 210  
url: /ja/nodejs-cpp/convert-json-to-csv/  
description: Aspose.Cells for Node.js via C++を使用したJSONデータをCSVに変換する方法を学びましょう。  
---  

## **JSONをCSVに変換**  

Aspose.Cellsは、シンプルなJSONおよびネストされたJSONの両方をCSVに変換することをサポートしています。そのために、APIは[**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)および[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility)クラスを提供します。[**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)クラスは、[**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--)（配列をテーブルとして処理）などのJSONレイアウトのオプションを提供します。[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility)クラスは、[**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)クラスで設定されたレイアウトオプションを使用してJSONを処理します。  

次のコード例では、[**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions)および[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility)クラスを使用して[ソースJSONファイル](104398869.json)を読み込み、[出力CSVファイル](104398870.csv)を生成します。  

### **サンプルコード**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");


// Create sample JSON if missing
const jsonPath = path.join(sourceDir, "SampleJson.json");

// Read JSON file
const str = fs.readFileSync(jsonPath, "utf-8");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();

// Set JsonLayoutOptions
const importOptions = new AsposeCells.JsonLayoutOptions();
importOptions.setConvertNumericOrDate(true);
importOptions.setArrayAsTable(true);
importOptions.setIgnoreTitle(true);
AsposeCells.JsonUtility.importData(str, cells, 0, 0, importOptions);

// Save Workbook
workbook.save(outputDir + "SampleJson_out.csv");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
