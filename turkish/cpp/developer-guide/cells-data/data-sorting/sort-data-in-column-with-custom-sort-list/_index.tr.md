---
title: C++ ile Özel Sıralama Listesi ile Sütundaki Veriyi Sırala
linktitle: Özel Sıralama Listesi ile Sütunda Verileri Sıralama
type: docs
weight: 290
url: /tr/cpp/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for C++ API’sini kullanarak özel liste ile sütundaki veriyi nasıl sıralayacağınızı öğrenin.
keywords: Özel Sıralama Listesi ile Sütunda Veri Sıralama, Özel liste ile veri sırala.
---

## **Olası Kullanım Senaryoları**

Sütundaki veriyi özel bir liste kullanarak sıralayabilirsiniz. Bu [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) yöntemiyle yapılabilir. Ancak, bu yöntem yalnızca özel listedeki öğelerde virgül yoksa çalışır. Eğer "USA,US", "Çin,CN" gibi virgüller içeriyorsa, o zaman [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) yöntemini kullanmanız gerekir. Burada, son parametre String değil, bir String Dizisidir.

## **Özel Sıralama Listesi ile Sütunda Verileri Sıralama**

Aşağıdaki örnek kod, [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) yöntemini kullanarak özel sıralama listesi ile veriyi nasıl sıralayacağınızı gösterir. Bu kodda kullanılan [örnek Excel dosyasını](50528327.xlsx) ve bunun tarafından oluşturulan [çıkış Excel dosyasını](50528328.xlsx) inceleyin. Aşağıdaki ekran görüntüsü, kodun çalışma anında örnek Excel dosyasına olan etkisini gösterir.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Örnek Kod**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
