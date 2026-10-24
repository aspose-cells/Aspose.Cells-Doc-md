---
title: 保護および保護解除
linktitle: 暗号化と保護
type: docs
weight: 68
url: /ja/net/protect-and-unprotect/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/net/security-features/]
description: このセクションでは、C# コードを使用して Excel ファイルの暗号化と復号化、Excel データの保護を行う方法を紹介します。ファイルの暗号化、読み取り専用保護、ワークブック構造の保護、ワークシートの保護、デジタル署名について解説します
keywords: Aspose.Cells, .NET, 暗号化, 復号化, パスワード, 保護, 保護解除, ワークブック保護, ワークシート保護, 読み取り専用, デジタル署名, C#
---

Excel ワークブックには、不正アクセスから保護する必要のある、機密性の高い財務情報、ビジネス情報、または個人情報が保存されることがよくあります。Aspose.Cells for .NET は、Microsoft Excel の機能に対応する包括的な保護機能セットを提供し、ファイルレベル、ワークブックレベル、ワークシートレベルでデータを保護できます。

{{% alert color="primary" %}}
Aspose.Cells for .NET は、MS Excel と同様に、ファイルレベルからデータレベルまで幅広い保護機能を提供します。これらの機能には、パスワードによるファイルの暗号化、変更用パスワードによる読み取り専用アクセスの強制、ワークブック構造の保護、ワークシートの保護、ワークブックへのデジタル署名が含まれます。
{{% /alert %}}

## Excel ファイルの暗号化と復号化
Excel ファイルに設定されたパスワードは、不正なユーザーがワークブックの内容を開いたり閲覧したりするのを防ぎます。ワークブックを暗号化するには、パスワード文字列を `Workbook.Settings.Password` に割り当ててからワークブックを保存します。Aspose.Cells はファイルを暗号化された形式で書き込みます。復号化のために暗号化されたワークブックを開くには、`LoadOptions` オブジェクトをインスタンス化し、暗号化時に使用されたパスワードと同じものを `LoadOptions.Password` に設定して、`Workbook` コンストラクタに渡します。Aspose.Cells は提供されたパスワードを透過的に適用するため、ファイルが通常のワークブックであるかのように、以降のコードで復号化された内容を操作できます。

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## 読み取り専用保護 (変更用パスワード)
Excel は 2 つの異なるパスワード層をサポートしています。1 つ目はファイル自体を暗号化する「開くためのパスワード」で、これについては前のセクションで説明しました。2 つ目は変更用パスワードで、ワークブックを開くことをブロックするものではありません。代わりに、変更用パスワードが指定されない限り、Excel はファイルを読み取り専用モードで開くことを推奨します。この動作は、Aspose.Cells では `Workbook.Settings.WriteProtection` を通じて設定します。`Password` プロパティに変更用パスワードを設定し、`Author` プロパティに保護を適用したユーザーを識別する情報を設定します。`WriteProtection.ValidatePassword(string)` メソッドを使用して、指定された変更用パスワードが正しいかどうかを確認します。一致する場合は `true` を返し、一致しない場合は `false` を返します。

```csharp
using System;
using Aspose.Cells;
// 新しいワークブックを最初から作成する
Workbook workbook = new Workbook();
// 最初のワークシートのセル A1 にサンプル値を書き込む
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// 書き込み保護を設定する: 変更用のパスワードと作成者を設定する
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// 書き込み保護を永続化するためにワークブックを保存する
workbook.Save("WriteProtectedWorkbook.xlsx");
// 正しいパスワードを使用して変更用のパスワードを検証する
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// 別の分岐を示すために、正しくないパスワードを使用して変更用のパスワードを検証する
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## ワークブック構造の保護と保護解除
ワークブック構造を保護すると、他のユーザーが非表示のワークシートを表示したり、新しいワークシートを追加したり、ワークシートを移動、削除、非表示化、名前変更したりするのを防ぐことができます。保護状態はシート内のセルの内容ではなく、シート構造に適用されます。構造保護を適用するには、`workbook.Protect(ProtectionType.Structure, "password")` を呼び出します。保護を解除するには、正しいパスワードを指定して `workbook.Unprotect("password")` を呼び出します。ここで使用される `ProtectionType.Structure` 列挙値は、`ProtectionType.Windows` などの他の保護タイプとは異なります。

```csharp
using System;
using Aspose.Cells;
// 新しいワークブックを作成
Workbook workbook = new Workbook();
// 2番目のワークシートを追加
workbook.Worksheets.Add();
// 最初のワークシートのセルA1にサンプル値を書き込む
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// ワークブックの構造を保護
workbook.Protect(ProtectionType.Structure, "StructPwd");
// ワークブックをstructure_protected.xlsxとして保存
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// ファイルを新しいWorkbookインスタンスに再読み込み
Workbook loadedWorkbook = new Workbook(filePath);
// 構造保護を解除
loadedWorkbook.Unprotect("StructPwd");
// 確認メッセージを出力
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## ワークシートの保護と保護解除
ワークシートの保護は、ワークシートのセルを偶発的または意図的な変更からロックします。ユーザーはパスワードを指定しないとロックされたセルを編集できません。これは、共有スプレッドシートで数式、ヘッダー、指定されたデータ入力領域を保護するために一般的に使用される保護です。ワークシートを保護するには、`worksheet.Protect(ProtectionType.All, "password")` を呼び出します。`ProtectionType.All` を使用すると、ロックされたセルの選択、セルの書式設定、行と列の挿入、行と列の削除など、利用可能なすべての保護オプションが有効になります。保護を解除するには、正しいパスワードを指定して `worksheet.Unprotect("password")` を呼び出します。`Contents`、`Objects`、`Scenarios` などの他の保護タイプをビット単位の OR で組み合わせることで、より細かい制御が可能です。

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## デジタル署名の追加と検証
デジタル署名は、ワークブックの内容が本物であり、署名されてから変更されていないことを受信者に保証します。Aspose.Cells は `Aspose.Cells.DigitalSignatures` 名前空間を通じてデジタル署名サポートを提供します。典型的なワークフローは、`System.Security.Cryptography.X509Certificates.X509Certificate2` を介して `.pfx` 証明書ファイルを読み込み、`Aspose.Cells.DigitalSignatures.DigitalSignature` でラップし、署名を `DigitalSignatureCollection` に追加して、`Workbook.AddDigitalSignature(DigitalSignatureCollection)` を通じてコレクションをワークブックに適用します。`DigitalSignature.Comments` プロパティには、署名時刻や目的など、署名のコンテキストを記録できます。署名後にワークブックに加えられた変更はすべて署名を無効化するため、受信側で検証ステップを行うことで改ざんを検出できます。

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## 関連記事
- [Excel ファイルの暗号化と復号化](/cells/ja/net/encrypt-and-decrypt-excel-files/)
- [ワークブック構造の保護と保護解除](/cells/ja/net/protect-and-unprotect-workbook-structure/)
- [ワークシートの保護と保護解除](/cells/ja/net/protect-and-unprotect-worksheets/)
- [共有ワークブックのパスワード保護または保護解除](/cells/ja/net/password-protect-or-unprotect-the-shared-workbook/)
- [デジタル署名の割り当てと検証](/cells/ja/net/assign-and-validate-digital-signatures/)
- [Aspose.Cells を使用して変更用パスワードを確認する](/cells/ja/net/check-password-to-modify-using-aspose-cells/)
- [暗号化された Office Open XML (OOXML) ファイルのファイル形式を検出する](/cells/ja/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel ファイルの暗号化](/cells/ja/net/encrypting-excel-files/)
- [ファイル形式を検出する方法とファイルが暗号化されているかどうかを確認する方法](/cells/ja/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}