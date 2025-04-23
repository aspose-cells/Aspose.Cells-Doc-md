---
title: Etiqueta de datos personalizada con texto enriquecido del punto del gráfico en C++
description: Aprenda cómo agregar etiquetas de datos personalizadas con texto enriquecido a puntos de gráficos en Aspose.Cells for C++. Nuestra guía le mostrará cómo formatear las etiquetas con diferentes fuentes, colores y opciones de alineación para mejorar la apariencia y legibilidad de sus gráficos.
keywords: Aspose.Cells for C++, gráficos, texto enriquecido, etiquetas de datos personalizadas, fuentes, colores, alineación, apariencia, legibilidad.
type: docs
weight: 10
url: /es/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Puede usar Aspose.Cells para crear etiquetas de datos personalizadas con texto enriquecido en puntos del gráfico. Aspose.Cells proporciona el método [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/) para devolver el objeto [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) que se puede usar para establecer las propiedades de fuente del texto como su color, negrita, etc.

{{% /alert %}}

## Etiqueta de Datos Personalizada con Texto Enriquecido del Punto del Gráfico

El siguiente código accede al primer punto de la primera serie, establece su texto y luego configura la fuente de los primeros 10 caracteres estableciendo su color a rojo y su negrita en **true**.

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

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
