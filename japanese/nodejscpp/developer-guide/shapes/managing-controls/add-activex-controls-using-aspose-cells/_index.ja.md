---
title: ActiveXコントロールをAspose.Cells for Node.js via C++を使用して追加
linktitle: Aspose.Cells を使用して ActiveX コントロールを追加する
type: docs
weight: 260
url: /ja/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Aspose.Cells for Node.js via C++を使用してワークシートにActiveXコントロールを追加する方法を学びます。 
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して[**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-)メソッドでActiveXコントロールを追加できます。このメソッドは、ワークシート内に追加するActiveXコントロールの種類を指定するパラメータ[**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/)を取ります。値は以下の通りです。

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

ActiveXコントロールをシェイプコレクション内に追加したら、[**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--)プロパティを介してActiveXコントロールオブジェクトにアクセスでき、その後さまざまなプロパティを設定できます。

{{% /alert %}}

Aspose.Cellsを使用してToggle Button ActiveXコントロールを追加するサンプルコードは、次のとおりです。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const sheet = wb.getWorksheets().get(0);

// Add Toggle Button ActiveX Control inside the Shape Collection
const s = sheet.getShapes().addActiveXControl(AsposeCells.ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX control object and set its linked cell property
const c = s.getActiveXControl();
c.setLinkedCell("A1");

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "AddActiveXControls_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
