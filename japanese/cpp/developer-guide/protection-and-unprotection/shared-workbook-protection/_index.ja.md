---
title: 共有ワークブックのパスワード保護または解除をC++で行う
linktitle: 共有ブックをパスワードで保護または保護解除
type: docs
weight: 10
url: /ja/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Aspose.Cells for C++を使用して、共有ワークブックのパスワード保護または解除方法を学びます。
---

## **可能な使用シナリオ**

以下のスクリーンショットに示すように、Microsoft Excelで共有ブックを保護または保護解除することができます。Aspose.Cellsでも、[**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/)メソッドと[**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/)メソッドを使用することでこの機能をサポートしています。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **共有ワークブックのパスワード保護または保護解除**

次のサンプルコードは、ブックを作成し、共有を有効にした状態で保護し、[出力Excelファイル](55541777.xlsx)として保存します。スクリーンショットに示すように、保護を解除しようとすると、Microsoft Excelがパスワードの入力を要求します。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
