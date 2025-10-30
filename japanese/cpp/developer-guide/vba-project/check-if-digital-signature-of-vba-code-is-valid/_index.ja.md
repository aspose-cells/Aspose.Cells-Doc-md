---
title: C++でVBAコードのデジタル署名が有効かどうかをチェックします
linktitle: VBAコードのデジタル署名が有効かどうかを確認する
type: docs
weight: 120
url: /ja/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Aspose.Cellsを使用してC++でVBAコードのデジタル署名の有効性を確認する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/) プロパティを使用してVBAコードのデジタル署名が有効かどうかを確認できます。有効な署名の場合は**true**を返し、そうでなければ**false**を返します。VBAコードを変更すると、そのデジタル署名は無効になります。

{{% /alert %}}

## **C++でVBAコードのデジタル署名が有効かどうかを確認する**

以下のコードは、提供されたリンクからダウンロードできる[サンプルExcelファイル](5115030.xlsm)を使用して、このプロパティの使用例を示しています。同じExcelファイルには有効な署名がありますが、そのVBAコードを変更して保存し、再度確認すると署名が無効になっていることがわかります。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the workbook from an existing Excel file with VBA project
    Workbook workbook(srcDir + u"sampleVBAProjectSigned.xlsm");

    // Check if the VBA Code Project is valid signed
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    // Modify the VBA Code
    U16String code = workbook.GetVbaProject().GetModules().Get(1).GetCodes();
    code = u"Welcome to Aspose.Cells"; // Directly setting new code here
    workbook.GetVbaProject().GetModules().Get(1).SetCodes(code);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsm");

    // Reload the workbook
    workbook = Workbook(srcDir + u"output_out.xlsm");

    // Now the signature is invalid
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
