---
title: Leer subtítulo del gráfico desde un archivo ODS con C++
linktitle: Leer subtítulo de gráfico de archivo ODS
description: Aprende cómo usar Aspose.Cells for C++ para leer el subtítulo del gráfico desde un archivo de hoja de cálculo OpenDocument (ODS). Nuestra guía demostrará cómo extraer y acceder al subtítulo de un gráfico para análisis o visualización adicional.
keywords: Aspose.Cells for C++, Leer subtítulo del gráfico, Hoja de cálculo OpenDocument, Archivo ODS, Extracción de gráfico, Análisis de datos.
type: docs
weight: 160
url: /es/cpp/read-chart-subtitle-from-ods-file/
---

## **Leer subtítulo del gráfico desde un archivo ODS**

Aspose.Cells le brinda la capacidad de leer subtítulos de gráficos en archivos ODS mediante el uso de la propiedad [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/). El siguiente código de ejemplo carga el [archivo ODS de muestra](89620481.ods) y lee el subtítulo del gráfico usando la propiedad [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) e imprime en la ventana de la consola. Consulte la salida de la consola del código a continuación para obtener referencia.

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load excel file containing charts
    Workbook workbook(srcDir + u"SampleChart.ods");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Print chart subtitle
    cout << "Chart Subtitle: " << chart.GetSubTitle().GetText().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
