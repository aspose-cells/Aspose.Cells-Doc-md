---
title: C++でワークシートがパスワード保護されているか検出
linktitle: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 360
url: /ja/cpp/detect-if-worksheet-is-password-protected/
description: Aspose.Cells for C++を使用して、ワークシートがパスワード保護されているか検出する方法を学びます。
---

{{% alert color="primary" %}}

ワークブックやワークシートは個別に保護することが可能です。例えば、複数のシートがパスワード保護されているスプレッドシートもありますが、スプレッドシート自体は保護されていない場合もあります。Aspose.Cells APIは、特定のワークシートがパスワード保護されているか否かを検出する手段を提供します。本記事は、Aspose.Cells for C++ APIを使用した例を示しています。

{{% /alert %}}

Aspose.Cells for C++は、[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/)プロパティを公開し、ワークシートがパスワード保護されているかどうかを検出します。Boolean型の[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/)プロパティは、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)がパスワード保護されていれば**true**、そうでなければ**false**を返します。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
