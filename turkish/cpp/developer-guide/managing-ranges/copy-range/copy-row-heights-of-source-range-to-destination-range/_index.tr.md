---
title: Kaynak Aralığının Satır Yüksekliklerini C++ ile Hedef Aralığa Kopyala
linktitle: Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Kopyala
type: docs
weight: 590
url: /tr/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Aspose.Cells for C++ kullanarak kaynak aralıktan hedef aralığa satır yüksekliğini kopyalama yöntemini öğrenin.
---

{{% alert color="primary" %}}

Bazen kullanıcılar, kaynak aralıktaki satır yüksekliklerini hedef aralığa kopyalamak ister. Aspose.Cells, bu amaçla [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) enum'unu sağlar. Eğer [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) özelliğini [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) enum'u ile ayarlarsanız, kaynak aralıktaki tüm satırların yüksekliği hedef aralığa kopyalanır.

{{% /alert %}}

Aşağıdaki örnek kod, [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) enum'unu kullanarak kaynak aralıktaki satır yüksekliklerini hedef aralığa nasıl kopyalayacağını açıklar. Bu kodla üretilen Excel dosyasını Microsoft Excel’de açtığınızda, hedef aralığın satır yüksekliklerinin tam olarak kaynak aralığa eşit olduğunu göreceksiniz.

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

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
