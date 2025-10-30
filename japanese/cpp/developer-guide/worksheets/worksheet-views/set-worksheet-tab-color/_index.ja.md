---
title: C++でワークシートタブの色を設定する
linktitle: ワークシートタブの色を設定
type: docs
weight: 120
url: /ja/cpp/set-worksheet-tab-color/
description: この記事は、C++ APIまたはライブラリを使用してExcelワークシートのタブの色をプログラム的に設定するサンプルコードを示しています。
keywords: Excelタブの色をC++で設定する、コード例
---

{{% alert color="primary" %}}

Aspose.Cells を使用すると、個々のワークシートタブの色を変更して目立たせることができます。たとえば、Expenses を赤、Sales を緑、Assets を青などにすることができます。

{{% /alert %}}

## **Microsoft Excel でワークシートのタブの色を設定する**
1. 現在のワークシートの下部にあるタブシートでタブを右クリックします。
1. **タブの色**を選択します。
1. パレットから色を選択します。
1. **OK** をクリックします。

## **Aspose.Cellsでワークシートのタブの色を設定する**
以下のサンプルコードは、Aspose.Cellsでタブの色を設定する方法を示しています。

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
