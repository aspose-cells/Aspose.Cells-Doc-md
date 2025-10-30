---  
title: Node.jsを使ったC++経由での、他言語での小計および合計ラベルの実装  
linktitle: 他の言語で小計または合計ラベルを実装する  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **可能な使用シナリオ**  

時々、中国語、日本語、アラビア語、ヒンディー語などの非英語言語で小計と合計のラベルを表示したい場合があります。Aspose.Cells for Node.js via C++は[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスと[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/)プロパティを使ってこれを可能にします。[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスの利用方法についてはこの記事を参照してください。  

- [ピーグラフのカスタムサブトータルラベルおよびその他のラベル用のGlobalizationSettingsクラスの使用](/cells/ja/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **他の言語で小計または合計ラベルを実装する**  

以下のサンプルコードは、[サンプルエクセルファイル](5115151.xlsx)を読み込み、中国語で小計と合計の名前を実装しています。参考のために、このコードで生成された[出力Excelファイル](5115152.xlsx)を確認してください。まず[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)クラスを作成し、それをコード内で使用します。  

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
// This function will return the sub total name
getTotalName(functionType) {
return "Chinese Total - 可能的用法";
}

// This function will return the grand total name
getGrandTotalName(functionType) {
return "Chinese Grand Total - 可能的用法";
}
}
```  

次に、上記で作成したクラスをコード内で次のように使用します：  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Set the globalization setting to change subtotal and grand total names
const globalizationSettings = new AsposeCells.GlobalizationSettings();
workbook.getSettings().setGlobalizationSettings(globalizationSettings);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply subtotal on A1:B10
const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
worksheet.getCells().subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

// Set the width of the first column
worksheet.getCells().setColumnWidth(0, 40);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
