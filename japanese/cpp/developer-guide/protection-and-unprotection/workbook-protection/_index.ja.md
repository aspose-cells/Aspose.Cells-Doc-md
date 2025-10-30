---
title: ワークブック構造をC++で保護および解除
linktitle: ブック構造の保護と保護解除
type: docs
weight: 40
url: /ja/cpp/protect-and-unprotect-workbook-structure/
description: Aspose.Cellsを使用してExcelファイルのワークブック構造をC++で保護および解除します。
---

{{% alert color="primary" %}}
他のユーザーによる隠しワークシートの表示、追加、移動、削除、または非表示、およびワークシートの名前の変更を防ぐために、Excelブックの構造をパスワードで保護できます。
{{% /alert %}}

## **MS Excelでワークブック構造を保護および解除**

**![ブック構造の保護と保護解除](protect-and-unprotect-workbook-structure.png)**

1. **レビュー > ブックの保護** をクリックします。
1. **パスワードボックス** にパスワードを入力します。
1. **OK** を選択し、パスワードを再入力して確認し、その後再度 **OK** を選択します。

## **Aspose.Cells for C++を使用してワークブック構造を保護する**
Excelファイルのワークシートの構造を保護するためには、次の簡単なコード行のみが必要です。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.Cells for C++を使用してワークブック構造の保護を解除する**
Aspose.Cells APIを使用してワークブック構造を保護解除するのは簡単です。正しいパスワードが必要です。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
注意：正しいパスワードが必要です。
{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
