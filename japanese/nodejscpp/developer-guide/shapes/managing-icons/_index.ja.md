---  
title: Node.jsとC++を使用してワークシートにアイコンを追加  
linktitle: アイコンを管理する  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/insert-svg-to-excel/  
---  

## Aspose.Cells for Node.js via C++でワークシートにアイコンを追加する

Excel ファイルに 'アイコン' を追加する必要がある場合は、このドキュメントが役立ちます。[Aspose.Cells](https://products.aspose.com/cells/) を使用して、Excel ファイルにアイコンを追加する方法について説明します。

挿入アイコン操作に対応する Excel インターフェースは次のとおりです。

![](1.png)

- ワークシートに挿入するアイコンの位置を選択します
- *挿入*->*アイコン* を左クリックします
- 開いたウィンドウで、上図の赤い四角内のアイコンを選択します
- 左クリックで*挿入*を選択すると、Excelファイルに挿入されます。

効果は以下のようになります。

![](2.png)

ここでは、[Aspose.Cells](https://products.aspose.com/cells/)を使ったアイコン挿入を支援するための*サンプルコード*を用意しています。また、必要な[サンプルファイル](sample.xlsx)とアイコン[リソースファイル](icon.zip)もあります。Excelのインターフェースを使用して、[リソースファイル](icon.zip)と同じ表示効果のアイコンを[サンプルファイル](sample.xlsx)に挿入しました。

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

プロジェクトで上記のコードを実行すると、次の結果が得られます。

![](3.png)  

