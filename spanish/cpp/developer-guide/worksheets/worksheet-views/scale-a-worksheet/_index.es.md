---
title: Cómo escalar una hoja de cálculo con C++
linktitle: Cómo escalar una hoja de trabajo
type: docs
weight: 130
url: /es/cpp/how-to-scale-a-worksheet/
description: Este artículo te muestra código que explica cómo escalar una hoja de cálculo usando la biblioteca Aspose.Cells con C++.
keywords: Escalar en C++, Cómo escalar una hoja de cálculo usando C++, Escalar una hoja de cálculo en C++.
---

## **Escenarios de uso posibles**
Escalar una hoja de trabajo puede ser útil por varias razones, dependiendo del contexto en el que estés trabajando. Aquí algunas razones comunes para escalar una hoja de trabajo:
1. Ajustar al tamaño de página: Para asegurarte de que todo el contenido quepa en una sola página o en un número específico de páginas al imprimir, facilitando la lectura y gestión sin tener que pasar varias páginas.

1. Presentación: Para que la hoja de cálculo luzca más organizada y profesional, especialmente al compartirla con otros en reuniones o informes.

1. Legibilidad: Para ajustar el tamaño del texto y otros elementos para una mejor legibilidad, especialmente para personas que puedan tener dificultades para leer fuentes pequeñas.

1. Gestión del espacio: Para optimizar el uso del espacio en una hoja de cálculo, asegurando que no haya espacios en blanco innecesarios y que toda la información importante sea visible sin desplazamiento excesivo.

1. Visualización de datos: En el caso de gráficos y diagramas, el escalado puede ayudar a hacer que sean más comprensibles ajustando el tamaño para que se ajusten apropiadamente al espacio disponible.

1. Consistencia: Para mantener una apariencia y sensación coherentes en varias hojas de cálculo o documentos, lo cual es particularmente importante en entornos profesionales y educativos.

## **Cómo escalar una hoja de trabajo en Excel**
Escalar una hoja de cálculo en Excel puede ayudarte a ajustar tu contenido a una sola página o a un número específico de páginas al imprimir. Aquí están los pasos para escalar una hoja de cálculo:

1. Abre tu hoja de cálculo: Abre la hoja de Excel que deseas escalar.

1. Ve a la pestaña de Diseño de página: Haz clic en la pestaña de Diseño de página en la cinta.

1. Grupo de Escalar para ajustarse: En la pestaña de Diseño de página, encuentra el grupo Escalar para ajustarse. Aquí tienes opciones para ajustar la escala. Ancho: Esta opción te permite especificar cuántas páginas de ancho tendrá la hoja al imprimir. Alto: Esta opción te permite especificar cuántas páginas de alto tendrá la hoja al imprimir. Escala: También puedes establecer un porcentaje de escala personalizado aquí.
<br>
<img src="1.png" width=60% />

1. Ajusta ancho y alto: Establece el ancho y alto en el número de páginas deseado. Por ejemplo, configura ambos en 1 página si quieres que la hoja quepa en una sola página.

1. Ajusta el porcentaje de escala (si es necesario): Si prefieres establecer un porcentaje de escala específico, ajusta la casilla de Escala. Por ejemplo, establecerlo en 50% reducirá todo a la mitad de tamaño.


## **Cómo escalar una hoja de cálculo usando C++**
Aspose.Cells es una biblioteca potente para trabajar con archivos de Excel de manera programática. Para escalar una hoja de cálculo usando Aspose.Cells, debes seguir estos pasos: carga [archivo de ejemplo](sample.xlsx) y ajusta la configuración de impresión para que el contenido quepa en el número deseado de páginas o en un porcentaje específico del tamaño original.

### **Ejemplo: Ajustar a página completa**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the worksheet to fit to 1 page wide and 1 page tall
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the modified workbook
    workbook.Save(u"output_fit_to_page.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
<br>
<img src="3.png" width=60% />

### **Ejemplo: Escalar a porcentaje**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the scaling to a specific percentage (e.g., 75%)
    pageSetup.SetZoom(75);

    // Save the modified workbook
    workbook.Save(u"output_scaled_percentage.xlsx");

    // Clean up Aspose.Cells resources
    Aspose::Cells::Cleanup();

    return 0;
}
```
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
