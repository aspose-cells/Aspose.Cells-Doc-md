---  
title: メモリ使用量最適化と大規模データセットを扱うためのNode.js via C++でのビッグファイル処理  
linktitle: 大規模なデータセットを扱う場合のメモリ使用量を最適化する  
type: docs  
weight: 180  
url: /ja/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

大規模なデータセットを含むワークブックを作成したり、大きなMicrosoft Excelファイルを読み込む場合、プロセスが使用するRAMの総量は常に懸念事項です。この課題に対応するために調整可能な措置があります。Aspose.Cells for Node.js via C++はいくつかの関連オプションとAPI呼び出しを提供し、メモリ使用を抑制・最適化します。また、より効率的に動作させ、高速化できます。  

セルのデータのメモリ使用を最適化し、総合的なメモリコストを減らすために [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) オプションを使用してください。大規模なセルデータセットを構築する際、デフォルトの設定（[**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)）に比べて一定量のメモリを節約することができます。  

{{% /alert %}}  

## **メモリの最適化**  

### **大きなExcelファイルの読み取り**  

以下の例は、最適化モードで大きなMicrosoft Excelファイルを読み取る方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **大きなExcelファイルの書き込み**  

以下の例は、大規模なデータセットをワークシートに書き込む方法を最適化モードで示しています。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **注意**  

デフォルトオプションの[**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)はすべてのバージョンに適用されます。大規模なセルデータセットを持つワークブック作成などの特定の状況では、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)オプションがメモリ使用を最適化し、アプリケーションのメモリコストを削減することができます。ただし、このオプションは一部の特定のケースではパフォーマンス低下を引き起こすこともあります。  

1. **セルへのランダムかつ繰り返しアクセス**：セルコレクションへのアクセスに最も効率的な順序は、1行ごとにセルをアクセスし、その後行ごとに進む方法です。特に、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)、[**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection)、[**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)から取得した列挙子を使用して行やセルにアクセスすると、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)を使用した場合にパフォーマンスが最大化します。  
2. **セルや行の挿入と削除**：セルや行への挿入/削除操作が多い場合、*MemoryPreference*モードでは*Normal*モードに比べてパフォーマンスの低下が顕著になることに注意してください。  
3. **異なるセルタイプの操作**：ほとんどのセルが文字列値や数式を含む場合、メモリコストは*Normal*モードと同じですが、多くの空セルや、数値、ブール値などが含まれる場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)オプションはより良いパフォーマンスを提供します。  

{{< app/cells/assistant language="nodejs-cpp" >}}
