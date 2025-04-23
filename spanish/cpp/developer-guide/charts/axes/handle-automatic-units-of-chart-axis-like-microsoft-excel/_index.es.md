---
title: Manejar unidades automáticas en el eje del gráfico como Microsoft Excel con C++
linktitle: Manejar unidades automáticas en el eje del gráfico
description: Aprende cómo manejar unidades automáticas en ejes de gráficos en Aspose.Cells for C++, similar a Microsoft Excel. Nuestra guía te mostrará cómo configurar y personalizar las unidades automáticas en un eje de gráfico, incluyendo la visualización en notación científica y ajuste de escala.
keywords: Aspose.Cells for C++, ejes de gráficos, unidades automáticas, Microsoft Excel, configuración, personalización, notación científica, escalado.
type: docs
weight: 120
url: /es/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Escenarios de uso posibles**
Las primeras versiones de Aspose.Cells no pudieron manejar correctamente las unidades automáticas del eje del gráfico cuando el gráfico se renderizaba a imagen o PDF. Ahora, Aspose.Cells admite el manejo de unidades automáticas del eje del gráfico. No hay cambio de código. Simplemente convierta su gráfico en imagen o PDF y se renderizará el eje del gráfico exactamente como lo hace Microsoft Excel.

## **Manejar Unidades Automáticas del Eje del Gráfico como Microsoft Excel**
El siguiente código de muestra carga el [archivo de Excel de muestra](61767755.xlsx) y genera el [gráfico de PDF de salida](61767752.pdf). La captura de pantalla muestra las unidades automáticas del eje del gráfico en rectángulos rojos y también compara el gráfico del archivo de Excel de muestra con el gráfico del PDF de salida. Ambos son exactamente similares.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Código de muestra**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
