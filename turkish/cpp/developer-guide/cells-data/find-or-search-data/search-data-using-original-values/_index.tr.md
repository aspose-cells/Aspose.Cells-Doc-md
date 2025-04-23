---
title: Orijinal Değerler Kullanarak Veri Arama (C++)
linktitle: Orijinal Değerler Kullanarak Veri Arama
type: docs
weight: 380
url: /tr/cpp/search-data-using-original-values/
description: Aspose.Cells for C++ API’sini kullanarak orijinal değerlerle Veri aramayı nasıl yapacağınızı öğrenin.
keywords: Orijinal Değerleri Kullanarak Veri Arama, Orijinal Değerleri Kullanarak Veri Bulma, Orijinal Değerlerle Veri Arama, Orijinal Değerlerle Veri Bulma
---

{{% alert color="primary" %}}

Bazen verinin değeri bazı şekilde biçimlendirildiği için gizlidir. Örneğin, D4 hücresinin değeri =Sum(A1:A2) ve değeri 20'dir ancak --- olarak biçimlendirilmiştir, bu nedenle 20 değeri gizlidir ve Microsoft Excel bulma seçenekleri kullanılarak bulunamaz. Bununla birlikte, Aspose.Cells kullanarak [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/) kullanarak bulunabilir.

{{% /alert %}}

Aşağıdaki örnek kod yukarıdaki noktayı açıklar. Microsoft Excel bulma seçenekleri kullanılarak bulunamayan D4 hücresini [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/) kullanarak bulur ancak Aspose.Cells kullanarak bulabilir. Daha fazla bilgi için kod içindeki yorumları okuyun.

## Orijinal değerleri kullanarak veri arama C++ kodu

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add 10 in cell A1 and A2
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(10);

    // Add Sum formula in cell D4 but customize it as ---
    Cell cell = worksheet.GetCells().Get(u"D4");

    Style style = cell.GetStyle();
    style.SetCustom(u"---", true);
    cell.SetStyle(style);

    // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
    cell.SetFormula(u"=Sum(A1:A2)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
    FindOptions options;
    options.SetLookInType(LookInType::OriginalValues);
    options.SetLookAtType(LookAtType::EntireContent);

    Cell foundCell;
    int32_t obj = 20;

    // Find 20 which is Sum(A1:A2) and formatted as ---
    foundCell = worksheet.GetCells().Find(obj, foundCell, options);

    // Print the found cell
    std::cout << foundCell.ToString().ToUtf8() << std::endl;

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
