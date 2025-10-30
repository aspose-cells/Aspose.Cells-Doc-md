---  
title: Diagrammdatenbeschriftungsform anpassen, um Text mit C++ einzupassen  
description: Erfahren Sie, wie Sie die Form der Datenbeschriftung in einem Diagramm anpassen, um den Text in Aspose.Cells for C++ einzupassen. Unser Leitfaden zeigt Ihnen, wie Sie die Größe und Form des Beschriftungskontainers anpassen, um sicherzustellen, dass der Text korrekt angezeigt wird, ohne abgeschnitten oder überlappt zu werden.  
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenbeschriftungen, Formenänderung, Textanpassung, Abschneidung, Überlappung.  
type: docs  
weight: 220  
url: /de/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

Die Excel-Anwendung bietet die Option **Form an Text anpassen** für Diagrammdatenbeschriftungen, um die Größe der Form zu erhöhen, damit der Text hineinpasst.  

{{% /alert %}}  

## **So passen Sie die Form der Datenbeschriftung in einem Diagramm an, damit der Text in Microsoft Excel passt**  

Diese Option kann in der Excel-Benutzeroberfläche durch Auswahl einer beliebigen Datenbeschriftung im Diagramm aufgerufen werden. Klicken Sie mit der rechten Maustaste und wählen Sie das Menü **Datenbeschriftungen formatieren**. Unter dem Tab **Größe & Eigenschaften** expandieren Sie **Ausrichtung**, um die zugehörigen Eigenschaften einschließlich der Option **Form ändern, um Text anzupassen** anzuzeigen.  

## **So passen Sie die Form der Diagrammdatenbeschriftungen mit Aspose.Cells for C++ an**  

Um die Excel-Funktion nachzuahmen, die die Formen der Datenbeschriftungen an den Text anpasst, haben die Aspose.Cells APIs die boolesche Eigenschaft [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext) freigegeben. Der folgende Code zeigt ein einfaches Nutzungsszenario der [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext)-Eigenschaft.  

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
