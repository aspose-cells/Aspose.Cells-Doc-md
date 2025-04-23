---
title: ワークブック内外のシートをコピーおよび移動する（C++）
linktitle: シートのコピーと移動
type: docs
weight: 80
url: /ja/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Aspose.Cells for C++を使用してExcelのワークシート内および間でのコピーと移動方法を学習します。
---

{{% alert color="primary" %}}

複数のシートに共通のフォーマットやデータ入力を持たせる必要がある場合があります。例えば、四半期予算の作成において、同じ列見出し、行見出し、数式を含むシートを複数作成したい場合です。これには、1つのシートを作成し、それを複数コピーする方法があります。

Aspose.Cellsは、ワークブック内またはワークブック間でワークシートを最高の精度でコピーまたは移動する機能をサポートします。データ、書式設定、テーブル、行列、グラフ、画像、その他のオブジェクトを含むワークシートがコピーされます。

{{% /alert %}}

## **ワークシートのコピーおよび移動**

### **ワークブック内のワークシートのコピー**

すべての例の最初のステップは次の通りです：

1. Microsoft Excelでいくつかのデータを入力した2つのワークブックを作成します。この例では、新たに2つのワークブックを作成し、シートにデータを入力しました：
   - FirstWorkbook.xlsx（3つのシート）
   - SecondWorkbook.xlsx（1つのシート）

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [Aspose.Cells for C++をダウンロード](https://downloads.aspose.com/cells/cpp)
   1. 開発コンピュータにインストールする

1. プロジェクトを作成します。
   1. 好みのIDEで新しいC++プロジェクトを作成します

1. 参照を追加します。
   1. プロジェクトにAspose.Cells for C++ライブラリを追加します

1. ワークブック内のワークシートをコピーします。
   最初の例では、FirstWorkbook.xlsx の最初のワークシート（Copy）をコピーします。

このコードを実行すると、ワークシート「Copy」が「Last Sheet」としてFirstWorkbook.xlsx内にコピーされます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook excelWorkbook1(srcDir + u"FirstWorkbook.xlsx");

    // Get worksheet collection reference
    WorksheetCollection worksheets = excelWorkbook1.GetWorksheets();

    // Copy third worksheet (index 2) within the workbook
    worksheets.AddCopy(worksheets.Get(2).GetName());

    // Save modified workbook
    excelWorkbook1.Save(outDir + u"FirstWorkbookCopied_out.xlsx");

    std::cout << "Worksheet copied successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ワークブック内のワークシートを移動**

以下のコードは、ワークブック内のワークシートを別の位置に移動する方法を示しています。このコードを実行すると、FirstWorkbook.xlsx内でインデックス1の「Move」という名前のワークシートがインデックス2に移動します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create input and output file paths
    U16String inputFilePath = srcDir + u"FirstWorkbook.xlsx";
    U16String outputFilePath = outDir + u"FirstWorkbookMoved_out.xlsx";

    // Load source workbook
    Workbook excelWorkbook2(inputFilePath);

    // Access worksheet collection and move target sheet
    WorksheetCollection sheets = excelWorkbook2.GetWorksheets();
    sheets.Get(u"Move").MoveTo(2);

    // Save modified workbook
    excelWorkbook2.Save(outputFilePath);

    std::cout << "Worksheet moved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ワークブック間でワークシートをコピーする**

コードを実行すると、「Copy」という名前のシートを持つワークシートが、SecondWorkbook.xlsxにコピーされます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open source workbooks
    Workbook excelWorkbook3(srcDir + u"FirstWorkbook.xlsx");
    Workbook excelWorkbook4(srcDir + u"SecondWorkbook.xlsx");

    // Access worksheets collection from second workbook
    WorksheetCollection sheets4 = excelWorkbook4.GetWorksheets();

    // Add new worksheet to destination workbook
    sheets4.Add();

    // Copy specified worksheet from source to destination
    Worksheet sourceSheet = excelWorkbook3.GetWorksheets().Get(u"Copy");
    sheets4.Get(1).Copy(sourceSheet);

    // Save modified workbook
    excelWorkbook4.Save(outDir + u"CopyWorksheetsBetweenWorkbooks_out.xlsx");

    std::cout << "Worksheets copied successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ワークブック間でワークシートを移動する**

このコードを実行すると、「Move」という名前のワークシートがFirstWorkbook.xlsx から「Sheet3」の名前でSecondWorkbook.xlsxに移動します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open first workbook
    Workbook excelWorkbook5(srcDir + u"FirstWorkbook.xlsx");

    // Open second workbook and add new worksheet
    Workbook excelWorkbook6(srcDir + u"SecondWorkbook.xlsx");
    excelWorkbook6.GetWorksheets().Add();

    // Copy third worksheet from first workbook to third position in second workbook
    WorksheetCollection sheets5 = excelWorkbook5.GetWorksheets();
    WorksheetCollection sheets6 = excelWorkbook6.GetWorksheets();
    sheets6.Get(2).Copy(sheets5.Get(2));

    // Remove copied worksheet from source workbook
    sheets5.RemoveAt(2);

    // Save modified workbooks
    excelWorkbook5.Save(outDir + u"FirstWorkbookWithMove_out.xlsx");
    excelWorkbook6.Save(outDir + u"SecondWorkbookWithMove_out.xlsx");

    std::cout << "Worksheets moved successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```
