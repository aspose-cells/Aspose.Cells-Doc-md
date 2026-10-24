---
title: 保護および保護解除
linktitle: 暗号化と保護
description: このセクションでは、Python コードを使用して Excel ファイルの暗号化と復号化、Excel データの保護方法を紹介します。ファイルの暗号化、読み取り専用保護、ワークブック構造の保護、ワークシートの保護、デジタル署名について解説します
keywords: Aspose.Cells, Python via .NET, 暗号化, 復号化, パスワード, 保護, 保護解除, ワークブック保護, ワークシート保護, 読み取り専用, デジタル署名, Python
type: docs
weight: 68
url: /ja/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel ワークブックには、不正アクセスから守るべき機密性の高い財務情報、ビジネス情報、または個人情報が保存されることがよくあります。Aspose.Cells for Python via .NET は、Microsoft Excel の機能に対応する包括的な保護機能セットを提供し、ファイルレベル、ワークブックレベル、ワークシートレベルでデータを保護できます。

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET は、MS Excel と同様に、ファイルレベルからデータレベルまで幅広い保護機能を提供します。これらの機能には、パスワードによるファイルの暗号化、変更用パスワードによる読み取り専用アクセスの強制、ワークブック構造の保護、ワークシートの保護、ワークブックへのデジタル署名が含まれます。
{{% /alert %}}

## Excel ファイルの暗号化と復号化
Excel ファイルに設定されたパスワードは、不正ユーザーがワークブックの内容を開いたり閲覧したりすることを防ぎます。ワークブックを暗号化するには、`workbook.settings.password` にパスワード文字列を設定し、ワークブックを保存します。Aspose.Cells はファイルを暗号化された形式で書き込みます。復号化のために暗号化されたワークブックを開くには、`LoadOptions` オブジェクトをインスタンス化し、`load_options.password` に暗号化時に使用されたのと同じパスワードを設定して、それを `Workbook` コンストラクタに渡します。Aspose.Cells は提供されたパスワードを透過的に適用するため、以降のコードはファイルが通常のワークブックであるかのように、復号化された内容を操作できます。

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## 読み取り専用保護（変更用パスワード）
Excel は 2 つの異なるパスワード層をサポートしています。1 つ目はファイル自体を暗号化する「開くためのパスワード」で、前述のセクションで説明されています。2 つ目は「変更用パスワード」で、ワークブックを開くこと自体は制限しませんが、変更用パスワードが指定されない限り Excel はファイルを読み取り専用モードで開くことを推奨します。この動作は Aspose.Cells で `workbook.settings.write_protection` を通じて設定します。`password` プロパティに変更用パスワードを、`author` プロパティに保護を適用したユーザーを識別する情報を設定します。`write_protection.validate_password(string)` メソッドを使用して、指定された変更用パスワードが正しいかどうかを確認できます。一致する場合は `true`、それ以外の場合は `false` を返します。

```python
import aspose.cells as ac
# ゼロから新しいワークブックを作成する
workbook = ac.Workbook()
# 最初のワークシートのセル A1 にサンプル値を書き込む
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# 書き込み保護を構成する：変更用パスワードと作成者を設定する
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# 書き込み保護が永続化されるようにワークブックを保存する
workbook.save("WriteProtectedWorkbook.xlsx")
# 正しいパスワードを使用して変更用パスワードを検証する
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# 別の分岐を示すために、誤ったパスワードを使用して変更用パスワードを検証する
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## ワークブック構造の保護と保護解除
ワークブック構造を保護すると、他のユーザーが非表示のワークシートを表示したり、新しいワークシートを追加したり、ワークシートを移動、削除、非表示化、名前変更したりする操作を防止できます。保護対象はシートの構造であり、シート内のセル内容ではありません。構造保護を適用するには、`workbook.protect(ProtectionType.STRUCTURE, "password")` を呼び出します。保護を解除するには、`workbook.unprotect("password")` を呼び出し、正しいパスワードを指定します。ここで使用される `ProtectionType.STRUCTURE` 列挙値は、`ProtectionType.WINDOWS` などの他の保護タイプとは異なります。

```python
import aspose.cells as ac
# 新しいワークブックを作成
workbook = ac.Workbook()
# 2番目のワークシートを追加
workbook.worksheets.add()
# 最初のワークシートのセルA1にサンプル値を書き込む
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# ワークブックの構造を保護
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# ワークブックをstructure_protected.xlsxとして保存
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# ファイルを新しいWorkbookインスタンスに再読み込み
loaded_workbook = ac.Workbook(file_path)
# 構造保護を解除
loaded_workbook.unprotect("StructPwd")
# 確認メッセージを出力
print("Structure protection has been successfully removed from the workbook.")
```

## ワークシートの保護と保護解除
ワークシートの保護は、ワークシートのセルを偶発的または意図的な変更からロックします。ユーザーはパスワードを入力しないとロックされたセルを編集できません。これは、共有スプレッドシートで数式、ヘッダー、指定されたデータ入力領域を保護するために一般的に使用される保護です。ワークシートを保護するには、`worksheet.protect(ProtectionType.ALL, "password")` を呼び出します。`ProtectionType.ALL` を使用すると、ロックされたセルの選択、セルの書式設定、行と列の挿入、行と列の削除など、利用可能なすべての保護オプションが有効になります。保護を解除するには、正しいパスワードを指定して `worksheet.unprotect("password")` を呼び出します。ビットごとの OR 演算子を使用して、`Contents`、`Objects`、`Scenarios` などの他の保護タイプを組み合わせることで、より細かい制御が可能です。

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## デジタル署名の追加と検証
デジタル署名は、ワークブックの内容が本物であり、署名後に変更されていないことを受信者に保証します。Aspose.Cells は `aspose.cells.digital_signatures` 名前空間を通じてデジタル署名機能を提供します。典型的なワークフローは、`System.Security.Cryptography.X509Certificates.X509Certificate2` を通じて `.pfx` 証明書ファイルを読み込み、`aspose.cells.digital_signatures.DigitalSignature` でラップし、署名を `DigitalSignatureCollection` に追加して、`workbook.add_digital_signature(DigitalSignatureCollection)` を通じてそのコレクションをワークブックに適用します。`digital_signature.comments` プロパティには、署名時刻や目的などの署名コンテキストを記録できます。署名後にワークブックに加えた変更はすべて署名を無効化するため、受信側で検証手順を実行することで改ざんを検出できます。

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## 関連記事
- [Excel ファイルの暗号化と復号化](/cells/ja/python-net/encrypt-and-decrypt-excel-files/)
- [ワークブック構造の保護と保護解除](/cells/ja/python-net/protect-and-unprotect-workbook-structure/)
- [ワークシートの保護と保護解除](/cells/ja/python-net/protect-and-unprotect-worksheets/)
- [共有ワークブックのパスワード保護または保護解除](/cells/ja/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [デジタル署名の割り当てと検証](/cells/ja/python-net/assign-and-validate-digital-signatures/)
- [Aspose.Cells を使用した変更用パスワードの確認](/cells/ja/python-net/check-password-to-modify-using-aspose-cells/)
- [暗号化された Office Open XML - OOXML ファイルのファイル形式を検出](/cells/ja/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel ファイルの暗号化](/cells/ja/python-net/encrypting-excel-files/)
- [ファイル形式を検出する方法とファイルが暗号化されているかどうかを確認する方法](/cells/ja/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}