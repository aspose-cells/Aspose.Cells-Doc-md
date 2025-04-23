---
title: C++でのデータテーブルの配列数式の計算
linktitle: データテーブルの配列式の計算
description: C++でのMicrosoft Excelのデータテーブルの配列数式を計算するためにAspose.Cellsライブラリを使用する方法。既存のExcelファイルを読み込むか、新しいExcelファイルを作成して、Aspose.Cellsが提供するメソッドを使用してデータテーブルの配列数式を計算し、結果を取得します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、データテーブル、配列数式、計算、C++
type: docs
weight: 70
url: /ja/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft Excelでデータテーブルを作成するには、データ > 何れかの分析 > データテーブル... を使用します。 Aspose.Cellsでは今、データテーブルの配列式を計算することができます。任意のタイプの数式を計算するために通常通り [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) を使用してください。

{{% /alert %}}

次のサンプルコードでは、[元のExcelファイル](5115535.xlsx) を使用しました。セルB1の値を100に変更すると、黄色で塗られたデータテーブルの値が120になる様子が次の画像で示されます。サンプルコードは、[出力PDF](5115538.pdf) を生成します。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下は[元のExcelファイル](5115535.xlsx) から[出力PDF](5115538.pdf) を生成するために使用されたサンプルコードです。詳細についてはコメントをお読みください。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
