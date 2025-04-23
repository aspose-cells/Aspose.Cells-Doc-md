---
title: C++ ile Cell.FormulaLocal ı Excel VBA Range.FormulaLocal a benzer şekilde uygula
linktitle: Cell.FormulaLocal ı uygula
type: docs
weight: 30
url: /tr/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aspose.Cells kullanarak C++ ile Excel VBA Range.FormulaLocal a benzer şekilde Cell.FormulaLocal ı nasıl uygulayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel Formülleri farklı yerel ayarlar, bölgeler veya dillerde farklı adlara sahip olabilir. Örneğin, **SUM** fonksiyonu Almanca'da **SUMME** olarak adlandırılır. Aspose.Cells, diğer dillerdeki fonksiyon adlarıyla çalışamaz. Microsoft Excel VBA'da, dil veya bölgeye göre işlevin adını döndüren **Range.FormulaLocal** özelliği bulunmaktadır. Aspose.Cells aynı amaç için [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) özelliğini sağlar. Ancak bu özellik, sadece [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) metodunu uyguladığınızda çalışacaktır.

## **Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal'ı uygulamanın nasıl olduğunu aşağıdaki örnek kod açıklar. Metod, standart fonksiyonun yerel adını döndürür. Standart fonksiyon adı **SUM** ise **UserFormulaLocal_SUM** döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz, örneğin **SUM** Almanca'da **SUMME** ve Rusça'da **TEXT** için **ТЕКСТ** olur. Lütfen aşağıdaki örnek kodun konsol çıktısını inceleyin.**

Aşağıdaki örnek kod, [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) yöntemini uygulamanın nasıl yapıldığını açıklar. Bu yöntem, standart işlevin yerel adını döndürür. Standart işlev adı **SUM** ise **UserFormulaLocal_SUM**'ı döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel işlev adlarını döndürebilirsiniz. Örneğin; **SUM** Almanca'da **SUMME** ve **TEXT** Rusça'da **ТЕКСТ** tarafından değiştirilir. Ayrıca aşağıdaki örneğin konsol çıktısını referans için aşağıdaki örnek kodu görün.

## **Örnek Kod**

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

## **Konsol Çıktısı**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
