---
title: Determinare quali assi esistono nel grafico con C++
description: Impara come determinare quale asse esiste in un grafico creato con Aspose.Cells for C++. La nostra guida ti aiuterà a capire come identificare e accedere ai diversi assi di un grafico, inclusi assi di categoria, valore, e secondari.
keywords: Aspose.Cells for C++, grafico, asse, esistenza, categoria, valore, secondario.
type: docs
weight: 140
url: /it/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A volte, l'utente ha bisogno di sapere se un particolare asse esiste nel Grafico. Ad esempio, vuole sapere se esiste un Asse dei Valori Secondari all'interno del grafico o meno. Alcuni grafici come Diagramma a Torta, Torta Esplosa, TortaPie, TortaBarra, Torta3D, Torta3DEsplosa, Anello, Anello Esploso, ecc. non hanno un asse.

Aspose.Cells fornisce il metodo [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) per determinare se il grafico ha un particolare asse o meno.

{{% /alert %}}

Il seguente esempio di codice dimostra l'uso di [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) per determinare se il grafico di esempio ha assi di categoria e valore primari e secondari.

## Codice C++ per determinare quali assi esistono nel grafico

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart
    Chart chart = worksheet.GetCharts().Get(0);

    // Determine which axis exists in the chart
    bool ret = chart.HasAxis(AxisType::Category, true);
    std::wcout << u"Has Primary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Category, false);
    std::wcout << u"Has Secondary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, true);
    std::wcout << u"Has Primary Value Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, false);
    std::wcout << u"Has Secondary Value Axis: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Output della console generato dall'esempio di codice

L'output della console del codice è stato mostrato di seguito che mostra true per la categoria primaria e l'asse dei valori e false per la categoria secondaria e l'asse dei valori.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
