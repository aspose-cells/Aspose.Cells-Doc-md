---
title: Aspose.Cellsを使用して編集用パスワードを確認（C++）
linktitle: 修正パスワードの確認
type: docs
weight: 2400
url: /ja/cpp/check-password-to-modify-using-aspose-cells/
description: 指定されたパスワードが編集パスワードと一致するかどうかをAspose.Cellsを使って確認します。
---

{{% alert color="primary" %}}

プログラム的に指定されたパスワードが[編集用パスワード]と一致するかどうかを確認する必要がある場合があります。Aspose.Cellsは、WorkbookSettings.WriteProtection.ValidatePassword()メソッドを提供し、これを使ってパスワードの正確性を確認します。

{{% /alert %}}

## **Microsoft Excelで変更するためのパスワードをチェックする**

Microsoft Excelで作成するワークブックに**開くためのパスワード**および**変更するためのパスワード**を割り当てることができます。これらのパスワードを指定するためのMicrosoft Excelが提供するインターフェースを示すスクリーンショットをご覧ください。

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cellsを使用して変更パスワードを確認する**

次のサンプルコードは、[元のExcel](5112232.xlsx)ファイルをロードします。**開くためのパスワード**は1234であり、**変更するためのパスワード**は5678です。コードはまず、567が正しい**変更するためのパスワード**かどうかをチェックし、falseを返し、次に5678が**変更するためのパスワード**かどうかをチェックし、trueを返します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **コンソール出力**

上記のサンプルコードで[元のExcel](5112232.xlsx)ファイルをロードした後のコンソール出力はこちらです。

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
