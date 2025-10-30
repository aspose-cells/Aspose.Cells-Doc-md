---
title: Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalをC++で実装する方法
linktitle: Cell.FormulaLocalの実装
type: docs
weight: 30
url: /ja/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aspose.Cellsを使用してExcel VBAのRange.FormulaLocalに似たCell.FormulaLocalを実装する方法を学びましょう。
---

## **可能な使用シナリオ**

Microsoft Excelの関数は、異なる地域や言語で異なるロケール名を持つ場合があります。例えば、**SUM**関数はドイツ語では**SUMME**と呼ばれます。Aspose.Cellsでは、非英語の関数名は使用できません。Microsoft Excel VBAには、関数の名前をその言語や地域に合わせて返す**Range.FormulaLocal**プロパティがあります。Aspose.Cellsもこの目的のために[**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/)プロパティを提供しています。ただし、このプロパティは[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/)メソッドを実装している場合にのみ機能します。

## **Excel VBAのRange.FormulaLocalと同様にCell.FormulaLocalを実装する**

以下のサンプルコードは、[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/)メソッドの実装方法を説明しています。このメソッドは、標準関数のローカル名を返します。標準関数名が **SUM** の場合、**UserFormulaLocal_SUM** を返します。**SUM** はドイツ語では **SUMME** 、ロシア語では **ТЕКСТ** となります。必要に応じてコードを変更し、正しいローカル関数名を返してください。また、下記のサンプルコードのコンソール出力も参照してください。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

// Implement GlobalizationSettings class
class GS : public GlobalizationSettings
{
public:
    virtual U16String GetLocalFunctionName(const U16String& standardName) override
    {
        // Change the SUM function name as per your needs.
        if (standardName == u"SUM")
        {
            return u"UserFormulaLocal_SUM";
        }

        // Change the AVERAGE function name as per your needs.
        if (standardName == u"AVERAGE")
        {
            return u"UserFormulaLocal_AVERAGE";
        }

        return u"";
    }
};

void Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal()
{
    // Create workbook
    Workbook wb;

    // Assign GlobalizationSettings implementation class
    wb.GetSettings().SetGlobalizationSettings(new GS());

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access some cell
    Cell cell = ws.GetCells().Get(u"C4");

    // Assign SUM formula and print its FormulaLocal
    cell.SetFormula(u"SUM(A1:A2)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;

    // Assign AVERAGE formula and print its FormulaLocal
    cell.SetFormula(u"=AVERAGE(B1:B2, B5)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
