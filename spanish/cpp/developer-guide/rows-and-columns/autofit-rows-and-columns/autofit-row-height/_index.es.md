---
title: Ajuste automático de la altura de fila al cargar archivo con C++
linktitle: Ajustar automáticamente la altura de la fila cuando se carga el archivo
type: docs
weight: 120
url: /es/cpp/autofit-row-height/
description: Aprenda cómo ajustar automáticamente las filas cuya altura no es personalizada usando Aspose.Cells con C++.
keywords: Ajustar automáticamente la altura de la fila al cargar el archivo, ajusta automáticamente la altura de la fila al abrir el archivo de Excel.
---

## **Escenarios de uso posibles**
La altura de la fila se ajusta automáticamente para coincidir con la fuente del contenido, pero cuando la altura de la fila almacenada no coincide con la altura del contenido en el archivo, MS Excel ajustará automáticamente la altura de la fila al cargar el archivo, mientras que Aspose.Cells no ajustará automáticamente para mejorar el rendimiento. Si necesita usar el programa Aspose.Cells para ajustar automáticamente las alturas de línea al cargar archivos, puede lograrlo mediante el parámetro [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

Por favor, consulte los siguientes datos de la imagen. Podemos observar que la altura de la fila en caché en la línea 11 es de 15, pero Excel ajustó automáticamente la altura de la fila al cargar el archivo.
<br>
<img src="1.png" width=70% />

## **Ajustar la altura de la fila usando Aspose.Cells**
Si carga directamente el archivo y lo guarda en PDF, los datos no se mostrarán completamente en PDF porque la altura de la línea en caché es solo de 15.
<br>
<img src="2.png" width=70% />
<br>
Si configura el parámetro [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) en true al cargar el archivo, entonces Aspose.Cells ajustará automáticamente la altura de la fila. La altura ajustada puede cumplir de manera efectiva con los requisitos de visualización del texto.
<br>
<img src="3.png" width=70% />

## **Código de muestra en C++**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
