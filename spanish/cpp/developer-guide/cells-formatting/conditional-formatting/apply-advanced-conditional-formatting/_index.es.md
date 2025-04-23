---
title: Aplicar formato condicional avanzado con C++
linktitle: Aplicar Formato Condicional Avanzado
description: Cómo usar la biblioteca Aspose.Cells en C++ para aplicar formato condicional avanzado. Ajustando estos criterios, tendrás más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional avanzado, C++, Condicional, Formateo
type: docs
weight: 70
url: /es/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 y versiones posteriores (2010/2013/2016) proporciona algunas características avanzadas para el formato condicional. Por ejemplo, le permite aplicar sombreado de celdas, bordes, iconos de colores, flechas, banderas y formato de fuente, etc. que se ha vuelto bastante sofisticado.

{{% /alert %}}

## **Aplicar Formato Condicional Avanzado a Archivos de Microsoft Excel**
El formato condicional puede:

- Agregar barras de datos sombreadas para mejorar gráficamente los números subyacentes mediante la inclusión de un gráfico de barras simple en las celdas.
- Sombrear automáticamente las celdas con escalas de colores basadas en su relación con los valores en otras celdas del rango. La configuración por defecto sombrea el valor más bajo en rojo moviéndose hasta el valor más alto en verde.
- Utilizar conjuntos de iconos de forma similar a las escalas de colores, pero en lugar de sombrear las celdas, agrega pequeños iconos, como flechas y semáforos en las celdas.

Aspose.Cells admite completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en formato XLSX en las celdas en tiempo de ejecución. Este ejemplo demuestra un ejercicio para tipos avanzados de formato condicional que incluyen conjuntos de iconos, barras de datos, escalas de colores, periodos de tiempo, top/bottom y otras reglas con diferentes conjuntos de atributos.

### **Calcular el Color Elegido por Microsoft Excel para Formato Condicional de Escala de Color**
Aspose.Cells le permite calcular el color seleccionado por Microsoft Excel cuando se usa formato condicional de escala de color en un archivo de plantilla. Vea el código de muestra a continuación para aprender cómo calcular el color seleccionado por Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
