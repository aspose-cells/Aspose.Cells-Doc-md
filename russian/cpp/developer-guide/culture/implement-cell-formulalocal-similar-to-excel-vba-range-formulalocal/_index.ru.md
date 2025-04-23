---
title: Реализация Cell.FormulaLocal, аналогичного Excel VBA Range.FormulaLocal, с помощью C++
linktitle: Реализовать Cell.FormulaLocal
type: docs
weight: 30
url: /ru/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Узнайте, как реализовать Cell.FormulaLocal, аналогичный Excel VBA Range.FormulaLocal, с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Формулы Microsoft Excel могут иметь разные названия в различных локалях, регионах или языках. Например, функция **SUM** называется **SUMME** на немецком. Aspose.Cells не может работать с именами функций на не-английском языке. В Microsoft Excel VBA есть свойство **Range.FormulaLocal**, которое возвращает название функции в соответствии с его языком или регионом. Aspose.Cells также предоставляет свойство [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) для этой цели. Однако это свойство будет работать только при реализации метода [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/).

## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**

Приведенный ниже образец кода объясняет, как реализовать метод [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/). Метод возвращает локальное название стандартной функции. Если стандартное название функции **SUM**, он возвращает **UserFormulaLocal_SUM**. Вы можете изменить код в соответствии с вашими потребностями и вернуть правильные локальные названия функций, например **SUM** - **SUMME** на немецком, а **TEXT** - **ТЕКСТ** на русском. Также ознакомьтесь с выводом консоли приведенного ниже образца кода для справки.

## **Образец кода**

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

## **Вывод в консоль**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
