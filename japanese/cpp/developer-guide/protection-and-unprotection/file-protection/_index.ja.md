---
title: C++を使用してExcelファイルを暗号化および復号化
linktitle: Excelファイルの暗号化および復号化
type: docs
weight: 10
url: /ja/cpp/encrypt-and-decrypt-excel-files/
description: C++を使用してExcelファイルを暗号化および復号化する方法。Excelファイルをロックおよびロック解除します。
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365)を使用して、スプレッドシートを暗号化およびパスワード保護することができます。暗号化には、暗号化サービスプロバイダー（CSP）によって提供されるアルゴリズムが使用されます。暗号化キーの長さを適切に選択することが重要です。一部のCSPは40ビットまたは56ビットを超える長さをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化には、最小128ビットのキー長が必要です。Microsoft Windowsには、強力な暗号化タイプを提供するCSPも含まれています。例えば、「Microsoft Strong Cryptographic Provider」などです。128ビットの暗号化は、銀行がインターネットバンキングシステムとの接続を暗号化する際に使用するものです。

Aspose.Cellsを使用すると、任意の暗号化タイプでMicrosoft Excelファイルを暗号化およびパスワード保護することができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（ここではMicrosoft Excel 2003）でファイルの暗号化設定を行うには：

1. **ツール**メニューから**オプション**を選択します。ダイアログが表示されます。
1. **セキュリティ**タブを選択します。
1. パスワードを入力し、**詳細**をクリックします。
1. 暗号化方式を選択し、パスワードを確認します。

## **Aspose.CellsでExcelファイルを暗号化**

次の例は、Aspose.Cells APIを使用してExcelファイルを暗号化し、パスワード保護する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify XOR encryption type
    workbook.SetEncryptionOptions(EncryptionType::XOR, 40);

    // Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Workbook encrypted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **修正パスワードを指定するオプション**

次の例は、Aspose.Cells APIを使用して既存のファイルの**修正パスワード**Microsoft Excelオプションを設定する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"SpecifyPasswordToModifyOption.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Set the password for modification
    workbook.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Password for modification set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.CellsでExcelファイルを復号化**

次のコード例のように、Aspose.Cells APIを使用してパスワード保護されたExcelファイルを容易に開き、復号することができます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create load options and set password
    LoadOptions loadOptions;
    loadOptions.SetPassword(u"password");

    // Open encrypted Excel file
    Workbook workbook(u"Book1.xlsx", loadOptions);

    // Remove password protection
    workbook.GetSettings().SetPassword(nullptr);

    // Save the modified workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Password removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**

- [ODSファイルの暗号化および復号化](/cells/ja/cpp/encrypt-and-decrypt-ods-files/)
- [強力な暗号化タイプの設定](/cells/ja/cpp/setting-strong-encryption-type/)
- [ブックを書き込み保護する際に著者を指定する](/cells/ja/cpp/specify-author-while-write-protecting-workbook/)
- [暗号化されたファイルのパスワードの検証](/cells/ja/cpp/verify-password-of-encrypted-excel-and-ods-files/)
{{< app/cells/assistant language="cpp" >}}
