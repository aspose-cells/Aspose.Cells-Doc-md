---
title: AbstractCalculationEngine kullanarak Bir Aralık Değeri Döndürme C++ ile
linktitle: Aspose.Cells kitaplığını kullanarak Microsoft Excel de bir dizi değeri döndüren soyut bir hesaplama motoru tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak bir dizi değeri alabiliriz ve sonucu döndürebiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
description: Bu makale, Aspose.Cells kütüphanesi kullanılarak Microsoft Excel de bir Aralık değeri döndüren soyut bir hesaplama motorunu tanıtmaktadır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak bir aralık değeri alabilir ve sonucu döndürebiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, bir dizi değer döndüren soyut bir hesaplama motoru
type: docs
weight: 55
url: /tr/cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel tarafından desteklenmeyen kullanıcı tanımlı veya özel işlevleri uygulamak için kullanılan [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) sınıfını sağlar.

Bu makale, [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) aralığındaki değerlerin nasıl döndürüleceğini açıklayacaktır.

{{% /alert %}}

Aşağıdaki kod, [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) sınıfının kullanımını gösterir ve yöntemi aracılığıyla değer aralığını döndürür.

`CalculateCustomFunction` işlevine sahip bir sınıf oluşturun. Bu sınıf [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) uygulamasını gerçekleştirir.

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

Şimdi yukarıdaki fonksiyonu programınızda kullanın.

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
