---
title: Establecer el Código de Formato de Valores de la Serie del Gráfico con C++
linktitle: Formato de número
type: docs
weight: 100
url: /es/cpp/set-the-values-format-code-of-chart-series/
description: Aprende cómo establecer el código de formato de valores de la serie del gráfico en Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo formatear los datos de la serie del gráfico usando el código de formato apropiado, permitiéndote presentar tus datos de manera precisa y profesional.
keywords: Aspose.Cells for C++, serie de gráfico, código de formato de valores, formato, presentación de datos, precisión, profesionalismo.
---

## **Escenarios de uso posibles**
Puedes establecer el código de formato de valores de la serie del gráfico usando la propiedad [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/). Esta propiedad no solo es útil para la serie basada en el rango dentro de la hoja de cálculo, sino que también funciona bien para la serie creada con un array de valores.

## **Establecer el código de formato de valores de la serie del gráfico**
 El siguiente código de ejemplo añade una serie en el gráfico vacío que no tenía series previamente. Agrega la serie usando un array de valores. Una vez que agrega la serie, la formatea con el código `$#,##0` usando la propiedad [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) y el número `10000` se convierte en `$10,000`. La captura de pantalla muestra el efecto del código en el [archivo de Excel de ejemplo](51740712.xlsx) y en el [archivo de Excel de salida](51740713.xlsx) después de la ejecución.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Código de muestra**
```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
