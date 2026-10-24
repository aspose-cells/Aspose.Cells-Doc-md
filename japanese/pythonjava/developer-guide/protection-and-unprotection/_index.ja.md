---
title: 保護および保護解除
linktitle: 保護
description: このセクションでは、Excelファイルの暗号化と復号化、Excelデータの保護方法について紹介します。ファイルの暗号化、読み取り専用保護、ワークブック構造の保護、ワークシートの保護、Pythonコードを使用したデジタル署名について説明します
keywords: Aspose.Cells, Python via Java, 暗号化, 復号化, パスワード, 保護, 保護解除, ワークブック保護, ワークシート保護, 読み取り専用, デジタル署名, Python
type: docs
weight: 68
url: /ja/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel ワークブックには、不正アクセスから守る必要のある、機密性の高い財務情報、ビジネス情報、個人情報がしばしば保存されます。Aspose.Cells for Python via Java は、Microsoft Excel の機能を反映した包括的な保護機能セットを提供し、ファイルレベル、ワークブックレベル、ワークシートレベルでデータを保護できます。

{{% alert color="primary" %}}
Aspose.Cells for Python via Java は、MS Excel と同様に、ファイルレベルからデータレベルまで幅広い保護機能を提供します。これらの機能には、パスワードによるファイルの暗号化、変更用パスワードによる読み取り専用アクセスの強制、ワークブック構造の保護、ワークシートの保護、ワークブックへのデジタル署名が含まれます。
{{% /alert %}}

## Excel ファイルの暗号化と復号化
Excel ファイルに設定されたパスワードは、許可されていないユーザーがワークブックの内容を開いたり閲覧したりするのを防ぎます。ワークブックを暗号化するには、`workbook.getSettings().setPassword(...)` にパスワード文字列を設定し、ワークブックを保存します。Aspose.Cells はファイルを暗号化された形式で書き込みます。復号化のために暗号化されたワークブックを開くには、`LoadOptions` オブジェクトをインスタンス化し、暗号化時に使用されたのと同じパスワードを `load_options.setPassword(...)` で設定して、それを `Workbook` コンストラクタに渡します。Aspose.Cells は指定されたパスワードを透過的に適用するため、以降のコードはファイルが通常のワークブックであるかのように復号化された内容を操作できます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## 読み取り専用保護（変更用パスワード）
Excel は 2 つの異なるパスワード層をサポートします。1 つ目はファイル自体を暗号化する「開くためのパスワード」で、前のセクションで説明しました。2 つ目は「変更用パスワード」で、ユーザーがワークブックを開くことを妨げるものではなく、変更用パスワードが指定されない限り Excel はファイルを読み取り専用モードで開くことを推奨します。この動作は Aspose.Cells では `workbook.getSettings().getWriteProtection()` を通じて設定します。`setPassword(...)` で変更用パスワードを設定し、`setAuthor(...)` で保護を適用した人を識別するために作成者を設定します。指定された変更用パスワードが正しいかどうかを確認するには `writeProtection.validatePassword(String)` メソッドを使用します。一致する場合は `true` を返し、そうでない場合は `false` を返します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# 新規ワークブックを最初から作成します
workbook = Workbook()
# 最初のワークシートのセルA1にサンプルの値を書き込みます
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# 書き込み保護を設定します: 変更用のパスワードと作成者を設定します
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# 書き込み保護が永続化されるようにワークブックを保存します
workbook.save("WriteProtectedWorkbook.xlsx")
# 正しいパスワードを使用して変更用パスワードを検証します
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# 別のパターンを示すために、誤ったパスワードを使用して変更用パスワードを検証します
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## ワークブック構造の保護と保護解除
ワークブック構造を保護すると、他のユーザーが非表示のワークシートを閲覧したり、新しいワークシートを追加したり、ワークシートを移動、削除、非表示化、名前変更したりすることができなくなります。保護された状態はシート構造に適用され、いずれかのシート内のセル内容には適用されません。構造保護を適用するには、`workbook.protect(ProtectionType.STRUCTURE, "password")` を呼び出します。保護を解除するには、正しいパスワードを指定して `workbook.unprotect("password")` を呼び出します。`ProtectionType.STRUCTURE` 列挙値がここで使用され、`ProtectionType.WINDOWS` などの他の保護タイプとは区別されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# 新しいワークブックを作成
workbook = Workbook()
# 2番目のワークシートを追加
workbook.getWorksheets().add()
# 最初のワークシートのセルA1にサンプル値を書き込む
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# ワークブックの構造を保護
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# ワークブックをstructure_protected.xlsxとして保存
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# ファイルを新しいWorkbookインスタンスに再読み込み
loaded_workbook = Workbook(file_path)
# 構造保護を解除
loaded_workbook.unprotect("StructPwd")
# 確認メッセージを出力
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## ワークシートの保護と保護解除
ワークシート保護は、誤操作または意図的な変更からワークシートのセルをロックします。ユーザーはパスワードを指定しないとロックされたセルを編集できません。これは、共有スプレッドシートの数式、ヘッダー、指定されたデータ入力領域を保護するために一般的に使用される保護です。ワークシートを保護するには、`worksheet.protect(ProtectionType.ALL, "password")` を呼び出します。`ProtectionType.ALL` を使用すると、ロックされたセルの選択、セルの書式設定、行と列の挿入、行と列の削除など、利用可能なすべての保護オプションが有効になります。保護を解除するには、正しいパスワードを指定して `worksheet.unprotect("password")` を呼び出します。より詳細な制御は、`ProtectionType.CONTENTS`、`ProtectionType.OBJECTS`、`ProtectionType.SCENARIOS` などの他の保護タイプをビット単位の OR で組み合わせることで実現できます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## デジタル署名の追加と検証
デジタル署名は、ワークブックの内容が認証済みであり、署名後に変更されていないことを受信者に保証します。Aspose.Cells は `Aspose.Cells.DigitalSignatures` 名前空間を通じてデジタル署名機能を提供します。一般的なワークフローは、`java.security.KeyStore` 経由で `.pfx` 証明書ファイルをロードし、それを `Aspose.Cells.DigitalSignatures.DigitalSignature` でラップし、署名を `DigitalSignatureCollection` に追加して、`workbook.addDigitalSignature(digitalSignatureCollection)` を通じてコレクションをワークブックに適用します。`digitalSignature.getComments()` プロパティには、署名時刻や目的などの署名情報を記録できます。署名後にワークブックに加えた変更はすべて署名を無効にするため、受信側で検証ステップを実行することで改ざんを検出できます。

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Java KeyStoreを使用してPFXファイルから証明書を読み込む
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# 証明書を取得する
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# デジタル署名を作成する
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# ワークブックを作成し、署名を追加する
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## 関連記事
- [Excel ファイルの暗号化と復号化](/cells/ja/python-java/encrypt-and-decrypt-excel-files/)
- [ワークブック構造の保護と保護解除](/cells/ja/python-java/protect-and-unprotect-workbook-structure/)
- [ワークシートの保護と保護解除](/cells/ja/python-java/protect-and-unprotect-worksheet/)
- [Aspose.Cells を使用した変更用パスワードの確認](/cells/ja/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}