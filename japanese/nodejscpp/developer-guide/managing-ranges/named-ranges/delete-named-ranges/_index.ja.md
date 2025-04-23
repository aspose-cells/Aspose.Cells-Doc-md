---
title: Node.js経由でC++を使用して名前定義範囲を削除
linktitle: 名前付き範囲の削除
type: docs
weight: 90
url: /ja/nodejs-cpp/Delete-named-ranges/
description: Aspose.Cells for Node.js via C++を使用してExcelやOpenOfficeファイルから定義された名前や名前範囲を削除する方法を学べます。
---

## **紹介**
Excelファイルに多くの定義名や名前付き範囲がある場合、参照されないためにいくつかをクリアする必要があります。

## **MS Excelで名前付き範囲を削除する**

Excelから名前付き範囲を削除するには、次の手順に従うことができます：
1. Microsoft Excelを開き、名前付き範囲が含まれているワークブックを開きます。
2. Excelリボンの「数式」タブに移動します。
3. 「定義された名前」グループの「名前マネージャー」ボタンをクリックします。これにより名前マネージャーのダイアログボックスが開きます。
4. 名前マネージャーのダイアログボックスで、削除したい名前付き範囲を選択します。
5. 「削除」ボタンをクリックします。プロンプトが表示されたら削除を確認します。
6. 「閉じる」ボタンをクリックして名前マネージャーのダイアログボックスを閉じます。
7. 変更を保存するためにワークブックを保存します。

## **Aspose.Cells for Node.js via C++を使用して名前範囲を削除する**
Aspose.Cells for Node.js via C++を使用すると、リスト内の[テキスト]や[インデックス]を指定して名前範囲や定義済みの名前を削除できます。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

注意：定義された名前が数式で参照されている場合は削除できません。定義された名前の数式のみ削除可能です。

## **一部の名前付き範囲を削除する**
定義名を削除する際には、ファイル内のすべての数式によって参照されているかどうかを確認する必要があります。
名前範囲の削除パフォーマンスを向上させるために、一緒にいくつか削除することもできます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **重複した定義名を削除する**
定義された名前が重複しているためにExcelファイルが壊れることがあります。これらの重複した名前を削除してファイルを修復できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



