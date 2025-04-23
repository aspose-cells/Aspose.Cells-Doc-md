---
title: Node.jsとC++を用いた行または列の固定解除
linktitle: ペインの固定解除
type: docs
weight: 190
url: /ja/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: このこの記事では、Node.js APIとC++を使用して、Excelワークシートの行、列、ペインをプログラム的にアンフリーズ（固定解除）する方法を学びます。
keywords: ペインのアンフリーズ、行のアンフリーズ、列のアンフリーズ、C++経由のNode.jsによるウィンドウのアンフリーズ。
---

## **紹介**

この記事では、行、列、ペインのアンフリーズ方法を学びます。Excelファイルのシートが固定されている場合、シートをアンフリーズしたり、固定された行や列、ペインを調整したりしたいことがあります。


## **Excelで**

1. 表示タブ > 固定ウィンドウ > 固定ウィンドウの解除 をクリックします。

**![Excel でのペインの固定解除](Unfreeze-Panes.png)**




## **Aspose.Cells for Node.js via C++を使用して行、列、またはペインをアンフリーズ。**
Aspose.Cells for Node.js via C++を使えば簡単にペインの固定解除ができます。[**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--)メソッドを使用してペインの固定解除を行ってください。

1. 凍結したファイルを開くためにワークブックを作成します。
Worksheet.unfreezePanes()メソッドを使ったペインのアンフリーズ。
3. ファイルを保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

添付 [サンプルソースの Excel ファイル](Frozen.xlsx) です。
