---
title: 保護および保護解除
linktitle: 暗号化と保護
description: このセクションでは、Excelファイルの暗号化と復号化、Excelデータの保護方法を紹介します。ファイルの暗号化、読み取り専用保護、ワークブック構造の保護、ワークシートの保護、JavaScriptコードを使用したデジタル署名について説明します。
keywords: Aspose.Cells, Node.js via Java, 暗号化, 復号化, パスワード, 保護, 保護解除, ワークブック保護, ワークシート保護, 読み取り専用, デジタル署名, JavaScript
type: docs
weight: 68
url: /ja/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel ワークブックには、機密性の高い財務情報、ビジネス情報、個人情報が保存されることが多く、不正アクセスから守る必要があります。Aspose.Cells for Node.js via Java は、Microsoft Excel の機能を反映した包括的な保護機能セットを提供しており、ファイルレベル、ワークブックレベル、ワークシートレベルでデータを保護できます。

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java は、ファイルレベルからデータレベルまで、MS Excel と同様の幅広い保護機能を提供します。これらの機能には、パスワードによるファイルの暗号化、変更用パスワードによる読み取り専用アクセスの強制、ワークブック構造の保護、ワークシートの保護、ワークブックへのデジタル署名が含まれます。
{{% /alert %}}

## Excel ファイルの暗号化と復号化
Excel ファイルに設定されたパスワードは、許可されていないユーザーがワークブックの内容を開いたり閲覧したりすることを防ぎます。ワークブックを暗号化するには、`workbook.getSettings().setPassword(...)` にパスワード文字列を設定し、ワークブックを保存します。Aspose.Cells はファイルを暗号化された形式で書き込みます。暗号化されたワークブックを復号化のために開くには、`LoadOptions` オブジェクトをインスタンス化し、`loadOptions.setPassword(...)` に暗号化時に使用したものと同じパスワードを設定して、`Workbook` コンストラクタに渡します。Aspose.Cells は提供されたパスワードを透過的に適用するため、ファイルが通常のワークブックであるかのように、復号化されたコンテンツに対してコードの残りの部分を操作できます。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## 読み取り専用保護（変更用パスワード）
Excel は 2 つの異なるパスワード層をサポートしています。1 つ目はファイル自体を暗号化する「開くためのパスワード」で、前述のセクションで説明されています。2 つ目は「変更用パスワード」で、ワークブックを開くことをブロックするものではありません。代わりに、変更用パスワードが指定されない限り、Excel はファイルを読み取り専用モードで開くことを推奨します。この動作は Aspose.Cells では `workbook.getSettings().getWriteProtection()` を通じて設定します。`Password` プロパティに変更用パスワードを設定し、`Author` プロパティに保護を適用したユーザーを識別するための情報を設定します。`writeProtection.validatePassword(string)` メソッドを使用して、指定された変更用パスワードが正しいかどうかを確認します。一致する場合は `true` を返し、一致しない場合は `false` を返します。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// 最初のワークシートのセルA1にサンプル値を書き込む
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// 書き込み保護を構成：変更用パスワードと作成者を設定する
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// 書き込み保護を保持するためにワークブックを保存する
workbook.save("WriteProtectedWorkbook.xlsx");
// 正しいパスワードを使用して変更用パスワードを検証する
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// 誤ったパスワードを使用して変更用パスワードを検証し、もう一方の分岐を示す
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## ワークブック構造の保護と保護解除
ワークブック構造を保護すると、他のユーザーが非表示のワークシートを表示したり、新しいワークシートを追加したり、ワークシートを移動、削除、非表示化、名前変更したりすることができなくなります。保護状態はシート内のセル内容ではなくシート構造に適用されます。構造保護を適用するには、`workbook.protect(ProtectionType.Structure, "password")` を呼び出します。保護を解除するには、`workbook.unprotect("password")` を呼び出し、正しいパスワードを指定します。ここで使用される `ProtectionType.Structure` 列挙値は、`ProtectionType.Windows` などの他の保護タイプとは区別されます。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// 2番目のワークシートを追加
workbook.getWorksheets().add();
// 最初のワークシートのセルA1にサンプル値を書き込む
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// ワークブックの構造を保護する
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// ワークブックをstructure_protected.xlsxとして保存
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// 新しいWorkbookインスタンスにファイルを再読み込み
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// 構造保護を解除する
loadedWorkbook.unprotect("StructPwd");
// 確認メッセージを表示
console.log("Structure protection has been successfully removed from the workbook.");
```

## ワークシートの保護と保護解除
ワークシートの保護は、偶発的または故意の変更からワークシートのセルをロックします。ユーザーはパスワードを指定しないとロックされたセルを編集できません。これは、共有スプレッドシートで数式、ヘッダー、指定されたデータ入力領域を保護するために一般的に使用されます。ワークシートを保護するには、`worksheet.protect(ProtectionType.All, "password")` を呼び出します。`ProtectionType.All` を使用すると、ロックされたセルの選択、セルの書式設定、行と列の挿入、行と列の削除など、利用可能なすべての保護オプションが有効になります。保護を解除するには、正しいパスワードを指定して `worksheet.unprotect("password")` を呼び出します。`Contents`、`Objects`、`Scenarios` などの他の保護タイプをビット単位の OR で組み合わせることで、より細かい制御が可能になります。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## デジタル署名の追加と検証
デジタル署名は、ワークブックの内容が本物であり、署名されてから変更されていないことを受信者に保証します。Aspose.Cells は `AsposeCells.DigitalSignature` や `AsposeCells.DigitalSignatureCollection` などのクラスを通じてデジタル署名をサポートしています。典型的な流れでは、`.pfx` 証明書ファイルとそのパスワード、署名コメントから直接 `AsposeCells.DigitalSignature` を作成し、`DigitalSignatureCollection` に追加して、`workbook.addDigitalSignature(DigitalSignatureCollection)` でワークブックに適用します。`DigitalSignature.Comments` プロパティには、署名時刻や目的などの署名コンテキストを記録できます。署名後にワークブックに変更が加えられると署名が無効になるため、受信側で検証手順を行うことで改ざんを検出できます。

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}