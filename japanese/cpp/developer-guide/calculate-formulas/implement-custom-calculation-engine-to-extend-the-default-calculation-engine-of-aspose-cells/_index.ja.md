---
title: C++を使ったAspose.Cellsの既定の計算エンジンを拡張するカスタム計算エンジンの実装
linktitle: カスタム計算エンジンの実装
description: このタイトルは、Aspose.Cellsライブラリを使用し、C++でカスタム計算エンジンを実装して既定の計算エンジンを拡張する方法を説明します。既存のExcelファイルを読み込むか、新しいファイルを作成し、Aspose.Cellsのメソッドを利用してカスタム計算エンジンを実装し、その結果を取得します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、カスタム計算エンジン、既定の計算エンジンを拡張、C++
type: docs
weight: 80
url: /ja/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **カスタム計算エンジンの実装**

Aspose.CellsにはほとんどすべてのMicrosoft Excel式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することが可能であり、より大きな力と柔軟性を提供します。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

以下のコードは、カスタム計算エンジンを実装しています。そのエンジンは[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)インターフェースを実装しており、[**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/)メソッドを持っています。このメソッドはすべての数式に対して呼び出されます。このメソッド内で、**TODAY**関数をキャプチャし、システムの日付に1日を追加します。したがって、現在の日付が2023年07月27日である場合、カスタムエンジンはTODAY()を2023年07月28日として計算します。

### **プログラミングサンプル**

```c++
#include <iostream>
#include <cwctype>
#include "Aspose.Cells.h"
#include <chrono>

using namespace Aspose::Cells;

class CustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        U16String funcName = data.GetFunctionName();
        std::u16string upperName;
        for (int i = 0; i < funcName.GetLength(); ++i)
        {
            upperName.push_back(std::towupper(funcName[i]));
        }
		if (upperName == u"TODAY")
		{
			auto now = std::chrono::system_clock::now();
			std::time_t now_time = std::chrono::system_clock::to_time_t(now);
			std::tm local_tm;

#ifdef _WIN32
			localtime_s(&local_tm, &now_time);
#else
			localtime_r(&now_time, &local_tm);
#endif

            Date today{ local_tm.tm_year + 1900, local_tm.tm_mon + 1, local_tm.tm_mday };
			data.SetCalculatedValue(Date{ today.year, today.month, today.day + 1 });
		}
    }

    bool GetProcessBuiltInFunctions() override { return true; }
};

class ImplementCustomCalculationEngine
{
public:
    static void Run()
    {
        Workbook workbook;
        Worksheet sheet = workbook.GetWorksheets().Get(0);
        Cell a1 = sheet.GetCells().Get(u"A1");
        Style style = a1.GetStyle();
        style.SetNumber(14);
        a1.SetStyle(style);
        a1.SetFormula(u"=TODAY()");
        workbook.CalculateFormula();
        std::cout << "The value of A1 with default calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        CustomEngine engine;
        CalculationOptions opts;
        opts.SetCustomEngine(&engine);
        workbook.CalculateFormula(opts);
        std::cout << "The value of A1 with custom calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
    }
};

int main()
{
    Aspose::Cells::Startup();
    ImplementCustomCalculationEngine::Run();
    Aspose::Cells::Cleanup();
    return 0;
}

```

### **結果**

上記のサンプルコードのコンソール出力を確認してください。カスタムエンジンを使用した場合、A1の値（日時）はカスタムエンジンを使用しなかった場合の結果よりも1日後になるはずです。

### **関連記事**

{{% alert color="primary" %}}

[ワークシートに書き込まずにカスタム関数を直接計算する](/cells/ja/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
