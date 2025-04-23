---  
title: Ridimensiona la forma dell etichetta dati del grafico per adattarsi al testo con C++  
description: Scopri come ridimensionare la forma dell etichetta dei dati nel grafico per adattarsi al testo in Aspose.Cells for C++. La nostra guida ti mostrerà come regolare le dimensioni e la forma del contenitore dell etichetta per garantire che il testo venga visualizzato correttamente senza troncature o sovrapposizioni.  
keywords: Aspose.Cells for C++, grafici, etichette dei dati, ridimensionamento della forma, adattamento del testo, troncature, sovrapposizioni.  
type: docs  
weight: 220  
url: /it/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

L'applicazione Excel fornisce l'opzione **Ridimensiona forma per adattare il testo** per le etichette dati del grafico al fine di aumentare le dimensioni della forma in modo che il testo vi entri.  

{{% /alert %}}  

## **Come Ridimensionare la Forma della etichetta dati del grafico per Adattare il Testo in Microsoft Excel**  

Questa opzione può essere accessibile sull'interfaccia Excel selezionando qualsiasi etichetta dei dati sul grafico. Fai clic con il tasto destro e seleziona il menu **Formato etichette dati**. Nella scheda **Dimensione e proprietà**, espandi **Allineamento** per rivelare le proprietà correlate, inclusa l'opzione **Ridimensiona forma per adattare il testo**.  

## **Come ridimensionare la forma dell'etichetta dati del grafico per adattarsi al testo con Aspose.Cells for C++**  

Per imitare la funzione di Excel di ridimensionare le forme delle etichette dei dati per adattarsi al testo, le API Aspose.Cells hanno esposto la proprietà di tipo Boolean [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext). Il seguente esempio di codice mostra uno scenario di utilizzo semplice della proprietà [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext).  

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

