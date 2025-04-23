---
title: C++を使って数式を含むCSVファイルを読み込むまたはインポートする方法
linktitle: 数式を持つCSVファイルを読み込むまたはインポートする
type: docs
weight: 350
url: /ja/cpp/load-or-import-csv-file-with-formulas/
description: Aspose.Cells for C++を使用して数式を含むCSVファイルを読み込みまたはインポートします。
---

{{% alert color="primary" %}} 

CSVファイルには主にテキストデータが含まれており、通常は数式は含まれていません。ただし、場合によってはCSVファイルに数式が含まれることがあります。そのようなCSVファイルは、[TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/)を**true**に設定して読み込む必要があります。このプロパティを**true**に設定すると、Aspose.Cellsは数式を単なるテキストとして扱わず、通常の数式として処理します。Aspose.Cellsの数式計算エンジンがそれらを処理します。

{{% /alert %}} 

以下のコード例は、数式を含むCSVファイルを読み込みインポートする方法を示しています。任意のCSVファイルを使用できます。例として、[シンプルなCSVファイル](5115034.csv)を使用し、このデータが含まれています。ご覧のとおり、数式を含んでいます。

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    //For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    //Create TxtLoadOptions with specified settings
    TxtLoadOptions opts;
    opts.SetSeparator(u','); // Set the separator to a comma
    opts.SetHasFormula(true); // Indicate that the CSV may have formulas

    // Load the CSV file into a Workbook object
    Workbook workbook(srcDir + u"sample.csv", opts);

    // You can also import the CSV file starting from cell D4 (indices 3,3)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().ImportCSV(srcDir + u"sample.csv", opts, 3, 3);

    // Save the workbook in Xlsx format
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "CSV file loaded and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

まずCSVファイルを読み込み、その後セルD4に再度インポートします。最後に、ワークブックオブジェクトをXLSX形式で保存します。[出力されるXLSXファイル](5115052.xlsx)はこのようになります。ご覧のとおり、セルC3とF4に数式が含まれており、その結果は800です。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
