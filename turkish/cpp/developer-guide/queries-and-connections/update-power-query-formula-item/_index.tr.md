---
title: Power Query Formülü Öğesine C++ ile Güncelleme
linktitle: Güç Sorgusu Formül Öğesini Güncelle
type: docs
weight: 120
url: /tr/cpp/update-power-query-formula-item/
description: Power Query Formülü Öğelerini Excel dosyalarında veri kaynağı dosya konumlarını değiştirmek için Aspose.Cells for C++ kullanarak nasıl güncelleyebileceğinizi öğrenin.
---

## **Kullanım Senaryosu**

Veri kaynağı dosyalarının taşındığı durumlar olabilir ve Excel dosyası dosyayı bulamaz. Bu durumda, Aspose.Cells API, [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) sınıfını kullanarak Power Query Formülü öğesini güncelleme seçeneği sunar ve kaynak dosya konumunu günceller.

## **Power Query Formel Öğesi Güncelleme**

Aspose.Cells API, Power Query Formülü Öğelerini güncelleme yeteneği sağlar. Aşağıdaki kod parçası, [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/) özelliğini kullanarak Excel dosyasındaki veri kaynağı dosyasını güncellemeyi gösterir. Kaynak ve çıktı dosyaları referansınız için eklenmiştir.

- [Kaynak Dosya 1](106364953.xlsx)
- [Kaynak Dosya 2](106364954.xlsx)
- [Çıktı Dosyası](106364955.xlsx)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SamplePowerQueryFormula.xlsx");
    DataMashup mashupData = workbook.GetDataMashup();

    PowerQueryFormulaCollection powerQueryFormulas = mashupData.GetPowerQueryFormulas();
    for (int i = 0; i < powerQueryFormulas.GetCount(); ++i)
    {
        PowerQueryFormula formula = powerQueryFormulas.Get(i);
        PowerQueryFormulaItemCollection powerQueryFormulaItems = formula.GetPowerQueryFormulaItems();
        for (int j = 0; j < powerQueryFormulaItems.GetCount(); ++j)
        {
            PowerQueryFormulaItem item = powerQueryFormulaItems.Get(j);
            if (item.GetName() == u"Source")
            {
                U16String newValue = u"Excel.Workbook(File.Contents(\"" + srcDir + u"SamplePowerQueryFormulaSource.xlsx" + u"\"), null, true)";
                item.SetValue(newValue);
            }
        }
    }

    workbook.Save(outDir + u"SamplePowerQueryFormula_out.xlsx");
    std::cout << "PowerQueryFormula updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
