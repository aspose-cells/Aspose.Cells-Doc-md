---
title: Obtener DrawObject y Bound al renderizar a PDF con C++ usando la clase DrawObjectEventHandler
linktitle: Obtener DrawObject y Bound al renderizar a PDF
type: docs
weight: 70
url: /es/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Aprende cómo usar la clase DrawObjectEventHandler en C++ para capturar DrawObject y Bound al renderizar archivos de Excel a PDF o imágenes.
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona una clase abstracta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) que tiene un método [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/). El usuario puede implementar [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) y utilizar el método [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) para obtener el [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) y Bound mientras se representa Excel a PDF o Imagen. Aquí tienes una breve descripción de los parámetros del método [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) se inicializará y se devolverá al representar

- x: Izquierda de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: Arriba de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- width: Ancho de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- height: Altura de [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

Si estás renderizando un archivo de Excel a PDF, entonces puedes utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) con [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). De manera similar, si estás renderizando un archivo de Excel a imagen, puedes utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) con [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/).

## **Obtener DrawObject y Bound al representar a PDF utilizando la clase DrawObjectEventHandler**

Por favor, consulta el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](64716821.xlsx) y lo guarda como [pdf de salida](64716822.pdf). Al renderizar a PDF, utiliza la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) y captura el [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) y Bound de las celdas y objetos existentes, como imágenes, etc. Si el tipo [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) es celda, imprime su Bound y StringValue. Y si el tipo [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) es Imagen, imprime su Bound y nombre de forma. Consulta la salida por consola del código de ejemplo a continuación para obtener más ayuda.

## **Código de muestra**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class ClsDrawObjectEventHandler : public DrawObjectEventHandler
{
public:
    void Draw(DrawObject& drawObject, float x, float y, float width, float height) override
    {
        std::cout << std::endl;

        if (drawObject.GetType() == DrawObjectEnum::Cell)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Cell Value]: " << drawObject.GetCell().GetStringValue().ToUtf8() << std::endl;
        }

        if (drawObject.GetType() == DrawObjectEnum::Image)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Shape Name]: " << drawObject.GetShape().GetName().ToUtf8() << std::endl;
        }

        std::cout << "----------------------" << std::endl;
    }
};

void Run()
{
    Workbook wb(u"sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");
    PdfSaveOptions opts;
    auto drawObjectEventHandler = std::make_shared<ClsDrawObjectEventHandler>();
    opts.SetDrawObjectEventHandler(drawObjectEventHandler.get());
    wb.Save(u"outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
