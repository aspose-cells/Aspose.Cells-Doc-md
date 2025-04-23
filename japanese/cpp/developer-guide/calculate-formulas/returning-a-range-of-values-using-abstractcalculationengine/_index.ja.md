---
title: AbstractCalculationEngineを使用した値の範囲の返却（C++）
linktitle: AbstractCalculationEngineを使用して値の範囲を返す
description: この記事では、C++とAspose.Cellsライブラリを使用してMicrosoft Excelで値の範囲を返す抽象計算エンジンを紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成し、Aspose.Cellsのメソッドを使用して範囲の値を取得し、結果を返します。最後に、変更されたExcelファイルを保存します。
keywords: Aspose.Cells、Excel、値の範囲を返す抽象計算エンジン
type: docs
weight: 55
url: /ja/cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excelの組み込み関数としてサポートされていないユーザー定義またはカスタム関数を実装するために使用される[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)クラスを提供します。

この記事では、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)から値の範囲を返す方法について説明します。

{{% /alert %}}

以下のコードは、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)クラスの使用例を示し、そのメソッドを通じて値の範囲を返します。

`CalculateCustomFunction`という関数を持つクラスを作成します。このクラスは[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)を実装しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomFunctionStaticValue : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
		Vector<Object> row1{Object(Date{2015, 6, 12, 10, 6, 30}) ,Object(2)};
        Vector<Object> row2{ Object(3.0) ,Object(U16String(u"Test")) };

        Vector<Vector<Object>> values{ row1 , row2 };

        // Create Object with the 2D Vector and set as calculated value
        Object calculatedValue(values);

        // Set the calculated value in the CalculationData object
        data.SetCalculatedValue(calculatedValue);
    }
};

```

次に、プログラムで上記の関数を使用します。

```c++
int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    Cell cell = cells.Get(0, 0);
    cell.SetArrayFormula(u"=MYFUNC()", 2, 2);

    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    CalculationOptions calculationOptions;

    // Create and set custom engine with proper memory management
    std::shared_ptr<CustomFunctionStaticValue> customEngine = 
        std::make_shared<CustomFunctionStaticValue>();
    calculationOptions.SetCustomEngine(customEngine.get());

    workbook.CalculateFormula(calculationOptions);

    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);
    workbook.Save(outDir + u"output_out.xlsx");
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
