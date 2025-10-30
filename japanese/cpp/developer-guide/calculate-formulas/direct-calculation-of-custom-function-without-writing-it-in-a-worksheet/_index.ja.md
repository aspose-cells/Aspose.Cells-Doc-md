---
title: ワークシートに書き込まずにカスタム関数を直接計算するC++による方法
linktitle: カスタム関数の直接計算
description: Microsoft Excelでワークシートに関数を記述せずにカスタム関数を直接計算するためにAspose.Cellsライブラリを使用する方法について紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成することで、Aspose.Cellsが提供するメソッドを使用してカスタム関数を計算し、結果を取得し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, カスタム関数、直接計算、ワークシートに記述不要
type: docs
weight: 90
url: /ja/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **ワークシートに書き込まずにカスタム関数を直接計算**

このトピックでは、ワークシートに書き込むことなく直接カスタム関数を計算する方法を説明します。これには、[**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)メソッドを使用してください。

このメソッドの使用例を示すサンプルコードをご覧ください。MyCompany::CustomFunction()というカスタム関数を使用し、その値を自分で "Aspose.Cells." と計算し、その後、この値が自動的にセルA1の値"Welcome to "と連結され、最終的な計算値は"Welcome to Aspose.Cells."となります。コードでも分かるように、私たちはカスタム関数をどこにも書いておらず、独自のロジックで直接計算しています。

### **プログラミングサンプル**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class ICustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        // Check the formula name and calculate it yourself
        if (data.GetFunctionName() == u"MyCompany.CustomFunction")
        {
            // This is our calculated value
            data.SetCalculatedValue(Aspose::Cells::Object(u"Aspose.Cells."));
        }
    }
};

class ImplementDirectCalculationOfCustomFunction
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        // Create a workbook
        Workbook wb;

        // Access first worksheet
        Worksheet ws = wb.GetWorksheets().Get(0);

        // Add some text in cell A1
        ws.GetCells().Get(u"A1").PutValue(u"Welcome to ");

        // Create a calculation options with custom engine
        CalculationOptions opts;
        opts.SetCustomEngine(new ICustomEngine());

        // This line shows how you can call your own custom function without
        // a need to write it in any worksheet cell
        // After the execution of this line, it will return
        // Welcome to Aspose.Cells.
        Aspose::Cells::Object ret = ws.CalculateFormula(u"=A1 & MyCompany.CustomFunction()", opts);

        // Print the calculated value on Console
        std::cout << "Calculated Value: " << ret.ToString().ToUtf8() << std::endl;

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementDirectCalculationOfCustomFunction::Run();
    return 0;
}
```

### **コンソール出力**

上記のサンプルコードのコンソール出力は以下の通りです。

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **関連記事**

{{% alert color="primary" %}}

[Aspose.Cellsの既定の計算エンジンを拡張するカスタム計算エンジンを実装する](/cells/ja/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
