---
title: Especificar cómo cruzar cadenas en HTML de salida usando HtmlCrossType con C++
linktitle: Especificar HtmlCrossType en HTML de salida
type: docs
weight: 140
url: /es/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aprende cómo controlar el desbordamiento de cadenas en HTML de salida usando Aspose.Cells for C++ con HtmlCrossType.
---

## **Escenarios de uso posibles**

Cuando una celda contiene texto o una cadena que es más ancha que la anchura de la celda, ésta desborda si la siguiente celda en la siguiente columna es nula o está vacía. Cuando guardas tu archivo de Excel en HTML, puedes controlar este desbordamiento especificando el tipo de cruce usando la enumeración [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). Tiene los siguientes valores:

- **HtmlCrossType.Default**: Se muestra como MS Excel, dependiendo de la siguiente celda. Si la siguiente celda está vacía, la cadena se cruzará o se truncará.

- **HtmlCrossType.MSExport**: Muestra la cadena como exportación HTML de MS Excel.

- **HtmlCrossType.Cross**: Muestra la cadena cruzada de HTML, el rendimiento para la creación de archivos HTML grandes será más de diez veces más rápido que configurar el valor como Predeterminado o Ajustar a la celda.

- **HtmlCrossType.FitToCell**: Solo mostrar la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en HTML de salida utilizando HtmlCrossType**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](51740732.xlsx) y lo guarda en formato HTML especificando diferentes [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). Descargue los [HTMLs de salida](51740734.zip) generados con este código. El archivo de Excel de muestra contiene la imagen con borde de color rojo como se muestra en esta captura de pantalla que demuestra el efecto de los valores [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) en el HTML de salida.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
