---  
title: Изменение размера фигуры метки данных графика для соответствия текста с помощью C++  
description: Узнайте, как изменить размер фигуры метки данных в графике, чтобы она соответствовала тексту в Aspose.Cells for C++. Наше руководство покажет, как настроить размеры и форму контейнера метки, чтобы текст отображался правильно без обрезки или перекрытия.  
keywords: Aspose.Cells for C++, построение графиков, метки данных, изменение формы, встройка текста, обрезка, перекрытие.  
type: docs  
weight: 220  
url: /ru/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

Приложение Excel предлагает опцию **Изменить форму для подгонки текста** для подписей данных диаграммы, чтобы увеличить размер формы так, чтобы текст помещался внутри нее  

{{% /alert %}}  

## **Как изменить форму подписей данных в диаграмме, чтобы они соответствовали тексту в Microsoft Excel**  

Этот параметр можно получить в интерфейсе Excel, выбрав любую метку данных на диаграмме. Щелкните правой кнопкой мыши и выберите меню **Формат меток данных**. На вкладке **Размер и свойства** разверните раздел **Выравнивание**, чтобы открыть связанные свойства, включая опцию **Изменить форму для фиксации текста**.  

## **Как изменить размер формы метки данных графика, чтобы она соответствовала тексту, используя Aspose.Cells for C++**  

Чтобы имитировать функцию Excel по изменению размера форм меток данных для соответствия текста, API Aspose.Cells предоставил булевое свойство [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext). В следующем примере показано простое использование сценария свойства [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext).  

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
