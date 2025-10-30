---
title: C++ kullanarak Veri Aralığını ve Dilimleyici Grubu Konumunu Belirterek Sparkline Kopyalama
linktitle: Veri Aralığını ve Konumu Belirterek Sparkline Kopyalama
type: docs
weight: 300
url: /tr/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Aspose.Cells for C++ kullanarak veri aralığını ve konumu belirterek sparklines nasıl kopyalanır öğrenin.
---

{{% alert color="primary" %}}

Microsoft Excel, bir sparkline grubunun veri aralığını ve konumunu belirterek bir sparkline kopyalamanıza izin verir. Aspose.Cells, bu özelliği destekler.

{{% /alert %}}

Microsoft Excel'de sparkline kopyalamak için:

1. Sparkline içeren hücreyi seçin.
1. **Tasarım** sekmesinin **Sparkline** bölümünden **Veri Düzenle**'yi seçin.
1. **Grup Konumunu ve Veriyi Düzenle**'yi seçin.
1. Veri aralığını ve konumu belirtin.
1. **Tamam**'a tıklayın.

Aspose.Cells, sparkline grubunun veri aralığını ve konumunu belirlemek için `SparklineCollection.Add(dataRange, row, column)` metodunu sağlar. Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ilk sparkline grubuna erişir ve ona veri aralıklarını ve konumlarını ekler. Sonunda, çıktıyı diske kaydeder ve bu da yukarıdaki ekran görüntüsünde gösterilmiştir.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
