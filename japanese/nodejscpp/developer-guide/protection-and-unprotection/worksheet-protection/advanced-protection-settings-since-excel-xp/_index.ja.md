---
title: Excel XP以降の高度な保護設定をNode.jsをC++経由で利用可能
linktitle: Excel XP以降の高度な保護設定
type: docs
weight: 30
url: /ja/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

Excel 2002またはXPのリリース以降、Microsoftは多くの高度な保護設定を追加しました。

{{% /alert %}}


## **紹介**

これらの保護設定により、ユーザーは次の操作を制限または許可できます：

- 行または列の削除。
- 内容、オブジェクト、またはシナリオの編集。
- セル、行、または列の書式設定。
- 行、列、またはハイパーリンクの挿入。
- ロックされたセルまたはロックされていないセルの選択。
- ピボットテーブルなどの使用。

Aspose.Cells for Node.js via C++はExcel XP以降のすべての高度な保護設定をサポートします。

### **Excel XPおよびそれ以降のバージョンを使用した高度な保護設定**

Excel XPで利用可能な保護設定を表示するには：

1. **ツール**メニューから、**保護**の後に**シートを保護**を選択します。ダイアログが表示されます。

Excel 2016で利用可能な保護設定を見るには：

1. **ファイル**メニューから、**ワークブックを保護**, その後**現在のシートを保護**を選択します。
1. **レビュー**メニューで**シートを保護**を選択します。

上記の手順に従うと、ダイアログが表示され、シートの機能の許可または制限やシートにパスワードを設定できます。

### **Aspose.Cells for Node.js via C++を使用した高度な保護設定**

Aspose.Cells for Node.js via C++はすべての高度な保護設定をサポートします。

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスによって表されます。

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスは、これらの高度な保護設定を適用するために使用される [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) プロパティを提供します。[**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) プロパティは実際には、いくつかの制限を無効または有効にするためのいくつかのブーリアンプロパティをカプセル化した [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) クラスのオブジェクトです。

以下は小さなサンプルアプリケーションです。それはExcelファイルを開いて、Excel XPおよびそれ以降のバージョンでサポートされる高度な保護設定のほとんどを使用します。

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)メソッドを使用しないでください。また、[**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--)プロパティを使用してファイルをExcel97-2003またはXlsx形式で保存してください。高度な保護設定はExcel XP以降のみ対応です。

{{% /alert %}}

### **セルロックの問題**

セルの編集を制限したい場合は、保護設定を適用する前にセルをロックする必要があります。そうしないと、シートが保護されていてもセルは編集可能です。Microsoft Excel XPでセルをロックするには次のダイアログを使用します：

|**Excel XPでセルをロックするダイアログ**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells APIを使ってセルをロックすることも可能です。各セルには、Boolean型の[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)書式設定と[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)プロパティがあります。[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)プロパティを**true**または**false**に設定して、セルをロックまたはアンロックします。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
