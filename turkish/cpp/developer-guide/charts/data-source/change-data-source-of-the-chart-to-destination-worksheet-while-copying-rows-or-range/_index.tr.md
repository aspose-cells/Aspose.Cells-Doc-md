---  
title: Grafiğin Veri Kaynağını Hedef Çalışma Sayfası Olarak Değiştirme ve Satır veya Aralık Kopyalama ile C++ Kullanma  
description: Aspose.Cells for C++ te, satırları veya aralığı kopyalarken grafiğin veri kaynağını hedef çalışma sayfasına nasıl değiştireceğinizi öğrenin. Kılavuzumuz, grafiğin veri aralığını güncelleme ve hedef çalışma sayfasına bağlama adımlarını gösterecek, böylece kopyalanan satır veya aralıklar grafikte doğru şekilde yansıtılır.  
keywords: Aspose.Cells for C++, grafik çizimi, veri kaynağı, hedef çalışma sayfası, satırlar, aralık, kopyalama, güncelleme, veri aralığı, bağlantı.  
type: docs  
weight: 440  
url: /tr/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Olası Kullanım Senaryoları**

Grafiklerin veri kaynağı, satır veya aralıkları yeni bir çalışma sayfasına kopyaladığınızda değişmez. Örneğin, grafik veri kaynağı =Sheet1!$A$1:$B$4 ise, satırlar veya aralıklar yeni bir çalışma sayfasına kopyalandığında veri kaynağı aynı kalır yani =Sheet1!$A$1:$B$4 olur. Bu, Microsoft Excel'de de aynı davranıştır. Ancak, yeni hedef çalışma sayfasını göstermek istiyorsanız, [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) özelliğini kullanın ve [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/) metodunu çağırırken **true** olarak ayarlayın. Hedef çalışma sayfanız DestSheet ise, grafiğin veri kaynağı =Sheet1!$A$1:$B$4'ten =DestSheet!$A$1:$B$4' e değişecektir.

## **Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**

Aşağıdaki örnek kod, grafik içeren satır veya aralıkları yeni bir çalışma sayfasına kopyalarken [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) özelliğinin kullanımını açıklamaktadır. Kod, [örnek excel dosyasını](5113699.xlsx) kullanmakta ve [çıktı excel dosyasını](5113697.xlsx) üretmektedir.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
