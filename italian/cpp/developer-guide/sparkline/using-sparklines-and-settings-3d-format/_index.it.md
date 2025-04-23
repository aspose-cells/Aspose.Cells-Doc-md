---
title: Usare Sparklines e impostazioni di formattazione 3D con C++
linktitle: Utilizzo di Sparklines e Impostazioni Formato 3D
type: docs
weight: 40
url: /it/cpp/using-sparklines-and-settings-3d-format/
description: Impara come usare sparklines e applicare formattazione 3D nei file Excel usando Aspose.Cells con C++.
---

## **Utilizzo delle Sparklines**
Microsoft Excel 2010 può analizzare le informazioni in modi più variati che mai. Consente agli utenti di monitorare ed evidenziare importanti tendenze dei dati con nuovi strumenti di analisi e visualizzazione dei dati. Le Sparklines sono mini-grafici che è possibile inserire all'interno delle celle, in modo da poter visualizzare dati e grafici sulla stessa tabella. Quando le sparklines vengono utilizzate correttamente, l'analisi dei dati è più rapida e diretta. Forniscono inoltre una visione semplice delle informazioni, evitando fogli di lavoro affollati con molti grafici elaborati.

Aspose.Cells fornisce un'API per manipolare le sparklines nei fogli di calcolo.
### **Le Sparklines in Microsoft Excel**
Per inserire sparklines in Microsoft Excel 2010:

1. Selezionare le celle in cui si desidera che compaiano le sparklines. Per renderle facili da visualizzare, selezionare le celle a lato dei dati.
1. Fare clic su **Inserisci** nella barra multifunzione e quindi scegliere **colonna** nel gruppo **Sparklines**.
1. Selezionare o inserire il intervallo di celle nel foglio di lavoro che contengono i dati di origine. I grafici compariranno.

Le Sparklines ti aiutano a visualizzare le tendenze, ad esempio, il record di vittorie o sconfitte per una lega di softball. Le Sparklines possono persino sommare l'intera stagione di ogni squadra nella lega.
### **Sparklines utilizzando Aspose.Cells**
Gli sviluppatori possono creare, cancellare o leggere sparklines (nel file modello) usando l'API fornita da Aspose.Cells. Le classi che gestiscono sparklines sono contenute nel namespace [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/) quindi è necessario importare questo namespace prima di usare queste funzionalità.

Aggiungendo grafici personalizzati per un determinato intervallo di dati, i programmatori hanno la libertà di aggiungere diversi tipi di piccoli grafici alle aree di celle selezionate.

L'esempio di seguito mostra la funzione Sparklines. L'esempio mostra come:

1. Aprire un semplice file modello.
1. Leggere le informazioni delle sparklines per un foglio di lavoro.
1. Aggiungere nuove sparklines per un dato intervallo di dati in un'area di celle.
1. Salvare il file Excel su disco.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Impostazione del Formato 3D**
Potresti avere bisogno di stili di grafici 3D per ottenere solo i risultati per il tuo scenario. Aspose.Cells fornisce l'API pertinente per applicare la formattazione 3D di Microsoft Excel 2007.

Di seguito è riportato un esempio completo per dimostrare come creare un grafico e applicare la formattazione 3D di Microsoft Excel 2007. Dopo aver eseguito il codice di esempio, verrà aggiunto un grafico a colonne (con effetti 3D) al foglio di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
