---
title: Aggiungi filigrana WordArt al grafico con C++
description: Impara come usare Aspose.Cells for C++ per aggiungere una filigrana WordArt a un grafico in Microsoft Excel. La nostra guida dimostrerà come creare e posizionare una filigrana WordArt per migliorare l appeal visivo e l unicità del tuo grafico.
keywords: Aspose.Cells for C++, filigrana WordArt, filigrana grafico, Microsoft Excel, appeal visivo, unicità del grafico.
type: docs
weight: 50
url: /it/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

Puoi usare WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, estendere un titolo, decorare il testo, far si che il testo si adatti a una forma predefinita o applicare il testo interessato all'area di tracciamento di un grafico come filigrana. Il WordArt diventa un oggetto che puoi spostare o posizionare nei tuoi fogli di calcolo per aggiungere decorazioni.

L'esempio seguente mostra come aggiungere una forma WordArt come filigrana per l'area di tracciamento del grafico.

{{% /alert %}} 

L'esempio seguente mostra come aggiungere una forma WordArt come watermark all'area di trama di un grafico esistente.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"sample.xlsx");

    // Get the chart in the first worksheet.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Add a WordArt watermark (shape) to the chart's plot area.
    Shape wordart = chart.GetShapes().AddTextEffectInChart(MsoPresetTextEffect::TextEffect2,
        u"CONFIDENTIAL", u"Arial Black", 66, false, false, 1200, 500, 2000, 3000);

    // Get the shape's fill format.
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency.
    wordArtFormat.SetTransparency(0.9);

    // Get the line format.
    LineFormat lineFormat = wordart.GetLine();

    // Set Line format to invisible.
    lineFormat.SetWeight(0.0);

    // Save the excel file.
    workbook.Save(outputDir + u"output_out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
