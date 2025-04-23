---  
title: Ändra storlek på diagrammets datamärkesform för att passa texten med C++  
description: Lär dig hur du ändrar storleken på datamärkets form i ett diagram för att passa texten i Aspose.Cells for C++. Vår guide visar hur du justerar storlek och form på etikettbehållaren för att säkerställa att texten visas korrekt utan avklippning eller överlappning.  
keywords: Aspose.Cells for C++, diagram, datamärken, formändring, texts fit, avklippning, överlappning.  
type: docs  
weight: 220  
url: /sv/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

Excel-programmet tillhandahåller alternativet **Ändra form för att passa text** för diagrammets datamärken för att öka storleken på formen så att texten passar inuti den.  

{{% /alert %}}  

## **Hur man ändrar diagrammets mikroform för att passa texten i Microsoft Excel**  

Detta alternativ kan nås via Excel-gränssnittet genom att välja någon av datalabels på diagrammet. Högerklicka och välj menyn **Format Data Labels**. Under fliken **Storlek & Egenskaper** expanderar du **Anpassning** för att visa relaterade egenskaper inklusive **Ändra storlek på formen för att fixa texten**.  

## **Hur man ändrar storlek på diagrammets datapunktetiketter för att passa text med Aspose.Cells for C++**  

För att efterlikna Excels funktion för att ändra storlek på datalabelsformer för att passa texten har Aspose.Cells API:erna exponerat den booleska egenskapen [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext). Följande kod visar ett enkelt exempel på hur du använder egenskapen [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext).  

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

