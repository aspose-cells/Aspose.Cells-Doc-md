---
title: Возврат диапазона значений с помощью AbstractCalculationEngine на C++
linktitle: Возвращение Диапазона Значений с Использованием AbstractCalculationEngine
description: Эта статья представляет абстрактный движок расчетов, который возвращает диапазон значений в Microsoft Excel с помощью Aspose.Cells и C++. Загружая существующий файл Excel или создавая новый, мы можем использовать методы Aspose.Cells для получения диапазона значений и возврата результата. В конце сохраняем изменённый файл Excel.
keywords: Aspose.Cells, Excel, абстрактный расчетный движок, возвращающий серию значений
type: docs
weight: 55
url: /ru/cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет класс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/), который используется для реализации определяемых пользователем или пользовательских функций, которые не поддерживаются Microsoft Excel в качестве встроенных функций.

В данной статье будет объяснено, как вернуть диапазон значений из [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

{{% /alert %}}

Следующий код демонстрирует использование класса [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) и возвращает диапазон значений через его метод.

Создайте класс с функцией `CalculateCustomFunction`. Этот класс реализует [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

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

Теперь используйте вышеуказанную функцию в вашей программе.

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
{{< app/cells/assistant language="cpp" >}}
