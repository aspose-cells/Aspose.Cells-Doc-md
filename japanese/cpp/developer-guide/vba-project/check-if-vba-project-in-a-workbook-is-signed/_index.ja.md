---
title: Workbook内のVBAプロジェクトが署名されているかどうかをC++で確認する
linktitle: ブックのVBAプロジェクトが署名されているかどうかを確認
type: docs
weight: 70
url: /ja/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aspose.Cellsを使用してC++でWorkbook内のVBAプロジェクトが署名されているかどうかを確認します。
---

{{% alert color="primary" %}}

Microsoft Excelの**Tools > Digital Signatures...**メニューコマンドを使用して、VBAプロジェクトが署名されているかどうかを確認できます。同様に、Aspose.Cellsの[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned)を使用してプログラム的に確認することもできます。

{{% /alert %}}

## **C++でWorkbook内のVBAプロジェクトが署名されているかどうかを確認する**

以下のコードは、ワークブックをロードし、そのVBAプロジェクトが署名されているかどうかを [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned)プロパティを使用して判定します。署名されている場合は **true** を返し、そうでなければ**false**を返します。

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
    U16String sampleFilePath = srcDir + u"Sample1.xlsx";

    // Create workbook
    Workbook workbook(sampleFilePath);

    // Check if the VBA project is signed
    bool isSigned = workbook.GetVbaProject().IsSigned();
    std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
