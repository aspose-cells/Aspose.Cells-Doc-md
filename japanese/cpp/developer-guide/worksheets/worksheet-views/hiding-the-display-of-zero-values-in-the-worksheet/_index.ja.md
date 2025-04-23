---
title: C++を使用してシートの表示におけるゼロ値を非表示にする
linktitle: ワークシートでゼロ値を非表示にする
type: docs
weight: 50
url: /ja/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: この記事では、C++のライブラリまたはAPIを使用してExcelスプレッドシート内のゼロ値をプログラム的に非表示にするサンプルコードを紹介します。
keywords: Excelシートのゼロ値をC++で非表示にする
---

{{% alert color="primary" %}} 

時折、スプレッドシートでゼロ値を非表示にする必要があります。これは個人の好みである場合もありますし、書式設定の基準である場合もあります。

{{% /alert %}} 

Microsoft Excel でワークシートでゼロ値を非表示にするには:

1. **ツール** メニューから **オプション** を選択し、次に **表示** タブを選択します。
1. **ゼロ値** オプションを選択解除します。
1. **OK** をクリックします。

Aspose.Cells を使用してゼロを非表示にするデモンストレーションとなるサンプルコードを以下に示します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
