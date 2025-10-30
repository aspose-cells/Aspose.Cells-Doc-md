---
title: Convertir un gráfico de Excel a Imagen con C++
linktitle: Convertir un gráfico de Excel a imagen
type: docs
weight: 20
url: /es/cpp/convert-an-excel-chart-to-image/
description: Aprenda cómo convertir gráficos de Excel en imágenes usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Los gráficos son visualmente atractivos y facilitan a los usuarios ver comparaciones, patrones y tendencias en los datos. Por ejemplo, en lugar de analizar columnas de números de la hoja de trabajo, un gráfico muestra de un vistazo si las ventas están cayendo o aumentando, o cómo las ventas reales comparan con las ventas proyectadas. A menudo, se pide a las personas que presenten información estadística y gráfica de manera fácil de entender y mantener. Una imagen ayuda.

A veces, se necesitan gráficos en una aplicación o páginas web. O pueden ser necesarios para un documento de Word, un archivo PDF, una presentación de PowerPoint u otra aplicación. En cada caso, quieres renderizar el gráfico como una imagen para poder usarlo en otro lugar.

{{% /alert %}}

## **Convertir gráficos a imágenes**

En los ejemplos aquí, un gráfico circular y un gráfico de columnas se convierten en imágenes.

### **Convertir un gráfico circular a un archivo de imagen**

Primero, cree un gráfico circular en Microsoft Excel y luego conviértalo en un archivo de imagen con Aspose.Cells. El código de este ejemplo crea una imagen EMF basada en el gráfico circular en el archivo de plantilla de Microsoft Excel.

|**Salida: imagen del gráfico circular**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Crear un gráfico circular en Microsoft Excel:
   1. Abra un nuevo libro en Microsoft Excel.
   1. Ingrese algunos datos en una hoja de cálculo.
   1. Crear un gráfico circular basado en los datos.
   1. Guarde el archivo.

|**El archivo de entrada.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Descargue e instale Aspose.Cells:
   1. [Descargar Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
   1. Instálelo en su equipo de desarrollo.

Todos los componentes [Aspose](http://www.aspose.com/) funcionan en modo de evaluación cuando se instalan por primera vez. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos de salida.

1. Cree un proyecto:
   1. Inicie su entorno de desarrollo en C++ (por ejemplo, Visual Studio).
   1. Cree una nueva aplicación de consola.
   1. Añada una referencia a Aspose.Cells. Este proyecto usa Aspose.Cells, así que añada una referencia a la biblioteca Aspose.Cells.
   1. Escribir el código que encuentra y convierte el gráfico. A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Se utilizan muy pocas líneas de código.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Convirtiendo un Gráfico de Columnas a un Archivo de Imagen**

Primero, cree un gráfico de columnas en Microsoft Excel y conviértalo en un archivo de imagen, como se mencionó anteriormente. Después de ejecutar el código de ejemplo, se crea un archivo JPEG basado en el gráfico de columnas en el archivo de Excel plantilla.

|**Archivo de salida: una imagen de gráfico de columnas.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Crear un gráfico de columnas en Microsoft Excel:
   1. Abra un nuevo libro en Microsoft Excel.
   1. Ingrese algunos datos en una hoja de cálculo.
   1. Cree un gráfico de columnas basado en los datos.
   1. Guarde el archivo.

|**Archivo de entrada.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Configure un proyecto, con referencias, como se describe arriba.
1. Convierta dinámicamente el gráfico en una imagen. A continuación se muestra el código utilizado por el componente para completar la tarea. El código es similar al anterior:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
