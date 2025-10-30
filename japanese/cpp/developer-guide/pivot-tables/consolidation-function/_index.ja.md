---
title: C++を使用した集計機能
linktitle: 統合機能
type: docs
weight: 20
url: /ja/cpp/consolidation-function/
description: Aspose.Cellsを使ってピボットテーブルのデータフィールドにConsolidationFunctionを適用する方法を学びます。
---

## **統合機能**

Aspose.Cellsを使用して、ピボットテーブルのデータフィールド（または値フィールド）に統合機能を適用できます。Microsoft Excelにおいては、値フィールドを右クリックし、 **「値フィールドの設定...」** を選択し、その後 **「値の集計方法」** タブを選択します。そこから、合計、カウント、平均、最大値、最小値、積、重複排除のような任意の統合機能を選択できます。

Aspose.Cellsは、次の統合機能をサポートするための[**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/)列挙型を提供します。

- ConsolidationFunction::平均
- ConsolidationFunction::カウント
- ConsolidationFunction::数値のカウント
- ConsolidationFunction::異なる値のカウント
- ConsolidationFunction::最大値
- ConsolidationFunction::最小値
- ConsolidationFunction::積
- ConsolidationFunction::標準偏差
- ConsolidationFunction::母標準偏差
- ConsolidationFunction::合計
- ConsolidationFunction::分散
- ConsolidationFunction::母分散

### **ピボットテーブルのデータフィールドに統合機能を適用する**

次のコードは、最初のデータフィールド（または値フィールド）に **平均** の統合機能を適用し、2番目のデータフィールド（または値フィールド）に **重複排除** の統合機能を適用します。

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
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

重複排除の統合機能は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
