---
title: Node.js経由C++を使用した共有数式の設定
linktitle: 共有式数式の設定
type: docs
weight: 10
url: /ja/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

 この記事は、数式を計算させるシートに関数を追加したい場合の方法をAspose.Cells for Node.js via C++を用いて解説します。

{{% /alert %}}

## Aspose.Cells for Node.js via C++を使用した共有数式の設定

次のサンプルワークシートのようなデータで満たされたワークシートがあるとします。

|**入力ファイル（1列のデータ）**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

B2に関数を追加し、最初のデータ行の売上税を計算したいとします。税金は9%です。売上税を計算する式は次のとおりです:"=A2*0.09"。この記事では、Aspose.Cellsでこの式を適用する方法について説明します。

Aspose.Cellsを使用すると、[**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) プロパティを使用して式を指定できます。その他のセル（B3、B4、B5など）に式を追加するためには、2つのオプションがあります。

最初のセルのように操作し、各セルに対して数式を設定し、セル参照を更新します（A3*0.09、A4*0.09、A5*0.09など）。これには各行のセル参照を更新する必要があります。また、Aspose.Cellsは各数式を個別に解析しなければならず、大きなスプレッドシートや複雑な数式の場合は時間がかかることがあります。さらに、ループで多少簡略化できますが、追加のコード行が必要です。

もう1つの方法は、**共有式**を使用することです。共有式を使用すると、式は各行のセル参照に自動的に更新されるため、税金が正しく計算されます。[**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) メソッドは、最初の方法よりも効率的です。

次の例では、その使用方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
