---  
title: Node.jsを使った範囲境界の設定について  
linktitle: 範囲のボーダーを設定  
type: docs  
weight: 600  
url: /ja/nodejs-cpp/set-range-border/  
---  

## **可能な使用シナリオ**  
範囲に境界線を設定したい場合、各セルに個別に設定する必要はありません。範囲に対して境界線を設定できます。Aspose.Cells for Node.js via C++はこの機能を提供します。  
このサンプルコードは、Aspose.Cells for Node.js via C++を使用して範囲境界線を設定する方法を示しています。  

## **Excelで範囲のボーダーを設定する**  
Excelで範囲のボーダーを設定するには、次の手順に従います:  
1. ボーダーを適用する範囲のセルを選択します。  
2. リボンの「ホーム」タブに移動し、「フォント」グループを検索します。  
3. 「フォント」グループ内で、「ボーダー」ドロップダウンボタンをクリックします。  
<br>  
<img src="border.png" />  
4. ドロップダウンメニュー内のオプションから適用するボーダーの種類を選択します。プリセットのボーダースタイルを選択するか、独自のボーダーをカスタマイズすることができます。  
5. 希望のボーダースタイルを選択したら、そのボーダーが選択したセル範囲に適用されます。  

## **Aspose.Cells for Node.js via C++を使って範囲境界線を設定する**  
この例では、次のことができます:  

1. ワークブックを作成する。  
2. 最初のワークシートのセルにデータを追加します。  
3. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)を作成します。  
4. 範囲の内側の境界線を設定します。  
5. 範囲の外側の境界線を設定します。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
