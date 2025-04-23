---
title: C++による1904日付システムの実装
linktitle: 1904年日付システムを実装する
description: Aspose.Cellsは、スプレッドシートファイルを操作するC++ライブラリです。1904日付システムの実装をサポートしており、1月1日1904年の日付システムに基づいた計算や書式設定が可能です。この記事は、Aspose.Cellsを使用して1904日付システムを実装する方法を説明します。
keywords: Aspose.Cells、1904日付システム、スプレッドシート、計算、書式設定
type: docs
weight: 7000
url: /ja/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excelは1900年日付システム（Windows用Excelのデフォルトの日付システム）と1904年日付システムの2つをサポートしています。 1904年日付システムは通常、Macintosh Excelファイルとの互換性を提供するために使用され、Excel for Macintoshを使用している場合はデフォルトのシステムです。 Aspose.Cellsを使用してExcelファイルに1904年日付システムを設定できます。

{{% /alert %}}

Microsoft Excel（例えばMicrosoft Excel 2003）で1904年日付システムを実装するには:

1. **ツール**メニューから**オプション**を選択し、**計算**タブを選択します。
1. **1904年日付システム**オプションを選択します。
1. **OK** をクリックします。

|**Microsoft Excelで1904年日付システムを選択**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Aspose.CellsのAPIを使用してこの機能を実現するサンプルコードを以下に示します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
