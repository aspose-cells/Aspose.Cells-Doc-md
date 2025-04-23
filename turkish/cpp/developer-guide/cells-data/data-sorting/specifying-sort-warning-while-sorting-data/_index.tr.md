---
title: C++ kullanarak Sıralama Sırasında Sıralama Uyarısı Belirtme
linktitle: Veri Sıralaması Yaparken Özel Sıralama Uyarısını Belirtme
type: docs
weight: 140
url: /tr/cpp/specifying-sort-warning-while-sorting-data/
description: Aspose.Cells for C++ API’sini kullanarak veriyi sıralarken sıralama uyarısını nasıl belirteceğinizi öğrenin.
keywords: Veri sıralama işlemi yaparken sıralama uyarısı eklemek, veri sıralama sırasında sıralama uyarısı ayarlamak, veri sıralama sırasında sıralama uyarısı seçmek.
---

## **Olası Kullanım Senaryoları**

Lütfen {11, 111, 22} gibi bu metinsel verileri düşünün. Bu metinsel veri, metin olarak sıralandığından 111 22'den önce gelir. Ancak, bu veriyi metin değil, sayı olarak sıralamak istiyorsanız, o zaman bu veri {11, 22, 111} olacak çünkü sayısal olarak 111 22'den sonra gelir. Aspose.Cells, bu sorunu çözmek için {0} özelliğini sağlar. Lütfen bu özelliği **true** olarak ayarlayın ve metinsel verileriniz sayısal veri olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, metinsel veri gibi görünen metinsel verilerin sıralandığında Microsoft Excel tarafından gösterilen sıralama uyarısını göstermektedir.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, daha önce açıklandığı gibi [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/) özelliğinin kullanımını açıklar. Daha fazla yardım için lütfen [örnek Excel dosyasını](43352075.xlsx) ve [çıktı Excel dosyasını](43352076.xlsx) kontrol edin.

```c++
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

    // Create workbook
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
