---
title: Node.jsを使ったC++経由での保護と解除
linktitle: 暗号化と保護
description: このセクションでは、Excel ファイルの暗号化と復号、および Excel データの保護について説明します。取り上げるトピックは、ファイル暗号化、読み取り専用保護、ワークブック構造の保護、ワークシートの保護、JavaScript コードによるデジタル署名です。
keywords: Aspose.Cells, Node.js, C++, 暗号化, 復号化, パスワード, 保護, 保護解除, ワークブック保護, ワークシート保護, 読み取り専用, デジタル署名, JavaScript
type: docs
weight: 68
url: /ja/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel ワークブックには、権限のないアクセスから保護する必要がある、機密性の高い財務情報、業務情報、個人情報が保存されることがよくあります。Aspose.Cells for Node.js via C++ は、Microsoft Excel の機能に対応する包括的な保護機能を提供し、ファイルレベル、ワークブックレベル、ワークシートレベルでデータを保護できます。

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ は、MS Excel と同様、ファイルレベルからデータレベルにわたる幅広い保護機能を提供します。これには、パスワードによるファイルの暗号化、変更用パスワードを要求して読み取り専用アクセスを適用すること、ワークブック構造の保護、ワークシートの保護、ワークブックへのデジタル署名の追加が含まれます。
{{% /alert %}}

## Excel ファイルの暗号化と復号化
Excel ファイルにパスワードを設定すると、権限のないユーザーがワークブックを開いたり、その内容を表示したりすることを防止できます。ワークブックを暗号化するには、`workbook.getSettings().setPassword()` にパスワード文字列を設定し、ワークブックを保存します。Aspose.Cells は暗号化された形式でファイルを書き込みます。暗号化されたワークブックを開いて復号化するには、`LoadOptions` オブジェクトをインスタンス化し、`loadOptions.setPassword()` を暗号化時に使用したのと同じパスワードに設定してから、`Workbook` コンストラクターに渡します。Aspose.Cells は指定されたパスワードを透過的に適用するため、残りのコードでは、ファイルが通常のワークブックであるかのように、復号化された内容を操作できます。

```javascript
const AsposeCells = require("aspose.cells.node");
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
Excel は 2 つの異なるパスワード層に対応しています。1 つ目は「開くためのパスワード」で、ファイル自体を暗号化し、前のセクションで説明しました。2 つ目は変更用パスワードで、ワークブックを開くことを阻止するものではありません。変更用パスワードが指定されない限り、Excel はファイルを読み取り専用モードで開くよう推奨します。この動作は Aspose.Cells では `workbook.getSettings().getWriteProtection()` を使用して構成します。その `password` プロパティに変更用パスワードを設定し、`author` プロパティに保護を適用した人物を指定します。指定された変更用パスワードが正しいかどうかを確認するには、`writeProtection.validatePassword(string)` メソッドを使用します。一致する場合は `true`、それ以外の場合は `false` を返します。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// 最初のワークシートのセルA1にサンプル値を書き込む
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// 書き込み保護を設定する：変更用のパスワードと作成者を設定する
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// 書き込み保護を永続化するためにブックを保存する
workbook.save("WriteProtectedWorkbook.xlsx");
// 正しいパスワードを使用して変更用パスワードを検証する
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// もう一方の分岐を示すために、誤ったパスワードを使用して変更用パスワードを検証する
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## ワークブック構造の保護と保護解除
ワークブック構造を保護すると、他のユーザーが非表示のワークシートを表示したり、新しいワークシートを追加したり、ワークシートを移動、削除、非表示にしたり、名前を変更したりできなくなります。保護される状態は、どのシート内のセル内容ではなく、シートの構造に適用されます。構造保護を適用するには、`workbook.protect(ProtectionType.Structure, "password")` を呼び出します。保護を解除するには、`workbook.unprotect("password")` を呼び出して正しいパスワードを指定します。ここでは `ProtectionType.Structure` の列挙値が使用されており、これは `ProtectionType.Windows` などの他の保護タイプとは区別されます。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// 2番目のワークシートを追加
workbook.getWorksheets().add();
// 最初のワークシートのセルA1にサンプル値を書き込む
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// ワークブックの構造を保護する
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// ワークブックをstructure_protected.xlsxとして保存する
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// ファイルを新しいWorkbookインスタンスに再読み込みする
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// 構造保護を解除する
loadedWorkbook.unprotect("StructPwd");
// 確認メッセージを出力する
console.log("Structure protection has been successfully removed from the workbook.");
```

## ワークシートの保護と保護解除
ワークシート保護は、ワークシートのセルを偶発的な変更や意図的な変更からロックします。ユーザーはパスワードを指定しない限り、ロックされたセルを編集できません。これは、共有スプレッドシートの数式、ヘッダー、または指定されたデータ入力領域を保護するために通常使用される保護方法です。ワークシートを保護するには、`worksheet.protect(ProtectionType.All, "password")` を呼び出します。`ProtectionType.All` を使用すると、ロックされたセルの選択、セルの書式設定、行と列の挿入、行と列の削除など、利用可能なすべての保護オプションが有効になります。保護を解除するには、正しいパスワードを指定して `worksheet.unprotect("password")` を呼び出します。`Contents`、`Objects`、`Scenarios` などの他の保護タイプをビット単位の OR 演算で組み合わせると、より細かい制御が可能です。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## デジタル署名の追加と検証
デジタル署名により、受信者は、ワークブックの内容が真正であり、署名されてから変更されていないことを確認できます。Aspose.Cells は `Aspose.Cells.DigitalSignatures` 名前空間を介してデジタル署名機能を提供します。一般的なワークフローでは、Node.js の crypto ユーティリティを使用して `.pfx` 証明書ファイルを読み込み、`Aspose.Cells.DigitalSignatures.DigitalSignature` でラップして、署名を `DigitalSignatureCollection` に追加し、`workbook.addDigitalSignature(digitalSignatureCollection)` を使用してコレクションをワークブックに適用します。`digitalSignature.comments` プロパティには、署名日時や目的など、署名に関するコンテキストを記録できます。署名後にワークブックに変更を加えると、署名は無効になります。そのため、受信側での検証ステップで改ざんを検出できます。

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## 関連記事
- [Excel ファイルの暗号化と復号化](/cells/ja/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [ワークブック構造の保護と保護解除](/cells/ja/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [ワークシートの保護と保護解除](/cells/ja/nodejs-cpp/protect-and-unprotect-worksheets/)
- [共有ワークブックのパスワード保護または保護解除](/cells/ja/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [デジタル署名の割り当てと検証](/cells/ja/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Aspose.Cells を使用して変更用パスワードを確認する](/cells/ja/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [暗号化された Office Open XML - OOXML ファイルのファイル形式を検出する](/cells/ja/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel ファイルの暗号化](/cells/ja/nodejs-cpp/encrypting-excel-files/)
- [ファイル形式を検出し、ファイルが暗号化されているかを確認する](/cells/ja/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}