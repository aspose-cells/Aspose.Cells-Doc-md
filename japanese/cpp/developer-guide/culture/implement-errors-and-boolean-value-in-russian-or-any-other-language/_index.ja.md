---
title: ロシア語やその他の言語でエラーやブール値を実装する方法
linktitle: エラーとブール値の実装
type: docs
weight: 40
url: /ja/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aspose.Cellsを使ってロシア語や他の言語でエラーとブール値を実装する方法を学びましょう。
---

## **可能な使用シナリオ**

Microsoft Excelをロシア語ロケールまたは言語やその他のロケール・言語で使用している場合、そのロケールや言語に従ったエラーとブール値が表示されます。Aspose.Cellsの[**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/)プロパティを使うことで、同様の動作を実現できます。これには、[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)クラスの以下のメソッドをオーバーライドする必要があります。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **ロシア語または他の言語でエラーおよび真偽値を実装する**

下記のサンプルコードは、ロシア語または他の言語でのエラーおよび真偽値の実装方法を説明しています。このコードで使用される [サンプルExcelファイル](73990159.xlsx) およびその [出力PDF](73990160.pdf) を確認してください。スクリーンショットは、サンプルExcelファイルと出力PDFの違いを参照用に示しています。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class RussianGlobalization : public GlobalizationSettings
{
public:
    virtual U16String GetErrorValueString(const U16String& err) override
    {
        if (err == u"#NAME?")
        {
            return u"#RussianName-имя?";
        }
        return u"RussianError-ошибка";
    }

    virtual U16String GetBooleanValueString(bool bv) override
    {
        return bv ? u"RussianTrue-правда" : u"RussianFalse-ложный";
    }
};

class ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        Workbook wb(u"sampleRussianGlobalization.xlsx");

        auto russianGlobalization = std::make_shared<RussianGlobalization>();
        wb.GetSettings().SetGlobalizationSettings(russianGlobalization.get());

        wb.CalculateFormula();

        wb.Save(u"outputRussianGlobalization.pdf");

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage::Run();
    return 0;
}
```
