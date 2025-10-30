---
title: Node.js経由でフォームコントロールにマクロを割り当てる（C++利用）
linktitle: フォームコントロールにマクロを割り当てる
type: docs
weight: 60
url: /ja/nodejs-cpp/assign-macro-to-form-control/
description: Aspose.Cells for Node.js via C++を使用して、ボタンなどのフォームコントロールにマクロコードを割り当てる方法を学ぶ 
keywords: Node.js経由でフォームコントロールにマクロを割り当て（C++利用）、フォームコントロール用マクロコード（Node.js経由C++）、XLSMに統合されたマクロ（Node.js/C++）
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、ボタンなどのフォームコントロールにマクロコードを割り当てることができます。Workbook内のフォームコントロールに新しいマクロコードを割り当てるには、[**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--)プロパティを使用してください。

{{% /alert %}}

 以下のサンプルコードは、新しいワークブックを作成し、フォームボタンにマクロコードを割り当て、その出力をXLSM形式で保存します。Microsoft Excelで出力されたXLSMファイルを開くと、次のマクロコードが見えます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## ** Node.jsでフォームコントロールにマクロを割り当て**

 マクロコード付きの出力XLSMファイルを生成するサンプルコードをこちらに示します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);

const moduleIdx = workbook.getVbaProject().getModules().add(sheet);
const module = workbook.getVbaProject().getModules().get(moduleIdx);
module.setCodes(
"Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub"
);

const button = sheet.getShapes().addButton(2, 0, 2, 0, 28, 80);
button.setPlacement(AsposeCells.PlacementType.FreeFloating);
button.getFont().setName("Tahoma");
button.getFont().setIsBold(true);
button.getFont().setColor(AsposeCells.Color.Blue);
button.setText("Aspose");

button.setMacroName(sheet.getName() + ".ShowMessage");

const outputFilePath = path.join(dataDir, "Output.out.xlsm");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
