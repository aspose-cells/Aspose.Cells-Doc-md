---
title: C++での保護と解除
linktitle: 暗号化と保護
description: このセクションでは、Excel ファイルの暗号化と復号化、および Excel データの保護について紹介します。ファイル暗号化、読み取り専用保護、ワークブック構造の保護、ワークシートの保護、C++ コードを使用したデジタル署名について説明します
keywords: Aspose.Cells, Aspose.Cells for C++, 暗号化, 復号化, パスワード, 保護, 保護解除, ワークブック保護, ワークシート保護, 読み取り専用, デジタル署名, C++
type: docs
weight: 68
url: /ja/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel ワークブックには、不正アクセスから保護する必要がある、機密性の高い財務情報、ビジネス情報、または個人情報が格納されることがよくあります。Aspose.Cells for C++ は、Microsoft Excel の機能を反映した包括的な保護機能セットを提供し、ファイルレベル、ワークブックレベル、ワークシートレベルでデータを保護できます。

{{% alert color="primary" %}}
Aspose.Cells for C++ は、MS Excel と同様に、ファイルレベルからデータレベルまで幅広い保護機能を提供します。これらの機能には、ファイルのパスワードによる暗号化、変更用パスワードによる読み取り専用アクセスの強制、ワークブック構造の保護、ワークシートの保護、ワークブックへのデジタル署名が含まれます。
{{% /alert %}}

## Excel ファイルの暗号化と復号化
Excel ファイルに設定されたパスワードは、不正なユーザーがワークブックの内容を開いたり閲覧したりするのを防ぎます。ワークブックを暗号化するには、`workbook.GetSettings().SetPassword()` にパスワード文字列を割り当ててからワークブックを保存します。Aspose.Cells はファイルを暗号化された形式で書き込みます。暗号化されたワークブックを開いて復号化するには、`LoadOptions` オブジェクトをインスタンス化し、暗号化時に使用されたのと同じパスワードを `LoadOptions.SetPassword()` に設定して、`Workbook` コンストラクタに渡します。Aspose.Cells は指定されたパスワードを透過的に適用するため、以降のコードでは、ファイルが通常のワークブックであるかのように復号化された内容を操作できます。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 読み取り専用保護（変更用パスワード）
Excel は 2 つの異なるパスワード層をサポートしています。1 つ目はファイル自体を暗号化する「開くためのパスワード」で、前のセクションで説明されています。2 つ目は「変更用パスワード」で、ワークブックを開くことをブロックするものではなく、変更用パスワードが指定されない限り、Excel はファイルを読み取り専用モードで開くことを推奨します。この動作は Aspose.Cells では `workbook.GetSettings().GetWriteProtection()` を通じて設定します。`Password` プロパティに変更用パスワードを設定し、`Author` プロパティに保護を適用したユーザーを識別する情報を設定します。`WriteProtection.ValidatePassword()` メソッドを使用して、指定された変更用パスワードが正しいかどうかを確認します。一致する場合は `true` を返し、一致しない場合は `false` を返します。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## ワークブック構造の保護と保護解除
ワークブック構造を保護すると、他のユーザーが非表示のワークシートを表示したり、新しいワークシートを追加したり、ワークシートを移動、削除、非表示にしたり、名前を変更したりすることができなくなります。保護された状態はシートの構造に適用され、シート内のセルの内容には適用されません。構造保護を適用するには、`workbook.Protect(ProtectionType::Structure, "password")` を呼び出します。保護を解除するには、`workbook.Unprotect("password")` を呼び出し、正しいパスワードを指定します。ここで使用される `ProtectionType::Structure` 列挙値は、`ProtectionType::Windows` などの他の保護タイプとは区別されます。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 新しいワークブックを作成
    Workbook workbook;
    // 2番目のワークシートを追加
    workbook.GetWorksheets().Add();
    // 最初のワークシートのセルA1にサンプル値を書き込む
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // ワークブックの構造を保護
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // ワークブックをstructure_protected.xlsxとして保存
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // ファイルを新しいWorkbookインスタンスに再読み込み
    Workbook loadedWorkbook(filePath);
    // 構造の保護を解除
    loadedWorkbook.Unprotect(u"StructPwd");
    // 確認メッセージを出力
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## ワークシートの保護と保護解除
ワークシートの保護は、ワークシートのセルを偶発的または故意の変更からロックします。ユーザーはパスワードを指定せずにロックされたセルを編集することはできません。これは、共有スプレッドシートで数式、ヘッダー、または指定されたデータ入力領域を保護するために使用される一般的な保護です。ワークシートを保護するには、`worksheet.Protect(ProtectionType::All, "password")` を呼び出します。`ProtectionType::All` を使用すると、ロックされたセルの選択、セルの書式設定、行と列の挿入、行と列の削除など、利用可能なすべての保護オプションが有効になります。保護を解除するには、正しいパスワードを指定して `worksheet.Unprotect("password")` を呼び出します。ビット単位の OR を使用して `Contents`、`Objects`、`Scenarios` などの他の保護タイプを組み合わせることで、より細かい制御が可能になります。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## デジタル署名の追加と検証
デジタル署名は、受信者にワークブックの内容が本物であり、署名されてから変更されていないことを保証します。Aspose.Cells は `Aspose::Cells::DigitalSignatures` 名前空間を通じてデジタル署名のサポートを提供します。典型的なワークフローは、`.pfx` 証明書ファイルを読み込み、`Aspose::Cells::DigitalSignatures::DigitalSignature` でラップし、署名を `DigitalSignatureCollection` に追加し、`workbook.AddDigitalSignature(DigitalSignatureCollection)` を通じてコレクションをワークブックに適用します。`DigitalSignature.GetComments()` プロパティは、署名時刻や目的などの署名コンテキストを記録できます。署名後にワークブックに加えられた変更はすべて署名を無効にするため、受信側で検証ステップを実行することで改ざんを検出できます。

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 関連記事
- [Excel ファイルの暗号化と復号化](/cells/ja/cpp/encrypt-and-decrypt-excel-files/)
- [ワークブック構造の保護と保護解除](/cells/ja/cpp/protect-and-unprotect-workbook-structure/)
- [ワークシートの保護と保護解除](/cells/ja/cpp/protect-and-unprotect-worksheets/)
- [共有ワークブックのパスワード保護または保護解除](/cells/ja/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Aspose.Cells を使用して変更用パスワードを確認する](/cells/ja/cpp/check-password-to-modify-using-aspose-cells/)
- [暗号化された Office Open XML - OOXML ファイルのファイル形式を検出する](/cells/ja/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel ファイルの暗号化](/cells/ja/cpp/encrypting-excel-files/)
- [ファイル形式を検出し、ファイルが暗号化されているかどうかを確認する方法](/cells/ja/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}