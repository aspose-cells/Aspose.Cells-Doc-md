---  
title: Redimensionner la forme de l étiquette de données du graphique pour qu elle s adapte au texte avec C++  
description: Apprenez comment redimensionner la forme de l’étiquette de données dans un graphique pour qu’elle s’adapte au texte en utilisant Aspose.Cells for C++. Notre guide vous montrera comment ajuster la taille et la forme du conteneur de l’étiquette afin d’assurer que le texte s’affiche correctement sans troncature ni chevauchement.  
keywords: Aspose.Cells for C++, diagramme, étiquettes de données, redimensionnement de la forme, ajustement du texte, troncature, chevauchement.  
type: docs  
weight: 220  
url: /fr/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

L'application Excel propose l'option **Redimensionner la forme pour s'adapter au texte** pour les étiquettes de données du graphique afin d'augmenter la taille de la forme afin que le texte s'y insère.  

{{% /alert %}}  

## **Comment redimensionner la forme de l'étiquette de données du graphique pour s'adapter au texte dans Microsoft Excel**  

Cette option peut être accessible via l'interface Excel en sélectionnant n'importe quelle étiquette de données sur le graphique. Faites un clic droit et choisissez le menu **Format DataLabels**. Dans l'onglet **Taille & Propriétés**, développez **Alignement** pour révéler les propriétés associées, y compris l'option **Redimensionner la forme pour corriger le texte**.  

## **Comment redimensionner la forme de l’étiquette de données du graphique pour qu’elle s’adapte au texte en utilisant Aspose.Cells for C++**  

Pour imiter la fonction d'Excel de redimensionnement des formes d'étiquettes de données pour les adapter au texte, les APIs Aspose.Cells ont exposé la propriété Booléenne [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext). Le code ci-dessous montre un scénario d'utilisation simple de la propriété [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext).  

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
