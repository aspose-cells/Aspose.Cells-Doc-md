---
title: C++を使用してワークシートの保護と解除
linktitle: ワークシートの保護と保護解除
type: docs
weight: 40
url: /ja/cpp/protect-and-unprotect-worksheets/
description: Aspose.Cells for C++を使用してExcelファイルのワークシートの保護と解除
---

{{% alert color="primary" %}}
ワークシート上のデータの変更、移動、または削除を他のユーザーが誤ってまたは意図的に防ぐために、Excelワークシートのセルをロックし、その後シートをパスワードで保護できます。 
{{% /alert %}}

## **MS Excelのワークシートを保護および解除**

**![ワークシートの保護と保護解除](protect-and-unprotect-worksheet.png)**

1. **レビュー > ワークシートの保護** をクリックします。
1. **パスワードボックス** にパスワードを入力します。
1. **許可** オプションを選択します。
1. **OK** を選択し、パスワードを再入力して確認し、その後再度 **OK** を選択します。

## **Aspose.Cells for C++を使用してワークシートを保護**
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

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.Cells for C++を使用してワークシートの保護を解除**
Aspose.Cells APIを使えば、ワークシートの保護の解除は簡単です。ワークシートがパスワードで保護されている場合、正しいパスワードが必要です。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [Excel XP以降の高度な保護設定](/cells/ja/cpp/advanced-protection-settings-since-excel-xp/)
- [ワークシートがパスワードで保護されているかどうかを検出する](/cells/ja/cpp/detect-if-worksheet-is-password-protected/)
- [ワークシートの保護](/cells/ja/cpp/protecting-worksheets/)
- [ワークシートの保護を解除する](/cells/ja/cpp/unprotect-a-worksheet/)
- [ワークシートを保護するために使用されたパスワードの検証](/cells/ja/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
