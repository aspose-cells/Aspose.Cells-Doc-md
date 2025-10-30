---
title: Node.jsをC++で使用してActiveXコンボボックスコントロールを更新
linktitle: ActiveX ComboBoxコントロールを更新
type: docs
weight: 170
url: /ja/nodejs-cpp/update-activex-combobox-control/
description: Aspose.Cells for Node.js via C++を使用してActiveXコンボボックスコントロールの値の読み書き方法を学びます。 
---

## **可能な使用シナリオ**
Aspose.Cells for Node.js via C++を使用してActiveXコンボボックスコントロールの値を読み書きできます。ActiveXコントロールには[Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--)を介してアクセスし、[ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--)で型を確認します。これは[ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/)の値を返し、それを[ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) オブジェクトにタイプキャストして、さまざまなプロパティを読み取りまたは変更できます。

以下のサンプルコードで使用される[サンプルExcelファイル](5115124.xlsx)をダウンロードしてください。
## **ActiveX ComboBoxコントロールを更新**
以下のスクリーンショットは、[サンプルExcelファイル](5115124.xlsx)に対するサンプルコードの効果を示しています。見るとおり、ActiveX ComboBoxの値が"これはコンボボックスコントロールです"に更新されています。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **サンプルコード**
次のサンプルコードでは、[サンプルExcelファイル](5115124.xlsx)内のActiveX ComboBoxコントロールの値を更新します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SourceFile_activex.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook(filePath);

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null)
{
// Access Shape ActiveX Control
const c = shape.getActiveXControl();

if (c instanceof AsposeCells.ComboBoxActiveXControl)
{
// Type cast ActiveXControl into ComboBoxActiveXControl and change its value
const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
comboBoxActiveX.setValue("This is combo box control with updated value.");

}

}

// Save the workbook
const outputFilePath = path.join(dataDir, "OutputFile_out.xlsx");
wb.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
