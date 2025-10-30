---
title: C++でシートのハイパーリンクを編集する
linktitle: ワークシートのハイパーリンクを編集
type: docs
weight: 330
url: /ja/cpp/editing-hyperlinks-of-worksheet/
description: Aspose.Cells for C++ APIを通じてシートのハイパーリンクを編集する方法を学びます。
keywords: ハイパーリンクの編集、ワークシートのハイパーリンクの編集、セルのハイパーリンクの編集、ワークシートのすべてのハイパーリンクにアクセス
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、[**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/)コレクションを使用してワークシートのすべてのハイパーリンクにアクセスできます。このコレクションから1つずつハイパーリンクにアクセスしてそのプロパティを編集することができます。

{{% /alert %}}

次のサンプルコードは、ワークシートのすべてのハイパーリンクにアクセスし、それらの[**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/)プロパティをAsposeのウェブサイトに変更します。

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
