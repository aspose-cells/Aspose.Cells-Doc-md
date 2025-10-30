---  
title: C++ ile Grafik Etiketlerini Metne Sığdırmak İçin Yeniden Boyutlandırma  
description: Aspose.Cells for C++ kullanarak grafikteki veri etiketi şeklinin boyutunu, metni sığdıracak şekilde nasıl yeniden boyutlandıracağınızı öğrenin. Kılavuzumuz, etiket kutusunun boyutunu ve şeklini ayarlayarak metnin doğru şekilde gösterilmesini sağlayacak.  
keywords: Aspose.Cells for C++, grafik çizimi, veri etiketleri, şekil yeniden boyutlandırma, metni sığdırma, kırpma, çakışma.  
type: docs  
weight: 220  
url: /tr/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

Excel uygulaması, grafiklerin Veri Etiketleri için **Metni Sığdırmak İçin Şekli Yeniden Boyutlandır** seçeneğini sağlar.  

{{% /alert %}}  

## **Microsoft Excel'de Metni Sığdırmak İçin Grafiğin Veri Etiket Şeklini Yeniden Boyutlandırma**  

Bu seçenek, grafikte herhangi bir veri etiketini seçerek Excel arayüzünden erişilebilir. Sağ tık yapın ve **Veri Etiketlerini Biçimlendir** menüsünü seçin. **Boyut ve Özellikler** sekmesi altında, **Hizalama** genişletildiğinde, ilgili özellikleri ve **Metni Düzeltmek İçin Şekli Yeniden Boyutlandır** seçeneğini göreceksiniz.  

## **Aspose.Cells for C++ kullanarak Grafik’in Veri Etiketi Şeklinin Metne Uygun Boyutlara Getirilmesi nasıl yapılır.**  

Excel'in veri etiketi şekillerini metne göre yeniden boyutlandırma özelliğini taklit etmek için, Aspose.Cells API'leri Boolean türü [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext) özelliğini ortaya çıkardı. Aşağıdaki kod parçası, [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext) özelliğinin basit kullanım senaryosunu göstermektedir.  

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Create an instance of Workbook containing the Chart
    Workbook book(inputFilePath);

    // Access the Worksheet that contains the Chart
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Iterate through each Chart in the Worksheet
    for (int32_t i = 0; i < sheet.GetCharts().GetCount(); i++)
    {
        Chart chart = sheet.GetCharts().Get(i);

        // Iterate through each NSeries in the Chart
        for (int32_t index = 0; index < chart.GetNSeries().GetCount(); index++)
        {
            // Access the DataLabels of indexed NSeries
            DataLabels labels = chart.GetNSeries().Get(index).GetDataLabels();

            // Set ResizeShapeToFitText property to true
            labels.SetIsResizeShapeToFitText(true);
        }

        // Calculate Chart
        chart.Calculate();
    }

    // Save the result
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    book.Save(outputFilePath);

    std::cout << "Chart calculations and modifications completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

{{< app/cells/assistant language="cpp" >}}
