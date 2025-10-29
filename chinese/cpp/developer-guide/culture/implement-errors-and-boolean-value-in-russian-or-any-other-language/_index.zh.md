---
title: 用C++实现错误和布尔值（俄语或任何其他语言）
linktitle: 实现错误和布尔值
type: docs
weight: 40
url: /zh/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: 学习如何使用 Aspose.Cells 与 C++ 在俄语或其他任何语言中实现错误和布尔值。
---

## **可能的使用场景**

如果你使用的是俄语或其他任何语言的微软Excel，它会根据该语言显示错误和布尔值。你可以在使用 Aspose.Cells 时通过使用 [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) 属性实现类似的行为。你需要重写 [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) 类的以下方法。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **以俄语或其他任何语言实现错误和布尔值**

以下示例代码说明了如何在俄语或其他任何语言中实现错误和布尔值。请查看此代码中使用的[Sample Excel File](73990159.xlsx)及其[Output PDF](73990160.pdf)。屏幕截图显示了示例Excel文件和输出PDF之间的差异作为参考。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **示例代码**

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
{{< app/cells/assistant language="cpp" >}}
