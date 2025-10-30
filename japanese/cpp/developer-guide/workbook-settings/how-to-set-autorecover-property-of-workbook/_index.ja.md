---
title: Excelドキュメントの作成アプリケーションの自動回復設定をC++で行う方法
linktitle: ワークブックのAutoRecoverプロパティを設定する方法
type: docs
weight: 220
url: /ja/cpp/how-to-set-autorecover-property-of-workbook/
description: ブックの自動回復プロパティを有効または無効にする方法（Aspose.Cells for C++を使用）を学びます。
---

{{% alert color="primary" %}}

Aspose.Cells を使用して、ブックの自動回復プロパティを設定できます。このプロパティのデフォルト値は **true** です。ブックでこれを **false** に設定すると、Microsoft Excel はそのExcelファイルの自動回復（自動保存）を無効にします。

Aspose.Cells は、このオプションを有効または無効にするための [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) プロパティを提供します。

{{% /alert %}}

以下のコードは、ブックの [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) プロパティの使用方法を示しています。最初にこのプロパティのデフォルト値（**true**）を読み取り、その後に **false** に設定し、ブックを保存します。その後、再度ブックを読み取り、このプロパティの値（この時点では **false**）を確認します。

## C++ コード：Workbook の自動回復プロパティを設定

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
