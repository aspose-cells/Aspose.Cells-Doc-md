---  
title: Cambiar tamaño de la forma de etiqueta de datos del gráfico para que quepa con C++  
description: Aprende cómo cambiar el tamaño de la forma de la etiqueta de datos en un gráfico para que quepa en Aspose.Cells for C++. Nuestra guía te mostrará cómo ajustar el tamaño y la forma del contenedor de la etiqueta para asegurar que el texto se muestre correctamente sin truncarse ni superponerse.  
keywords: Aspose.Cells for C++, graficación, etiquetas de datos, cambio de tamaño, ajuste de texto, truncamiento, superposición.  
type: docs  
weight: 220  
url: /es/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

La aplicación de Excel proporciona la opción **Redimensionar la forma para que se ajuste al texto** para las Etiquetas de Datos en el Gráfico con el fin de aumentar el tamaño de la forma para que el texto quepa en ella.  

{{% /alert %}}  

## **Cómo Cambiar el Tamaño de la Forma de la Etiqueta de Datos en un Gráfico en Microsoft Excel**  

Esta opción puede accederse en la interfaz de Excel seleccionando alguna de las etiquetas de datos en el gráfico. Haz clic derecho y selecciona el menú **Formato de etiquetas de datos**. En la pestaña **Tamaño y propiedades**, expande **Alineación** para revelar las propiedades relacionadas, incluyendo la opción **Redimensionar forma para ajustar el texto**.  

## **Cómo redimensionar la forma de las etiquetas de datos del gráfico para que se ajusten al texto usando Aspose.Cells for C++**  

Para imitar la función de Excel de redimensionar las formas de etiquetas de datos para que se ajusten al texto, las API de Aspose.Cells han expuesto la propiedad booleana [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext). El siguiente código muestra un escenario de uso simple de la propiedad [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext).  

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

