---
title: Получить DrawObject и Bound при рендеринге в PDF с использованием класса DrawObjectEventHandler
linktitle: Получить DrawObject и Bound при рендеринге в PDF
type: docs
weight: 70
url: /ru/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Узнайте, как использовать класс DrawObjectEventHandler в C++, чтобы захватывать DrawObject и Bound при рендеринге файлов Excel в PDF или изображения.
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет абстрактный класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/), который содержит метод [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/). Пользователь может реализовать [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) и использовать метод [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) для получения [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) и границ при рендеринге Excel в PDF или изображение. Вот краткое описание параметров метода [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/).

- drawObject: объект [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) будет инициализирован и возвращен при рендеринге

- x: слева от [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: сверху [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- ширина: ширина [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- высота: высота [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

Если вы рендерите файл Excel в PDF, то вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) с [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). Аналогично, если вы рендерите файл Excel в изображение, вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) с [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/).

## **Получите объект DrawObject и Bound при рендеринге в Pdf с использованием класса DrawObjectEventHandler**

Пожалуйста, посмотрите следующий пример кода. Он загружает [пример файла Excel](64716821.xlsx) и сохраняет его как [выходной PDF](64716822.pdf). При рендеринге в PDF он использует свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) и захватывает [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) и Bound существующих ячеек и объектов, например изображений. Если [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) по типу является ячейкой, он выводит его Bound и StringValue. Если [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) по типу изображение, он выводит его Bound и название Shape. Для более подробной информации смотрите вывод в консоль из примера кода ниже.

## **Образец кода**

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

## **Вывод в консоль**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
