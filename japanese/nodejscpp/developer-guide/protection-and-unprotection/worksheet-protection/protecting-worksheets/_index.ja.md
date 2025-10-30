---
title: Node.jsとC++を使ったワークシート保護
linktitle: ワークシートの保護
type: docs
weight: 10
url: /ja/nodejs-cpp/protecting-worksheets/
description: Aspose.Cells for Node.js via C++を使ったExcelのワークシートの保護方法について、行、列、特定のセルの保護も含めて学習します。
---


{{% alert color="primary" %}}

ワークシートが保護された場合、ユーザーが行えない操作が制限されます。例えば、データ入力、行や列の挿入・削除などです。

{{% /alert %}}

## **ワークシートを保護**

### **紹介**

Microsoft Excelの一般的な保護オプション:

- コンテンツ
- オブジェクト
- シナリオ

保護されたワークシートは機密データを非表示または保護しないため、ファイルの暗号化とは異なります。一般的に、ワークシートの保護はプレゼンテーション目的に適しています。ユーザーはワークシート内のデータ、コンテンツ、および書式設定を変更できなくなります。

### **ワークシートを保護する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表されます。

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートに保護を適用するための[**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)メソッドを提供します。[**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)メソッドは、次のパラメータを受け取ります：

- 保護の種類、ワークシートに適用する保護の種類。保護の種類はProtectionType列挙型のヘルプを使用して適用されます。
- 新しいパスワード、ワークシートを保護するために使用する新しいパスワード。
- 古いパスワード、ワークシートがすでにパスワードで保護されている場合は、古いパスワードを渡します。ワークシートがすでに保護されていない場合は、nullを渡します。

[**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype)列挙型は、次の事前定義された保護タイプを含みます：

|**保護タイプ**|**説明**|
| :- | :- |
|All|このワークシート上で何も変更できない|
|Contents|このワークシートにデータを入力できない|
|Objects|描画オブジェクトを変更できない|
|Scenarios|保存されたシナリオを変更できない|
|Structure|ユーザーは構造を変更できません|
|Windows|保護はウィンドウに適用されています|
|None|保護は適用されていません|

以下の例は、ワークシートにパスワードを設定して保護する方法を示しています。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

上記のコードを使用してワークシートを保護した後、ワークシートの保護を開いて確認することができます。ファイルを開いてワークシートにデータを追加しようとすると、次のダイアログが表示されます:

|**ユーザーがワークシートを変更できないと警告するダイアログ**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

ワークシートで作業するには、**ツール**メニューの**保護**から**ワークシートの保護を解除**を選択します。

ワークシートの保護を解除メニュー項目を選択すると、次のようなダイアログが開きます。パスワードを入力するように求められます。

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excelを使用してワークシート内の一部のセルを保護する**

特定のシナリオでは、ワークシート内の一部のセルだけをロックする必要がある場合があります。特定のセルだけをロックしたい場合は、他のすべてのセルのロックを解除する必要があります。ワークシート内のすべてのセルは既にロック状態に初期設定されています。これは、MS Excelで任意のExcelファイルを開き、**書式 | セル**をクリックして**セルの書式設定**ダイアログボックスを表示し、次に**保護**タブをクリックして「ロック済み」のチェックボックスがデフォルトでONになっていることを確認できます。

以下のポイントは、MS Excelを使ってセルのロックを行う方法を示しています。この方法はMicrosoft Office Excel 97、2000、2002、2003やそれ以降のバージョンに適用されます。

1. **全選択**ボタン(行1の行番号の直上および列文字Aの左直上の灰色の四角形)をクリックしてワークシート全体を選択します。
2. **書式**メニューから**セル**をクリックし、**保護**タブを選択して、**ロック**のチェックを外す。
   これにより、ワークシート上のすべてのセルのロックが解除されます。
   **セル**コマンドが利用できない場合、ワークシートの一部は既にロックされている可能性があります。 **ツール**メニューで、**保護**を指して、**ワークシートの保護を解除**をクリックします。
3. ロックしたいセルだけを選択し、ステップ2を繰り返しますが、その際は**ロック**のチェックを入れます。
4. **ツール**メニューから**保護**にマウスを合わせて**シートの保護**をクリックし、その後**OK**をクリックします。
5. **シートの保護**ダイアログボックスで、パスワードを指定したり、ユーザーに変更させたい要素を選択できます。

### **Aspose.Cellsを使ったワークシートの一部セルの保護**

この方法では、Aspose.Cells APIのみを使用してタスクを実行します。

例：以下は、ワークシートの一部セルを保護する方法の例です。最初にすべてのセルのロックを解除し、その後、セル（A1、B1、C1）をロックします。最後に、ワークシートを保護します。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトには、ブール型の[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)が含まれています。[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)プロパティをtrueまたはfalseに設定し、*Column/Row.applyStyle()*メソッドを適用して行または列のロック状態を制御できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **ワークシート内の行を保護する**

Aspose.Cellsを使えば、任意の行を簡単にロックできます。ここでは、[**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row)クラスの[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)メソッドを使用して、特定の行に[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)を適用します。このメソッドは二つの引数を取ります：[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトと、適用されるフォーマットに関するすべてのメンバーを持つ[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)オブジェクト。

以下の例は、ワークシートの行を保護する方法を示しています。最初にすべてのセルのロックを解除し、その後最初の行だけをロックします。最後に、ワークシートを保護します。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトには、ブール型の[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)があります。[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)プロパティをtrueまたはfalseに設定して、行または列のロックを制御します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **ワークシート内の列を保護する**

Aspose.Cellsを使えば、任意の列を簡単にロックできます。ここでは、[**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column)クラスの[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-)メソッドを使用して、特定の列に[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)を適用します。このメソッドは二つの引数を取ります：[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトと、適用されるフォーマットに関するすべてのメンバーを持つ[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)オブジェクト。

以下の例は、ワークシートの列を保護する方法を示しています。最初にすべてのセルのロックを解除し、その後最初の列だけをロックします。最後に、ワークシートを保護します。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトには、ブール型の[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)があります。[**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)プロパティをtrueまたはfalseに設定して、行または列のロックを制御します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **ユーザーに範囲の編集を許可する**

次の例は、保護されたワークシートで範囲の編集を許可する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
