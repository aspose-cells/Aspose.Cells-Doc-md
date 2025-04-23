---  
title: Node.js経由のC++を使ったワークブックの数式計算モード設定  
linktitle: ワークブックの式の計算モードを設定する  
description: この記事では、Microsoft Excelでワークブックの数式計算モードを設定する方法をAspose.Cells for Node.js via C++とともに紹介します。既存のExcelファイルを読み込むか新たに作成し、Aspose.Cellsの提供するメソッドを使用して数式計算モードを設定し、その結果を取得できます。最後に、変更を加えたExcelファイルをディスクに保存します。  
keywords: Aspose.Cells、Excel、ワークブック、数式計算モード、設定、Node.js via C++  
type: docs  
weight: 110  
url: /ja/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
Microsoft Excelでは、フォーミュラ計算モード、つまりフォーミュラの計算方法を設定できます。3つの可能な値があります。  

- 自動 - 何かが変更されるたびに再計算し、ワークブックが開かれるたびに再計算します。  
- データテーブル以外自動 - 何かが変更されるたびに再計算しますが、データテーブルを除外します。  
- マニュアル - ユーザーがF9またはCTRL+ALT+F9を押すか、ワークブックが保存されたときにのみ再計算します。  
{{% /alert %}}  

Microsoft Excelでの式計算モードを設定するには:  

1. **式**、次に**計算オプション**を選択します。  
1つのオプションを選択します。  

Aspose.Cells for Node.js via C++では、[**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--)モードのプロパティを使って**数式計算モード**を設定することもできます。これには、次の値のいずれかを持つ[**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype)列挙体を指定します。  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

