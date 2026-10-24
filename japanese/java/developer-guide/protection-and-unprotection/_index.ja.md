---
title: Excelファイルの暗号化、復号化、保護および解除
linktitle: 暗号化と保護
description: このセクションでは、Java コードを使用して Excel ファイルを暗号化および復号化し、Excel データを保護する方法を紹介します。ファイル暗号化、読み取り専用保護、ワークブック構造の保護、ワークシート保護、およびデジタル署名について取り上げます。
keywords: Aspose.Cells, Java, 暗号化, 復号化, パスワード, 保護, 保護解除, ワークブック保護, ワークシート保護, 読み取り専用, デジタル署名
type: docs
weight: 68
url: /ja/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel ワークブックには、機密性の高い財務情報、業務情報、個人情報などが保存されていることがよくあり、これらの情報への不正アクセスを防ぐ必要があります。Aspose.Cells for Java は、Microsoft Excel の機能に対応する包括的な保護機能を提供し、ファイルレベル、ワークブックレベル、ワークシートレベルでデータを保護できます。

{{% alert color="primary" %}}
Aspose.Cells for Java は、MS Excel に類似した、ファイルレベルからデータレベルまでの幅広い保護機能を提供します。これらの機能には、パスワードによるファイルの暗号化、変更用パスワードによる読み取り専用アクセスの適用、ワークブック構造の保護、ワークシートの保護、ワークブックへのデジタル署名の適用が含まれます。
{{% /alert %}}

## Excel ファイルの暗号化と復号化
Excel ファイルに設定したパスワードは、不正なユーザーがワークブックを開いたり閲覧したりするのを防ぎます。ワークブックを暗号化する場合は、`Workbook.Settings.Password`（`workbook.getSettings().setPassword(...)` 経由でアクセス）にパスワード文字列を設定し、その後、ワークブックを保存します。Aspose.Cells は暗号化された形式でファイルを書き込みます。暗号化されたワークブックを復号化して開く場合は、`LoadOptions` オブジェクトをインスタンス化し、暗号化時に使用したパスワードと同じパスワードを `LoadOptions.Password`（`loadOptions.setPassword(...)` 経由でアクセス）に設定して、`Workbook` コンストラクターに渡します。Aspose.Cells は指定されたパスワードを透過的に処理するため、ファイルが通常のワークブックであるかのように、残りのコードで復号済みのコンテンツを操作できます。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## 読み取り専用保護（変更用パスワード）
Excel では、異なる 2 種類のパスワードがサポートされています。1 つ目はファイル自体を暗号化する「開くためのパスワード」であり、前のセクションで説明しました。2 つ目は「変更用パスワード」であり、ワークブックを開くことを妨げるものではありません。変更用パスワードが指定されない限り、Excel ではファイルを読み取り専用モードで開くことが推奨されます。Aspose.Cells では、`Workbook.Settings.WriteProtection`（`workbook.getSettings().getWriteProtection()` 経由でアクセス）を使ってこの動作を設定します。`Password` プロパティ（`writeProtection.setPassword(...)` 経由）を変更用パスワードに設定し、`Author` プロパティ（`writeProtection.setAuthor(...)`）には、保護を適用したユーザーを識別する情報を設定します。指定した変更用パスワードが正しいかを確認するには、`WriteProtection.validatePassword(String)` メソッドを使用します。一致する場合は `true` を返し、一致しない場合は `false` を返します。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## ワークブック構造の保護と保護解除
ワークブック構造を保護すると、他のユーザーが非表示のワークシートを表示したり、新しいワークシートを追加したり、ワークシートを移動したり、削除したり、非表示にしたり、名前を変更したりすることができません。この保護は、任意のシート内のセル内容ではなく、シート構造に適用されます。ワークブック構造を保護するには、`workbook.protect(ProtectionType.STRUCTURE, "password")` を呼び出します。保護を解除するには、`workbook.unprotect("password")` を呼び出して、正しいパスワードを指定します。ここでは `ProtectionType.STRUCTURE` 列挙型の値を使用します。これは `ProtectionType.WINDOWS` などの他の保護タイプとは異なります。

```java
import com.aspose.cells.*;
// 新しいワークブックを作成
Workbook workbook = new Workbook();
// 2番目のワークシートを追加
workbook.getWorksheets().add();
// 最初のワークシートのセルA1にサンプル値を書き込む
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// ワークブックの構造を保護
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// ワークブックをstructure_protected.xlsxとして保存
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// ファイルを新しいWorkbookインスタンスに再読み込み
Workbook loadedWorkbook = new Workbook(filePath);
// 構造保護を解除
loadedWorkbook.unprotect("StructPwd");
// 確認メッセージを出力
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## ワークシートの保護と保護解除
ワークシートの保護は、ワークシートのセルを誤操作や意図的な変更からロックします。ユーザーはパスワードを指定しない限り、ロックされたセルを編集できません。これは、共有スプレッドシートの数式、ヘッダー、または指定されたデータ入力領域を守るために通常使用される保護です。ワークシートを保護するには、`worksheet.protect(ProtectionType.ALL, "password")` を呼び出します。`ProtectionType.ALL` を使用すると、ロックされたセルの選択、セルの書式設定、行と列の挿入、行と列の削除など、利用可能なすべての保護オプションが有効になります。保護を解除するには、正しいパスワードを指定して `worksheet.unprotect("password")` を呼び出します。`CONTENTS`、`OBJECTS`、`SCENARIOS` などの他の保護タイプをビット単位 OR で組み合わせることで、より細かな制御も可能です。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## デジタル署名の追加と検証
デジタル署名により、受信者は、ワークブックの内容が真正であり、署名されてから変更されていないことを確認できます。Aspose.Cells は、`com.aspose.cells.DigitalSignatures` パッケージを通じてデジタル署名機能を提供します。一般的な手順では、Java セキュリティ API（`java.security.KeyStore` や `java.security.cert.X509Certificate` など）を使用して `.pfx` 証明書ファイルを読み込み、`com.aspose.cells.DigitalSignatures.DigitalSignature` でラップします。次に、署名を `DigitalSignatureCollection` に追加し、`workbook.addDigitalSignature(DigitalSignatureCollection)` を使用してコレクションをワークブックに適用します。`DigitalSignature.getComments()` プロパティは、署名時刻や目的などの署名コンテキストを記録するために使用できます。署名後にワークブックに対して行われた変更は署名を無効にするため、受信側での検証ステップで改ざんを検出できます。

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## 関連記事
- [Excel ファイルの暗号化と復号化](/cells/ja/java/encrypt-and-decrypt-excel-files/)
- [ワークブック構造の保護と保護解除](/cells/ja/java/protect-and-unprotect-workbook-structure/)
- [ワークシートの保護と保護解除](/cells/ja/java/protect-and-unprotect-worksheet/)
- [共有ワークブックのパスワードによる保護と保護解除](/cells/ja/java/password-protect-or-unprotect-the-shared-workbook/)
- [デジタル署名の割り当てと検証](/cells/ja/java/assign-and-validate-digital-signatures/)
- [暗号化された Office Open XML - OOXML ファイルの形式を検出する](/cells/ja/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [ファイル形式を検出し、ファイルが暗号化されているかを確認する](/cells/ja/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}