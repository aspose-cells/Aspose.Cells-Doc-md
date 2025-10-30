---
title: C++ ile Veri Sıralama
linktitle: Veri Sıralama
type: docs
weight: 130
url: /tr/cpp/sort-data-of-excel/
description: Aspose.Cells for C++ API kullanarak veriyi nasıl sıralayacağınızı öğrenin.
keywords: Verileri artan veya azalan sırada, arka plan rengine göre sıralama
---

{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in birçok kullanışlı özelliklerinden biridir. Kullanıcılara verileri taramayı kolaylaştırmak için sıralama imkanı sağlar. Aspose.Cells, geliştiricilere çalışma sayfası verilerini alfabetik veya sayısal olarak sıralama imkanı sunar, bu da Microsoft Excel'in verileri nasıl sıraladığına benzer şekilde çalışır.

{{% /alert %}}

## **Microsoft Excel'de Veri Sıralama**

Microsoft Excel'de veri sıralamak için:

1. **Veri**'yi **Sırala** menüsünden seçin. Sırala iletişim kutusu görüntülenecektir.
1. Sıralama seçeneğini seçin.

Genellikle, sıralama bir liste üzerinde yapılır - verilerin sütunlarda gösterildiği, verilerin bağlantılı bir grup olduğu.

## **Aspose.Cells ile Veri Sıralama**

Aspose.Cells, verileri artan veya azalan sırada sıralamak için kullanılan [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/) sınıfını sağlar. Sınıf, örneğin Key1 ... Key3 ve Order1 ... Order3 gibi önemli üyelere sahiptir. Bu üyeler sıralı anahtarları tanımlamak ve anahtar sıralama sırasını belirlemek için kullanılır.

Veri sıralaması gerçekleştirmeden önce anahtarları tanımlamalı ve sıralama düzenini belirlemelisiniz. Sınıf, çalışsayadaki hücre verilerine dayalı veri sıralamasını gerçekleştirmek için kullanılan [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) yöntemini sağlar.

[**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) yöntemi aşağıdaki parametreleri kabul eder:

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), altındaki çalışsayadaki hücreler.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), hücre aralığı. Veri sıralaması uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Microsoft Excel'de oluşturulmuş "Book1.xls" şablon dosyasını kullanır. Aşağıdaki kodu çalıştırdıktan sonra, veri uygun bir şekilde sıralanır.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

*Soldan Sağa* sıralamak istiyorsanız, [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/) özniteliğini kullanın.

{{% /alert %}}

### **Arka plan rengine göre veri sıralama**

Excel, arka plan rengine göre verileri sıralama özelliği sunar. Aynı özellik, Aspose.Cells kullanılarak DataSorter kullanılarak sağlanır, burada [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor, arka plan rengine göre verilere sıralama yapmak için [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) içinde kullanılabilir. Belirtilen renkteki tüm hücreler, [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), işlevinde belirtilen sırada yerleştirilir ve geri kalan hücrelerin sırası hiç değişmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Özel Sıralama Listesi ile Sütunda Verileri Sıralama](/cells/tr/cpp/sort-data-in-column-with-custom-sort-list/)
- [Veri Sıralama Sırasında Uyarıyı Belirtme](/cells/tr/cpp/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="cpp" >}}
