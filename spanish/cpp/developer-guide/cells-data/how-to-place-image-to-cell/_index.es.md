---
title: Cómo Insertar Imagen en la Celda con C++
linktitle: Cómo insertar una imagen en una celda
type: docs
weight: 130
url: /es/cpp/how-to-insert-picture-in-cell/
description: Aprende cómo insertar una imagen en una celda con Aspose.Cells usando C++.
keywords: Cómo insertar una imagen en una celda, insertar una imagen sobre celdas, colocar una imagen en una celda, colocar una imagen sobre celdas, Cómo colocar una imagen en una celda, Cómo colocar una imagen sobre celdas, Cambiar entre Imagen en celda y Imagen sobre celdas, Cambiar entre Lugar en celda y Lugar sobre celdas
---

## **Escenarios de uso posibles**
La imagen añade un toque de brillo a tu hoja de cálculo y proporciona una representación visual del contenido. También facilitan la comprensión de los datos y la obtención de ideas. Aunque has podido usar imágenes en Excel durante muchos años, Excel solo recientemente ha habilitado la función de que las imágenes sean valores reales de celda. Incluso si se modifica la disposición del dibujo, seguirá vinculado a los datos. Puedes usarlo en tablas, ordenar, filtrar, incluir en fórmulas, ¡y más!

## **Cómo insertar una imagen en una celda utilizando Excel**
Acerca de cómo insertar una imagen en una celda en Excel, sigue estos pasos:

1. Ve a la pestaña Insertar y haz clic en la opción Imágenes.
2. Selecciona **Colocar en celda**. Selecciona una de las siguientes fuentes en el menú desplegable Insertar imagen de (**Este dispositivo**, **Imágenes de stock** y **Imágenes en línea**). Este dispositivo para insertar una imagen desde tu dispositivo. Imágenes de stock para insertar una imagen desde imágenes de stock. Imágenes en línea para insertar una imagen desde la web.
<br>
<img src="1.png" width=60% />
3. Selecciona la imagen e insértala en una celda.
<br>
<img src="8.png" width=60% />

## **Cómo insertar una imagen sobre celdas utilizando Excel**
Acerca de cómo insertar una imagen sobre celdas en Excel, sigue estos pasos:

1. Ve a la pestaña Insertar y haz clic en la opción Imágenes.
2. Selecciona **Colocar sobre celdas**. Selecciona una de las siguientes fuentes en el menú desplegable Insertar imagen de (**Este dispositivo**, **Imágenes de stock** y **Imágenes en línea**). Este dispositivo para insertar una imagen desde tu dispositivo. Imágenes de stock para insertar una imagen desde imágenes de stock. Imágenes en línea para insertar una imagen desde la web.
<br>
<img src="2.png" width=60% />
3. Selecciona la imagen e insértala sobre las celdas.
<br>
<img src="3.png" width=60% />

## **Cómo cambiar de Imagen en celda a Imagen sobre celdas utilizando Excel**
Puedes cambiar fácilmente de **Imagen en celda** a **Imagen sobre celdas**. Sigue estos pasos, por favor:
1. Haz clic derecho en la celda y selecciona **Imagen en celda** > **Colocar sobre celdas**. 
<br>
<img src="4.png" width=60% />
2. El resultado después de cambiar es el siguiente:
<br>
<img src="5.png" width=60% />

## **Cómo cambiar de Imagen sobre celdas a Imagen en celda utilizando la biblioteca de Excel Aspose.Cells para Python**
Puede cambiar fácilmente de **Imagen sobre celdas** a **Imagen en celda**. Siga estos pasos:
1. Haga clic derecho en la imagen y seleccione **Insertar en celda**. 
<br>
<img src="6.png" width=60% />
2. El resultado después de cambiar es el siguiente:
<br>
<img src="7.png" width=60% />

## **Cómo Insertar Imagen en la Celda Usando C++**
Insertar imagen en celda usando Aspose.Cells. Consulte el siguiente código de ejemplo. Después de ejecutar el código de ejemplo, se insertará una imagen en una celda.
1. Crea un objeto Workbook. 
2. Obtener la celda donde desea insertar la imagen.
3. Establecer la propiedad Cell.EmbeddedImage. 
4. Finalmente, guarda el libro en formato [XLSX de salida](out.xlsx). 

## **Código de muestra**

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cell D8
    Cell d8 = worksheet.GetCells().Get(u"D8");

    // Read image file into byte vector
    std::ifstream file("aspose.png", std::ios::binary);
    std::vector<uint8_t> imageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // Convert to Aspose's Vector and set embedded image in cell D8
    d8.SetEmbeddedImage(Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
