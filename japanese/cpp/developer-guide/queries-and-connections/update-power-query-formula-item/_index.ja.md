---
title: C++を使った Power Query フォーマルアイテムの更新
linktitle: Power Query Formulaアイテムの更新
type: docs
weight: 120
url: /ja/cpp/update-power-query-formula-item/
description: Excelファイル内のデータソースの場所を変更するために、Aspose.Cells for C++を使用して Power Query フォーマルアイテムを更新する方法を学びます。
---

## **使用シナリオ**

データソースファイルが移動され、Excelファイルがファイルを見つけられない場合があります。そのような場合、Aspose.Cells APIは、[*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/)クラスを使ってソースファイルの場所を更新するオプションを提供します。

## **Power Query Formula Itemの更新**

Aspose.Cells API は、Power Query フォーマルアイテムを更新する機能を提供します。以下のコードスニペットは、[**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/) プロパティを使用してExcelファイルのデータソースファイルの場所を更新する例です。ソースファイルと出力ファイルは参考のために添付されています。

- [元のファイル 1](106364953.xlsx)
- [元のファイル 2](106364954.xlsx)
- [出力ファイル](106364955.xlsx)

## **サンプルコード**

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
