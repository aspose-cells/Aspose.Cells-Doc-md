---
title: Tick Etiket Yönünü C++ ile Değiştir
linktitle: Tick Etiketi Yönünü Değiştirme
description: Aspose.Cells for C++ teki tik etiketi yönünü nasıl değiştireceğinizi öğrenin. Rehberimiz, eksenlerde yatay, dikey ve açılandırılmış yönler de dahil olmak üzere tik etiketi yönünü ayarlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for C++, tik etiketi, yön, orientasyon, eksenler, yatay, dikey, açılandırılmış.
type: docs
weight: 170
url: /tr/cpp/change-tick-label-direction/
---

## **Tick Etiketi Yönünü Değiştirme**

Aspose.Cells, diyagram tik etiketi yönünü [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) özelliği kullanarak değiştirme imkanı sağlar. [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) özelliği, [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) enumeration değerini kabul eder. [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) enumeration aşağıdaki üyeleri sağlar:

- Yatay
- Dikey
- 90 Derece Döndür
- 270 Derece Döndür
- Yığınlanmış

Aşağıdaki resim kaynak ve çıktı dosyalarını karşılaştırmaktadır:

### **Kaynak dosya görüntüsü**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Çıktı dosyası görüntüsü**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Aşağıdaki kod parçacığı, işaret etiket yönünü Rotate90'dan Yatay'a değiştirir.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Kaynak ve çıktı dosyaları aşağıdaki linklerden indirilebilir.

[Kaynak Dosya](105480221.xlsx)

[Çıktı Dosyası](105480223.xlsx)
