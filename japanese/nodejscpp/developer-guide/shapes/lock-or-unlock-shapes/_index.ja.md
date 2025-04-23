---
title: Node.js経由でシェイプをロックまたはアンロック
linktitle: 形状のロックまたはロック解除
type: docs
weight: 200
url: /ja/nodejs-cpp/lock-or-unlock-shapes/
description: この資料は、Aspose.Cellsライブラリを使用してNode.js経由でシェイプをロックまたはアンロックして保護する方法を示すコード例です。
keywords: Node.jsでシェイプをロックして保護する方法：Node.js経由でシェイプのロックやアンロックを行う方法についての説明。
---

## **可能な使用シナリオ**

場合によっては、特定のワークシート内のすべての形状を保護して、望ましくない状況によって破壊されるのを防ぐ必要があります。その場合は、指定されたワークシート内のすべての形状をロックする必要があります。 

スプレッドシートやドキュメント内の図形をロックすることは、いくつかの理由で有益です：
1. 偶発的な変更を防ぐ：図形をロックすることで、ユーザーによる誤った移動やサイズ変更、削除を防ぎます。特に複雑なドキュメントでは、図形が注釈やイラスト、またはドキュメントのデザインの一部として使われる場合に重要です。
1. レイアウトとデザインの維持：図形はドキュメントのレイアウトやビジュアルデザインにおいて重要な役割を果たします。それらをロックすることで、意図した外観を維持し、ドキュメントの専門性と視覚的魅力を保ちます。
1. データの整合性：スプレッドシートでは、図形を使って重要なデータポイントを強調したり、コメントを追加したり、ビジュアルな説明を提供したりします。これらの図形をロックすることで、提供される文脈情報の正確性と完全性を確保します。
1. 共有ドキュメントの一貫性：複数のユーザーがドキュメントで共同作業する際、それぞれの技術レベルは異なる場合があります。図形をロックすることで、予期しない変更を防ぎ、ドキュメントの一貫性を維持します。
1. セキュリティ：敏感なドキュメントでは、図形をロックすることは情報保護の一環となります。例えば、財務報告書や法的文書において、ロックされた図形は重要な注釈やハイライトを安全に保護するために使われます。

時には、特定の保護されたワークシートで特定の図形を変更できる必要があり、その場合これらの図形のロック解除が必要です。この記事では、指定した図形のロックとロック解除の方法を詳しく紹介します。

## **Excelで図形をロックする方法**

Microsoft Excelでセルをロックする方法は次のとおりです：

1. Excelファイルを開く：ロックしたい図形を含むExcelファイルを開きます。

1. 図形を選択：ロックしたい図形をクリックします。複数の図形を選択するには、Ctrlキーを押しながら各図形をクリックします。

1. 図形の書式設定パネルを開く：選択した図形上で右クリックし、「サイズとプロパティ」を選択します。あるいは、リボンの「書式」タブに移動し、「サイズ」グループのダイアログランチャー（小さな矢印）をクリックして「図形の書式設定」パネルを開きます。
1. 図形をロック： 「図形の書式設定」パネルの「サイズとプロパティ」タブ（四角形と矢印のアイコン）に移動します。「プロパティ」セクションで、「ロック」のチェックボックスをオンにします。
<br>
<img src="1.png" width=60% />
1. シートを保護：リボンの「校閲」タブに移動し、「シートの保護」をクリックします。パスワード（任意）を設定し、許可したい操作（ロックされたセルの選択、セルの書式設定など）を選び、「OK」をクリックします。
<br>
<img src="2.png" width=60% />

## **指定したワークシート内の全ての図形をロックする方法**

指定したワークシートのすべての図形を保護するには、`worksheet.protect(ProtectionType.Objects)`メソッドを使用します。以下のサンプルコードを参照してください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const text = "This is a test";
const worksheet = workbook.getWorksheets().get(0);

let shape = worksheet.getShapes().addTextBox(1, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addRectangle(5, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addButton(9, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addOval(13, 0, 1, 0, 50, 100);
shape.setText(text);

// Protect all shapes in a specified worksheet 
shape.getWorksheet().protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or shape.getWorksheet().protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.

workbook.save("Locked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **保護されたワークシート内の指定した図形のアンロック方法**

保護されたワークシート内の特定の図形のロック解除には、`shape.isLocked`を使用します。以下のサンプルコードをご覧ください。

注意：`shape.isLocked`は、ワークシートが保護されている場合のみ有効です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Locked.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get protected worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the specified shape to be unlocked
const shape = worksheet.getShapes().get("TextBox 1");

// Unlock the specified shape
if (!worksheet.getProtection().getAllowEditingObject() && shape.isLocked()) {
shape.setIsLocked(false);
}

workbook.save("UnLocked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

