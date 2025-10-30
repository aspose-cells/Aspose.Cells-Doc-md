---
title: パスワードを使用してシート保護を検証する
linktitle: ワークシートを保護するために使用されたパスワードの検証
type: docs
weight: 370
url: /ja/cpp/verify-password-used-to-protect-the-worksheet/
description: Aspose.Cells for C++を使って、シートの保護に使用されたパスワードを検証する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cells の API は [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) クラスを向上させ、いくつかの便利なプロパティとメソッドを導入しています。 そのようなメソッドの1つは、*string* のインスタンスとしてパスワードを指定し、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) を保護すると同じパスワードが使用されたかを検証する [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) です。

{{% /alert %}}

[**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/)メソッドは、指定されたパスワードが保護されたシートのパスワードと一致すれば**true**を返し、一致しなければ**false**を返します。以下のコードは、[**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/)メソッドと[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/)プロパティを用いて、パスワード保護を検出し、パスワードの検証を行います。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
